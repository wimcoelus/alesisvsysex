from PyQt5.QtWidgets import *
from alesisvsysex.protocol.types import *

class IntegerSelector:

    def __init__(self, model, field):
        self._widget = None
        self.fieldName = field
        self.model = model
        self.modelClass = getattr(model, field).__class__

    def initializeWidget(self):
        widget = QSpinBox()
        self._widget = widget
        widget.setRange(self.modelClass._MIN, self.modelClass._MAX)
        widget.setSingleStep(1)
        self.updateState()
        widget.valueChanged.connect(self.updateModel)
        
    def widget(self):
        if self._widget is None:
            self.initializeWidget()
        return self._widget

    def updateState(self):
        self._widget.setValue(getattr(self.model, self.fieldName).as_int())
    
    def updateModel(self):
        setattr(self.model, self.fieldName, self.modelClass(self._widget.value()))

class EnumSelector:

    def __init__(self, model, field):
        self._widget = None
        self.fieldName = field
        self.model = model
        self.enumClass = model._params[field].__class__
        self.enumValues = list(sorted(self.enumClass._VALUES.items(), key=lambda x: x[1]))

    def initializeWidget(self):
        widget = QComboBox()
        self._widget = widget
        for k, v in self.enumValues:
            widget.addItem(k, v)
        self.updateState()
        widget.currentIndexChanged.connect(self.updateModel)
        
    def widget(self):
        if self._widget is None:
            self.initializeWidget()
        return self._widget

    def updateState(self):
        datum = getattr(self.model, self.fieldName).as_int()
        index = self._widget.findData(datum)
        if index != -1:
            self._widget.setCurrentIndex(index)
        else:
            raise RuntimeError("Invalid state for component '%s' field '%s'"
                               % (self.model.__class__.__name__, self.fieldName))

    def updateModel(self):
        setattr(self.model, self.fieldName, self.enumClass(self._widget.currentData()))
