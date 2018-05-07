from alesisvsysex.protocol.types import *
import unittest

class TestTypes(unittest.TestCase):
    def test_intval_as_int(self):
        v = IntValue(5)
        assert v.as_int() == 5

    def test_intval_serialize(self):
        v = IntValue(5)
        assert v.serialize() == bytes([5])

    def test_intval_deseiralize(self):
        assert IntValue.deserialize(bytes([5])).as_int() == 5

    def test_enumval_const_str(self):
        v = PadModeEnum('Toggle CC')
        assert v.as_int() == 0x01

    def test_enumval_const_int(self):
        v = PadModeEnum(0x01)
        assert v.as_int() == 0x01

    def test_enumval_as_str(self):
        v = PadModeEnum(0x01)
        assert v.as_string() == "Toggle CC"

    def test_enumval_serialize(self):
        v = PadModeEnum(0x01)
        assert v.serialize() == bytes([0x01])

    def test_enumval_deserialize(self):
        assert PadModeEnum.deserialize(bytes([0x01])).as_int() == 0x01

if __name__ == '__main__':
    unittest.main()
