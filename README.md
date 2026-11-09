# UR10 robot-simulator – Hogeschool Utrecht

Programmeer een echte industriële robotarm (Universal Robots UR10) – eerst in de simulator, daarna in het echt bij de HU.
Alles draait in je browser: je hoeft niets te installeren.

## Starten (± 3 minuten)
1. Log in op GitHub (gratis account).
2. Klik op de groene knop **Code → Codespaces → Create codespace on main**.
3. Wacht tot VS Code in je browser geladen is (de eerste keer duurt dit een paar minuten).
4. Open de robot: tabblad **PORTS** (onderin) → regel **Robot (PolyScope)** → klik op het wereldbol-icoon.
   Zet achter het adres: `/vnc.html?autoconnect=true&resize=scale` en druk op Enter.
5. In PolyScope: klik op **ON** en daarna **START** (of laat `r.zet_aan()` dat doen).

## Je eerste programma
Open `voorbeelden/01_eerste_beweging.py` en klik rechtsboven op ▶ (*Run Python File*).
Kijk in het PolyScope-tabblad: de robot beweegt!

| Opdracht | Bestand |
|---|---|
| 1. Laat de robot bewegen | `voorbeelden/01_eerste_beweging.py` |
| 2. Teken een vierkant | `voorbeelden/02_vierkant_tekenen.py` |
| 3. Pak en plaats een blokje | `voorbeelden/03_pak_en_plaats.py` |

## De belangrijkste opdrachten
```python
from robot import Robot
r = Robot()
r.beweeg_gewrichten([0, -90, 90, -90, -90, 0])  # 6 hoeken in graden
r.beweeg_lineair(x=-500, y=-200, z=300)         # rechte lijn naar x,y,z in mm
r.wacht(1)                                      # seconden
r.uitgang(0, True)                              # gripper dicht (uitgang 0)
r.start()                                       # stuur alles naar de robot
```

## Van simulator naar de echte robot
Je code werkt ook op de echte UR10 bij de HU. Alleen het adres verandert:
```python
r = Robot("192.168.1.10")
```
Programma's die je in PolyScope maakt (`.urp`), komen in de map `programs`. Rechtermuisklik → *Download* om ze op te slaan.

## Stoppen
Sluit het tabblad; de codespace stopt na 30 minuten vanzelf. Je werk blijft bewaard.
Gratis: ongeveer 60 uur per maand per GitHub-account.

## Veiligheid (echte robot)
De echte robot draait alleen onder begeleiding van een HU-docent of -student, eerst op lage snelheid.
