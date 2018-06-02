from alesisvsysex.protocol.model import AlesisVMini

__all__ = ['FileDevice']

class FileDevice (object):
    
    def __init__(self, filename):
        self.filename = filename

    def get_config(self):
        with open(self.filename, 'rb') as f:
            return AlesisVMini.deserialize(f.read())
    
    def set_config(self, model):
        with open(self.filename, 'wb') as f:
            f.write(model.serialize())

