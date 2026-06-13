import requests
import json
import signal
import sys
import time as time
import os
import logging
import socket


base_url = "http://localhost:3000/signalk/v2/api/resources/"
tracks_pending_url = base_url + "tracks-pending"
uploaded_tracks_url = base_url + "uploaded-tracks"
RENDER_ENDPOINT = "https://gpxupload.onrender.com/upload-json"

running = True

script_dir = os.path.dirname(os.path.realpath(__file__))
log_file = os.path.join(script_dir, 'track_upload.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False


def handle_exit(sig, frame):
    global running
    logging.info("\Did not receive signal from signal K")
    running = False

# register signal handlers for graceful shutdown
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)


def process_tracks():
    global log_file
    if os.path.exists(log_file) and os.path.getsize(log_file) > 5 * 1024 * 1024:
        with open(log_file, 'r') as f:
            lines = f.readlines()
        with open(log_file, 'w') as f:
            f.writelines(lines[-100:])

    try:
        response = requests.get(tracks_pending_url, timeout=5)
        if response.status_code != 200:
            logging.error(f"could not fetch tracks. Status: {response.status_code}")
            return
        tracks = response.json()
        for track_id, track_data in tracks.items():
            if not running:
                logging.info("Closing process due to signal.")
                sys.exit(0)
            render_response = requests.post(RENDER_ENDPOINT, json=track_data, timeout=60)
            
            if render_response.status_code == 200:
                logging.info(f"Success: Track {track_id} uploaded.")
                mark_track_as_uploaded(track_id, track_data)
            else:
                logging.error(f"Error uploading {track_id}: {render_response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error processing tracks: {e}")


def mark_track_as_uploaded(track_id, track_data):
    try:
        put_response = requests.put(f"{uploaded_tracks_url}/{track_id}", json=track_data, timeout=5)
        
        if put_response.status_code in [200, 201]:
            #delete from pending
            del_response = requests.delete(f"{tracks_pending_url}/{track_id}", timeout=5)
            
            if del_response.status_code in [200, 202, 204]:
                logging.info(f"Track {track_id} moved from pending to uploaded successfully.")
            else:
                logging.error(f"Could not delete {track_id} from pending: {del_response.status_code}")
        else:
            logging.error(f"Could not create {track_id} in uploaded-tracks: {put_response.status_code}")

    except Exception as e:
        logging.error(f"Network error while moving {track_id}: {e}")

        
if __name__ == "__main__":
    if is_connected():
        process_tracks()
    else:
        exit(0)
