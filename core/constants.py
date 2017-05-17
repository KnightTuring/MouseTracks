from core.functions import SimpleConfig


DEFAULT_NAME = 'Default'

COLOURS_MAIN = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'white': (255, 255, 255),
    'grey': (127, 127, 127),
    'gray': (127, 127, 127),
    'black': (0, 0, 0),
    'orange': (255, 127, 0),
    'pink': (255, 0, 127),
    'purple': (127, 0, 255)
}

COLOUR_MODIFIERS = {
    'light': (128, 0.5),
    'dark': (0, 0.5)
}

_config_defaults = [
    ('Main', {
        'UpdatesPerSecond': (60, int, 'This is probably best left at 60 even if'
                                      ' you have a higher refresh rate.'),
        'RepeatKeyPress': (0.0, float, 'Record a new key press at this frequency'
                                        ' if a key is being held down (set to 0.0 to disable).'),
        'RepeatClicks': (0.18, float, 'Record a new click at this frequency'
                                      ' if the mouse is being held down (set to 0.0 to disable).')
    }),
    ('CompressMaps', {
        '__note__': ['Set how often the older tracks should be compressed, and by how much.',
                     'This helps keep the most recent data visibile.'],
        'TrackMaximum': (432000, int),
        'TrackReduction': (1.1, float),
        'SpeedMaximum': (108000, int),
        'SpeedReduction': (1.3, float)
    }),
    ('Save', {
        'Frequency': (120, int),
        'MaximumAttemptsNormal': (8, int, 'Maximum number of failed save attempts'
                                          ' before the tracking continues.'),
        'MaximumAttemptsSwitch': (24, int, 'Maximum number of failed save attempts'
                                          ' when switching profile.'
                                          ' If this fails then the latest data will be lost.'),
        'WaitAfterFail': (5, int, 'How many seconds to wait before trying again.')
    }),
    ('Paths', {
        'Data': ('Data', str)
    }),
    ('Timer', {
        'CheckPrograms': (2, int),
        'CheckResolution': (1, int),
        'ReloadPrograms': (600, int)
    }),
    ('GenerateImages', {
        '__note__': ['For the best results, make sure the upscale resolution'
                     ' is higher than or equal to the highest recorded resolution.'],
        'UpscaleResolutionX': (3840, int),
        'UpscaleResolutionY': (2160, int),
        'OutputResolutionX': (1920, int),
        'OutputResolutionY': (1080, int),
        'FileType': ('jpg', str)
    }),
    ('GenerateHeatmap', {
        'NameFormat': ('Result\\[FriendlyName] [MouseButtons] Heatmap - [ColourProfile]', str),
        'MouseButtonLeft': (True, bool),
        'MouseButtonMiddle': (True, bool),
        'MouseButtonRight': (True, bool),
        'GaussianBlurSize': (20, int),
        'ExponentialMultiplier': (1.0, float),
        'ColourProfile': ('Jet', str),
        'SetMaxRange': (0, int, 'Manually set the highest value.'
                                ' Set to 0 to use auto, otherwise use trial and error'
                                ' to get it right.')
    }),
    ('GenerateTracks', {
        'NameFormat': ('Result\\[FriendlyName] Tracks - [ColourProfile]', str),
        'ColourProfile': ('WhiteToBlack', str)
    }),
    ('GenerateSpeedMap', {
        'NameFormat': ('Result\\[FriendlyName] Speed - [ColourProfile]', str),
        'ColourProfile': ('WhiteToBlack', str)
    }),
    ('GenerateCombined', {
        'NameFormat': ('Result\\[FriendlyName] Combined - [ColourProfile]', str),
        'ColourProfile': ('WhiteToBlack', str)
    })
]

CONFIG = SimpleConfig('config.ini', _config_defaults)
