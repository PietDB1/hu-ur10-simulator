# Voorbeeld 4: bouw een toren - elk blokje 50 mm hoger neerzetten
# Hetzelfde programma staat in de blokken: Voorbeelden > 4. Toren bouwen
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()        # simulator. Voor de echte robot: Robot("IP-adres van de robot")

hoogte = 200
r.startpositie()
for count in range(3):
    r.beweeg_lineair(500, 300, 300)
    r.omlaag(200, "gripper")
    r.grijper(True)
    r.wacht(0.5)
    r.omhoog(200, "gripper")
    r.beweeg_lineair(500, -300, 300)
    r.omlaag(hoogte, "gripper")
    r.grijper(False)
    r.wacht(0.5)
    r.omhoog(hoogte, "gripper")
    hoogte = hoogte - 50
r.startpositie()

r.start()
