from PyQt5.QtWidgets import *
from alesisvsysex.protocol.types import AbstractEnumValue, IntValue
from alesisvsysex.protocol.model import AlesisV, CompoundComponent, BasicComponent
from alesisvsysex.ui.values import *

class BasicWidget (QGroupBox):
    
    def __init__(self, parent, model, name, component_key):
        super().__init__(name, parent)
        self.componentName = name
        self.componentKey = component_key
        self.model = getattr(model, component_key)
        self.children = []
        self.childNames = []
        self.createChildren()
        self.initLayout()

    def addChild(self, fieldName, fieldValue):
        self.childNames.append(fieldName)
        self.children.append(fieldValue)

    def createChildren(self):
        for field, cls, _ in self.model._PARAMS:
            fieldName = QLabel(field)
            if issubclass(cls, IntValue):
                self.addChild(fieldName, IntegerSelector(self.model, field))
            elif issubclass(cls, AbstractEnumValue):
                self.addChild(fieldName, EnumSelector(self.model, field))

    def initLayout(self):
        layout = QFormLayout()
        for fieldName, fieldValue in zip(self.childNames, self.children):
            layout.addRow(fieldName, fieldValue.widget())
        self.setLayout(layout)
        
    def setModel(self, model):
        self.model = getattr(model, self.componentKey)
        for c in self.children:
            c.setModel(self.model)

class CompoundWidget (QGroupBox):
    
    def __init__(self, parent, model, name, component_key):
        if name is not None:
            super().__init__(name, parent)
        else:
            super().__init__(parent)
        self.componentName = name
        self.componentKey = component_key
        self.model = getattr(model, component_key)
        self.children = []
        self.createChildren()
        self.initLayout()

    def addChild(self, widget):
        self.children.append(widget)

    def createChildren(self):
        for name, _, __ in self.model._COMPONENTS:
            model = self.model._components[name]
            if isinstance(model, BasicComponent):
                self.addChild(BasicWidget(self, self.model, name, name))
            elif isinstance(model, CompoundComponent):
                self.addChild(CompoundWidget(self, self.model, name, name))

    def initLayout(self):
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        for widget in self.children:
            layout.addWidget(widget)
        self.setLayout(layout)

    def setModel(self, model):
        self.model = getattr(model, self.componentKey)
        for c in self.children:
            c.setModel(self.model)
