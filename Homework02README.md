# Signal-Processing

Application Area: Music 

Purpose: See how sinusoids of specific frequencies lead to specific sounds.
On Blackboard, get the documents DSPFirst-lab3.pdf and twinkle.pdf. The former has
the background material that you need for this assignment and the latter has the music to
use. Both are from [MSY98].

(a) The document twinkle.pdf has 8 lines of notes from Twinkle, Twinkle Little Star. You
will write a Python program to produce an audio file of the 24 notes from lines 1 and 3.

(b) The first note will be C5 (key number 52) on the keyboard shown in Figure C.2 on page
436. The other notes will be relative to this note.

(c) For each note of the song, you will need to determine its approximate frequency, which
will be an offset of the key A4 (key number 49). The formula for this becomes
f = 440 × 2(keyNumber−49)/12

You will then use this frequency to produce 0.5 second of values of a cosine wave. When
creating your “continuous” signal, use a step rate of 1/8000 in your time values and an
amplitude of 1.

(d) Each note will represent 0.5 second of a sound, regardless of what the sheet music actually
says. That is, don’t differentiate between quarter notes, half notes, and so forth.

(e) You will ultimately produce a single sequence of values for the 24 notes by concatenating
the values of each of the cosine waves.

(f) You will create a .wav file called twinkle.wav using your sequence of values and a sample
rate of fs = 8000. Use the PySoundFile library https://pysoundfile.readthedocs.io/.
Note that this is not part of the Anaconda distribution, so you will need to install it.

(g) Your program will be called hw02.py (write it EXACTLY like that, including the zero).
General requirements about the Python problems:

a) Your code should run using Python 3.6 or greater and should not need libraries not provided
in the Anaconda distribution unless instructed to do so.

b) As a comment in your source code, include your name.


Reference: https://www.pythonforengineers.com/audio-and-digital-signal-processingdsp-in-python/
