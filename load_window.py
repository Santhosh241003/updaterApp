from packages import *
from Style_sheet import *
from visualize_plots_window import *
from logo_loading import *

class LoadWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #style sheet
        self.setWindowTitle("Let's start!!!")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_length = screen_geometry.width()
        screen_width = screen_geometry.height()
        
        # Set window size as a percentage of screen size
        pos_x = int(screen_length * 0.098)  
        pos_y = int(screen_width * 0.092)
        

        # window geometry
        self.setGeometry(pos_x,pos_y, int(screen_length*0.78), int(screen_width*0.858))

        #central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #vboxlayout
        layout = QVBoxLayout(central_widget)
        layout.addSpacerItem(QSpacerItem(20, int(0.25*screen_width), QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        
        self.load_button = QPushButton('Load Data File', self)
        self.load_button.setObjectName("loadButton")
        self.load_button.setMinimumSize(int(screen_length*0.13), int(screen_width*0.06))
        self.load_button.clicked.connect(self.loading_data)
        layout.addWidget(self.load_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(QSpacerItem(20, int(0.25*screen_width), QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        
        
    # def load_data(self):
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(resource_path('assets/load_pic.png')) # Ensure the image exists
        painter.drawPixmap(self.rect(), pixmap)  # Scale image to fit window

    def loading_data(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Data File", "", 
            "Data Files (*.zip);;All Files (*)"
        )
        if file_path:
            try:
                if file_path.endswith('.zip'):
                    
                    
                    # Create a temporary directory to extract files
                    zip_filename = os.path.splitext(os.path.basename(file_path))[0]
                    temp_dir = os.path.join(os.path.dirname(file_path), zip_filename)
                    os.makedirs(temp_dir, exist_ok=True)
                    
                    # Extract the zip file
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)
                        
                    # Now you can access the extracted files in temp_dir
                    extracted_files = os.listdir(temp_dir)
                    for i in extracted_files:
                        # Create the full path to the .orb file
                        if i.endswith('.orb'):
                            orb_file_path = os.path.join(temp_dir, i)
                            
                            # Create the new zip filename
                            zip_filename = i.replace('.orb', '.zip')
                            zip_file_path = os.path.join(temp_dir, zip_filename)
                            
                            # Copy the .orb file to a new .zip file
                            shutil.copy2(orb_file_path, zip_file_path)
                            
                            # Create the output directory for extraction
                            temp_dir_2 = os.path.join(temp_dir, i.replace('.orb', ''), 'raw_files')
                            os.makedirs(temp_dir_2, exist_ok=True)
                            
                            # Extract the zip file
                            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                                zip_ref.extractall(temp_dir_2)
                        
                        # print(f"Extracted {i} to {temp_dir_2}")

                    
                else:
                    raise ValueError("Unsupported file format")
                self.viz_window = VisualizationWindow(file_path= temp_dir_2)
                # self.viz_window = VisualizationWindow()
                self.viz_window.show()
                self.close()
            except Exception as e:
                error_dialog = QWidget()
                error_dialog.setWindowTitle("Error")
                error_dialog.setGeometry(400, 400, 300, 100)
                error_layout = QVBoxLayout(error_dialog)
                error_layout.addWidget(QLabel(f"Error loading data: {str(e)}"))
                error_dialog.show()
