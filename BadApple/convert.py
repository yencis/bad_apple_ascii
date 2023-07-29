import cv2
from PIL import Image
import math
path = "badapple.mp4"
"""
yencis
"""
ASCII = [" ", ".", ",", "%", "@"]

video = cv2.VideoCapture(path)

frameCount = 0
success = 1
while success:
    success, imgobj = video.read()
    if not success:
        break
    with open('badapple.txt', 'a', 10000000) as ba:
        dim = (int(imgobj.shape[1] * 0.1), int(imgobj.shape[0] * 0.1))
        resized = cv2.resize(imgobj, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        for i in range(gray.shape[0]):
            cur_val = ""
            count = 0
            for j in range(gray.shape[1]):
                ascii_val = ASCII[int(round(gray[i][j] * (1 / 255) * 4, 0))]
                if cur_val == "":
                    cur_val = ascii_val
                    count += 1
                elif ascii_val != cur_val:
                    ba.write(cur_val + "|" + str(count)+"|`")
                    cur_val = ascii_val
                    count = 1
                else:
                    count += 1
            ba.write(cur_val + "|" + str(count) + "\n")
    frameCount += 1

print(frameCount)
