import mido
from alesisvsysex.protocol.sysex import SysexMessage

__all__ = ['AlesisMIDIDevice']

class AlesisMIDIDevice (object):
    
    def __init__(self, portName, modelClass):
        self._port = mido.open_ioport(portName)
        self.modelClass = modelClass
    
    def __del__(self):
        try:
            self._port.close()
        except:
            pass

    @classmethod
    def findPortsForModel(cls, model):
        ports = list()
        for port in mido.get_ioport_names():
            if port.startswith(model._PORT_PREFIX):
                ports = ports + [(port, model)]
        return ports

    def _send(self, message):
        if not isinstance(message, SysexMessage):
            raise ValueError("Can only send a SysexMessage")
        p = mido.Parser()
        p.feed(message.serialize())
        self._port.send(p.get_message())

    def _recv(self):
        while True:
            r = self._port.receive()
            if r.type == 'sysex':
                break
        return SysexMessage.deserialize(r.bin())

    def get_config(self):
        self._send(SysexMessage('query', self.modelClass))
        return self._recv().model
    
    def set_config(self, model):
        model_bin = model.serialize()
        self._send(SysexMessage('update', model))
        if self.get_config().serialize() != model_bin:
            raise RuntimeError('Failed to update configuration')

