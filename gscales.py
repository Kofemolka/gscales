import sys

notes = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" ]
tuning = [ "E", "B", "G", "D", "A", "E" ]
frets = 24

scales = {
    "arabian" : { 0, 2, 3, 5, 6, 8, 9, 11 },
    "persian" : { 0, 1, 4, 5, 6, 8, 11 },
    "byzantine" : { 0, 1, 4, 5, 7, 8, 11 }, 
    "egyptian" : { 0, 2, 5, 7, 10 },
    "oriental" : { 0, 1, 4, 5, 6, 9, 10 },
    "japanese" : { 0, 2, 5, 7, 8 },
    "hirajoshi" : { 0, 2, 3, 7, 8 },
    "asavari_asc" : { 0, 1, 5, 7, 8 },
    "asavari_desc" : { 0, 1, 3, 5, 7, 8, 10 },
    "hungarian" : { 0, 2, 3, 6, 7, 8, 11 },
    "romanian" : { 0, 2, 3, 6, 7, 9, 10 },
    "hijaz" : { 0, 1, 4, 5, 7, 8, 10 },

    "mixolid_b6" : { 0, 2, 4, 5, 7, 8, 10 },

    "maj" : { 0, 2, 4, 5, 7, 9, 11 },
    "maj_pent" : { 0, 2, 4, 7, 9 },
    "maj_blues" : { 0, 2, 3, 4, 7, 9 },
    
    "min" : { 0, 2, 3, 5, 7, 8, 10 },
    "min_harm" : { 0, 2, 3, 5, 7, 8, 11 },
    "min_mel" : { 0, 2, 3, 5, 7, 9, 11 },
    "min_pent" : { 0, 3, 5, 7, 10 },
    "min_blues" : { 0, 3, 5, 6, 7, 10 },

    "dim" : { 0, 2, 3, 5, 6, 8, 11 },
    "aug" : { 0, 3, 4, 7, 8, 11 },
    "whole" : { 0, 2, 4, 6, 8, 10 }
}

def build_string(tuning, root, scale):
    stringBase = notes.index(tuning)
    rootNote = notes.index(root)    

    scaleNotes = [ (s+rootNote) % 12 for s in scale ]

    print(tuning + ": ", end='')
    for f in range(0, frets):
        note = (stringBase + f) % 12
        if note in scaleNotes:
            if note == scaleNotes[0]:
                print(' * ', end='')
            else:
                print(' {0} '.format(scaleNotes.index(note)+1), end='')
        else:
            print('   ', end='')
        print('|', end='')

    print()
    
def print_neck():
    print('   ', end='')

    for f in range(0,frets):
        if f in [0,3,5,7,9,12]:
            print(' {0}  '.format(f), end='')
        else:
            print('    ', end='')
    print()

if len(sys.argv) < 3:
    print("Usage: {0} <KEY> <scale>".format(sys.argv[0]))
    print("[Scales]:")
    for k,v in scales.items():
        print(k)

else:
    key = sys.argv[1]
    scale = sys.argv[2]
    print("=== {0} scale in key of {1} ===".format(scale, key))

    print_neck()        
    for t in tuning:
        build_string(t, key, scales[scale])
