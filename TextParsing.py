import datetime
import srt 
import heapq
import queue as Q
from HighlightClip import Clip
from audio import audioPriority
import matplotlib.pyplot as plt
import numpy as np

def main():
    """Opens the soccer video file and allows access to it's contents"""
    with open("Soccermatch/Y2Mate.is - FULL MATCH Real Madrid 2 - 3 Barça (2017) Me... (1).srt","r") as f:
        reader = srt.parse(f)
        clips: dict[int, Clip] = {}
        
        for sub in reader:
            clip = parseHelper(sub)
            clips[clip.getId()] = clip
            
        f.close()

    pq = Q.PriorityQueue()

    for i in range(1, 1370):
        clips[i].audio_priority = audioPriority(clips[i])
        clips[i].priority -= clips[i].audio_priority
        pq.put((clips[i].priority, clips[i].id, clips[i]))
    
    clipList = []

    totalTime: int = 0
    while totalTime < 30:
        current: Clip = pq.get()[2]
        totalTime += current.getDuration()
        clipList.append(current.getId())
        print(f"{current.getId()} : {current.getPriority()}")

def parseHelper(sub):
        id = sub.index
        start = round(sub.start.seconds, 1)
        end = round(sub.end.seconds, 1)
        duration = round(abs(start - end))

        # If start and end timestamps are switched.
        if start > end:
            start, end = end, start

        content = sub.content

        priority = priorityCheck(content)

        return Clip(id, start, end, duration, priority)


def priorityCheck(text) -> int:
    """Takes in a sentence and returns the priority."""
    keywords5: list[str] = ["goal", "assist", "injury", "injured", "red card", "yellow card", "sent off", "free kick", "penalty","banger", "penalty", "hat trick", "nutmeg","cross","shot","all alone",]
    keywords4: list[str] = ["stunning","rocket","oh my go","foul","score","down the wing",]
    keywords3: list[str] = ["amaz","brutal","restart","stun","shock","super","spectacular"]
    keywords2 = []
    keywords1 = []
    
    if wordExists(text, keywords5):
        return -5

    elif wordExists(text, keywords4):
        return -4
    
    elif wordExists(text, keywords3):
        return -3

    elif wordExists(text, keywords2):
        return -2
    
    elif wordExists(text, keywords1):
        return -1
    
    else:
        return 0


def wordExists(sentence, words) -> bool:
    """
    sentence = A text sentence.
    words = A list of keywords.
    """
    for word in words:
        if word in sentence:
            return True
    return False


main()
