import datetime
import srt 
import heapq
import queue as Q
from HighlightClip import Clip

def main():
    pq = Q.PriorityQueue()
    """Opens the soccer video file and allows access to it's contents"""
    with open("Soccermatch/Y2Mate.is - FULL MATCH Real Madrid 2 - 3 Barça (2017) Me... (1).srt","r") as f:
        reader = srt.parse(f)
        clips: dict[int, Clip] = {}
        
        for sub in reader:
            clip = parseHelper(sub)
            
            clips[clip.getId()] = clip
            pq.put((clip.priority,clip.id,clip))
        f.close()
        print(clips[1].getPriority())
    # print(clips[28].getStart())
    totalTime: int = 0
    while totalTime < 30:
        current: Clip = pq.get()[2]
        print(current)
        totalTime += current.getDuration()
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
