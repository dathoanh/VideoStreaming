import cv2
import os

class VideoStream:
    def __init__(self, filename):
        self.filename = filename
        self.fullVideo = []
        try:
            self.file = open(filename, 'rb')
        except:
            raise IOError
        self.frameNum = 0
        
    def nextFrame(self):
        """Get next frame - Get frames from video"""
        data = self.file.read(5) # Get the framelength from the first 5 bits
        if data: 
            framelength = int(data)
            data = self.file.read(framelength)
            self.frameNum += 1
        return data

    def getFullVideo(self):
        """Get next frame - Get frames from video"""
        if self.filename:
            # Get the framelength from the first 5 bits
            data = self.file.read(5)
            if data:
                framelength = int(data)
                self.fullVideo.append(framelength)
                data = self.file.read(framelength)
            return data


    def getTotalFrames(self):
        """Get total number of frames."""
        while self.getFullVideo():
            pass
        self.totalFrames = len(self.fullVideo)
        self.file.close()
        self.file = open(self.filename, 'rb')
    
    def getFps(self):
        """Get frames per second."""
        cap = cv2.VideoCapture("./{0}".format(self.filename))
        self.fps = int(cap.get(cv2.CAP_PROP_FPS))

    def getTotalTime(self):
        """Get total time of the video."""
        self.getTotalFrames()
        self.getFps()
        self.totalTime = self.totalFrames / self.fps
        
    def frameNbr(self):
        """Get frame number."""
        return self.frameNum
    
    def resetFrame(self):
        """Reset the movie frame to 0"""
        self.file.seek(0)
        self.frameNum = 0

    def getWidthvsHeight(self):
        cap = cv2.VideoCapture("./{0}".format(self.filename))
        self.width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)