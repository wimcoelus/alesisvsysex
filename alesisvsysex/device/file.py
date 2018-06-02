from alesisvsysex.protocol.sysex import SysexMessage

__all__ = ['FileDevice']

class FileDevice (object):
    
    def __init__(self, filename):
        self.filename = filename

    def get_config(self):
        with open(self.filename, 'rb') as f:
            return SysexMessage.deserialize(f.read()).model

    def set_config(self, model):
        with open(self.filename, 'wb') as f:
            f.write(SysexMessage('update', model).serialize())
