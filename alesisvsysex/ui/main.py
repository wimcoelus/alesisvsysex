from PyQt5.QtWidgets import QApplication
from alesisvsysex.protocol.model import AlesisVMini
from alesisvsysex.ui.window import AlesisVSysexApplication

def main(argv):
    app = QApplication(argv)
    ex = AlesisVSysexApplication(AlesisVMini())
    return app.exec_()

