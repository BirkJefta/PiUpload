#checks for Wi-Fi connection and runs upload.py when connected
#!/bin/bash
INTERFACE=$1
ACTION=$2

case "$ACTION" in
    up)
        if [ "$INTERFACE" = "wlan0" ]; then
            # Kør upload med det samme, når vi får Wi-Fi
            /usr/bin/python3 /home/pi/Desktop/Hovedopgave2/PiUpload/upload.py
        fi
        ;;
esac