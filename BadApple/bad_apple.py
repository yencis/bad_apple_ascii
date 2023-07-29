from itertools import islice
import time

with open('badapple.txt','r') as ba:
    count = 1
    while count < 6573:
        comp_frames = list(islice(ba, 36))
        if not comp_frames:
            break
        frame = ""
        for comp_frame in comp_frames:
            values = comp_frame.split("|")
            frame += "".join([values[i] * (int(values[i+1])*2) for i in range(0, len(values), 2)])+"\n"
        print(frame)
        time.sleep(0.016666666)
        count += 1
