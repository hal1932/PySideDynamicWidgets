# encoding: utf-8
import PySide.QtGui as QtGui


class ListWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.__items = []
        self.__setup_ui()

    def __setup_ui(self):
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        button1 = QtGui.QPushButton('button1')
        button1.clicked.connect(self.__add_button)
        main_layout.addWidget(button1)

        '''
        for item in self.__items:
            button = QtGui.QPushButton(item)
            main_layout.addWidget(button)
        '''

    def __add_button(self):
        index = len(self.__items)
        self.layout().addWidget(QtGui.QPushButton(str(index)))
        self.__items.append(str(index))
        # self.__setup_ui()
