from PyQt5.QtWidgets import *
from alesisvsysex.protocol.types import *

class IntegerSelector (QSpinBox):

    def __init__(self, parent, model, field):
        super().__init__(parent)
        self.fieldName = field
        self.model = model
        self.setRange(0x00, 0x7f)
        self.setSingleStep(1)
        self.updateState()
        self.valueChanged.connect(self.updateModel)
        
    def updateState(self):
        self.setValue(getattr(self.model, self.fieldName).as_int())
    
    def updateModel(self):
        setattr(self.model, self.fieldName, IntValue(self.value()))
    
    def setModel(self, model):
        self.model = model
        self.updateState()

class EnumSelector (QComboBox):

    def __init__(self, parent, model, field):
        super().__init__(parent)
        self.fieldName = field
        self.model = model
        self.enumClass = model._params[field].__class__
        self.enumValues = list(sorted(self.enumClass._VALUES.items(), key=lambda x: x[1]))
        for k, v in self.enumValues:
            self.addItem(k, v)
        self.updateState()
        self.currentIndexChanged.connect(self.updateModel)
        
    def updateState(self):
        for i, (k, v) in enumerate(self.enumValues):
            if getattr(self.model, self.fieldName).as_int() == v:
                self.setCurrentIndex(i)
                break
        else:
            raise RuntimeError("Invalid state for component '%s' field '%s'"
                               % (self.model.__class__.__name__, self.fieldName))
                               
    def updateModel(self):
        setattr(self.model, self.fieldName, self.enumClass(self.enumValues[self.currentIndex()][1]))

    def setModel(self, model):
        self.model = model
        self.updateState()
