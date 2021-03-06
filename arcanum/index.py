import sys, logging, datetime
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from components.uiElements import connectionDialog, mainWindow

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#It creates the main window and the connection dialog, sets the main window size and position, the app icon & stylesheet and the window moving
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE (Its the idea, I may have actually forgotten about it sofar!)

#Variables

class Window():
    def __init__(self):
        super(Window, self).__init__()
        dial = connectionDialog.CreateUI()
        dial.show()
    
    def createMain(self):
        main = mainWindow.Window()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p',
    filename='./logs/' + str(datetime.datetime.now()).split(".")[0] + 'arcanum.log',
    level=logging.DEBUG)
    log = logging.getLogger()

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    log.info("Qt version:" + str(QtCore.QT_VERSION_STR))
    log.info("PyQt version:" + str(Qt.PYQT_VERSION_STR))
    #log.info("SIP version:"+ str(sip.SIP_VERSION_STR))

    #Creating the QApplication
    app = QtWidgets.QApplication(sys.argv)

    #set the application icon  
    app_icon = QtGui.QIcon()
    app_icon.addFile('./resources/icons/icon16.png', QtCore.QSize(16,16))
    app_icon.addFile('./resources/icons/icon32.png', QtCore.QSize(32,32))
    app_icon.addFile('./resources/icons/icon64.png', QtCore.QSize(64,64))
    app_icon.addFile('./resources/icons/icon128.png', QtCore.QSize(128,128))
    app_icon.addFile('./resources/icons/icon256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    
    #Set the main styling of the app
    with open("./stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)

    #Misc stuff
    window = Window()
    sys.exit(app.exec_())

"""

          _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\    \                /::\____\                /::\____\                /::\____\        
       /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::|   |               /:::/    /               /::::|   |        
      /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::::|   |              /:::/    /               /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/    /               /::::::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/    /               /:::/|::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /:::/    /               /:::/ |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    /      _____    /:::/  |::|___|______  
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/____/      /\    \  /:::/   |::::::::\    \ 
/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/____/     \:::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\|:::|    /      /::\____\/:::/    |:::::::::\____\
\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|\:::\    \      \::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /|:::|____\     /:::/    /\::/    / ~~~~~/:::/    /
 \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /  \:::\    \      \/____/  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \:::\    \   /:::/    /  \/____/      /:::/    / 
          \::::::/    /         |:::::::::/    /    \:::\    \                       \::::::/    /           |::|/:::/    /    \:::\    \ /:::/    /               /:::/    /  
           \::::/    /          |::|\::::/    /      \:::\    \                       \::::/    /            |::::::/    /      \:::\    /:::/    /               /:::/    /   
           /:::/    /           |::| \::/____/        \:::\    \                      /:::/    /             |:::::/    /        \:::\__/:::/    /               /:::/    /    
          /:::/    /            |::|  ~|               \:::\    \                    /:::/    /              |::::/    /          \::::::::/    /               /:::/    /     
         /:::/    /             |::|   |                \:::\    \                  /:::/    /               /:::/    /            \::::::/    /               /:::/    /      
        /:::/    /              \::|   |                 \:::\____\                /:::/    /               /:::/    /              \::::/    /               /:::/    /       
        \::/    /                \:|   |                  \::/    /                \::/    /                \::/    /                \::/____/                \::/    /        
         \/____/                  \|___|                   \/____/                  \/____/                  \/____/                  ~~                       \/____/         
                                                                                                                                                                               
"""
