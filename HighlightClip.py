"""
Class for objects called Clip, which contains timestamps from the video.
Each clip is assigned a priority when it is entered based on textual keywords from the transcript,
energy levels from the audio, and score changes from image recognition. 
"""


class Clip:
    """A class to encapsulate the metrics of a highlight clip."""
    id: int
    start: int
    end: int
    duration: int
    priority: int


    def __init__(self,id,start,end,duration, priority):
        """
        Instantiates the class.
        id = Unique identifier token for a particular clip.
        start = Start of the clip in seconds
        end = End of the clip in seconds
        duration = Duration of the clip in seconds
        priority = Integer value from 0-5 to with 5 being the highest priority for a clip. 
                   A higher priority clip is more likely to be included in the highlight 
                   compilation than one which has lower priority. 
                   Priority is assigned based on text, image, and audio recognition.
        """
        self.id = id
        self.start = start      # Stores the start in seconds
        self.end = end          # Stores the end time of the clip in seconds.
        self.duration = duration
        self.priority = priority


    def getId(self):
        """Returns the ID for a clip."""
        return self.id


    def getStart(self):
        """Returns the start of the clip in seconds."""
        return self.start


    def getStartMs(self):
        """Returns the start of the clip in milliseconds (ms)."""
        return self.start * 1000

    
    def getEnd(self):
        """Returns the end of the clip in seconds."""
        return self.end


    def getEndMs(self):
        """Returns the end of the clip in milliseconds (ms)."""
        return self.end * 1000


    def getDuration(self):
        """Gives you the duration of the timestamp."""
        return self.end - self.start


    def getPriority(self):
        """Returns the priority for a given Clip."""
        return self.priority

    
    def setStart(self, x):
        """Sets the start of the clip in seconds."""
        self.start = x

    
    def setEnd(self, x):
        """Sets the end of the clip in seconds."""
        self.end = x

    
    def setDuration(self, x):
        """Sets the duration of the clip in seconds"""
        self.duration = x


    def setPriority(self, x):
        """Sets the priority for the Clip."""
        self.priority = x