import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class OSDetectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OS Detector")
        self.setGeometry(100, 100, 300, 100)

        label = QLabel(self)
        if sys.platform.startswith("darwin"):
            label.setText("You are on MacOS")
        elif sys.platform.startswith("win"):
            label.setText("You are on Windows")
        else:
            label.setText("Unknown Operating System")

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OSDetectorApp()
    window.show()
    sys.exit(app.exec())
