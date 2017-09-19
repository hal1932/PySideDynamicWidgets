# encoding: utf-8
import sys
import PySide.QtGui as QtGui
from main_window import MainWindow


def main():
    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.setup_ui()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
