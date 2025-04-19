import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                           QHBoxLayout, QFileDialog, QWidget, QLabel, QSplitter,
                           QScrollArea, QTextEdit,QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt6.QtGui import QScreen
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import letter,landscape,A4
from reportlab.lib.styles import getSampleStyleSheet
from PyQt6.QtGui import QIcon,QColor, QLinearGradient, QBrush,QPainter, QPixmap,QFont
# import pyqtgraph as pg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import zipfile
import shutil
import seaborn as sns
from PyQt6.QtWidgets import QMessageBox
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import Color,white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import textwrap
from reportlab.pdfbase.pdfmetrics import stringWidth
from io import BytesIO,StringIO
from reportlab.lib.utils import ImageReader
import json