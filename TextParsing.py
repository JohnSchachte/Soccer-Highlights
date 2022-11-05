import datetime
import pysrt
import srt 

id = 0
start: int
end: int
duration: int
content: str
priority = 0

def main():
    """Opens the soccer video file and allows access to it's contents"""
    with open("/Users/andydong/Downloads/Soccer-Highlights/Soccermatch/Video.srt","r") as f:
        reader = srt.parse(f)
        for sub in reader:
            start = sub.start.microseconds * 1000
            end = sub.end.microseconds * 1000
            duration = abs(start - end)
            content = sub.content
            print(start)
            print(end)
            print(duration)


class HighlightClip:
    """a class to encapsulate the metrics of a highlight clip."""
    id: int
    start: int
    end: int
    duration: int
    text: str
    maxDb: int
    avgDb: int
    priority: int

    def __init__(self,id,start,end,duration,text):
        """"""
        self.id = id
        self.start = start
        self.end = end
        self.duration = duration
        self.text = text

main()