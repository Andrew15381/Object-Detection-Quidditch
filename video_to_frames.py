import cv2
import numpy as np

def save_video_frames(src, trgt):
    cap = cv2.VideoCapture(src)
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        frame = cv2.filter2D(frame, -1, kernel)

        count += 1
        cv2.imwrite(trgt + '{0}.jpg'.format(count), frame)
    cap.release()

srcs = ['C:\\Users\\Admin\\Downloads\\VID_20190519_171447.mp4',
        'C:\\Users\\Admin\\Downloads\\VID_20190519_171602.mp4',
        'C:\\Users\\Admin\\Downloads\\VID_20190519_171730.mp4',
        'C:\\Users\\Admin\\Downloads\\VID_20190519_171633.mp4']

trgts = ['C:\\Users\\Admin\\Downloads\\Dataset5\\',
         'C:\\Users\\Admin\\Downloads\\Dataset6\\',
         'C:\\Users\\Admin\\Downloads\\Dataset7\\']

for src, trgt in zip(srcs, trgts):
    save_video_frames(src, trgt)
