Installation

    Download all files to your Raspberry Pi.

    Make the installation script executable:
    chmod +x install.sh

    Run the installation:
    ./install.sh


    IF IT DOESN'T WORK, THEN IT MIGHT BE BECAUSE OF HOW LINUX READS LINECHANGES. USE:
    sudo apt-get install -y dos2unix

    dos2unix install.sh

    dos2unix 99-track-upload.sh

    Then try again

    sudo ./install.sh
    


## Before running, ensure that RENDER_ENDPOINT in upload.py is set to your specific endpoint, for instance Render.com

Make sure Signal K ressources have the folders uploaded-tracks and tracks-pending. Or change the names in your version of the app.

For better experience, add a cron job:

    crontab -e

Then add this line at the bottom:

    0 * * * * /usr/bin/python3 /home/pi/Desktop/PiUpload/upload.py

Replace the path if you saved the project somewhere else.

How it works

    When internet is established, the program
    then gets the tracks recorded during sailing, and uploads them.
    If successfull moves the pending tracks to uploaded tracks as to not have duplicates.

    


Requires a Pi with Pi OS and Python 3.

Is intended to work with: https://github.com/BirkJefta/piTracks and https://github.com/BirkJefta/GPXUpload
