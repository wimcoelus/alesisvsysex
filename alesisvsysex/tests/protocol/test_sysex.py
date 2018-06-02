from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.model import AlesisVMini
from alesisvsysex.protocol.sysex import SysexMessage
import unittest

class TestSysex(unittest.TestCase):
    @unittest.skip("expects V25 message header")
    def test_sysex_serialize_query_v25(self):
        q = SysexMessage('query')
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x41, 0x62, 0x00, 0x5d, 0xf7])

    def test_sysex_serialize_query_vmini(self):
        q = SysexMessage('query')
        assert q.serialize() == bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x49, 0x62, 0x00, 0x38, 0xf7])

    @unittest.skip("uses V25 message header")
    def test_deserialize_query_v25(self):
        b = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x41, 0x62, 0x00, 0x5d, 0xf7])
        r = SysexMessage.deserialize(b)
        assert r.type == 'query'

    def test_deserialize_query_vmini(self):
        b = bytes([0xf0, 0x00, 0x00, 0x0e, 0x00, 0x49, 0x62, 0x00, 0x38, 0xf7])
        r = SysexMessage.deserialize(b)
        assert r.type == 'query'

    @unittest.skip("expects V25 message header")
    def test_sysex_serialize_update_v25(self):
        q = SysexMessage('update', AlesisVMini())
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

    @unittest.skip("relies on V25 model")
    def test_sysex_deserialize_reply(self):
        m = AlesisVMini()
        m.buttons.button1.cc = IntValue(0x55)
    
        q = SysexMessage('reply', m)
        b = q.serialize()
    
        r = SysexMessage.deserialize(b)
        assert r.type == 'reply'
        assert r.model.buttons.button1.cc.as_int() == 0x55

if __name__ == '__main__':
    unittest.main()
