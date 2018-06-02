from alesisvsysex.device.alesis import *
from alesisvsysex.protocol.sysex import *
from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.model import *
import unittest

class TestDevice(unittest.TestCase):
    @unittest.skip("requires connected device")
    def test_v25_constructor(self):
        d = AlesisMIDIDevice()
        assert d._port is not None

    @unittest.skip("requires connected device")
    def test_v25_send_recv(self):
        d = AlesisMIDIDevice()
        m = SysexMessage('query')
        d._send(m)
        r = d._recv()
        assert isinstance(r.model, AlesisVMini)

    @unittest.skip("requires connected device")
    def test_v25_get_config(self):
        d = AlesisMIDIDevice()
        r = d.get_config()
        assert isinstance(r, AlesisVMini)

    @unittest.skip("requires connected device")
    def test_v25_set_config(self):
        d = AlesisMIDIDevice()
        orig = d.get_config()
    
        new = orig.copy()
        new.knobs.knob1.cc = IntValue(new.knobs.knob1.cc.as_int() + 1)
        d.set_config(new)
    
        verify = d.get_config()
        success = (verify.knobs.knob1.cc.as_int() == new.knobs.knob1.cc.as_int())
    
        d.set_config(orig)
        assert(success)

if __name__ == '__main__':
    unittest.main()
