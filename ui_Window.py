# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Checkliste(object):
    def setupUi(self, Checkliste):
        if not Checkliste.objectName():
            Checkliste.setObjectName(u"Checkliste")
        Checkliste.resize(800, 600)
        Checkliste.setStyleSheet(u"/* Grundlegende Einstellungen */\n"
"* {\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Hauptfenster */\n"
"QMainWindow {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* Titel und \u00dcberschriften */\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #52b1b1;\n"
"}\n"
"\n"
"/* Kn\u00f6pfe */\n"
"QPushButton {\n"
"    background-color: #52b1b1;\n"
"    color: #ffffff;\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3d8e8e;\n"
"    border-color: #3d8e8e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #296666;\n"
"    border-color: #296666;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;\n"
"    border-color: #cccccc;\n"
"    color: #666666;\n"
"}\n"
"\n"
"/* Eingabefelder */\n"
"QLineEdit, QTextEdit {\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"  "
                        "  padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border-color: #3d8e8e;\n"
"}\n"
"\n"
"/* Combobox */\n"
"QComboBox {\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #52b1b1;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png); /* Ersetzen Sie dies durch den Pfad zu Ihrem Pfeilsymbol */\n"
"}\n"
"\n"
"/* Tabellen */\n"
"QTableWidget {\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #52b1b1;\n"
"    color: #ffffff;\n"
"    padding: 4px;\n"
"    border: 1px solid #dddddd;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border: 1px so"
                        "lid #dddddd;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #3d8e8e;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Scrollbars */\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #dddddd;\n"
"    background: #f0f0f0;\n"
"    width: 15px;\n"
"    margin: 18px 0 18px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #52b1b1;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #dddddd;\n"
"    background: #f0f0f0;\n"
"    height: 14px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    image: url(up_arrow.png); /* Ersetzen Sie dies durch den Pfad zu Ihrem Pfeilsymbol */\n"
"}\n"
"\n"
"/* Fortschrittsbalken */\n"
"QProgressBar {\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #52b1b1;\n"
"    wid"
                        "th: 20px;\n"
"}\n"
"\n"
"/* Checkboxen */\n"
"QCheckBox {\n"
"    font-size: 25px;\n"
"    font-weight: bold;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
" 	content: \"\u2714\";\n"
"    border: 2px solid #52b1b1;\n"
"    border-radius: 5px;\n"
"    background-color: #52b1b1;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked::after {\n"
"    content: \"H\";\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    display: block;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 2px solid #3d8e8e;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #3d8e8e;\n"
"}\n"
"")
        self.Haupt_Widgets = QWidget(Checkliste)
        self.Haupt_Widgets.setObjectName(u"Haupt_Widgets")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        self.Haupt_Widgets.setFont(font)
        self.HauptWidgets = QVBoxLayout(self.Haupt_Widgets)
        self.HauptWidgets.setObjectName(u"HauptWidgets")
        self.LayoutUnterschriften = QHBoxLayout()
        self.LayoutUnterschriften.setSpacing(10)
        self.LayoutUnterschriften.setObjectName(u"LayoutUnterschriften")
        self.LayoutUnterschriften.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.LayoutUnterschriften.setContentsMargins(0, -1, 0, -1)
        self.widget = QWidget(self.Haupt_Widgets)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 50))
        self.widget.setMaximumSize(QSize(200, 50))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 72, 18))
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 18, 200, 32))
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(200, 16777215))

        self.LayoutUnterschriften.addWidget(self.widget, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.BTN_erledigt = QPushButton(self.Haupt_Widgets)
        self.BTN_erledigt.setObjectName(u"BTN_erledigt")
        self.BTN_erledigt.setMinimumSize(QSize(200, 50))
        self.BTN_erledigt.setMaximumSize(QSize(200, 50))
        self.BTN_erledigt.setFont(font)
        self.BTN_erledigt.setCursor(QCursor(Qt.PointingHandCursor))

        self.LayoutUnterschriften.addWidget(self.BTN_erledigt, 0, Qt.AlignLeft)


        self.HauptWidgets.addLayout(self.LayoutUnterschriften)

        Checkliste.setCentralWidget(self.Haupt_Widgets)

        self.retranslateUi(Checkliste)

        QMetaObject.connectSlotsByName(Checkliste)
    # setupUi

    def retranslateUi(self, Checkliste):
        Checkliste.setWindowTitle(QCoreApplication.translate("Checkliste", u"Checkliste", None))
        self.label.setText(QCoreApplication.translate("Checkliste", u"Unterschrift", None))
        self.BTN_erledigt.setText(QCoreApplication.translate("Checkliste", u"Alles Erledigt", None))
    # retranslateUi

