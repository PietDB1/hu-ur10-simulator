"""
robot.py - eenvoudige besturing van een Universal Robots UR10 (CB3)

Werkt met de simulator (URSim) en met de echte robot, ook op oude software (3.1),
omdat alles als URScript-tekst via poort 30002 wordt verstuurd.

Gebruik:
    from robot import Robot

    r = Robot()                      # simulator (127.0.0.1)
    # r = Robot("192.168.1.10")      # echte robot: alleen het IP-adres veranderen

    r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])     # hoeken in graden
    r.beweeg_lineair(x=-400, y=-300, z=300)            # positie in mm
    r.wacht(1)
    r.uitgang(0, True)                                  # digitale uitgang 0 aan (bv. gripper)
    r.start()                                           # stuurt alles naar de robot

Let op: de robot moet AAN staan en de remmen moeten los zijn
(in PolyScope: knop 'ON' en daarna 'START', of gebruik r.zet_aan()).
"""

import math
import os
import socket
import time

# Veilige standaardwaarden voor scholieren (langzaam!)
SNELHEID_GEWRICHT = 0.5      # rad/s
VERSNELLING_GEWRICHT = 0.5   # rad/s^2
SNELHEID_LINEAIR = 0.1       # m/s   (= 100 mm/s)
VERSNELLING_LINEAIR = 0.3    # m/s^2


class Robot:
    def __init__(self, ip=None):
        # Zonder IP: gebruik ROBOT_IP uit de omgeving, anders de simulator
        self.ip = ip or os.environ.get("ROBOT_IP", "127.0.0.1")
        self.regels = []

    # ---------- bewegingen ----------
    def beweeg_gewrichten(self, hoeken_graden, snelheid=SNELHEID_GEWRICHT):
        """Beweeg naar 6 gewrichtshoeken (graden): basis, schouder, elleboog, pols1, pols2, pols3."""
        if len(hoeken_graden) != 6:
            raise ValueError("Geef precies 6 hoeken op.")
        q = [round(math.radians(h), 5) for h in hoeken_graden]
        self.regels.append(f"movej({q}, a={VERSNELLING_GEWRICHT}, v={snelheid})")

    def beweeg_lineair(self, x, y, z, rx=0.0, ry=180.0, rz=0.0, snelheid=SNELHEID_LINEAIR):
        """Beweeg in een rechte lijn naar positie x, y, z (mm) t.o.v. de robotvoet.
        rx, ry, rz is de stand van de 'hand' in graden (standaard: gripper wijst naar beneden)."""
        pose = [x / 1000, y / 1000, z / 1000,
                math.radians(rx), math.radians(ry), math.radians(rz)]
        pose = [round(p, 5) for p in pose]
        self.regels.append(f"movel(p{pose}, a={VERSNELLING_LINEAIR}, v={snelheid})")

    def wacht(self, seconden):
        self.regels.append(f"sleep({float(seconden)})")

    def uitgang(self, nummer, aan):
        """Zet een digitale uitgang (0-7) aan of uit, bijvoorbeeld om een gripper te sturen."""
        self.regels.append(f"set_standard_digital_out({int(nummer)}, {'True' if aan else 'False'})")

    def bericht(self, tekst):
        """Laat een tekst zien in het logboek van de robot."""
        tekst = str(tekst).replace('"', "'")
        self.regels.append(f'textmsg("{tekst}")')

    # ---------- versturen ----------
    def als_script(self):
        """Geeft het URScript-programma als tekst (handig om te bekijken of op te slaan)."""
        body = "\n".join("  " + r for r in self.regels)
        return f"def scholierenprogramma():\n{body}\nend\n"

    def start(self):
        """Stuur alle opdrachten in één keer naar de robot."""
        if not self.regels:
            print("Er staan nog geen opdrachten klaar.")
            return
        script = self.als_script()
        with socket.create_connection((self.ip, 30002), timeout=5) as s:
            s.sendall(script.encode("utf-8"))
        print(f"Programma met {len(self.regels)} opdrachten verstuurd naar {self.ip}.")
        self.regels = []

    def stop(self):
        """Stop de huidige beweging."""
        with socket.create_connection((self.ip, 30002), timeout=5) as s:
            s.sendall(b"stopj(2.0)\n")
        print("Stop verstuurd.")

    def opslaan(self, bestandsnaam="programma.script"):
        """Sla het programma op als .script-bestand (kan in PolyScope in een Script-node)."""
        with open(bestandsnaam, "w") as f:
            f.write(self.als_script())
        print(f"Opgeslagen als {bestandsnaam}")

    # ---------- robot aanzetten (dashboard-server, poort 29999) ----------
    def _dashboard(self, opdracht):
        with socket.create_connection((self.ip, 29999), timeout=5) as s:
            s.recv(1024)  # welkomstbericht
            s.sendall((opdracht + "\n").encode())
            return s.recv(1024).decode().strip()

    def zet_aan(self):
        """Zet de robot aan en laat de remmen los (zelfde als ON + START in PolyScope)."""
        print(self._dashboard("power on"))
        time.sleep(3)
        print(self._dashboard("brake release"))
        time.sleep(3)
