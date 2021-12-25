import cv2
from cvzone.HandTrackingModule import HandDetector

cam = cv2.VideoCapture(0)

cam.set(3, 900)
cam.set(4, 1200)

detector = HandDetector(detectionCon=0.8)

# rect_color = 255, 0, 255

class Rect():
    def __init__(self, posCenter, size=[100, 100], color=(255,0,255)):
        self.posCenter = posCenter
        self.size = size
        self.color = color

    def update(self, cursor):
        cx, cy = self.posCenter
        width, height = self.size

        if cx - width // 2 < cursor[0] < cx + width // 2 and \
                cy - height // 2 < cursor[1] < cy + height // 2:
            self.posCenter = cursor
            self.color = 0, 255, 0
        else:
            self.color = 255,0,255


# create rectangle objects
rectList = []
for x in range(5):
    rectList.append(Rect([x * 150 + 150, 150]))

while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)

    overlay = img.copy()

    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:  # if list is non-empty
        l, _, _ = detector.findDistance(8, 12, img)

        if l < 30:
            cursor = lmList[8]
            # print(cursor)
            for rect in rectList:
                rect.update(cursor)

    for rect in rectList:
        cx, cy = rect.posCenter
        width, height = rect.size
        rect_color = rect.color

        cv2.rectangle(overlay, (cx - width // 2, cy - height // 2), (cx + width // 2, cy + height // 2), rect_color, -1)

        img_new = cv2.addWeighted(overlay, 0.5, img, 0.5, 0)
        cv2.imshow("Image", img_new)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
