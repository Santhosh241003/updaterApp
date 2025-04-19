import requests
import json
import os
import sys
import zipfile
import logging
from pathlib import Path

class Updater:
    def __init__(self):
        self.update_url = 'http://localhost:8000/updates/version.json'
        self.current_dir = Path(os.path.dirname(os.path.abspath(__file__)))

    def check_for_updates(self, current_version):
        try:
            response = requests.get(self.update_url)
            if response.status_code == 200:
                version_info = response.json()
                server_version = version_info['version']
                if self._version_is_newer(server_version, current_version):
                    return True, version_info
            return False, None
        except Exception as e:
            logging.error(f"Error checking for updates: {str(e)}")
            return False, None

    def _version_is_newer(self, server_version, current_version):
        server_parts = [int(x) for x in server_version.split('.')]
        current_parts = [int(x) for x in current_version.split('.')]
        return server_parts > current_parts

    def download_and_install_update(self, version_info):
        try:
            download_url = version_info['download_url']
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                update_zip = self.current_dir / 'update.zip'
                with open(update_zip, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Extract update
                with zipfile.ZipFile(update_zip, 'r') as zip_ref:
                    zip_ref.extractall(self.current_dir)

                # Clean up
                os.remove(update_zip)
                return True
            return False
        except Exception as e:
            logging.error(f"Error during update: {str(e)}")
            return False
