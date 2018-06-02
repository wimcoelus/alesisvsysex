from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint
from alesisvsysex.device.alesis import AlesisMIDIDevice
from alesisvsysex.device.file import FileDevice
from alesisvsysex.ui.components import *
from alesisvsysex.ui.filedialog import *

__all__ = ['AlesisVSysexApplication']

all_windows = set()

def preserveWindow(window):
    all_windows.add(window)

def unpreserveWindow(window):
    all_windows.remove(window)

class DisappointingMainWindow (QMainWindow):
    # In order to create a second main window object that survives
    # long enough to interact with we have to prevent the GC from
    # deleting it.  That's easily enough handled.  In order to prevent
    # memory leaks we need to allow the GC to delete the window once
    # it is closed.  There is no signal for window-close, so we must
    # implement a closeEvent() method in order to catch the close
    # event.  Which requires subclassing QMainWindow().  Which we
    # wouldn't need to do, were it not for the GC being obnoxious and
    # the lack of a suitable existing signal to connect.  I am...
    # disappointed.

    # Another angle would be to create a QObject subclass with an
    # eventFilter() method and install it as an event filter on the
    # main window.  This still requires subclassing a Qt class, and
    # then doing the event-type dispatch "by hand".  Also
    # disappointing.

    def __init__(self, controller):
        super().__init__()
        preserveWindow(controller)
        self._controller = controller

    def closeEvent(self, event):
        unpreserveWindow(self._controller)
        self._controller = None
        event.accept()

class EditorWidget:

    def __init__(self, model):
        self.children = []
        self.model = model
        self._widget = QTabWidget()
        self.initLayout()
        
    def addChild(self, parent, child):
        parent.addWidget(child.widget())
        self.children.append(child)
        
    def initLayout(self):
        for (group_title, style, elements) in self.model._GROUPS:
            if style == 'horizontal':
                uiclass = BasicWidget
                layout = QHBoxLayout()
            else:
                uiclass = CompoundWidget
                layout = QVBoxLayout()

            for (name, key) in elements:
                self.addChild(layout, uiclass(self.model, name, key))

            pane = QWidget()
            pane.setLayout(layout)
            self._widget.addTab(pane, group_title)

    def widget(self):
        return self._widget

    def setModel(self, model):
        self.model = model
        for c in self.children:
            c.setModel(self.model)

class AlesisVSysexApplication:

    def __init__(self, model):
        self.model = model
        self.initMainWindow()

    def createActionMenu(self):
        actionMenu = QWidget(self.mainWidget)
        layout = QHBoxLayout()

        bsavef = QPushButton('Save To File', actionMenu)
        bsavef.clicked.connect(self.saveFile)
        layout.addWidget(bsavef)

        bloadf = QPushButton('Load From File', actionMenu)
        bloadf.clicked.connect(self.loadFile)
        layout.addWidget(bloadf)

        bsaved = QPushButton('Save To Device', actionMenu)
        bsaved.clicked.connect(self.saveDevice)
        layout.addWidget(bsaved)

        bloadd = QPushButton('Load From Device', actionMenu)
        bloadd.clicked.connect(self.loadDevice)
        layout.addWidget(bloadd)

        actionMenu.setLayout(layout)
        actionMenu.setFixedHeight(50)

        return actionMenu

    def initMainWidget(self):
        self.mainWidget = QWidget(self.mainWindow)
        layout = QVBoxLayout()
        layout.addWidget(self.createActionMenu())
        self.editorWidget = EditorWidget(self.model)
        layout.addWidget(self.editorWidget.widget())
        self.mainWidget.setLayout(layout)

    def initMainWindow(self):
        self.mainWindow = DisappointingMainWindow(self)
        self.statusBar = self.mainWindow.statusBar()
        self.mainWindow.setWindowTitle('Alesis V-Series SysEx Editor')
        self.initMainWidget()
        self.mainWindow.setCentralWidget(self.mainWidget)
        self.showStatusMessage('Ready.')
        self.mainWindow.show()

    def positionRelativeTo(self, parentWindow):
        parentPosition = parentWindow.pos()
        frameHeight = parentWindow.geometry().top() - parentPosition.y()
        if frameHeight == 0:
            frameHeight = 40
        targetPosition = parentPosition + 2 * QPoint(frameHeight, frameHeight)
        targetBottomRight = self.mainWindow.rect().bottomRight() + targetPosition
        if QApplication.desktop().availableGeometry(self.mainWindow).contains(targetBottomRight):
            self.mainWindow.move(targetPosition)

    def setModel(self, model):
        self.model = model
        self.editorWidget.setModel(model)

    def showStatusMessage(self, message):
        self.statusBar.showMessage(message)

    def saveFile(self):
        launchSaveFileDialog(self.mainWindow, self)
    
    def saveFileCallback(self, name):
        f = FileDevice(name)
        f.set_config(self.model)
        self.showStatusMessage("Saved configuration to '%s'." % name)
    
    def loadFile(self):
        launchLoadFileDialog(self.mainWindow, self)
        
    def loadFileCallback(self, name):
        f = FileDevice(name)
        window = self.__class__(f.get_config())
        window.positionRelativeTo(self.mainWindow)
        window.showStatusMessage("Loaded configuration from '%s'." % name)
    
    def saveDevice(self):
        device = AlesisMIDIDevice()
        device.set_config(self.model)
        self.showStatusMessage("Saved configuration to MIDI device.")
    
    def loadDevice(self):
        device = AlesisMIDIDevice()
        window = self.__class__(device.get_config())
        window.positionRelativeTo(self.mainWindow)
        window.showStatusMessage("Loaded configuration from MIDI device.")

