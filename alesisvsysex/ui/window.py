from PyQt5.QtWidgets import *
from alesisvsysex.protocol.model import AlesisV
from alesisvsysex.device.alesis import AlesisV25Device
from alesisvsysex.device.file import FileDevice
from alesisvsysex.ui.components import *
from alesisvsysex.ui.filedialog import *

__all__ = ['AlesisVSysexApplication']

class ContainerWidget (QWidget):

    def __init__(self):
        super().__init__()
        
    def getModel(self):
        p = self.parent()
        while not isinstance(p, EditorWidget):
            p = p.parent()
        return p.getModel()

class EditorWidget (QTabWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.children = []
        self.initLayout()
        
    def addChild(self, parent, widget):
        parent.addWidget(widget)
        self.children.append(widget)
        
    def initLayout(self):
    
        pane1l = QHBoxLayout()
        self.addChild(pane1l, BasicWidget(self, "Keys", 'keys'))
        self.addChild(pane1l, BasicWidget(self, "Pitch Wheel", 'pwheel'))
        self.addChild(pane1l, BasicWidget(self, "Mod Wheel", 'mwheel'))
        self.addChild(pane1l, BasicWidget(self, "Sustain", 'sustain'))
        
        pane1 = ContainerWidget()
        pane1.setLayout(pane1l)
        
        pane2l = QVBoxLayout()
        self.addChild(pane2l, CompoundWidget(self, "Knobs", 'knobs'))
    #    self.addChild(pane2l, CompoundWidget(self, "Buttons", 'buttons'))
        
        pane2 = ContainerWidget()
        pane2.setLayout(pane2l)
        
        pane3l = QVBoxLayout()
        self.addChild(pane3l,CompoundWidget(self, "Pads", 'pads'))
        
        pane3 = ContainerWidget()
        pane3.setLayout(pane3l)
        
        self.addTab(pane1, "Keys / Wheels / Sustain")
        self.addTab(pane2, "Knobs")
        self.addTab(pane3, "Pads")

    def getModel(self):
        return self.parentWidget().parentWidget().model
        
    def updateState(self):
        for c in self.children:
            c.updateState()

class MainWidget (QWidget):
    
    def __init__(self, parent, delegate, model):
        super().__init__(parent)
        self.delegate = delegate
        self.model = model
        self.initLayout()

    def createActionMenu(self):
        actionMenu = QWidget(self)
        layout = QHBoxLayout()

        bsavef = QPushButton('Save To File', actionMenu)
        bsavef.clicked.connect(self.delegate.saveFile)
        layout.addWidget(bsavef)

        bloadf = QPushButton('Load From File', actionMenu)
        bloadf.clicked.connect(self.delegate.loadFile)
        layout.addWidget(bloadf)

        bsaved = QPushButton('Save To Device', actionMenu)
        bsaved.clicked.connect(self.delegate.saveDevice)
        layout.addWidget(bsaved)

        bloadd = QPushButton('Load From Device', actionMenu)
        bloadd.clicked.connect(self.delegate.loadDevice)
        layout.addWidget(bloadd)

        actionMenu.setLayout(layout)
        actionMenu.setFixedHeight(50)

        return actionMenu

    def initLayout(self):
        layout = QVBoxLayout()
        self.actionWidget = self.createActionMenu()
        layout.addWidget(self.actionWidget)
        self.editorWidget = EditorWidget(self)
        layout.addWidget(self.editorWidget)
        self.setLayout(layout)

    def setModel(self, model):
        self.model = model
        self.updateState()

    def updateState(self):
        self.editorWidget.updateState()

class AlesisVSysexMainWindow (QMainWindow):

    def __init__(self, delegate, model):
        super().__init__()
        self.delegate = delegate
        self.model = model
        self.initWindow()

    def showStatusMessage(self, message):
        self.statusBar().showMessage(message)

    def initWindow(self):
        self.setWindowTitle('Alesis V-Series SysEx Editor')
        self.initWidget()
        self.showStatusMessage('Ready.')
        self.show()
        
    def initWidget(self):
        self.widget = MainWidget(self, self.delegate, self.model)
        self.setCentralWidget(self.widget)

    def setModel(self, model):
        self.model = model
        self.widget.setModel(model)

class AlesisVSysexApplication:

    def __init__(self):
        self.model = AlesisV()
        self.mainWindow = AlesisVSysexMainWindow(self, self.model)

    def setModel(self, model):
        self.model = model
        self.mainWindow.setModel(model)

    def showStatusMessage(self, message):
        self.mainWindow.showStatusMessage(message)

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

