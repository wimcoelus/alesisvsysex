from alesisvsysex.protocol.model import *
from alesisvsysex.protocol.types import *
import unittest

class TestModel(unittest.TestCase):
    def test_intvalue_range(self):
        assert IntValue._MAX == 127
        assert IntValue._MIN == 0

    def test_intvalue_range_enforcement(self):
        with self.assertRaises(ValueError):
            IntValue(128)

    def test_transpose_identity(self):
        serialized_transpose = bytes([0x0c])
        t = Transpose.deserialize(serialized_transpose)
        assert t.serialize() == serialized_transpose

    def test_transpose_range(self):
        assert Transpose._MAX == 12
        assert Transpose._MIN == -12

    def test_transpose_delta(self):
        assert Transpose(0).serialize() == b'\x0c'

    def test_keys_getattr(self):
        k = Keys(IntValue(0x01), IntValue(0x02), IntValue(0x03), IntValue(0x04))
        assert k.transpose.as_int() == 0x01
        assert k.octave.as_int() == 0x02
        assert k.channel.as_int() == 0x03
        assert k.curve.as_int() == 0x04

    def test_keys_bad_getattr(self):
        k = Keys()
        try:
            k.foo
            assert False
        except AttributeError:
            assert True
    
    def test_keys_default_const(self):
        k = Keys()
        d = {kk: cls(*v) for kk, cls, v in k._PARAMS}
        assert k.transpose.as_int() == d['transpose'].as_int()
        assert k.octave.as_int() == d['octave'].as_int()
        assert k.channel.as_int() == d['channel'].as_int()
        assert k.curve.as_int() == d['curve'].as_int()

    def test_keys_kwarg_const(self):
        k = Keys(octave=IntValue(0x79))
        d = {kk: cls(*v) for kk, cls, v in k._PARAMS}
        assert k.transpose.as_int() == d['transpose'].as_int()
        assert k.octave.as_int() == 0x79
        assert k.channel.as_int() == d['channel'].as_int()

    def test_keys_bad_kwarg_const(self):
        try:
            k = Keys(foo=IntValue(0x99))
            assert False
        except ValueError:
            assert True

    def test_keys_setattr(self):
        k = Keys(Transpose(0x01), IntValue(0x02), IntValue(0x03), IntValue(0x04))
        k.transpose = Transpose(0x8)
        k.octave = IntValue(0x7)
        k.channel = IntValue(0x6)
        k.curve = Curve(0x5)
        assert k.transpose.as_int() == 0x8
        assert k.octave.as_int() == 0x7
        assert k.channel.as_int() == 0x6
        assert k.curve.as_int() == 0x5

    def test_keys_num_bytes(self):
        k = Keys()
        assert k.num_bytes() == 4

    def test_keys_serialize(self):
        k = Keys(IntValue(0x0a), IntValue(0x0b), IntValue(0x0c), IntValue(0x0d))
        assert k.serialize() == bytes([0x0a, 0x0b, 0x0c, 0x0d])

    def test_keys_deserialize(self):
        b = bytes([0x0d, 0x0c, 0x0b, 0x03])
        k = Keys.deserialize(b)
        assert k.transpose.as_int() == 0x01
        assert k.octave.as_int() == 0x0c
        assert k.channel.as_int() == 0x0b
        assert k.curve.as_int() == 0x04

    def test_keys_copy(self):
        k1 = Keys(octave=IntValue(0x00))
        k2 = k1.copy()
        assert k2.octave.as_int() == 0x00
    
        k1.octave = IntValue(0x02)
        assert k1.octave.as_int() == 0x02
        assert k2.octave.as_int() == 0x00
    
        k2.octave = IntValue(0x05)
        assert k1.octave.as_int() == 0x02
        assert k2.octave.as_int() == 0x05

    def test_knobs_default_const(self):
        k = Knobs()
        assert k.knob1.cc.as_int() == 0x14

    def test_knobs_serialize(self):
        k = Knobs()
        assert k.serialize() == bytes([0x00, 0x14, 0x00, 0x7f, 0x00,
                                       0x00, 0x15, 0x00, 0x7f, 0x00,
                                       0x00, 0x16, 0x00, 0x7f, 0x00,
                                       0x00, 0x17, 0x00, 0x7f, 0x00])

    def test_knobs_deserialize(self):
        b = bytes([0x00, 0x7a, 0x00, 0x7f, 0x00,
                   0x00, 0x7b, 0x00, 0x7f, 0x00,
                   0x00, 0x7c, 0x00, 0x7f, 0x00,
                   0x00, 0x7d, 0x00, 0x7f, 0x00])
        k = Knobs.deserialize(b)
        assert k.knob1.cc.as_int() == 0x7a
        assert k.knob2.cc.as_int() == 0x7b
        assert k.knob3.cc.as_int() == 0x7c
        assert k.knob4.cc.as_int() == 0x7d

    def test_knobs_copy(self):
        k1 = Knobs()
        k1.knob1.cc = IntValue(0x10)
        k2 = k1.copy()
        assert k1.knob1.cc.as_int() == 0x10
    
        k1.knob1.cc = IntValue(0x11)
        assert k1.knob1.cc.as_int() == 0x11
        assert k2.knob1.cc.as_int() == 0x10
    
        k2.knob1.cc = IntValue(0x12)
        assert k1.knob1.cc.as_int() == 0x11
        assert k2.knob1.cc.as_int() == 0x12

    def test_pads_default_const(self):
        p = Pads()
        assert p.pad1.note.as_int() == 0x31

    def test_pads_serialize(self):
        p = Pads()
        assert p.serialize() == bytes([0x00, 0x31, 0x00, 0x00, 0x09,
                                       0x00, 0x20, 0x00, 0x00, 0x09,
                                       0x00, 0x2a, 0x00, 0x00, 0x09,
                                       0x00, 0x2e, 0x00, 0x00, 0x09,
                                       0x00, 0x24, 0x00, 0x00, 0x09,
                                       0x00, 0x25, 0x00, 0x00, 0x09,
                                       0x00, 0x26, 0x00, 0x00, 0x09,
                                       0x00, 0x27, 0x00, 0x00, 0x09])

    def test_pads_deserialize(self):
        b = bytes([0x00, 0x01, 0x00, 0x00, 0x09,
                   0x00, 0x02, 0x00, 0x00, 0x09,
                   0x00, 0x03, 0x00, 0x00, 0x09,
                   0x00, 0x04, 0x00, 0x00, 0x09,
                   0x00, 0x05, 0x00, 0x00, 0x09,
                   0x00, 0x06, 0x00, 0x00, 0x09,
                   0x00, 0x07, 0x00, 0x00, 0x09,
                   0x00, 0x08, 0x00, 0x00, 0x09])
        p = Pads.deserialize(b)
        assert (p.pad1.note.as_int() == 0x01 and p.pad2.note.as_int() == 0x02
                and p.pad3.note.as_int() == 0x03 and p.pad4.note.as_int() == 0x04
                and p.pad5.note.as_int() == 0x05 and p.pad6.note.as_int() == 0x06
                and p.pad7.note.as_int() == 0x07 and p.pad8.note.as_int() == 0x08)

    def test_buttons_default_const(self):
        b = Buttons()
        assert b.button1.cc.as_int() == 0x30

    def test_buttons_serialize(self):
        b = Buttons()
        assert b.serialize() == bytes([0x00, 0x30, 0x7f, 0x00, 0x00,
                                       0x00, 0x31, 0x7f, 0x00, 0x00,
                                       0x00, 0x32, 0x7f, 0x00, 0x00,
                                       0x00, 0x33, 0x7f, 0x00, 0x00])

    def test_buttons_deserialize(self):
        b = bytes([0x00, 0x40, 0x7f, 0x00, 0x00,
                   0x00, 0x41, 0x7f, 0x00, 0x00,
                   0x00, 0x42, 0x7f, 0x00, 0x00,
                   0x00, 0x43, 0x7f, 0x00, 0x00])
        b = Buttons.deserialize(b)
        assert (b.button1.cc.as_int() == 0x40 and b.button2.cc.as_int() == 0x41
                and b.button3.cc.as_int() == 0x42 and b.button4.cc.as_int() == 0x43)

    def test_alesisv_default_const(self):
        a = AlesisV25()
        assert a.buttons.button1.cc.as_int() == 0x30

    def test_vi49_length(self):
        assert AlesisVI49.num_bytes() == 385

    def test_find_by_id_invalid(self):
        assert AlesisModel.findModelByDeviceId([0xff, 0xff]) is None

    def test_find_by_id_v25(self):
        assert AlesisModel.findModelByDeviceId([0x00, 0x41]) == AlesisV25

    def test_find_by_id_vmini(self):
        assert AlesisModel.findModelByDeviceId([0x00, 0x49]) == AlesisVMini

if __name__ == '__main__':
    unittest.main()
