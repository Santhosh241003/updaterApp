from Export_pdf import export_to_pdf
from packages import *
from Style_sheet import *
from Export_pdf import *
from algorithm import *

class VisualizationWindow(QMainWindow):
    def __init__(self, file_path):
        super().__init__()
        # self.processed_data=self.process_data(file_path)
        self.file_path = file_path
        self.filename = os.path.basename(file_path)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.screen_length = screen_geometry.width()
        self.screen_width = screen_geometry.height()
        plt.style.use('dark_background')
        self.canvas = FigureCanvas(plt.figure(facecolor='black'))
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setFixedWidth(int(self.screen_length*0.20))
        self.toolbar.setStyleSheet(toolbar_css)
        self.data=process_data(file_path)
        self.plots_data={}
        self.precomputed_figures = {}
        # self.save_precomputed_plots(self.data)
        self.visualiseWindow_ui(self.data)
        
        

    # def save_precomputed_plots(self,data):
    #     """Generate and store figures in memory instead of saving as files."""

        
        
        # fig = self.canvas.figure
        # fig.set_facecolor('black')  # Set background color to black
        
        # ax = fig.add_subplot(111)
        # ax.set_facecolor('#121212')
        
        # x = np.linspace(0, 10, 100)
        # if metric == "Focus":
        #     y = np.sin(x)
        #     text = "Focus represents attention level over time. A higher value means better focus."
        # elif metric == "Cognitive Load":
        #     y = np.cos(x)
        #     text = "Cognitive Load indicates how much mental effort is being used. A lower value suggests a relaxed state."
        # elif metric == "Relaxation":
        #     y = np.sin(x) * np.cos(x)
        #     text = "Relaxation level is a balance of mental focus and physical calmness."
        # else:
        #     y = x
        #     text = "Select a metric to view data."
        
        # sns.set_style("whitegrid")
        # sns.set_style("dark")
        # sns.lineplot(x=x, y=y, marker="o", color="cyan", ax=ax)
        
        # ax.set_title(metric, color='white', fontsize=14)
        # ax.tick_params(colors='white')  # Set tick color to white
        # ax.spines['bottom'].set_color('white')
        # ax.spines['left'].set_color('white')


        # metrics = {
        #     "Focus": (np.sin, "Focus represents attention level over time."),
        #     "Cognitive Load": (np.cos, "Cognitive Load indicates mental effort."),
        #     "Relaxation": (lambda x: np.sin(x) * np.cos(x), "Relaxation level is a balance of mental focus and calmness.")
        # }

        

        # for metric, (func, text) in metrics.items():
        #     x = range(len(data))
        #     y = data

            
        #     # fig.set_facecolor('black')
        #     fig,ax = plt.subplots(figsize=(12,5))
        #     fig.patch.set_facecolor('#111111')  # Dark background for the figure
        #     ax.set_facecolor('#191919')


        #     # sns.set_style("dark")
        #     # sns.lineplot(x=x, y=y, marker="o", color="cyan", ax=ax)

        #     ax.plot(x, y, color='lime', linewidth=1, label='Relaxation Curve')
        #     # Add a reference line at y=40
        #     ax.axhline(y=0.5, color='gray', linestyle='dashed', linewidth=1.2, label='Reference Line')
        #     # Customize grid
        #     ax.grid(color='#333333', linestyle='--', linewidth=0.5)
        #     # Set labels with styling
        #     ax.set_xlabel("Time (In seconds)", fontsize=12, color='white', fontweight='bold')
        #     ax.set_ylabel(metric+" Score", fontsize=12, color='white', fontweight='bold')
        #     # Set title
        #     ax.set_title(metric, fontsize=14, color='white', fontweight='bold', loc='center')
        #     # Customize ticks
        #     ax.tick_params(axis='both', colors='white', labelsize=10)
        #     # Customize legend
        #     ax.legend(facecolor='#222222', edgecolor='white', fontsize=10)
            # ax.set_title(metric, color='white', fontsize=14)
            # ax.tick_params(colors='white')
            # ax.spines['bottom'].set_color('white')
            # ax.spines['left'].set_color('white')

            # ax.set_facecolor("#121212")  # Dark gray background
            # ax.patch.set_linewidth(3) 
            # ax.patch.set_boxstyle("round,pad=0.1")
        #     for spine in ax.spines.values():
        #         spine.set_linewidth(2)  # Increase thickness
        #         spine.set_capstyle('round')

        #     self.precomputed_figures[metric] = fig  # Store figure object

        # print("Precomputed plots saved in memory!")
    
    # def display_saved_plot(self, metric):
    #     """Retrieve and show the precomputed figure when called."""
    #     # if metric not in self.precomputed_figures:
    #     #     print(f"Figure for {metric} not found.")
    #     #     return

    #     # self.canvas.figure=None
    #     fig = self.precomputed_figures[metric]  # Retrieve precomputed figure
    #     # self.canvas.figure = fig  # Assign figure to canvas
    #     # self.canvas.draw()


    #     self.canvas.figure = fig
    #     self.canvas.draw()
        

    #     self.canvas.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    #     self.canvas.updateGeometry()
    #     self.right_layout.addWidget(self.canvas,alignment=Qt.AlignmentFlag.AlignCenter)


    #     # self.text_label.setText(text)
    #     self.text_label.setStyleSheet(text_color_bold)
    #     self.right_layout.addWidget(self.summary_keyword_txt)
    #     self.right_layout.addWidget(self.text_label)

    def visualiseWindow_ui(self,data=None):
        self.setWindowTitle('Data Visualization')

        # self.setGeometry(150, 75, 1400, 800)

        #setting into full screen mode
        screen = QApplication.instance().primaryScreen()
        screen_rect = screen.availableGeometry()
        self.setGeometry(screen_rect)

        # Main central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Create horizontal splitter
        # splitter = QSplitter(Qt.Orientation.Horizontal)
        left_widget= QWidget()
        left_widget.setFixedWidth(int(self.screen_length*0.20))
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)




        # main heading
        self.label = QLabel("Performance Metrics", left_widget)
        font = QFont("Arial", 18)  # Font: Arial, Size: 18, Bold
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")  # White text color
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)  # Align to top center
        self.label.setContentsMargins(0, 10, 0, 0)  # Set label position


        focus_text,cognitive_text,relaxation_text=self.get_summary_text(data)


        # first option 
        self.focus_btn = QPushButton('Focus')
        self.focus_btn.clicked.connect(lambda :self.generate_dummy_data('Focus',data,focus_text))

        #second option
        self.Cognitive_load_btn = QPushButton('Cognitive Load')
        self.Cognitive_load_btn.clicked.connect(lambda :self.generate_dummy_data('Cognitive load',data,cognitive_text))

        #third section
        self.relax_btn= QPushButton('Relaxation')
        self.relax_btn.clicked.connect(lambda :self.generate_dummy_data('Relaxation',data,relaxation_text))
        
        # Export pdf button
        self.export_btn= QPushButton('Export into PDF')
        self.export_btn.clicked.connect(lambda : export_to_pdf(self,self.plots_data,self.data))

        

        # adding stylesheet to buttons
        self.focus_btn.setStyleSheet(visualize_button_style)
        self.Cognitive_load_btn.setStyleSheet(visualize_button_style)
        self.relax_btn.setStyleSheet(visualize_button_style)
        self.export_btn.setStyleSheet(export_btn)



        self.right_widget=QWidget()
        self.right_layout=QVBoxLayout(self.right_widget)
        self.summary_keyword_txt=QLabel()

        self.text_label=QLabel()
        self.text_label.setWordWrap(True)  # Ensure text wraps within the label width
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
      




        left_layout.addWidget(self.label)
        left_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        left_layout.addWidget(self.focus_btn)
        left_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        left_layout.addWidget(self.Cognitive_load_btn)
        left_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        left_layout.addWidget(self.relax_btn)
        left_layout.addSpacerItem(QSpacerItem(2000, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        left_layout.addWidget(self.export_btn)
        left_widget.setLayout(left_layout)

        self.right_layout.addWidget(self.toolbar)
        self.right_layout.addWidget(self.canvas)

        self.right_widget.setLayout(self.right_layout)
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)


        self.show()

    def generate_dummy_data(self, metric,data,text_summary,draw=1):

        plt.rcdefaults()
        plt.figure(self.canvas.figure.number)
        plt.clf()
        fig = self.canvas.figure
        fig.set_facecolor('black')  # Set background color to black
        
        ax = fig.add_subplot(111)
        ax.set_facecolor('#121212')
        
        
        if metric == "Focus":
            y = data['Focus']
            x=range(len(y))


        elif metric == "Cognitive load":
            y = data['Cognitive load']
            x=range(len(y))

        elif metric == "Relaxation":
            y = data['Relaxation']
            x=range(len(y))
        
        
        # sns.set_style("whitegrid")
        sns.set_style("dark")
        sns.lineplot(x=x, y=y, color="cyan", ax=ax)
        
        ax.set_title(metric, color='#FFFF33', fontsize=14, fontweight='bold')
        ax.tick_params(colors='white')  # Set tick color to white
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        self.canvas.figure = fig
        self.plots_data[metric]=fig
        if draw:
            self.canvas.draw()

        self.summary_keyword_txt.setText('Summary')
        self.summary_keyword_txt.setMaximumHeight(50)
        self.summary_keyword_txt.setStyleSheet(summary_text_css)
        self.summary_keyword_txt.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.text_label.setText(text_summary)
        self.text_label.setStyleSheet(text_color_bold)
        self.text_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        

        self.right_layout.addWidget(self.summary_keyword_txt)
        self.right_layout.addWidget(self.text_label)
        
    def get_summary_text(self,data=None):

        #### will be generated using llms ####
        focus_text="Focus is measured by analyzing linked to and goal-directed tasks. The focus starts at a moderate level (~44), suggesting the user is engaged but not fully immersed initially. It gradually increases, peaking (~70) as the user becomes more attentive or encounters something mentally stimulating or challenging. While there are slight dips later on, focus remains relatively high, indicating consistent engagement with the task despite minor shifts in attention."
        cognitive_text="Cognitive load is evaluated using the . Theta waves (4–8 Hz) increase during working memory use, while beta waves increase with higher engagement. Cognitive load stays moderate (~30 45) throughout, reflecting a steady level of Peaks in cognitive load often overlap with high focus scores, indicating moments where the user is processing something complex or challenging .The relative stability of cognitive load, with only slight dips, suggests the task is demanding but manageable overall."
        relaxation_text="Relaxation is calculated by monitoring waves, which dominate in. The relaxation score starts relatively high (~41-57), showing the user is calm and comfortable at the beginning. Over time, relaxation gradually decreases, with noticeable dips. This could mean the task is becoming more demanding or slightly stressful as it progresses. Occasional recoveries suggest moments where the user feels at ease, possibly during simpler or more familiar parts of the task. The downward trend toward the end could reflect growing mental fatigue or increased effort in handling the task."

        return focus_text,cognitive_text,relaxation_text
        
        
        

        # # First horizontal section
        # first_section = QWidget()
        # first_layout = QVBoxLayout(first_section)
        # self.figure1 = Figure(figsize=(5, 4), dpi=100)
        # self.canvas1 = FigureCanvas(self.figure1)
        # first_layout.addWidget(self.canvas1)
        # self.plot_data(self.figure1,self.canvas1,1)
        # left_layout.addWidget(first_section)
        
        # # # Second horizontal section
        # second_section = QWidget()
        # second_layout = QVBoxLayout(second_section)
        # self.figure2 = Figure(figsize=(5, 4), dpi=100)
        # self.canvas2 = FigureCanvas(self.figure2)
        # second_layout.addWidget(self.canvas2)
        # self.plot_data(self.figure2,self.canvas2,2)
        # left_layout.addWidget(second_section)
        
        # # # Third horizontal section
        # third_section = QWidget()
        # third_layout = QVBoxLayout(third_section)
        # self.figure3 = Figure(figsize=(5, 4), dpi=100)
        # self.canvas3 = FigureCanvas(self.figure3)
        # third_layout.addWidget(self.canvas3)
        # self.plot_data(self.figure3,self.canvas3,3)
        # left_layout.addWidget(third_section)
        
        # # Make left section scrollable
        # left_scroll = QScrollArea()
        # left_scroll.setWidget(left_widget)
        # left_scroll.setWidgetResizable(True)
        
        # # Right section
        # right_widget = QWidget()
        # right_layout = QVBoxLayout(right_widget)
        
        # # Heading
        # self.heading = QLabel("Summary")
        # self.heading.setStyleSheet("font-size: 18pt; font-weight: bold;")
        # # heading.setFixedHeight(50)
        # # heading.setAlignment(Qt.AlignmentFlag.AlignTopCentre)
        # # print(heading.height())
        
        
        # # Summary text area
        # self.summary_text = QTextEdit()
        # self.summary_text.setReadOnly(True)
        

        # # Export button
        # self.export_button = QPushButton("Export to PDF")
        # self.export_button.setObjectName('exportPDFButton')
        # self.export_button.setMinimumSize(100, 40)  # At least 100x40
        # self.export_button.setMaximumSize(400, 100)  # At most 200x60

        # self.export_button.clicked.connect(self.export_to_pdf)
        # right_layout.addWidget(self.heading, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        # right_layout.addWidget(self.summary_text)
        # right_layout.addWidget(self.export_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        # right_layout.addStretch()  # Ensures proper spacing at the bottom


        # # # Add widgets to splitter
        # splitter.addWidget(left_scroll)
        # splitter.addWidget(right_widget)
        
        # Set initial sizes (60% left, 40% right)
        # splitter.setSizes([840, 560])
        
        # # Add splitter to main layout
        # main_layout.addWidget(splitter)
        
        # Plot initial data
        
    # def process_data(path):
    #     return None
    # def plot_data(self,figure,canvas,i):
    #     """Plot graph inside FigureCanvas"""
    #     figure.clear() 
    #     ax = figure.add_subplot(111)
    #     x = np.arange(i*50+0, i*50+50)
    #     y = np.arange(i*50+0, i*50+50)
    #     ax.plot(x, y)
    #     ax.set_title("Data Visualization")
    #     canvas.draw()
    