from struct import unpack_from
from .model import AlesisModel

__all__ = ['SysexMessage']

class SysexMessage (object):
    
    _TYPES = {
        'update':      [0x61],
        'query':       [0x62],
        'reply':       [0x63],
        'slot_update': [0x64],
        'slot_query':  [0x65],
        'slot_reply':  [0x66]
    }

    _MANUFACTURER_ALESIS = [0x00, 0x00, 0x0e]

    _START_BYTE = [0xf0]
    _END_BYTE   = [0xf7]

    _SLOT_QUERY_MESSAGE_LENGTH  = 3
    _SLOT_UPDATE_MESSAGE_LENGTH = 4
    _SLOT_REPLY_MESSAGE_LENGTH  = 3

    def __init__(self, msg_type, model, slot=None, offset=None, datum=None):
        self.type  = msg_type
        self.model = model
        self.slot = slot
        self.offset = offset
        self.datum = datum

    @classmethod
    def encodeWord(cls, word):
        return [word >> 7, word & 0x7f]

    def serialize(self):
        if self.type == 'query':
            body = b''
            length = self.model.num_bytes()
        elif (self.type == 'update') or (self.type == 'reply'):
            body = self.model.serialize()
            length = self.model.num_bytes()
        elif self.type == 'slot_query':
            body = bytes([self.slot] + self.encodeWord(self.offset))
            length = self._SLOT_QUERY_MESSAGE_LENGTH
        elif self.type == 'slot_update':
            body = bytes([self.slot] + self.encodeWord(self.offset) + [self.datum])
            length = self._SLOT_UPDATE_MESSAGE_LENGTH
        else:
            raise RuntimeError('Don\'t know how to encode %s messages' % self.type)

        return (bytes(self._START_BYTE
                      + self._MANUFACTURER_ALESIS
                      + self.model._DEVICE_ID
                      + self._TYPES[self.type]
                      + self.encodeWord(length))
                + body
                + bytes(self._END_BYTE))

    @classmethod
    def deserialize(cls, b):
        i = 0

        (start_byte, manufacturer, device_id, t, message_length) = unpack_from('B3s2sB2s', b, i)
        i += 9

        if [start_byte] != cls._START_BYTE:
            raise ValueError("Invalid start byte '0x%02x'" % start_byte[0])
        
        if list(manufacturer) != cls._MANUFACTURER_ALESIS:
            raise ValueError("Invalid manufacturer id")

        model_class = AlesisModel.findModelByDeviceId(list(device_id))
        if model_class is None:
            raise ValueError("Invalid device id")
        
        for k, v in cls._TYPES.items():
            if t == v[0]:
                msg_type = k
                break
        else:
            raise ValueError("Unknown message type '0x%02x'" % t[0])

        if (msg_type == "query") or (msg_type == 'update') or (msg_type == 'reply'):
            expected_length = model_class.num_bytes()
        elif msg_type == 'slot_reply':
            expected_length = cls._SLOT_REPLY_MESSAGE_LENGTH
        else:
            raise RuntimeError('Don\'t know expected length for %s messages' % msg_type)

        if message_length != bytes(cls.encodeWord(expected_length)):
            raise ValueError("Invalid message length")

        if msg_type == "query":
            model = None
            offset = None
            datum = None
        elif (msg_type == 'update') or (msg_type == 'reply'):
            model = model_class.deserialize(b[i : i + model_class.num_bytes()])
            offset = None
            datum = None
            i += model_class.num_bytes()
        elif msg_type == 'slot_reply':
            model = model_class
            offset = (b[i] << 7) | b[i + 1]
            datum = b[i + 2]
            i += cls._SLOT_REPLY_MESSAGE_LENGTH
        else:
            raise RuntimeError('Don\'t know how to decode %s messages' % msg_type)
        
        end_byte = b[i : i+1]
        if end_byte != bytes(cls._END_BYTE):
            raise ValueError("Invalid end byte '0x%02x'" % end_byte[0])
        i += 1
        
        return SysexMessage(msg_type, model, None, offset, datum)
