from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QIcon
from load_window import *
from Style_sheet import *
from logo_loading import *
from pyupdater.client import Client
from client_config import ClientConfig
import sys
import os

__version__ = '1.0.0'

def check_for_updates():
    client = Client(ClientConfig())
    app_update = client.update_check(ClientConfig.APP_NAME, __version__)
    
    if app_update:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("An update is available. Would you like to download and install it?")
        msg.setWindowTitle("Update Available")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            downloaded = app_update.download()
            if downloaded:
                if app_update.is_downloaded():
                    app_update.extract_restart()
                    return True
            QMessageBox.warning(None, "Update Failed", "Failed to download and install the update.")
    return False

def main():
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('assets/logo.png')))
    app.setStyleSheet(STYLESHEET)
    
    if not check_for_updates():
        load_window = LoadWindow()
        load_window.show()

    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()