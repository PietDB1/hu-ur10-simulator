#!/usr/bin/env bash
# Wacht tot de robot-simulator klaar is en toon dan de directe links.

if [ -n "$CODESPACE_NAME" ]; then
  BASIS="https://${CODESPACE_NAME}"
  DOMEIN="${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
  ROBOT="${BASIS}-6080.${DOMEIN}/vnc.html?autoconnect=true&resize=scale"
  BLOKKEN="${BASIS}-8000.${DOMEIN}/"
else
  ROBOT="http://localhost:6080/vnc.html?autoconnect=true&resize=scale"
  BLOKKEN="http://localhost:8000/"
fi

echo ""
echo "Robot-simulator wordt opgestart, even geduld..."
for i in $(seq 1 120); do
  if (echo > /dev/tcp/127.0.0.1/6080) 2>/dev/null; then
    echo ""
    echo "=============================================================="
    echo " ROBOT KLAAR!  Open met Cmd/Ctrl + klik:"
    echo ""
    echo " 1. Robotscherm (PolyScope):"
    echo "    $ROBOT"
    echo ""
    echo " 2. Programmeren met blokken:"
    echo "    $BLOKKEN"
    echo ""
    echo " Daarna in het robotscherm: ON -> START -> OK"
    echo "=============================================================="
    echo ""
    exit 0
  fi
  sleep 2
done

echo "De robot is na 4 minuten nog niet klaar."
echo "Probeer later deze link: $ROBOT"
