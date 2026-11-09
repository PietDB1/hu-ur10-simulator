# UR10 robot-simulator – Hogeschool Utrecht

Programmeer een echte industriële robotarm (Universal Robots UR10): eerst in de simulator, daarna in het echt bij de HU.
Alles draait in je browser. Je hoeft niets te installeren.

## Starten (± 5 minuten)
1. Log in op GitHub (gratis account).
2. Klik op de groene knop **Code → Codespaces → Create codespace on main**.
3. Wacht tot VS Code in je browser geladen is (de eerste keer duurt dit een paar minuten).
4. Kijk onderin bij **Terminal**. Zodra de robot klaar is, verschijnt daar **ROBOT KLAAR!** met twee links:
   het **robotscherm** en de **blokken**. Open ze met **Cmd + klik** (Mac) of **Ctrl + klik** (Windows).
5. Klik op **Connect** als die knop verschijnt. Je ziet nu het bedieningsscherm van de robot (PolyScope).
   Is het scherm zwart? Wacht 1 minuut. PolyScope start iets later op.
6. Zet de robot aan: **Go to initialization screen → ON → START → OK**.

## Programmeren met blokken (makkelijkst)
1. Open de link **Programmeren met blokken** uit de terminal (of tabblad **Poorten** → regel 8000 → wereldbolletje).
2. Klik op **⚡ Robot aanzetten** (hoeft maar één keer).
3. Sleep blokken uit de categorieën links naar het werkblad: **Beweging**, **Gripper**, **Herhalen**, enzovoort.
4. Klik op **▶ Uitvoeren** en kijk in het robotscherm hoe de arm beweegt.
   Rechts zie je de Python-code die bij jouw blokken hoort.

Je blokken worden in je browser bewaard. Met **⬇ .py** sla je het programma op als Python-bestand.

**Blokken en code horen bij elkaar**
- Klik op een blok: de bijbehorende regel Python-code licht geel op. Klik op een regel: het blok wordt geselecteerd.
- Klik op **✏ Code aanpassen**, verander de code en klik op **✓ Zet om naar blokken**. De blokken passen zich aan.
- Kies bij **📂 Voorbeelden** een voorbeeldprogramma. Dit zijn dezelfde programma's als in de map `voorbeelden`.
- **📖 Uitleg blokken** laat met tekeningen zien wat elk blok doet.

**Coördinaten:** x, y en z zijn dezelfde getallen als in het robotscherm bij **Move → Feature: View**.

## Je eerste programma in Python
Ga terug naar het tabblad met VS Code. Open `voorbeelden/01_eerste_beweging.py` en klik rechtsboven op ▶ (*Run Python File*).
Kijk in het robottabblad, bij **Move** of **Program → Graphics**: de arm beweegt!

| Opdracht | Bestand |
|---|---|
| 1. Laat de robot bewegen | `voorbeelden/01_eerste_beweging.py` |
| 2. Teken een vierkant | `voorbeelden/02_vierkant_tekenen.py` |
| 3. Pak en plaats een blokje | `voorbeelden/03_pak_en_plaats.py` |
| 4. Bouw een toren (variabele) | `voorbeelden/04_toren_bouwen.py` |

Pas getallen aan, sla op (Cmd/Ctrl + S) en klik weer op ▶.

## De belangrijkste opdrachten
```python
from robot import Robot
r = Robot()
r.startpositie()                          # arm rechtop, gripper naar beneden
r.omlaag(100, "gripper")                  # ook: omhoog, naar_links, naar_rechts, naar_voren, naar_achteren
r.naar_links(50, "voet")                  # "gripper" = t.o.v. gripper, "voet" = t.o.v. robotvoet
r.draai_basis(90)                         # hele arm draaien (graden)
r.draai_gripper(90)                       # alleen de gripper draaien (graden)
r.beweeg_lineair(500, 300, 300)           # naar punt x, y, z in mm (zoals Move -> View)
r.grijper(True)                           # True = dicht, False = open
r.wacht(1)                                # seconden
r.start()                                 # stuur alles naar de robot
```

## Programmeren zonder code (PolyScope)
1. **Program → Empty Program → Structure → Move**.
2. Klik op het waypoint → **Set waypoint** → beweeg de arm met de pijltjes → **OK**.
3. Voeg meer punten toe met **Structure → Waypoint**, en eventueel **Wait**, **Set** (gripper) of **Loop**.
4. Druk onderaan op ▶.
5. Opslaan: **File → Save As**. Het programma komt in de map `programs` in VS Code (rechtermuisklik → *Download*).

## Problemen?
| Probleem | Oplossing |
|---|---|
| Geen link "ROBOT KLAAR!" in de terminal | Ververs het VS Code-tabblad, of open zelf de link: tabblad **Poorten** → regel 6080 → wereldbolletje → zet `/vnc.html` achter het adres |
| Foutmelding **502 Bad Gateway** | De robot was nog niet klaar. Wacht 1 minuut. Helpt dat niet: tabblad **Poorten** → rechtermuisklik op 6080 → **Poort stoppen met doorsturen** → **Poort toevoegen** → `6080` |
| Je ziet een lijst met bestanden | Klik op **vnc.html** |
| Python: `Connection refused` | De robot start nog op. Wacht even en probeer opnieuw |
| De arm beweegt niet | Staat de robot op ON en START? Kijk je in het tabblad Move of Graphics? |
| Melding "Protective stop" | Het punt is onbereikbaar. Kies kleinere getallen en klik in PolyScope op **Enable** |

## Van simulator naar de echte robot
Je code werkt ook op de echte UR10 bij de HU. Alleen het adres verandert:
```python
r = Robot("192.168.1.10")   # IP-adres krijg je van je HU-begeleider
```

## Stoppen
Sluit het tabblad. De codespace stopt na 30 minuten vanzelf en je werk blijft bewaard.
Opnieuw starten gaat via github.com/codespaces.
Gratis: ongeveer 60 uur per maand per GitHub-account.

## Veiligheid (echte robot)
De echte robot draait alleen onder begeleiding van een HU-docent of -student, eerst op lage snelheid.
