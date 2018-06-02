from .model import AlesisVMini

__all__ = ['SysexMessage']

class SysexMessage (object):
    
    _TYPES = {
        'update': [0x61],
        'query':  [0x62],
        'reply':  [0x63]
    }

    _MANUFACTURER_ALESIS = [0x00, 0x00, 0x0e]
    _DEVICE_ID           = [0x00, 0x49]
    _MESSAGE_LENGTH      = [0x00, 0x38]

    _START_BYTE = [0xf0]
    _END_BYTE   = [0xf7]
    
    def __init__(self, msg_type, model=None):
        self.type  = msg_type
        self.model = model
    
    def serialize(self):
        if self.type == 'query':
            return bytes(self._START_BYTE + self._MANUFACTURER_ALESIS + self._DEVICE_ID
                         + self._TYPES[self.type]
                         + self._MESSAGE_LENGTH + self._END_BYTE)
        else:
            return bytes(self._START_BYTE + self._MANUFACTURER_ALESIS + self._DEVICE_ID
                         + self._TYPES[self.type]
                         + self._MESSAGE_LENGTH) + self.model.serialize() + bytes(self._END_BYTE)
                     
        
    @classmethod
    def deserialize(cls, b):
        i = 0
        
        start_byte = b[i : i+1]
        if start_byte != bytes(cls._START_BYTE):
            raise ValueError("Invalid start byte '0x%02x'" % start_byte[0])
        i += 1
        
        manufacturer = b[i : i + len(cls._MANUFACTURER_ALESIS)]
        if manufacturer != bytes(cls._MANUFACTURER_ALESIS):
            raise ValueError("Invalid manufacturer id")
        i += len(cls._MANUFACTURER_ALESIS)

        device_id = b[i : i + len(cls._DEVICE_ID)]
        if device_id != bytes(cls._DEVICE_ID):
            raise ValueError("Invalid device id")
        i += len(cls._DEVICE_ID)
        
        t = b[i : i + 1]
        for k, v in cls._TYPES.items():
            if t == bytes(v):
                msg_type = k
                break
        else:
            raise ValueError("Unknown message type '0x%02x'" % t[0])
        i += 1
        
        message_length = b[i : i + len(cls._MESSAGE_LENGTH)]
        if message_length != bytes(cls._MESSAGE_LENGTH):
            raise ValueError("Invalid message length")
        i += len(cls._MESSAGE_LENGTH)
        
        if msg_type == "query":
            model = None
        else:
            model = AlesisVMini.deserialize(b[i : i + AlesisVMini.num_bytes()])
            i += AlesisVMini.num_bytes()
        
        end_byte = b[i : i+1]
        if end_byte != bytes(cls._END_BYTE):
            raise ValueError("Invalid end byte '0x%02x'" % end_byte[0])
        i += 1
        
        return SysexMessage(msg_type, model)
