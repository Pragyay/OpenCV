import cv2
import numpy

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv[cy, cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]

    color = "NULL"

    if hue < 12:
        color = 'Orange'
    elif hue < 30:
        color = 'Yellow'
    elif hue < 93:
        color = 'Green'
    elif hue < 133:
        color = 'Blue'
    elif hue < 142:
        color = 'Purple'
    elif hue < 160:
        color = 'pink'
    else:
        color = 'Red'

    # print(pixel_center)
    center_color = frame[cy, cx]
    b, g, r = int(center_color[0]), int(center_color[1]), int(center_color[2])

    cv2.putText(frame, color, (int(width/2) - 40, int(height) - 20), 0, 1, (b, g, r), 2)

    cv2.circle(frame, (cx, cy), 10, (255,0,0), 5)

    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()