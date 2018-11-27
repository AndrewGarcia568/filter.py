import face_recognition
import cv2
from PIL import Image

class Feed:
    def __init__(self, frame):
        self.frame = frame[:, :, ::-1]
    
    def faceloc(self):
        return face_recognition.face_locations(self.frame)
   
    def display(self, frame):
        for (top, right, bottom, left) in (self.faceloc()):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        return cv2.imshow('Video', frame)

    def lengthratio(self, hf, h):
        res = hf / h
        return float(res)

    def widthratio(self, wf, w):
        res = wf / w
        return float(res)

    def resize(self, img, faceh, height, facew, width):
        resizedimg = cv2.resize(img, (0, 0), fx = 0.2+(float(self.widthratio(facew, width))), fy = 0.2+(float(self.lengthratio(faceh, height))))
        return resizedimg

    def overlaydis(self, src1, img):
        var = self.coords()
        src1.paste(img, var, img)
        src1.save("OUT.png")
        out = cv2.imread('OUT.png')
        out1 = out[:, :, ::-1]
        return cv2.imshow('Video', out1)
    def coords(self):
        for (top, right, bottom, left) in (self.faceloc()):
            var = (left - 120, top - 150)
        return var
