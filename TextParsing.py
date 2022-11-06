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
    with open("Video.srt","r") as f:
        reader = srt.parse(f)
        i = 0
        for sub in reader:
            print(sub)
            start = sub.start.seconds
            end = sub.end.seconds
            duration = abs(start - end)
            content = sub.content
            # i += 1
            # if i == 10:
            #     break
            print(start, end)
        
            

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
        """Instantiates the class."""
        self.id = id
        self.start = start
        self.end = end
        self.duration = duration
        self.text = text


    def getDuration(self):
        """Gives you the duration of the timestamp."""
        return self.end - self.start


    def 

main()