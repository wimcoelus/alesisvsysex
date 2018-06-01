from PyQt5.QtWidgets import QApplication
from alesisvsysex.protocol.model import AlesisV
from alesisvsysex.ui.window import AlesisVSysexApplication

def main(argv):
    app = QApplication(argv)
    ex = AlesisVSysexApplication(AlesisV())
    return app.exec_()

