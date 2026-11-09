# Voorbeeld 2: teken een vierkant (denk aan een pen in de gripper)
# Hetzelfde programma staat in de blokken: Voorbeelden > 2. Vierkant tekenen
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()        # simulator. Voor de echte robot: Robot("IP-adres van de robot")

r.startpositie()
r.omlaag(100, "gripper")
r.naar_voren(200, "voet")
r.naar_links(200, "voet")
r.naar_achteren(200, "voet")
r.naar_rechts(200, "voet")
r.omhoog(100, "gripper")

r.start()

# Uitdaging: teken een rechthoek van 300 x 100 mm, of een driehoek.
