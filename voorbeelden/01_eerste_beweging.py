# Voorbeeld 1: eerste beweging - draai de arm heen en terug
# Hetzelfde programma staat in de blokken: Voorbeelden > 1. Eerste beweging
# Start: klik rechtsboven op het driehoekje (Run Python File)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from robot import Robot

r = Robot()        # simulator. Voor de echte robot: Robot("IP-adres van de robot")

r.startpositie()
r.draai_basis(90)
r.wacht(1)
r.draai_basis(-90)

r.start()

# Probeer zelf: verander 90 in 45. Wat gebeurt er met een negatief getal?
