import struct

from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.component import *

__all__ = ['AlesisVMini', 'Keys' , 'PitchWheel', 'ModWheel', 'Sustain', 'Knob', 'Knobs', 'Pad', 'Pads' ]
    
class Keys (BasicComponent):

    _PARAMS = [
        ('base_note',   IntValue,   [0x0c]),
        ('octave',      IntValue,   [0x05]),
        ('channel',     IntValue,   [0x00]),
        ('curve',       IntValue,   [0x04])
    ]

class PitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00]),
        ('rate',        IntValue,   [0x50])
    ]

class ModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00]),
        ('cc',          IntValue,   [0x01]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f]),
        ('rate',        IntValue,   [0x50])
    ]
    
class Sustain (BasicComponent):

    _PARAMS = [
        ('mode',    SusModeEnum,    [0x00]),
        ('cc',          IntValue,   [0x40]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f]),
        ('channel',     IntValue,   [0x00])
    ]

class Knob (BasicComponent):

    _PARAMS = [
        ('mode',        KnobModeEnum,   [0x00]),
        ('cc',          IntValue,       [0xff]), # intentionally invalid
        ('min',         IntValue,       [0x00]),
        ('max',         IntValue,       [0x7f]),
        ('channel',     IntValue,       [0x00])
    ]
    
class Knobs (CompoundComponent):

    _COMPONENTS = [
        ('knob1', Knob, {'cc': IntValue(0x14)}),
        ('knob2', Knob, {'cc': IntValue(0x15)}),
        ('knob3', Knob, {'cc': IntValue(0x16)}),
        ('knob4', Knob, {'cc': IntValue(0x17)})
    ]

class Pad (BasicComponent):

    _PARAMS = [
        ('mode',    PadModeEnum,    [0x00]),
        ('note',    IntValue,       [0xff]), # intentionally invalid
        ('fixed',   IntValue,       [0x00]),
        ('curve',   IntValue,       [0x00]),
        ('channel', IntValue,       [0x09])
    ]

class Pads (CompoundComponent):

    _COMPONENTS = [
        ('pad1', Pad, {'note': IntValue(0x31)}),
        ('pad2', Pad, {'note': IntValue(0x20)}),
        ('pad3', Pad, {'note': IntValue(0x2a)}),
        ('pad4', Pad, {'note': IntValue(0x2e)}),
    ]

#class Button (BasicComponent):
#
#    _PARAMS = [
#        ('mode',    ButtonModeEnum, [0x00]),
#        ('cc',      IntValue,       [0xff]), # intentionally invalid
#        ('on',      IntValue,       [0x7f]),
#        ('off',     IntValue,       [0x00]),
#        ('channel', IntValue,       [0x00])
#    ]

#class Buttons (CompoundComponent):
#
#    _COMPONENTS = [
#        ('button1', Button, {'cc': IntValue(0x30)}),
#        ('button2', Button, {'cc': IntValue(0x31)}),
#        ('button3', Button, {'cc': IntValue(0x32)}),
#        ('button4', Button, {'cc': IntValue(0x33)})
#    ]

class AlesisVMini (CompoundComponent):

    _PORT_PREFIX = "VMini:VMini MIDI 2"

    _COMPONENTS = [
        ('keys',    Keys,       {}),
        ('pwheel',  PitchWheel, {}),
        ('mwheel',  ModWheel,   {}),
        ('sustain', Sustain,    {}),
        ('knobs',   Knobs,      {}),
        ('pads',    Pads,       {})
    ]

    _GROUPS = (('Keys / Wheels / Sustain', 'horizontal',
                (('Keys', 'keys'),
                 ('Pitch Wheel', 'pwheel'),
                 ('Mod Wheel', 'mwheel'),
                 ('Sustain', 'sustain'))),
               ('Knobs', 'vertical',
                (('Knobs', 'knobs'),)),
               ('Pads', 'vertical',
                (('Pads', 'pads'),)))
