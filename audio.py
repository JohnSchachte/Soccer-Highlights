from HighlightClip import Clip
import pandas as pd
import numpy as np
import librosa
x, sr = librosa.load("match.wav", sr = 16000)

def audioPriority(clip: Clip):
    
    start = clip.getStart()
    end = clip.getEnd()

    audio = x[start*sr:end*sr]
    energy = sum(abs(audio**2))
        
    if energy > 750:
      return 5
    
    elif energy > 600:
      return 4
    
    elif energy > 400:
      return 3

    elif energy > 350:
      return 2

    elif energy > 150:
      return 1
      
    else:
      return 0


def main():
    return
