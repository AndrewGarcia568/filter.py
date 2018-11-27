import face_recognition
import cv2
from PIL import Image
from fil import *

video_capture = cv2.VideoCapture(0)
face_locations = []
mask = cv2.imread("ironman1.png")
h = float(mask.shape[0])
w = float(mask.shape[1])
process = True

while True:
    ret, frame = video_capture.read()
    feed = Feed(frame)
    face = feed.faceloc()
    for (top, right, bottom, left) in face:
        img = Image.fromarray(frame)
        crop = img.crop( (left, top, right, bottom) )
        crop.save('recog.png')
        cropped = cv2.imread('recog.png')
        hf = float(cropped.shape[0])
        wf = float(cropped.shape[1])
        res = feed.resize(mask, hf, h, wf, w)
        res = Image.fromarray(res)
        res.save('bago.png')
        frame = Image.fromarray(frame)
        frame.save('frame.png')
        last = Image.open('ironman1.png')
        na = Image.open('frame.png').convert('RGBA')
        feed.overlaydis(na, last)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
