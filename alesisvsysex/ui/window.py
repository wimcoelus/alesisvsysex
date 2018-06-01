from PyQt5.QtWidgets import *
from alesisvsysex.device.alesis import AlesisV25Device
from alesisvsysex.device.file import FileDevice
from alesisvsysex.ui.components import *
from alesisvsysex.ui.filedialog import *

__all__ = ['AlesisVSysexApplication']

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
        self.mainWindow = QMainWindow()
        self.statusBar = self.mainWindow.statusBar()
        self.mainWindow.setWindowTitle('Alesis V-Series SysEx Editor')
        self.initMainWidget()
        self.mainWindow.setCentralWidget(self.mainWidget)
        self.showStatusMessage('Ready.')
        self.mainWindow.show()

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
        self.setModel(f.get_config())
        self.showStatusMessage("Loaded configuration from '%s'." % name)
    
    def saveDevice(self):
        device = AlesisV25Device()
        device.set_config(self.model)
        self.showStatusMessage("Saved configuration to MIDI device.")
    
    def loadDevice(self):
        device = AlesisV25Device()
        self.setModel(device.get_config())
        self.showStatusMessage("Loaded configuration from MIDI device.")

