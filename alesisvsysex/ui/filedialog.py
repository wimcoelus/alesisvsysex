from PyQt5.QtWidgets import *

__all__ = ["launchSaveFileDialog", "launchLoadFileDialog"]

FILE_TYPES = "SysEx Files (*.syx);;All Files (*)"
DEFAULT_EXT = ".syx"

def launchSaveFileDialog(parent, delegate):

    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    
    dialog = QFileDialog(parent)
    dialog.setOptions(options)
    dialog.setNameFilter(FILE_TYPES)
    dialog.setDefaultSuffix(DEFAULT_EXT)
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setAcceptMode(QFileDialog.AcceptSave)
    dialog.fileSelected.connect(delegate.saveFileCallback)
    dialog.open()
    
def launchLoadFileDialog(parent, delegate):

    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    
    dialog = QFileDialog(parent)
    dialog.setOptions(options)
    dialog.setNameFilter(FILE_TYPES)
    dialog.setDefaultSuffix(DEFAULT_EXT)
    dialog.setFileMode(QFileDialog.ExistingFile)
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    dialog.fileSelected.connect(delegate.loadFileCallback)
    dialog.open()

