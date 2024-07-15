import sys
import os
from screeninfo import get_monitors

import PySide6
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

logo_Pfad = os.path.abspath(r'data/icon.png')
global config_file

try: config = sys.argv[1]
except: config = ""

if ".cfg" in config:
    config_file = os.path.abspath(sys.argv[1])
else:
    config_file = os.path.abspath(r'config.cfg')

global MONITORE
MONITORE = []
for m in get_monitors():
    MONITORE.append(m)

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

        self.ui.BTN_erledigt.clicked.connect(self.check)


        MONI_width = 420
        MONI_heigth = 450
        posx = (MONITORE[0].width - MONI_width)
        posy = (MONITORE[0].height - MONI_heigth)
        self.resize(MONI_width, MONI_heigth)
        self.move(posx, posy-40)

        self.show()

    def check(self):
        if self.ui.lineEdit.text() == "": return
        self.close()

    def read_config(self):
        with open(config_file, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    
    def add_checkbox_elements(self):
        lines = self.read_config()
        for line in reversed(lines):
            self.checkbox = QCheckBox(line)
            self.checkbox.setCursor(Qt.PointingHandCursor)
            self.ui.HauptWidgets.insertWidget(0, self.checkbox)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    UiCore = UICheckliste()

    sys.exit(app.exec())