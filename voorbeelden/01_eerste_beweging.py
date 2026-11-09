# Opdracht 1: laat de robot bewegen
# Start: klik rechtsboven op het driehoekje (Run Python File)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()        # simulator. Voor de echte robot: Robot("192.168.1.10")
r.zet_aan()        # zet de robot aan en laat de remmen los

# Hoeken in graden: basis, schouder, elleboog, pols1, pols2, pols3
r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])     # rechtop, 'klaar'-stand
r.wacht(1)
r.beweeg_gewrichten([90, -90, 90, -90, -90, 0])    # draai de basis 90 graden
r.wacht(1)
r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])     # terug

r.start()

# Probeer zelf: verander de hoeken. Wat doet elk gewricht?
