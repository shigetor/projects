import sys

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings, Qt
from myapp import Ui_MainWindow

from PyQt5 import QtWidgets, QtCore

SETTINGS_TRAY = 'settings/tray'


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self._createActions()
        self._createToolBars()
        self._createContextMenu

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        # Edit menu
        editMenu = menuBar.addMenu("Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        # Help menu
        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)
        editMenu.addAction(self.cutAction)
        # Find and Replace submenu in the Edit menu
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")
        self.setWindowTitle('desktop')
        self.all_dates = {}
        self.button1.clicked.connect(self.find_date)
        self.button2.clicked.connect(self.delete_note)
        self.pushButton.clicked.connect(self.weather)
        self.button1.setStyleSheet("background-color: green;")
        self.button2.setStyleSheet("background-color:red")
        self.label.setStyleSheet('border-style: solid; border-width: 1px;background-color:#FFFFD2')
        self.frame.setStyleSheet('border-style: solid; border-width: 1px;background-color:#BBDED6')
        self.frame_2.setStyleSheet('border-style: solid; border-width: 1px;background-color:#AA96DA')
        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.lineEdit_2.textChanged.connect(self.magic)

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("New")
        # Creating actions using the second constructor
        self.openAction = QAction("Open...", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.helpContentAction = QAction("Help Content", self)
        self.aboutAction = QAction("About", self)

    def _createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Edit toolbar
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)

    def _createContextMenu(self):
        self.centralWidget.setContextMenuPolicy(self, Qt.ActionsContextMenu)
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        self.centralWidget.addAction(self.cutAction)

    def newFile(self):
        # Logic for creating a new file goes here...
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        # Logic for opening an existing file goes here...
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Pate</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        # Logic for launching help goes here...
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def closeEvent(self, event):

        close = QtWidgets.QMessageBox.question(self,
                                               "Оповещение",
                                               "Вы действительно хотите выйти?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def save_check_box_settings(self):
        settings = QSettings()
        settings.setValue(SETTINGS_TRAY, self.check_box.isChecked())
        settings.sync()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter:
            self.button1.clicked.connect(self.find_date())
        if e.key() == QtCore.Qt.Key_Delete:
            self.delete_note()

    def find_date(self):
        string_date = self.calendarWidget.selectedDate().getDate()
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        line_edit = self.lineEdit.text()
        self.textBrowser.clear()
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f'{key} - {self.all_dates[key]}')

    def delete_note(self):
        self.textBrowser.clear()

    def weather(self):
        owm = OWM('b7462886681078b26d85a070b3ed6c6e')
        mgr = owm.weather_manager()
        city = self.lineEdit_2.text()
        if city == '':
            self.label_2.setText('Укажите город')
        else:
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature = w.temperature('celsius')['temp']
            self.label_2.setText(f'Температура:{temperature}')

    def magic(self):
        self.label_2.setText(self.lineEdit_2.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
