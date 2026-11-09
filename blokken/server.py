"""
Kleine webserver voor de blokkenomgeving.
- Serveert de blokkenpagina (index.html) op poort 8000
- /uitvoeren : voert de Python-code uit die de blokken maken (stuurt de robot aan)
- /stop      : stopt de robot
- /aanzetten : zet de robot aan (ON + remmen los)
Start: python3 blokken/server.py   (gebeurt in de Codespace automatisch)
"""
import json
import os
import subprocess
import sys
import tempfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

MAP = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(MAP)            # map waar robot.py staat
POORT = int(os.environ.get("BLOKKEN_POORT", "8000"))


def draai_python(code, timeout=30):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        pad = f.name
    try:
        env = dict(os.environ, PYTHONPATH=ROOT)
        res = subprocess.run([sys.executable, pad], cwd=ROOT, env=env,
                             capture_output=True, text=True, timeout=timeout)
        return res.returncode == 0, (res.stdout + res.stderr).strip()
    except subprocess.TimeoutExpired:
        return False, "Het programma duurde te lang (meer dan 30 seconden)."
    finally:
        os.unlink(pad)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=MAP, **kw)

    def log_message(self, *args):
        pass  # geen rommel in de terminal

    def _json(self, ok, tekst):
        body = json.dumps({"ok": ok, "uitvoer": tekst}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        lengte = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(lengte) or b"{}")
        if self.path == "/uitvoeren":
            ok, uit = draai_python(data.get("code", ""))
        elif self.path == "/stop":
            ok, uit = draai_python("from robot import Robot\nRobot().stop()")
        elif self.path == "/aanzetten":
            ok, uit = draai_python("from robot import Robot\nRobot().zet_aan()")
        else:
            ok, uit = False, "Onbekende opdracht"
        if not ok and "Connection refused" in uit:
            uit = "Robot niet bereikbaar. Is de simulator al opgestart?\n\n" + uit
        self._json(ok, uit)


if __name__ == "__main__":
    print(f"Blokkenomgeving draait op poort {POORT}")
    ThreadingHTTPServer(("0.0.0.0", POORT), Handler).serve_forever()
