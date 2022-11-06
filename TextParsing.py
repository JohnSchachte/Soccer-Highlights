import datetime
import pysrt
import srt 

id: int
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
            id = sub.index
            start = round(sub.start.seconds, 1)
            end = round(sub.end.seconds, 1)
            duration = round(abs(start - end))
            content = sub.content
            print(id, start, end, duration)
            print(content)
        return start, end, duration, id


main()