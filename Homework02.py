# Micah Clarke
# ID: 1001288866

import numpy as np
import time
import scipy.io.wavfile
import math
import wave
import struct

def save_file(filename):

    wavfile = wave.open(filename,"w")

    # wav parameters

    # Number of channels
    nchannels = 1
    # Sample width in bytes
    sampwidth = 2
    # Number of frames or samples
    nframes = len(data)
    
    comptype = "NONE"
    compname = "not compressed"

    wavfile.setparams((nchannels, sampwidth, samples, nframes, comptype, compname))

    for sample in data:
        """
        struct - Takes the data from my "data" list and packs it as binary data or else
        the file is not readable by an audio player.

        h - Means 16 bit number

        32767.0 - The floating point numbers are not represented right and will not work
        when writing to the wave file. Convert the floating point numbers to fixed point
        to get full scale audio.
        """
        wavfile.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wavfile.close()

    return


    
# Keys from Lines 1 and 3
keys = [52,52,59,59,61,61,59,59,57,57,56,56,54,54,56,52,59,59,57,57,56,56,54,54]
# Counter for keys array (list)
j = 0
    
# Number of notes to be played
notes = 24
# Counter for number of notes to be played, used in while loop
i = 1
    
# Samples per second
samples = 8000
# Duration
duration = 0.5

# Signal data stored to be transferred to the wav file
data = []
# List for data points to be taken for each note
x = np.arange(0,0.5,1/samples)

while i <= notes :
        
    # Frequency Formula
    freq = 440*(2**((keys[j]-49)/12))

    # Generate wave for note
    waveform = np.cos(2 * np.pi * freq * x)

    # Store note data in list
    data = np.append(data,waveform)

    j += 1
    i += 1

  
save_file("twinkle.wav")

#scipy.io.wavfile.write('example.wav',8000,data) - Ended up not using this, but left for reference
#sd.play(data, samples) - Will play the tune without the wav file
