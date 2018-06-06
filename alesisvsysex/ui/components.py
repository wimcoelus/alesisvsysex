from PyQt5.QtWidgets import *
from alesisvsysex.protocol.types import AbstractEnumValue, IntValue
from alesisvsysex.protocol.model import CompoundComponent, BasicComponent
from alesisvsysex.ui.values import *

class BasicWidget:

    def __init__(self, model, name, component_key):
        self.name = name
        self._widget = None
        self.componentName = name
        self.componentKey = component_key
        self.model = getattr(model, component_key)
        self.children = []
        self.childNames = []
        self.createChildren()

    def addChild(self, fieldName, fieldValue):
        self.childNames.append(fieldName)
        self.children.append(fieldValue)

    def createChildren(self):
        for field, cls, _ in self.model._PARAMS:
            if issubclass(cls, IntValue):
                self.addChild(field, IntegerSelector(self.model, field))
            elif issubclass(cls, AbstractEnumValue):
                self.addChild(field, EnumSelector(self.model, field))

    def initializeWidget(self):
        self._widget = QGroupBox(self.name)
        layout = QFormLayout()
        for fieldName, fieldValue in zip(self.childNames, self.children):
            layout.addRow(QLabel(fieldName), fieldValue.widget())
        self._widget.setLayout(layout)

    def widget(self):
        if self._widget is None:
            self.initializeWidget()
        return self._widget

class CompoundWidget:

    def __init__(self, model, name, component_key):
        self.name = name
        self._widget = None
        self.componentName = name
        self.componentKey = component_key
        self.model = getattr(model, component_key)
        self.children = []
        self.createChildren()

    def addChild(self, child):
        self.children.append(child)

    def createChildren(self):
        for name, _, __ in self.model._COMPONENTS:
            model = self.model._components[name]
            if isinstance(model, BasicComponent):
                self.addChild(BasicWidget(self.model, name, name))
            elif isinstance(model, CompoundComponent):
                self.addChild(CompoundWidget(self.model, name, name))

    def initializeWidget(self):
        if self.name is not None:
            self._widget = QGroupBox(self.name)
        else:
            self._widget = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        for child in self.children:
            layout.addWidget(child.widget())
        self._widget.setLayout(layout)

    def widget(self):
        if self._widget is None:
            self.initializeWidget()
        return self._widget
