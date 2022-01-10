import struct

from alesisvsysex.protocol.types import *
from alesisvsysex.protocol.component import *

__all__ = ['AlesisModel', 'AlesisV25', 'AlesisVMini', 'AlesisVI25', 'AlesisVI49', 'Keys' , 'PitchWheel', 'VMiniPitchWheel', 'ModWheel', 'VMiniModWheel', 'Sustain', 'VMiniSustain', 'Knob', 'Knobs', 'Pad', 'Pads', 'VMiniPads', 'Button', 'Buttons']

class Keys (BasicComponent):

    _PARAMS = [
        ('transpose',   Transpose,  [0]),
        ('octave',      Octave,   [0x05]),
        ('channel',     MIDIChannelEnum,   [0x00]),
        ('curve',       Curve,      [0x05])
    ]

class VMiniKeys (BasicComponent):

    _PARAMS = [
        ('transpose',   Transpose,  [0]),
        ('octave',      VMiniOctave,   [0]),
        ('channel',     MIDIChannelEnum,   [0x00]),
        ('curve',       Curve,      [0x05])
    ]

class PitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelEnum,   [0x00])
    ]

class VIPitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelOmniEnum,   [0x00])
    ]

class VMiniPitchWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelEnum,   [0x00]),
        ('rate',        IntValue,   [0x50])
    ]

class ModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelEnum,   [0x00]),
        ('cc',          IntValue,   [0x01]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f])
    ]

class VIModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelOmniEnum,   [0x00]),
        ('cc',          IntValue,   [0x01]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f])
    ]

class VMiniModWheel (BasicComponent):

    _PARAMS = [
        ('channel',     MIDIChannelEnum,   [0x00]),
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
        ('channel',     MIDIChannelEnum,   [0x00])
    ]

class VISustain (BasicComponent):

    _PARAMS = [
        ('cc',          IntValue,   [0x40]),
        ('pressed',     IntValue,   [0x7f]),
        ('released',    IntValue,   [0x00]),
        ('channel',     MIDIChannelEnum,   [0x00])
    ]

class VMiniSustain (BasicComponent):

    _PARAMS = [
        ('mode',    SusModeEnum,    [0x00]),
        ('cc',          IntValue,   [0x40]),
        ('min',         IntValue,   [0x00]),
        ('max',         IntValue,   [0x7f]),
        ('channel',     MIDIChannelEnum,   [0x00])
    ]

class Knob (BasicComponent):

    _PARAMS = [
        ('mode',        KnobModeEnum,   [0x00]),
        ('cc',          IntValue,       [0xff]), # intentionally invalid
        ('min',         IntValue,       [0x00]),
        ('max',         IntValue,       [0x7f]),
        ('channel',     MIDIChannelEnum,       [0x00])
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
    
class VI25Knobs (CompoundComponent):
  
    _COMPONENTS = [
        ('knob1',  Knob, {'cc': IntValue(0x14)}),
        ('knob2',  Knob, {'cc': IntValue(0x15)}),
        ('knob3',  Knob, {'cc': IntValue(0x16)}),
        ('knob4',  Knob, {'cc': IntValue(0x17)}),
        ('knob5',  Knob, {'cc': IntValue(0x18)}),
        ('knob6',  Knob, {'cc': IntValue(0x19)}),
        ('knob7',  Knob, {'cc': IntValue(0x1a)}),
        ('knob8',  Knob, {'cc': IntValue(0x1b)}),
        
    ]

class VI61Knobs (CompoundComponent):

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
        ('knob12', Knob, {'cc': IntValue(0x1f)}),
        ('knob13', Knob, {'cc': IntValue(0x23)}),
        ('knob14', Knob, {'cc': IntValue(0x29)}),
        ('knob15', Knob, {'cc': IntValue(0x2e)}),
        ('knob16', Knob, {'cc': IntValue(0x2f)})
    ]

class Pad (BasicComponent):

    _PARAMS = [
        ('mode',    PadModeEnum,    [0x00]),
        ('note',    IntValue,       [0xff]), # intentionally invalid
        ('fixed',   IntValue,       [0x00]),
        ('curve',   Curve,          [0x01]),
        ('channel', MIDIChannelEnum,       [0x09])
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
        ('pad1',  Pad, {'note': IntValue(0x30), 'channel': MIDIChannelEnum(0x00)}),
        ('pad2',  Pad, {'note': IntValue(0x31), 'channel': MIDIChannelEnum(0x00)}),
        ('pad3',  Pad, {'note': IntValue(0x32), 'channel': MIDIChannelEnum(0x00)}),
        ('pad4',  Pad, {'note': IntValue(0x33), 'channel': MIDIChannelEnum(0x00)}),
        ('pad5',  Pad, {'note': IntValue(0x2c), 'channel': MIDIChannelEnum(0x00)}),
        ('pad6',  Pad, {'note': IntValue(0x2d), 'channel': MIDIChannelEnum(0x00)}),
        ('pad7',  Pad, {'note': IntValue(0x2e), 'channel': MIDIChannelEnum(0x00)}),
        ('pad8',  Pad, {'note': IntValue(0x2f), 'channel': MIDIChannelEnum(0x00)}),
        ('pad9',  Pad, {'note': IntValue(0x28), 'channel': MIDIChannelEnum(0x00)}),
        ('pad10', Pad, {'note': IntValue(0x29), 'channel': MIDIChannelEnum(0x00)}),
        ('pad11', Pad, {'note': IntValue(0x2a), 'channel': MIDIChannelEnum(0x00)}),
        ('pad12', Pad, {'note': IntValue(0x2b), 'channel': MIDIChannelEnum(0x00)}),
        ('pad13', Pad, {'note': IntValue(0x24), 'channel': MIDIChannelEnum(0x00)}),
        ('pad14', Pad, {'note': IntValue(0x25), 'channel': MIDIChannelEnum(0x00)}),
        ('pad15', Pad, {'note': IntValue(0x26), 'channel': MIDIChannelEnum(0x00)}),
        ('pad16', Pad, {'note': IntValue(0x27), 'channel': MIDIChannelEnum(0x00)}),
    ]

class Button (BasicComponent):

    _PARAMS = [
        ('mode',    ButtonModeEnum, [0x00]),
        ('cc',      IntValue,       [0xff]), # intentionally invalid
        ('on',      IntValue,       [0x7f]),
        ('off',     IntValue,       [0x00]),
        ('channel', MIDIChannelEnum,       [0x00])
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
    ]

class VI49Switches2 (CompoundComponent):

    _COMPONENTS = [
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
    ]

class VI49Switches3 (CompoundComponent):

    _COMPONENTS = [
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
    
class VI25Switches (CompoundComponent):
  
    _COMPONENTS = [
        ('button1', Button, {'cc': IntValue(0x30)}),
        ('button2', Button, {'cc': IntValue(0x31)}),
        ('button3', Button, {'cc': IntValue(0x32)}),
        ('button4', Button, {'cc': IntValue(0x33)}),
        ('button5', Button, {'cc': IntValue(0x34)}),
        ('button6', Button, {'cc': IntValue(0x35)}),
        ('button7', Button, {'cc': IntValue(0x36)}),
        ('button8', Button, {'cc': IntValue(0x37)}),
        
    ]

class VI25Switches2 (CompoundComponent):

    _COMPONENTS = [
        ('button9', Button, {'cc': IntValue(0x38)}),
        ('button10', Button, {'cc': IntValue(0x39)}),
        ('button11', Button, {'cc': IntValue(0x3a)}),
        ('button12', Button, {'cc': IntValue(0x3b)}),
        ('button13', Button, {'cc': IntValue(0x3c)}),
        ('button14', Button, {'cc': IntValue(0x3d)}),
        ('button15', Button, {'cc': IntValue(0x3e)}),
        ('button16', Button, {'cc': IntValue(0x3f)}),
    ]

class VI25Switches3 (CompoundComponent):
    
    _COMPONENTS = [
        ('button17', Button, {'cc': IntValue(0x40)}),
        ('button18', Button, {'cc': IntValue(0x41)}),
        ('button19', Button, {'cc': IntValue(0x42)}),
        ('button20', Button, {'cc': IntValue(0x43)}),
        ('button21', Button, {'cc': IntValue(0x44)}),
        ('button22', Button, {'cc': IntValue(0x45)}),
        ('button23', Button, {'cc': IntValue(0x46)}),
        ('button24', Button, {'cc': IntValue(0x47)}),
    ]

class VI61Switches (CompoundComponent):

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
        ('button13', Button, {'cc': IntValue(0x3c)}),
        ('button14', Button, {'cc': IntValue(0x3d)}),
        ('button15', Button, {'cc': IntValue(0x3e)}),
        ('button16', Button, {'cc': IntValue(0x3f)}),
    ]

class VI61Switches2 (CompoundComponent):

    _COMPONENTS = [
        ('button17', Button, {'cc': IntValue(0x40)}),
        ('button18', Button, {'cc': IntValue(0x41)}),
        ('button19', Button, {'cc': IntValue(0x42)}),
        ('button20', Button, {'cc': IntValue(0x43)}),
        ('button21', Button, {'cc': IntValue(0x44)}),
        ('button22', Button, {'cc': IntValue(0x45)}),
        ('button23', Button, {'cc': IntValue(0x46)}),
        ('button24', Button, {'cc': IntValue(0x47)}),
        ('button25', Button, {'cc': IntValue(0x48)}),
        ('button26', Button, {'cc': IntValue(0x49)}),
        ('button27', Button, {'cc': IntValue(0x4a)}),
        ('button28', Button, {'cc': IntValue(0x4b)}),
        ('button29', Button, {'cc': IntValue(0x4c)}),
        ('button30', Button, {'cc': IntValue(0x4d)}),
        ('button31', Button, {'cc': IntValue(0x4e)}),
        ('button32', Button, {'cc': IntValue(0x4f)}),
    ]

class VI61Switches3 (CompoundComponent):

    _COMPONENTS = [
        ('button33', Button, {'cc': IntValue(0x50)}),
        ('button34', Button, {'cc': IntValue(0x51)}),
        ('button35', Button, {'cc': IntValue(0x52)}),
        ('button36', Button, {'cc': IntValue(0x53)}),
        ('button37', Button, {'cc': IntValue(0x54)}),
        ('button38', Button, {'cc': IntValue(0x55)}),
        ('button39', Button, {'cc': IntValue(0x56)}),
        ('button40', Button, {'cc': IntValue(0x57)}),
        ('button41', Button, {'cc': IntValue(0x58)}),
        ('button42', Button, {'cc': IntValue(0x59)}),
        ('button43', Button, {'cc': IntValue(0x5a)}),
        ('button44', Button, {'cc': IntValue(0x5b)}),
        ('button45', Button, {'cc': IntValue(0x5c)}),
        ('button46', Button, {'cc': IntValue(0x5d)}),
        ('button47', Button, {'cc': IntValue(0x5e)}),
        ('button48', Button, {'cc': IntValue(0x5f)})
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
        ('keybed', Keys, {'octave': Octave(0x03)}),
        ('split', KeySplit, {}),
        ('lower_keybed', Keys, {'octave': Octave(0x03)}),
        ('upper_keybed', Keys, {'octave': Octave(0x03)})
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

    _SLOT_CONFIG  = False
    _LENGTH_DELTA = 0

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
        ('keys',    VMiniKeys,       {}),
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

class AlesisVI25 (AlesisModel):
  
    _PORT_PREFIX  = "VI25:VI25 MIDI 2"
    _DEVICE_ID    = [0x00, 0x3f]
    _SLOT_CONFIG  = True
    _LENGTH_DELTA = 0x50

    _COMPONENTS = [
        ('unknown',   VIUnknown,    {}),
        ('keys',      VIKeys,       {}),
        ('roll',      VIRoll,       {}),
        ('transport', Transport,    {}),
        ('pwheel',    VIPitchWheel, {}),
        ('mwheel',    VIModWheel,   {}),
        ('sustain',   VISustain,    {}),
        ('knobs',     VI25Knobs,    {}),
        ('pads',      VIPads,       {}),
        ('switches',  VI25Switches, {}),
        ('switches2',  VI25Switches2, {}),
        ('switches3',  VI25Switches3, {}),
        ('midi2din',  VIMIDI2DIN,   {})
    ]

    _GROUPS = (('Knobs', 'vertical',
                (('Knobs', 'knobs'),)),
               ('Switches 1-8', 'vertical',
                (('Switches', 'switches'),)),
               ('Switches 9-16', 'vertical',
                (('Switches', 'switches2'),)),
               ('Switches 17-24', 'vertical',
                (('Switches', 'switches3'),)),
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
class AlesisVI49 (AlesisModel):

    _PORT_PREFIX  = "VI49:VI49 MIDI 2"
    _DEVICE_ID    = [0x00, 0x3f]
    _SLOT_CONFIG  = True
    _LENGTH_DELTA = 0x50

    _COMPONENTS = [
        ('unknown',   VIUnknown,    {}),
        ('keys',      VIKeys,       {}),
        ('roll',      VIRoll,       {}),
        ('transport', Transport,    {}),
        ('pwheel',    VIPitchWheel, {}),
        ('mwheel',    VIModWheel,   {}),
        ('sustain',   VISustain,    {}),
        ('knobs',     VI49Knobs,    {}),
        ('pads',      VIPads,       {}),
        ('switches',  VI49Switches, {}),
        ('switches2',  VI49Switches2, {}),
        ('switches3',  VI49Switches3, {}),
        ('midi2din',  VIMIDI2DIN,   {})
    ]

    _GROUPS = (('Knobs', 'vertical',
                (('Knobs', 'knobs'),)),
               ('Switches 1-12', 'vertical',
                (('Switches', 'switches'),)),
               ('Switches 13-24', 'vertical',
                (('Switches', 'switches2'),)),
               ('Switches 25-36', 'vertical',
                (('Switches', 'switches3'),)),
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

class AlesisVI61 (AlesisModel):

    _PORT_PREFIX  = "VI61:VI61 MIDI 2"
    _DEVICE_ID    = [0x00, 0x40]
    _SLOT_CONFIG  = True

    _COMPONENTS = [
        ('unknown',   VIUnknown,    {}),
        ('keys',      VIKeys,       {}),
        ('roll',      VIRoll,       {}),
        ('transport', Transport,    {}),
        ('pwheel',    VIPitchWheel, {}),
        ('mwheel',    VIModWheel,   {}),
        ('sustain',   VISustain,    {}),
        ('knobs',     VI61Knobs,    {}),
        ('pads',      VIPads,       {}),
        ('switches',  VI61Switches, {}),
        ('switches2',  VI61Switches2, {}),
        ('switches3',  VI61Switches3, {}),
        ('midi2din',  VIMIDI2DIN,   {})
    ]

    _GROUPS = (('Knobs', 'vertical',
                (('Knobs', 'knobs'),)),
               ('Switches 1-16', 'vertical',
                (('Switches', 'switches'),)),
               ('Switches 17-32', 'vertical',
                (('Switches', 'switches2'),)),
               ('Switches 33-48', 'vertical',
                (('Switches', 'switches3'),)),
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
