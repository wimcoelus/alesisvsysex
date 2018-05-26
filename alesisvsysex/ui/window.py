from PyQt5.QtWidgets import *
from alesisvsysex.protocol.model import AlesisV
from alesisvsysex.device.alesis import AlesisV25Device
from alesisvsysex.device.file import FileDevice
from alesisvsysex.ui.components import *
from alesisvsysex.ui.filedialog import *

__all__ = ['AlesisVSysexApplication']

class EditorWidget (QTabWidget):

    def __init__(self, model):
        super().__init__()
        self.children = []
        self.model = model
        self.initLayout()
        
    def addChild(self, parent, child):
        parent.addWidget(child.widget())
        self.children.append(child)
        
    def initLayout(self):
    
        pane1l = QHBoxLayout()
        self.addChild(pane1l, BasicWidget(self.model, "Keys", 'keys'))
        self.addChild(pane1l, BasicWidget(self.model, "Pitch Wheel", 'pwheel'))
        self.addChild(pane1l, BasicWidget(self.model, "Mod Wheel", 'mwheel'))
        self.addChild(pane1l, BasicWidget(self.model, "Sustain", 'sustain'))
        
        pane1 = QWidget()
        pane1.setLayout(pane1l)
        
        pane2l = QVBoxLayout()
        self.addChild(pane2l, CompoundWidget(self.model, "Knobs", 'knobs'))
    #    self.addChild(pane2l, CompoundWidget(self.model, "Buttons", 'buttons'))
        
        pane2 = QWidget()
        pane2.setLayout(pane2l)
        
        pane3l = QVBoxLayout()
        self.addChild(pane3l,CompoundWidget(self.model, "Pads", 'pads'))
        
        pane3 = QWidget()
        pane3.setLayout(pane3l)
        
        self.addTab(pane1, "Keys / Wheels / Sustain")
        self.addTab(pane2, "Knobs")
        self.addTab(pane3, "Pads")

    def widget(self):
        return self

    def setModel(self, model):
        self.model = model
        for c in self.children:
            c.setModel(self.model)

class AlesisVSysexApplication:

    def __init__(self):
        self.model = AlesisV()
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

