import platform
import pywinstyles
import psutil
import subprocess
import os
import sys
from HDP_Backend import *
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QColorDialog, QFontDialog, QDialog, \
    QHBoxLayout, QComboBox,QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QColor

app = QApplication(sys.argv)
icon_path = os.path.join(os.path.dirname(__file__), 'Icons', 'hardwareicon.ico')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hardware Detection Program - Main');
        self.resize(1280, 840)
        self.setWindowIcon(QIcon(icon_path))
        pywinstyles.apply_style(self, "win7")

        button_style = """
                    QPushButton {
                background-color: rgba(169, 169, 169, 0.5);  /* Gray with 50% transparency */
                border: 2px solid rgba(0, 0, 0, 0.1);  /* Black border with 90% transparency */
                border-radius: 10px;  /* Less curved edges */
                font-family: "Segoe UI";  /* Set button font to Windows 7 font */
                font-size: 16px;  /* Font size */
            }
                """

        label_MAIN = QLabel("HDP - Main")
        label_MAIN.setAlignment(Qt.AlignCenter)
        label_MAIN.setFixedSize(300, 90)
        font = QFont("Segoe UI", 30)
        label_MAIN.setFont(font)

        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_MAIN)
        label_layout.addStretch()

        # Buttons setup
        CPU_button = QPushButton("CPU")
        CPU_button.setCheckable(True)
        CPU_button.setFixedSize(150, 150)
        CPU_button.setStyleSheet(button_style)
        CPU_button.clicked.connect(self.clb_CPU)

        System_button = QPushButton("System")
        System_button.setCheckable(True)
        System_button.setFixedSize(150, 150)
        System_button.setStyleSheet(button_style)
        System_button.clicked.connect(self.clb_System)

        GPU_button = QPushButton("GPU")
        GPU_button.setCheckable(True)
        GPU_button.setFixedSize(150, 150)
        GPU_button.setStyleSheet(button_style)
        GPU_button.clicked.connect(self.clb_GPU)

        Memory_button = QPushButton("Memory")
        Memory_button.setCheckable(True)
        Memory_button.setFixedSize(150, 150)
        Memory_button.setStyleSheet(button_style)
        Memory_button.clicked.connect(self.clb_Memory)

        Network_button = QPushButton("Network")
        Network_button.setCheckable(True)
        Network_button.setFixedSize(150, 150)
        Network_button.setStyleSheet(button_style)
        Network_button.clicked.connect(self.clb_Network)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        top_layout = QHBoxLayout()

        layout.addLayout(label_layout)
        layout.addSpacing(120)

        top_layout.addWidget(CPU_button)
        top_layout.addWidget(System_button)
        top_layout.addWidget(GPU_button)
        top_layout.addWidget(Memory_button)
        top_layout.addWidget(Network_button)

        top_layout.setSpacing(50)
        top_layout.insertStretch(0, 1)
        top_layout.addStretch(1)

        layout.addLayout(top_layout)
        layout.addStretch()
        layout.setContentsMargins(100, 150, 100, 100)

    def clb_CPU(self):
        window.close()
        window_CPU.show()
    def clb_System(self):
        window.close()
        window_SYSTEM.show()
    def clb_GPU(self):
        window.close()
        window_GPU.show()
    def clb_Memory(self):
        window.close()
        window_MEMORY.show()
    def clb_Network(self):
        window.close()
        window_NETWORK.show()

class CPU(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hardware Detection Program - CPU')
        self.resize(1080, 840)
        self.setWindowIcon(QIcon(icon_path))
        self.setStyleSheet("QMainWindow {"
                           "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                           "stop:0 gray, stop:1 white);"
                           "}")
        #pywinstyles.apply_style(self, "dark")
        pywinstyles.apply_style(self, "win7")


        label_CPU = QLabel("CPU - About")
        label_CPU.setAlignment(Qt.AlignCenter)
        label_CPU.setFixedSize(300, 90)
        font = QFont("Arial", 30)  # Its better to create a font = whatever and then put it in .setFont()
        label_CPU.setFont(font)
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_CPU)
        label_layout.addStretch()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_back)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_button)

        layout = QVBoxLayout(central_widget)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        layout.addStretch()

    def go_back(self):
        self.close()
        window.show()

class GPU(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hardware Detection Program - CPU')
        self.resize(1080, 840)
        self.setWindowIcon(QIcon(icon_path))
        self.setStyleSheet("QMainWindow {"
                           "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                           "stop:0 gray, stop:1 white);"
                           "}")
        pywinstyles.apply_style(self, "win7")

        label_GPU = QLabel("GPU - About")
        label_GPU.setAlignment(Qt.AlignCenter)
        label_GPU.setFixedSize(300, 90)
        font = QFont("Arial", 30)  # Its better to create a font = whatever and then put it in .setFont()
        label_GPU.setFont(font)
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_GPU)
        label_layout.addStretch()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_back)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_button)

        layout = QVBoxLayout(central_widget)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        layout.addStretch()

    def go_back(self):
        self.close()  # Close CPU window
        window.show()

class SYSTEM(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('Hardware Detection Program - SYSTEM')
        self.resize(1080, 840)
        self.setStyleSheet("QMainWindow {"
                           "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                           "stop:0 gray, stop:1 white);"
                           "}")
        pywinstyles.apply_style(self, "win7")

        label_CPU = QLabel("SYSTEM - About")
        label_CPU.setAlignment(Qt.AlignCenter)
        label_CPU.setFixedSize(300, 90)
        font = QFont("Arial", 30)  # Its better to create a font = whatever and then put it in .setFont()
        label_CPU.setFont(font)
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_CPU)
        label_layout.addStretch()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_back)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_button)

        layout = QVBoxLayout(central_widget)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        layout.addStretch()

    def go_back(self):
        self.close()  # Close CPU window
        window.show()

class NETWORK(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('Hardware Detection Program - NETWORK')
        self.resize(1080, 840)
        self.setStyleSheet("QMainWindow {"
                           "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                           "stop:0 gray, stop:1 white);"
                           "}")
        pywinstyles.apply_style(self, "win7")

        label_CPU = QLabel("NETWORK - About")
        label_CPU.setAlignment(Qt.AlignCenter)
        label_CPU.setFixedSize(400, 90)
        font = QFont("Arial", 30)  # Its better to create a font = whatever and then put it in .setFont()
        label_CPU.setFont(font)
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_CPU)
        label_layout.addStretch()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_back)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_button)

        layout = QVBoxLayout(central_widget)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        layout.addStretch()

    def go_back(self):
        self.close()  # Close CPU window
        window.show()

class MEMORY(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('Hardware Detection Program - MEMORY')
        self.resize(1080, 840)
        self.setStyleSheet("QMainWindow {"
                           "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
                           "stop:0 gray, stop:1 white);"
                           "}")
        pywinstyles.apply_style(self, "win7")

        label_CPU = QLabel("MEMORY - About")
        label_CPU.setAlignment(Qt.AlignCenter)
        label_CPU.setFixedSize(400, 90)
        font = QFont("Arial", 30)  # Its better to create a font = whatever and then put it in .setFont()
        label_CPU.setFont(font)
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(label_CPU)
        label_layout.addStretch()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        back_button = QPushButton("Back", self)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.go_back)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(back_button)

        layout = QVBoxLayout(central_widget)
        layout.addLayout(label_layout)
        layout.addLayout(button_layout)
        layout.addStretch()

    def go_back(self):
        self.close()
        window.show()


#Necessary properties
window = MainWindow()
window.setMaximumSize(1600, 900)
window.show()

window_CPU = CPU()
window_CPU.setMaximumSize(1600, 900)

window_GPU = GPU()
window_GPU.setMaximumSize(1600, 900)

window_SYSTEM = SYSTEM()
window_SYSTEM.setMaximumSize(1600, 900)

window_NETWORK = NETWORK()
window_NETWORK.setMaximumSize(1600, 900)

window_MEMORY = MEMORY()
window_MEMORY.setMaximumSize(1600, 900)


app.exec()
