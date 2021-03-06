import logging, qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets
from components.uiElements.tabs import overview, passwords, keys, settings
from components import dab, crypt
from components.uiElements import passItem, seperator

#This is the main file for creating the main ui
#It is split up into each tab on the side which have their own file for defining their part. This file combines them all.
#There is a secon part to the main uim which is the connectionDialog. It shows up on startup and is used for entering connection data.

class CreateUI:
    vPassList = None
    msg = None
    vHelper = None
    wPass = None
    scroll = None
    place = None
    newPass = None
    infoEdit = None
    password = ""
    def create(self):
        #Layouts
        #Main Layouts
        vBack = QtWidgets.QVBoxLayout() #Backbone layout for color at the lowest level
        vBack.setContentsMargins(0,0,0,0)
        vMain = QtWidgets.QVBoxLayout() #Layouts for the main stuff
        hMain = QtWidgets.QHBoxLayout()
        vMain.setContentsMargins(0,0,0,0)
        hMain.setContentsMargins(5,0,5,5)
        vToolRack = QtWidgets.QVBoxLayout() #Layout of the rack on the side
        vToolRack.setAlignment(QtCore.Qt.AlignTop)
        self.sCentral = QtWidgets.QStackedLayout()

        #Combine the pages of the sCentral layout
        #The tabs which are in different files are added here!
        wOverview = overview.Overview()
        wPasswords = passwords.Passwords()
        wKeys = keys.Keys()
        wSettings = settings.Settings()
        self.sCentral.addWidget(wPasswords)
        self.sCentral.addWidget(wKeys)
        self.sCentral.addWidget(wSettings)

        #Widget in the main layout for the background colour
        wBack = QtWidgets.QWidget()
        wBack.setObjectName("wMain")
        wBack.setLayout(vMain)
        vBack.addWidget(wBack)

        wToolRack = QtWidgets.QWidget()
        wToolRack.setObjectName("wRack")
        wToolRack.setMinimumWidth(200)
        wToolRack.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        wToolRack.setLayout(vToolRack)
        hMain.addWidget(wToolRack)

        wCentral = QtWidgets.QWidget()
        wCentral.setObjectName("wCentral")
        wCentral.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        wCentral.setLayout(self.sCentral)
        hMain.addWidget(wCentral)

        #Titlebar stuff
        tbLay = QtWidgets.QHBoxLayout()
        tbLay.setAlignment(QtCore.Qt.AlignRight)
        tbLay.setContentsMargins(0,0,0,0)
        tbWid = QtWidgets.QWidget()
        tbWid.setObjectName("titlebar")
        tbWid.setLayout(tbLay)
        
        mini = QtWidgets.QPushButton(qta.icon("fa.minus", color="#f9f9f9"), "")
        mini.setObjectName("minimize")
        mini.setMinimumSize(QtCore.QSize(30,30))
        """mini.clicked.connect(CreateUI.minimize(self))"""
        tbLay.addWidget(mini)

        quitBtn = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMinimumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        tbLay.addWidget(quitBtn)

        vMain.addWidget(tbWid)
        vMain.addLayout(hMain)
        
        #Populate the rack on the side
        rackBtnMinheight = 50
        rackIcoSize = QtCore.QSize(32, 32)
        btnOverview = QtWidgets.QPushButton(qta.icon("fa.compass", color="#f9f9f9"), "Overview")
        btnPasswords = QtWidgets.QPushButton(qta.icon("fa.lock", color="#f9f9f9"), "Passwords")
        btnKeys = QtWidgets.QPushButton(qta.icon("fa.key", color="#f9f9f9"), "Keys")
        btnSettings = QtWidgets.QPushButton(qta.icon("fa.cog", color="#f9f9f9"), "Settings")

        btnOverview.setMinimumHeight(rackBtnMinheight)
        btnPasswords.setMinimumHeight(rackBtnMinheight)
        btnKeys.setMinimumHeight(rackBtnMinheight)
        btnSettings.setMinimumHeight(rackBtnMinheight)

        btnOverview.setIconSize(rackIcoSize)
        btnPasswords.setIconSize(rackIcoSize)
        btnKeys.setIconSize(rackIcoSize)
        btnSettings.setIconSize(rackIcoSize)

        btnOverview.clicked.connect(lambda:CreateUI.switchTab(self, 0))
        btnPasswords.clicked.connect(lambda:CreateUI.switchTab(self, 0))
        btnKeys.clicked.connect(lambda:CreateUI.switchTab(self, 1))
        btnSettings.clicked.connect(lambda:CreateUI.switchTab(self, 2))

        """
        global prgWorking
        prgWorking = QtWidgets.QProgressBar()
        prgWorking.setTextVisible(False)
        prgWorking.setValue(0)
        #Hide the progressbar till its wanted again
        prgWorking.setVisible(False)
        prgWorking.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
        """

        #vToolRack.addWidget(btnOverview)
        vToolRack.addWidget(btnPasswords)
        #vToolRack.addWidget(btnKeys)
        vToolRack.addWidget(btnSettings)
        vToolRack.addWidget(wOverview)

        self.setLayout(vBack)

    #Set all the data in the wanted tab
    def setData(self, tab):
        #Overview
        if tab == 0:
            passwords.Passwords.createPassSlates(self)

        #Keys
        elif tab == 1:
            logging.debug("Keys tab set")

        #Settings
        elif tab == 2:
            settings.Settings.createData(self)

        #catch out of bounds
        else:
            logging.debug("The given tab index was not found!")

    """
    def updateProgressBar(self, value):
        prgWorking.setVisible(True)
        if value == 100:
            prgWorking.setValue(value)
            timer = QtCore.QTimer(self)
            timer.setSingleShot(True)
            timer.setInterval(1000)
            timer.timeout.connect(lambda:prgWorking.setVisible(False))
            timer.start()
        else:
            prgWorking.setValue(value)


        timer = QtCore.QTimer(self)
        timer.setSingleShot(True)
        timer.setInterval(500)
        timer.timeout.connect(lambda:CreateUI.updateProgressBar(self, 100))
        timer.start()
    """

    def getProgressValue(self):
        return prgWorking.value()

    def switchTab(self, tabIndex):
        CreateUI.setData(self, tabIndex)
        self.sCentral.setCurrentIndex(tabIndex)

    def minimize(self):
        self.showMinimized()


    def mousePressEvent(self, event):
        global dragging
        global clickPos
        clickPos = event.pos()
        if clickPos.y() < 121:
            self.showNormal()
        if event.buttons() == QtCore.Qt.LeftButton:
            dragging = True

    def mouseReleaseEvent(self, event):
        global dragging
        dragging = False
        posit = self.pos()
        if posit.y() < 15:
            self.maximize()

    def mouseMoveEvent(self, event):
        global dragging
        global clickPos
        if dragging and clickPos.y() < 121:
            self.move(self.pos() + (event.pos() - clickPos))
