from alesisvsysex.device.alesis import *
from alesisvsysex.protocol.sysex import *
from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.model import *
import unittest

class TestDevice(unittest.TestCase):
    def test_v25_constructor(self):
        d = AlesisV25Device()
        assert d._port is not None

    def test_v25_send_recv(self):
        d = AlesisV25Device()
        m = SysexMessage('query')
        d._send(m)
        r = d._recv()
        assert isinstance(r.model, AlesisV)

    def test_v25_get_config(self):
        d = AlesisV25Device()
        r = d.get_config()
        assert isinstance(r, AlesisV)

    def test_v25_set_config(self):
        d = AlesisV25Device()
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
