Installation

    Download all files to your Raspberry Pi.

    Make the installation script executable:
    chmod +x install.sh

    Run the installation:
    ./install.sh





#Before running, ensure that RENDER_ENDPOINT in upload.py is set to your specific endpoint, for instance Render.com

Make sure Signal K ressources have the folders uploaded-tracks and tracks-pending. Or change the names in your version of the app

How it works

    When internet is established, the program
    then gets the tracks recorded during sailing, and uploads them.
    If successfull moves the pending tacks to uploaded tracks as to not have duplicates.

    


requires a pi with pi os and python 3.

Is intended to work with:https://github.com/BirkJefta/piTracks and https://github.com/BirkJefta/GPXUpload
