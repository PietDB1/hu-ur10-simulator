# Opdracht 3: pak een blokje op en zet het ergens anders neer
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

GRIPPER = 0          # digitale uitgang waar de gripper op zit
HOOGTE_VEILIG = 300  # mm, hoogte om over dingen heen te bewegen
HOOGTE_PAK = 100     # mm, hoogte waarop het blokje gepakt wordt

def pak(r, x, y):
    r.beweeg_lineair(x, y, HOOGTE_VEILIG)
    r.uitgang(GRIPPER, False)        # gripper open
    r.beweeg_lineair(x, y, HOOGTE_PAK)
    r.uitgang(GRIPPER, True)         # gripper dicht
    r.wacht(0.5)
    r.beweeg_lineair(x, y, HOOGTE_VEILIG)

def plaats(r, x, y):
    r.beweeg_lineair(x, y, HOOGTE_VEILIG)
    r.beweeg_lineair(x, y, HOOGTE_PAK)
    r.uitgang(GRIPPER, False)        # gripper open
    r.wacht(0.5)
    r.beweeg_lineair(x, y, HOOGTE_VEILIG)

r = Robot()
r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])
pak(r, -500, -300)
plaats(r, -500, 300)
r.start()

# Uitdaging: stapel drie blokjes op elkaar (tip: maak HOOGTE_PAK een parameter).
