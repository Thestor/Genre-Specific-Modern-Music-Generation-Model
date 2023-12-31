import os

# Define the musical styles
genre = [
    'pop',
    'down',
    'basic'
]

styles = [
    [
        'data/pop/ariana',
        'data/pop/azari',
        'data/pop/balloon',
        'data/pop/bieber',
        'data/pop/chainsawman',
        'data/pop/domesticnokanojo',
        'data/pop/kanaria',
        'data/pop/kessokuband',
        'data/pop/kimetsunoyaiba',
        'data/pop/kiminonawa',
        'data/pop/loveandproducer',
        'data/pop/miku',
        'data/pop/naruto',
        'data/pop/pinocchiop',
        'data/pop/tuyu',
        'data/pop/utapri',
        'data/pop/yoasobi',
        'data/pop/youjosenki'
    ],
    [
        'data/down/angelbeats',
        'data/down/anohana',
        'data/down/clannad',
        'data/down/gokukoku',
        'data/down/gundamnarrative',
        'data/down/harmonie',
        'data/down/moomins',
        'data/down/nana',
        'data/down/soundofmagic',
        'data/down/suzume',
        'data/down/westlife',
        'data/down/yourlieinapril'
    ],
    [
        'data/basic/alan',
        'data/basic/alexgaudino',
        'data/basic/basshunter',
        'data/basic/cascada',
        'data/basic/culturebeat'
    ]
]

NUM_STYLES = sum(len(s) for s in styles)

# MIDI Resolution
DEFAULT_RES = 96
MIDI_MAX_NOTES = 128
MAX_VELOCITY = 127

# Number of octaves supported
NUM_OCTAVES = 7
OCTAVE = 12

# Min and max note (in MIDI note number)
MIN_NOTE = 24
MAX_NOTE = MIN_NOTE + NUM_OCTAVES * OCTAVE
NUM_NOTES = MAX_NOTE - MIN_NOTE

# Number of beats in a bar
BEATS_PER_BAR = 4
# Notes per quarter note
NOTES_PER_BEAT = 4
# The quickest note is a half-note
NOTES_PER_BAR = NOTES_PER_BEAT * BEATS_PER_BAR

# Training parameters
BATCH_SIZE = 8
SEQ_LEN = 8 * NOTES_PER_BAR

# Hyper Parameters
OCTAVE_UNITS = 64
STYLE_UNITS = 64
NOTE_UNITS = 3
TIME_AXIS_UNITS = 256
NOTE_AXIS_UNITS = 128

TIME_AXIS_LAYERS = 2
NOTE_AXIS_LAYERS = 2

# Move file save location
OUT_DIR = 'out'
MODEL_DIR = os.path.join(OUT_DIR, 'models')
MODEL_FILE = os.path.join(OUT_DIR, 'model.h5')
SAMPLES_DIR = os.path.join(OUT_DIR, 'samples')
CACHE_DIR = os.path.join(OUT_DIR, 'cache')
