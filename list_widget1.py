# encoding: utf-8
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui


class ListDelegate(QtGui.QItemDelegate):

    def paint(self, painter, option, index):
        if not index.isValid():
            return None

        data = index.data(QtCore.Qt.DisplayRole)

        button = QtGui.QStyleOptionButton()
        button.rect = option.rect
        button.state = option.state | QtGui.QStyle.State_Off
        button.text = str(data)
        QtGui.QApplication.style().drawControl(
            QtGui.QStyle.CE_PushButton, button, painter
        )


class MyListView(QtGui.QListView):

    def __init__(self, parent=None):
        super(MyListView, self).__init__(parent)

    def currentChanged(self, *args, **kwargs):
        print args, kwargs


class ListWidget1(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ListWidget1, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        button1 = QtGui.QPushButton('button1')
        button1.clicked.connect(self.__add_button)
        main_layout.addWidget(button1)

        self.__listview = MyListView()
        self.__listview.setModel(QtGui.QStandardItemModel(0, 1))
        # self.__listview.setItemDelegate(ListDelegate())
        main_layout.addWidget(self.__listview)

    def __add_button(self):
        model = self.__listview.model()
        count = model.rowCount()
        item = QtGui.QStandardItem(str(count))
        model.appendRow(item)

        index = model.index(count, 0, QtCore.QModelIndex())
        data = item.data(QtCore.Qt.DisplayRole)
        button = QtGui.QPushButton(data)
        self.__listview.setIndexWidget(index, button)
