from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.model import AlesisVMini, AlesisV25, AlesisVI49
from alesisvsysex.protocol.sysex import SysexMessage
import unittest

class TestSysex(unittest.TestCase):
    def test_sysex_serialize_query_v25(self):
        q = SysexMessage('query', AlesisV25)
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x41, 0x62, 0x00, 0x5d, 0xf7])

    def test_sysex_serialize_query_vmini(self):
        q = SysexMessage('query', AlesisVMini)
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x49, 0x62, 0x00, 0x38, 0xf7])

    def test_deserialize_query_v25(self):
        b = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x41, 0x62, 0x00, 0x5d, 0xf7])
        r = SysexMessage.deserialize(b)
        assert r.type == 'query'

    def test_deserialize_query_vmini(self):
        b = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x49, 0x62, 0x00, 0x38, 0xf7])
        r = SysexMessage.deserialize(b)
        assert r.type == 'query'

    def test_sysex_serialize_update_v25(self):
        q = SysexMessage('update', AlesisV25())
        begin = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x41, 0x61, 0x00, 0x5d])
        end = bytes([0xf7])
        res = q.serialize()
        assert res[0:len(begin)] == begin and res[-len(end):] == end

    def test_sysex_serialize_update_vmini(self):
        q = SysexMessage('update', AlesisVMini())
        begin = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x49, 0x61, 0x00, 0x38])
        end = bytes([0xf7])
        res = q.serialize()
        assert res[0:len(begin)] == begin and res[-len(end):] == end

    def test_sysex_deserialize_reply(self):
        m = AlesisV25()
        m.buttons.button1.cc = IntValue(0x55)
    
        q = SysexMessage('reply', m)
        b = q.serialize()
    
        r = SysexMessage.deserialize(b)
        assert r.type == 'reply'
        assert r.model.buttons.button1.cc.as_int() == 0x55

    def test_sysex_serialize_slot_query_vi49_slot1_offset0(self):
        q = SysexMessage('slot_query', AlesisVI49, 0, 0)
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x3f, 0x65, 0x00, 0x03, 0x00, 0x00, 0x00, 0xf7])

    def test_sysex_serialize_slot_query_vi49_slot23_offset143(self):
        q = SysexMessage('slot_query', AlesisVI49, 22, 143)
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x3f, 0x65, 0x00, 0x03, 0x16, 0x01, 0x0f, 0xf7])

    def test_sysex_serialize_slot_update_vi49(self):
        q = SysexMessage('slot_update', AlesisVI49, 17, 262, 0x45)
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x3f, 0x64, 0x00, 0x04, 0x11, 0x02, 0x06, 0x45, 0xf7])

if __name__ == '__main__':
    unittest.main()
