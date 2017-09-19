# encoding: utf-8
import PySide.QtGui as QtGui
from list_widget import ListWidget
from list_widget1 import ListWidget1


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def setup_ui(self):
        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QtGui.QVBoxLayout()
        central_widget.setLayout(main_layout)

        w = ListWidget1()
        main_layout.addWidget(w)
