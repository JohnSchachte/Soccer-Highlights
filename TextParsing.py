import datetime
import srt 

from HighlightClip import Clip

def main():
    """Opens the soccer video file and allows access to it's contents"""
    with open("/Users/yuvraj/Documents/University Files/Fall 2022/Soccer-Highlights/Soccermatch/captions.srt","r") as f:
        reader = srt.parse(f)
        clips: dict[int, Clip] = {}
        
        for sub in reader:
            clip = parseHelper(sub)
            clips[clip.getId()] = clip

        f.close()
    
    print(clips[28].getStart())
            

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
    keywords5 = ["goal", "stunning", "assist", "amazing", "rocket", "oh my go", "restarting", "foul", "injury", "brutal", "injured", "red card", "yellow card", "sent off", "free kick", "penalty","banger", "super", "penalty kick", "hat trick", "nutmeg", "amazing"]
    keywords4 = []
    keywords3 = []
    keywords2 = []
    keywords1 = []  
    text = "This was one heck of a goal."
    
    if wordExists(text, keywords5):
        return 5

    elif wordExists(text, keywords4):
        return 4
    
    elif wordExists(text, keywords3):
        return 3

    elif wordExists(text, keywords2):
        return 2
    
    elif wordExists(text, keywords1):
        return 1
    
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
