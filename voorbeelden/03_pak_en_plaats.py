# Voorbeeld 3: pak een blokje op en zet het ergens anders neer
# Hetzelfde programma staat in de blokken: Voorbeelden > 3. Pak en plaats
# Punten (x, y, z) in mm: dezelfde getallen als in het robotscherm bij Move > Feature: View
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()        # simulator. Voor de echte robot: Robot("IP-adres van de robot")

r.startpositie()
r.grijper(False)
r.beweeg_lineair(500, 300, 300)
r.omlaag(200, "gripper")
r.grijper(True)
r.wacht(0.5)
r.omhoog(200, "gripper")
r.beweeg_lineair(500, -300, 300)
r.omlaag(200, "gripper")
r.grijper(False)
r.wacht(0.5)
r.omhoog(200, "gripper")
r.startpositie()

r.start()
