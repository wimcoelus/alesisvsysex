from PyQt5.QtWidgets import QApplication
from alesisvsysex.protocol.model import AlesisModel
from alesisvsysex.device.alesis import AlesisMIDIDevice
from alesisvsysex.ui.window import AlesisVSysexApplication

def main(argv):
    app = QApplication(argv)
    # For the default model, pick the class of the first connected
    # device that we find, or an arbitrary valid model class if there
    # is no connected device.
    ports = AlesisMIDIDevice.findAllPorts()
    if len(ports) > 0:
        model_class = ports[0][1]
    else:
        model_class = AlesisModel.__subclasses__()[0]
    ex = AlesisVSysexApplication(model_class())
    return app.exec_()

