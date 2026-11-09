# Opdracht 2: teken een vierkant (denk aan een pen in de gripper)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()

# Startpunt in mm t.o.v. de robotvoet
x0, y0, z = -500, -200, 200
zijde = 200   # mm

r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])   # veilige startstand
r.beweeg_lineair(x0, y0, z + 50)                  # boven het papier
r.beweeg_lineair(x0, y0, z)                       # pen omlaag

for dx, dy in [(zijde, 0), (zijde, zijde), (0, zijde), (0, 0)]:
    r.beweeg_lineair(x0 + dx, y0 + dy, z)

r.beweeg_lineair(x0, y0, z + 50)                  # pen omhoog
r.start()

# Uitdaging: teken een driehoek, een cirkel (gebruik math.sin/cos) of je initialen.
