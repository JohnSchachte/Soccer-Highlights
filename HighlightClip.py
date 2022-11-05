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
def main():
    return
if __name__ == "__main__":
    main()
