# https://www.youtube.com/watch?v=gH_kQZo-NSk&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=2

import cv2 as cv

# img = cv.imread("./data/lena.png")
# cv.imshow("Lena",img)
# k = cv.waitKey(0) # Wait for a keystroke in the window

framewidth = 1200
frameheight = 720
capturing = cv.VideoCapture("./data/YogeshPhD_MidsurfaceTestCases.mp4")
# capturing = cv.VideoCapture(0) # webcam device
# capturing.set(3,framewidth)
# capturing.set(4,frameheight)

while True:
    success, img = capturing.read()  # reads frame by frame from video, into 'img' and result of import in 'sucess'
    img = cv.resize(img, (framewidth, frameheight))
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
