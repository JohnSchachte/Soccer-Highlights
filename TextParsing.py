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
        

main()