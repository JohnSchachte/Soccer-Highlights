import pysrt
import srt 

id: list
start: list
end: list
duration: list
text: list

def main():
    with open("/Users/andydong/Downloads/Soccer-Highlights/Soccermatch/Video.srt","r") as f:
        reader = srt.parse(f)
        for sub in reader:
            id.append(sub.index)
            start = sub.start
            end = sub.end
            duration = end - start
            text = sub.content
    print(sub)


main()
