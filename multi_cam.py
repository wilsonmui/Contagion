# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting cameras...")
webcam = VideoStream(src=0).start()
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the cameras recording
while True:

    # iterate over the cameras
    for wcam, pcam in zip(webcam, picam):
        wcamStream = wcam.read()
        wcamStream = imutils.resize(wcamStream, width=400)

        pcamStream = pcam.read()
        pcamStream = imutils.resize(pcamStream, width=400)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
webcam.stop()
picam.stop()
cv2.destroyAllWindows()
