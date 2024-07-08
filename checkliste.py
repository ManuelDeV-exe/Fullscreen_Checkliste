import sys
import os

import PySide6
from PySide6.QtGui import *
from PySide6.QtWidgets import *

logo_Pfad = os.path.abspath(r'data/icon.png')
global config_file
config_file = os.path.abspath(r'config.cfg')

from ui_Window import Ui_Checkliste

class UICheckliste(QMainWindow):
    def __init__(self):
        super(UICheckliste, self).__init__()
        self.ui = Ui_Checkliste()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(str(logo_Pfad)))

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.add_checkbox_elements()

        self.ui.HauptWidgets.setAlignment(Qt.AlignCenter)
        self.ui.LayoutUnterschriften.setAlignment(Qt.AlignCenter)

        self.ui.BTN_erledigt.clicked.connect(self.check)

        self.showFullScreen()

    def check(self):
        self.close()

    def read_config(self):
        with open(config_file, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    
    def add_checkbox_elements(self):
        lines = self.read_config()
        for line in lines:
            self.checkbox = QCheckBox(line)
            self.ui.HauptWidgets.insertWidget(self.ui.HauptWidgets.count() - 1, self.checkbox)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    UiCore = UICheckliste()

    sys.exit(app.exec())