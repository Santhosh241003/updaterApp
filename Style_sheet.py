STYLESHEET = """
QSplitter::handle {
    background-color: #d4d4d4;
}
VisualizationWindow{
    background-color: black;
}
QPushButton#loadButton {
    background-color: #FFFFFF;
    color: black;
    border-radius: 5px;
    font-weight: bold;
    padding: 10px;
    border: none;
}

QPushButton#loadButton:hover {
    background-color: #D8E2DA;
}

QPushButton#loadButton:pressed {
    background-color: #BDCBC0;
}
QPushButton#exportPDFButton {
    background-color: #dc422c;
    color: white;
    border-radius: 5px;
    font-weight: bold;
    padding: 10px;
    border: none;
}

QPushButton#exportPDFButton:hover {
    background-color: #b4210c;
}

QPushButton#exportPDFButton:pressed {
    background-color: #110f0f;
}
"""
toolbar_css="""
                QToolBar { background-color: white; border: none; }
                QToolButton { color: white; background-color: transparent; }
                QToolButton:hover { background-color: rgba(255, 255, 255, 0.1); }
            """
summary_text_css="""
QLabel {
    color: #FFB74D;
    font-size: 25px;
    font-weight: bold;
    background-color: transparent;
    padding: 3px;
}
"""
text_color_bold="""
QLabel {
    color: #E0E0E0;
    font-size: 16px;
    font-weight: bold;
}
"""
visualize_button_style = """
            QPushButton {
                background-color: #FFFFFF;
                color: black;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
                border: 1px solid #1F618D;
                min-width: 100px;
                max-width: 300px;
                margin: 0 auto 0 auto;
            }
            QPushButton:hover {
                background-color: #BDCBC0;
            }
            QPushButton:pressed {
                background-color: #BDCBC0;
            }
        """
export_btn="""
        QPushButton {
                background-color: #FFFFFF;
                color: black;
                font-size: 15px;
                font-weight: bold;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #1F618D;
            }
            QPushButton:hover {
                background-color: #BDCBC0;
            }
            QPushButton:pressed {
                background-color: #BDCBC0;
            }
"""
