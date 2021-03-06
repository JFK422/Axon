from PyQt5 import QtCore, QtWidgets

class MenuSeperator(QtWidgets.QWidget):
    def __init__(self, width = 300):
        super(MenuSeperator, self).__init__()
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setContentsMargins(QtCore.QMargins(0,0,0,0))

        wid = QtWidgets.QWidget()
        wid.setObjectName("seperator")
        wid.setMinimumHeight(3)
        wid.setMinimumWidth(3)
        wid.setMaximumHeight(3)
        wid.setMaximumWidth(width)
        vMenu.addWidget(wid)

        self.setLayout(vMenu)