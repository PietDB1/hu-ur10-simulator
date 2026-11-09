#!/usr/bin/env bash
# Wacht tot de robot-simulator klaar is en toon dan de directe link.

if [ -n "$CODESPACE_NAME" ]; then
  URL="https://${CODESPACE_NAME}-6080.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/vnc.html?autoconnect=true&resize=scale"
else
  URL="http://localhost:6080/vnc.html?autoconnect=true&resize=scale"
fi

echo ""
echo "Robot-simulator wordt opgestart, even geduld..."
for i in $(seq 1 120); do
  if (echo > /dev/tcp/127.0.0.1/6080) 2>/dev/null; then
    echo ""
    echo "=============================================================="
    echo " ROBOT KLAAR! Open de robot via deze link (Cmd/Ctrl + klik):"
    echo ""
    echo " $URL"
    echo ""
    echo " Daarna in de robot: ON -> START -> OK"
    echo "=============================================================="
    echo ""
    exit 0
  fi
  sleep 2
done

echo "De robot is na 4 minuten nog niet klaar."
echo "Probeer later deze link: $URL"
