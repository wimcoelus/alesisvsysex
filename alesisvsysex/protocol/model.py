import struct

from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.component import *

__all__ = ['AlesisModel', 'AlesisV25', 'AlesisVMini', 'AlesisVI49', 'Keys' , 'PitchWheel', 'VMiniPitchWheel', 'ModWheel', 'VMiniModWheel', 'Sustain', 'VMiniSustain', 'Knob', 'Knobs', 'Pad', 'Pads', 'VMiniPads', 'Button', 'Buttons']

class Keys (BasicComponent):

    _PARAMS = [
        ('base_note',   IntValue,   [0x0c]),
        ('octave',      IntValue,   [0x05]),
        ('channel',     IntValue,   [0x00]),
        ('curve',       IntValue,   [0x04])
    ]

class PitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00])
    ]

class VMiniPitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00]),
        ('rate',        IntValue,   [0x50])
    ]

class ModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00]),
        ('cc',          IntValue,   [0x01]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f])
    ]

class VMiniModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     IntValue,   [0x00]),
        ('cc',          IntValue,   [0x01]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f]),
        ('rate',        IntValue,   [0x50])
    ]

class Sustain (BasicComponent):

    _PARAMS = [
        ('cc',          IntValue,   [0x40]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f]),
        ('channel',     IntValue,   [0x00])
    ]

class VISustain (BasicComponent):

    _PARAMS = [
        ('cc',          IntValue,   [0x40]),
        ('pressed',     IntValue,   [0x7f]),
        ('released',    IntValue,   [0x00]),
        ('channel',     IntValue,   [0x00])
    ]

class VMiniSustain (BasicComponent):

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

class VI49Knobs (CompoundComponent):

    _COMPONENTS = [
        ('knob1',  Knob, {'cc': IntValue(0x14)}),
        ('knob2',  Knob, {'cc': IntValue(0x15)}),
        ('knob3',  Knob, {'cc': IntValue(0x16)}),
        ('knob4',  Knob, {'cc': IntValue(0x17)}),
        ('knob5',  Knob, {'cc': IntValue(0x18)}),
        ('knob6',  Knob, {'cc': IntValue(0x19)}),
        ('knob7',  Knob, {'cc': IntValue(0x1a)}),
        ('knob8',  Knob, {'cc': IntValue(0x1b)}),
        ('knob9',  Knob, {'cc': IntValue(0x1c)}),
        ('knob10', Knob, {'cc': IntValue(0x1d)}),
        ('knob11', Knob, {'cc': IntValue(0x1e)}),
        ('knob12', Knob, {'cc': IntValue(0x1f)})
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
        ('pad5', Pad, {'note': IntValue(0x24)}),
        ('pad6', Pad, {'note': IntValue(0x25)}),
        ('pad7', Pad, {'note': IntValue(0x26)}),
        ('pad8', Pad, {'note': IntValue(0x27)}),
    ]

class VMiniPads (CompoundComponent):

    _COMPONENTS = [
        ('pad1', Pad, {'note': IntValue(0x31)}),
        ('pad2', Pad, {'note': IntValue(0x20)}),
        ('pad3', Pad, {'note': IntValue(0x2a)}),
        ('pad4', Pad, {'note': IntValue(0x2e)}),
    ]

class VIPads (CompoundComponent):

    _COMPONENTS = [
        ('pad1',  Pad, {'note': IntValue(0x30), 'channel': IntValue(0x00)}),
        ('pad2',  Pad, {'note': IntValue(0x31), 'channel': IntValue(0x00)}),
        ('pad3',  Pad, {'note': IntValue(0x32), 'channel': IntValue(0x00)}),
        ('pad4',  Pad, {'note': IntValue(0x33), 'channel': IntValue(0x00)}),
        ('pad5',  Pad, {'note': IntValue(0x2c), 'channel': IntValue(0x00)}),
        ('pad6',  Pad, {'note': IntValue(0x2d), 'channel': IntValue(0x00)}),
        ('pad7',  Pad, {'note': IntValue(0x2e), 'channel': IntValue(0x00)}),
        ('pad8',  Pad, {'note': IntValue(0x2f), 'channel': IntValue(0x00)}),
        ('pad9',  Pad, {'note': IntValue(0x28), 'channel': IntValue(0x00)}),
        ('pad10', Pad, {'note': IntValue(0x29), 'channel': IntValue(0x00)}),
        ('pad11', Pad, {'note': IntValue(0x2a), 'channel': IntValue(0x00)}),
        ('pad12', Pad, {'note': IntValue(0x2b), 'channel': IntValue(0x00)}),
        ('pad13', Pad, {'note': IntValue(0x24), 'channel': IntValue(0x00)}),
        ('pad14', Pad, {'note': IntValue(0x25), 'channel': IntValue(0x00)}),
        ('pad15', Pad, {'note': IntValue(0x26), 'channel': IntValue(0x00)}),
        ('pad16', Pad, {'note': IntValue(0x27), 'channel': IntValue(0x00)}),
    ]

class Button (BasicComponent):

    _PARAMS = [
        ('mode',    ButtonModeEnum, [0x00]),
        ('cc',      IntValue,       [0xff]), # intentionally invalid
        ('on',      IntValue,       [0x7f]),
        ('off',     IntValue,       [0x00]),
        ('channel', IntValue,       [0x00])
    ]

class Buttons (CompoundComponent):

    _COMPONENTS = [
        ('button1', Button, {'cc': IntValue(0x30)}),
        ('button2', Button, {'cc': IntValue(0x31)}),
        ('button3', Button, {'cc': IntValue(0x32)}),
        ('button4', Button, {'cc': IntValue(0x33)})
    ]

class VI49Switches (CompoundComponent):

    _COMPONENTS = [
        ('button1', Button, {'cc': IntValue(0x30)}),
        ('button2', Button, {'cc': IntValue(0x31)}),
        ('button3', Button, {'cc': IntValue(0x32)}),
        ('button4', Button, {'cc': IntValue(0x33)}),
        ('button5', Button, {'cc': IntValue(0x34)}),
        ('button6', Button, {'cc': IntValue(0x35)}),
        ('button7', Button, {'cc': IntValue(0x36)}),
        ('button8', Button, {'cc': IntValue(0x37)}),
        ('button9', Button, {'cc': IntValue(0x38)}),
        ('button10', Button, {'cc': IntValue(0x39)}),
        ('button11', Button, {'cc': IntValue(0x3a)}),
        ('button12', Button, {'cc': IntValue(0x3b)}),

        ('button13', Button, {'cc': IntValue(0x40)}),
        ('button14', Button, {'cc': IntValue(0x41)}),
        ('button15', Button, {'cc': IntValue(0x42)}),
        ('button16', Button, {'cc': IntValue(0x43)}),
        ('button17', Button, {'cc': IntValue(0x44)}),
        ('button18', Button, {'cc': IntValue(0x45)}),
        ('button19', Button, {'cc': IntValue(0x46)}),
        ('button20', Button, {'cc': IntValue(0x47)}),
        ('button21', Button, {'cc': IntValue(0x48)}),
        ('button22', Button, {'cc': IntValue(0x49)}),
        ('button23', Button, {'cc': IntValue(0x4a)}),
        ('button24', Button, {'cc': IntValue(0x4b)}),

        ('button25', Button, {'cc': IntValue(0x50)}),
        ('button26', Button, {'cc': IntValue(0x51)}),
        ('button27', Button, {'cc': IntValue(0x52)}),
        ('button28', Button, {'cc': IntValue(0x53)}),
        ('button29', Button, {'cc': IntValue(0x54)}),
        ('button30', Button, {'cc': IntValue(0x55)}),
        ('button31', Button, {'cc': IntValue(0x56)}),
        ('button32', Button, {'cc': IntValue(0x57)}),
        ('button33', Button, {'cc': IntValue(0x58)}),
        ('button34', Button, {'cc': IntValue(0x59)}),
        ('button35', Button, {'cc': IntValue(0x5a)}),
        ('button36', Button, {'cc': IntValue(0x5b)})
    ]

class VIUnknown (BasicComponent):

    _PARAMS = [
        ('unk00', IntValue, [0x30]),
        ('unk01', IntValue, [0x30]),
        ('unk02', IntValue, [0x30]),
        ('unk03', IntValue, [0x30]),
        ('unk04', IntValue, [0x30]),
        ('unk05', IntValue, [0x30]),
        ('unk06', IntValue, [0x30]),
        ('unk07', IntValue, [0x30]),
        ('unk08', IntValue, [0x30]),
        ('unk09', IntValue, [0x30]),
        ('unk10', IntValue, [0x30]),
        ('unk11', IntValue, [0x30]),
        ('unk12', IntValue, [0x30]),
        ('unk13', IntValue, [0x30]),
        ('unk14', IntValue, [0x30]),
        ('unk15', IntValue, [0x4b])
    ]

class KeySplit (BasicComponent):

    _PARAMS = [
        ('split_disable', IntValue, [0x01]),
        ('split_point', IntValue, [0x00])
    ]

class VIKeys (CompoundComponent):

    _COMPONENTS = [
        ('keybed', Keys, {'octave': IntValue(0x03)}),
        ('split', KeySplit, {}),
        ('lower_keybed', Keys, {'octave': IntValue(0x03)}),
        ('upper_keybed', Keys, {'octave': IntValue(0x03)})
    ]

class VIRoll (BasicComponent):

    _PARAMS = [
        ('function', IntValue, [0x00]),
        ('time_div', IntValue, [0x00]),
        ('gate',     IntValue, [0x31]),
        ('swing',    IntValue, [0x00])
    ]

class TransportControl (BasicComponent):

    _PARAMS = [
        ('mode', IntValue, [0x00]),
        ('cc', IntValue, [0xff]),
    ]

class Transport (CompoundComponent):

    _COMPONENTS = [
        ('rewind',       TransportControl, {'cc': IntValue(116)}),
        ('fast_forward', TransportControl, {'cc': IntValue(117)}),
        ('stop',         TransportControl, {'cc': IntValue(118)}),
        ('play',         TransportControl, {'cc': IntValue(119)}),
        ('loop',         TransportControl, {'cc': IntValue(115)}),
        ('record',       TransportControl, {'cc': IntValue(114)}),
    ]

class VIMIDI2DIN (BasicComponent):

    _PARAMS = [
        ('transport',    IntValue, [0x01]),
        ('keybed',       IntValue, [0x01]),
        ('lower_keybed', IntValue, [0x01]),
        ('upper_keybed', IntValue, [0x01]),
        ('pitch_wheel',  IntValue, [0x01]),
        ('mod_wheel',    IntValue, [0x01]),
        ('sustain',      IntValue, [0x01]),
        ('knobs',        IntValue, [0x01]),
        ('pads',         IntValue, [0x01]),
        ('switches',     IntValue, [0x01])
    ]

class AlesisModel (CompoundComponent):

    @classmethod
    def findModelByDeviceId(cls, device_id):
        for subclass in cls.__subclasses__():
            if subclass._DEVICE_ID == device_id:
                return subclass

class AlesisV25 (AlesisModel):

    _PORT_PREFIX = "V25:V25 MIDI 2"
    _DEVICE_ID   = [0x00, 0x41]

    _COMPONENTS = [
        ('keys',    Keys,       {}),
        ('pwheel',  PitchWheel, {}),
        ('mwheel',  ModWheel,   {}),
        ('sustain', Sustain,    {}),
        ('knobs',   Knobs,      {}),
        ('pads',    Pads,       {}),
        ('buttons', Buttons,    {})
    ]

    _GROUPS = (('Keys / Wheels / Sustain', 'horizontal',
                (('Keys', 'keys'),
                 ('Pitch Wheel', 'pwheel'),
                 ('Mod Wheel', 'mwheel'),
                 ('Sustain', 'sustain'))),
               ('Knobs / Buttons', 'vertical',
                (('Knobs', 'knobs'),
                 ('Buttons', 'buttons'))),
               ('Pads', 'vertical',
                (('Pads', 'pads'),)))

class AlesisVMini (AlesisModel):

    _PORT_PREFIX = "VMini:VMini MIDI 2"
    _DEVICE_ID   = [0x00, 0x49]

    _COMPONENTS = [
        ('keys',    Keys,       {}),
        ('pwheel',  VMiniPitchWheel, {}),
        ('mwheel',  VMiniModWheel,   {}),
        ('sustain', VMiniSustain,    {}),
        ('knobs',   Knobs,      {}),
        ('pads',    VMiniPads,       {})
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

class AlesisVI49 (AlesisModel):

    _PORT_PREFIX = "VI49:VI49 MIDI 2"
    _DEVICE_ID   = [0x00, 0x3f]

    _COMPONENTS = [
        ('unknown',   VIUnknown,    {}),
        ('keys',      VIKeys,       {}),
        ('roll',      VIRoll,       {}),
        ('transport', Transport,    {}),
        ('pwheel',    PitchWheel,   {}),
        ('mwheel',    ModWheel,     {}),
        ('sustain',   VISustain,    {}),
        ('knobs',     VI49Knobs,    {}),
        ('pads',      VIPads,       {}),
        ('switches',  VI49Switches, {}),
        ('midi2din',  VIMIDI2DIN,   {})
    ]

    _GROUPS = (('Knobs', 'vertical',
                (('Knobs', 'knobs'),)),
               ('Switches', 'vertical',
                (('Switches', 'switches'),)),
               ('Pads', 'vertical',
                (('Pads', 'pads'),)),
               ('Roll', 'horizontal',
                (('Roll', 'roll'),)),
               ('Transport', 'vertical',
                (('Transport', 'transport'),)),
               ('Keys', 'vertical',
                (('Keys', 'keys'),)),
               ('Mod / Pitch', 'horizontal',
                (('Mod Wheel', 'mwheel'),
                 ('Pitch Wheel', 'pwheel'))),
               ('Sustain', 'horizontal',
                (('Sustain Pedal', 'sustain'),)))
