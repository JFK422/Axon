from PyQt5 import QtGui, QtCore, QtWidgets
import seperator, dab
import qtawesome as qta

class CreateUI(QtWidgets.QWidget):
    def setup(self, placeText, cryptText, infoText, index):
        self.thePlace = index

        CreateUI.thePlace = placeText.decode()
        place = QtWidgets.QLabel(placeText.decode())
        place.setObjectName("listText")
        crypto = QtWidgets.QLabel(cryptText.decode())
        crypto.setObjectName("listText")
        info = QtWidgets.QLabel(infoText.decode())
        info.setObjectName("listText")
        cross = qta.icon("fa.times", color="#f9f9f9")
        deleteBtn = QtWidgets.QPushButton(cross, "")
        deleteBtn.setObjectName("deleteBtn")
        deleteBtn.clicked.connect(lambda:dab.Database.delete(self, self.thePlace))

        wMain = QtWidgets.QWidget()
        wMain.setObjectName("passColor")

        

        #Layouts
        vBack = QtWidgets.QVBoxLayout()
        hMain = QtWidgets.QHBoxLayout()

        vBack.setContentsMargins(QtCore.QMargins(0,0,0,0))
        hMain.setContentsMargins(QtCore.QMargins(10,5,10,5))
        hMain.setAlignment(QtCore.Qt.AlignLeft)

        wMain.setLayout(hMain)

        sep = seperator.MenuSeperator()
        sep.setup()
        sep2 = seperator.MenuSeperator()
        sep2.setup()
        sep3 = seperator.MenuSeperator()
        sep3.setup()

        hMain.addWidget(place)
        hMain.addWidget(sep)
        hMain.addWidget(crypto)
        hMain.addWidget(sep2)
        hMain.addWidget(info)
        hMain.addWidget(sep3)
        hMain.addWidget(deleteBtn)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))