import time
import mido
from alesisvsysex.protocol.sysex import SysexMessage
from alesisvsysex.protocol.model import AlesisModel

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

    @classmethod
    def findAllPorts(cls):
        ports = list()
        for model_class in AlesisModel.__subclasses__():
            ports = ports + cls.findPortsForModel(model_class)
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
        if self.modelClass._SLOT_CONFIG:
            raise RuntimeError('Model class uses config slots')
        self._send(SysexMessage('query', self.modelClass))
        return self._recv().model
    
    def set_config(self, model):
        if self.modelClass._SLOT_CONFIG:
            raise RuntimeError('Model class uses config slots')
        model_bin = model.serialize()
        self._send(SysexMessage('update', model))
        if self.get_config().serialize() != model_bin:
            raise RuntimeError('Failed to update configuration')

    def get_slot_config(self, slot):
        if not self.modelClass._SLOT_CONFIG:
            raise RuntimeError('Model class does not use config slots')
        config = b''
        for offset in range(self.modelClass.num_bytes()):
            self._send(SysexMessage('slot_query', self.modelClass, slot, offset))
            reply = self._recv()
            config += bytes([reply.datum])
        return self.modelClass.deserialize(config)

    def set_slot_config(self, slot, model):
        if not self.modelClass._SLOT_CONFIG:
            raise RuntimeError('Model class does not use config slots')
        config = model.serialize()
        for offset in range(model.num_bytes()):
            self._send(SysexMessage('slot_update', model, slot, offset, config[offset]))
            # KLUDGE: The VI61 (and possibly other devices) don't
            # appear to like getting more than one update message per
            # USB packet...  Or it might be that they don't like
            # having two-and-a-bit, with the rest in the next packet.
            # This should be easy to accommodate: The Linux kernel
            # driver provides SNDRV_RAWMIDI_IOCTL_DRAIN which waits
            # until all pending MIDI output has been sent, which is
            # exposed by libalsa as snd_rawmidi_drain().  But we're
            # using mido, which uses python_rtmidi, which uses RtMidi,
            # which DOESN'T expose this functionality.  I'm sure that
            # there's a very good reason why not.  As a workaround,
            # since RtMidi sends messages "immediately", we sleep for
            # two milliseconds after each packet, being twice the
            # primary USB clock, in the hopes that it is sufficient to
            # clear the pending queue before we add to it.
            time.sleep(0.002)
