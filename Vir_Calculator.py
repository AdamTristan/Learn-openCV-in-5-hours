import cv2 as cv
from cvzone.HandTrackingModule import HandDetector as hd

# Basic preparation
cap = cv.VideoCapture(0)  # original camera of my computer
cap.set(3, 1920)  # change the size
cap.set(4, 1080)
detector = hd(detectionCon=0.7, maxHands=1)
alpha = 0.55  # alpha stands for the opacity of the button
eqa = ""  # initialize eqa
count = 0  # initialize count

class Buttom:

    def __init__(self, OriginalPosition, EndPosition, value):

        self.OriginalPosition = OriginalPosition
        self.EndPosition = EndPosition
        self.value = value

    def draw(self, image):  # Draw Function

        cv.rectangle(img_cp, self.OriginalPosition, self.EndPosition, (255, 255, 255), cv.FILLED)
        cv.rectangle(img_cp, self.OriginalPosition, self.EndPosition, (0, 0, 0), 2)
        cv.putText(img_cp, self.value, (self.OriginalPosition[0] + 20, self.OriginalPosition[1] + 85),
                   cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def isClick(self, x, y):  # Click Feedback
        if self.OriginalPosition[0] < x < self.EndPosition[0] and \
           self.OriginalPosition[1] < y < self.EndPosition[1]:
            cv.rectangle(img_cp, self.OriginalPosition, self.EndPosition, (255, 0, 255), cv.FILLED)
            cv.rectangle(img_cp, self.OriginalPosition, self.EndPosition, (0, 0, 0), 2)
            cv.putText(img_cp, self.value, (self.OriginalPosition[0] + 30, self.OriginalPosition[1] + 70),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
            return True
        else:
            return False

# Creating buttons
ButtonList = []
ButtonValueList = [['(', ')', '%', 'C'],
                   ['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['0', '.', '=', '+']]

for i in range(4):
    for j in range(5):
        xOriginalPosition = i * 100 + 100
        yOriginalPosition = j * 100 + 150
        xEndPosition = i * 100 + 200
        yEndPosition = j * 100 + 250
        ButtonList.append(Buttom((xOriginalPosition, yOriginalPosition),
                                 (xEndPosition, yEndPosition), ButtonValueList[j][i]))

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)  # flip horizontally
    img_cp = img.copy()  # another layer

    hands, img = detector.findHands(img, flipType=False)

    # Drawing the screen
    cv.rectangle(img_cp, (100, 150), (500, 65), (255, 255, 255), cv.FILLED)
    cv.rectangle(img_cp, (100, 150), (500, 65), (0, 0, 0), 2)

    # Drawing all the buttons
    for button in ButtonList:
        button.draw(img_cp)

    # Discriminate hands' motion
    if hands:
        lmList = hands[0]['lmList']
        length, _, img= detector.findDistance(lmList[4], lmList[8], img)  # Find the distance between two objects
        # print(length)  # for tests only
        x, y, z = lmList[8]
        if length < 38:
            for k, button in enumerate(ButtonList):
                if button.isClick(x, y) and count == 0:
                    if k == 14 and \
                    eqa != "" and eqa != "=" and eqa != "==":  # when click equal and eqa is not empty or have equal
                        eqa = str(eval(eqa))
                        print(eqa)
                        count = 1
                    if k == 15:  # c stands for clear all
                        eqa = ""
                    else:
                        currentValue = ButtonValueList[k % 5][k // 5]
                        eqa = eqa + currentValue
                        # print(currentValue)  # for tests only
                        # print("k =", k)
                        count = 1
                # else:
                    # print("YOUR HANDS IS NOT IN THE RIGHT PLACE!")

    # we use "count" to avoid repeat number
    if count != 0:
        count = count + 1
        if count > 8:
            count = 0

    # Display
    cv.putText(img_cp, eqa, (110, 133),
               cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

    # Final Image
    res = cv.addWeighted(img_cp, alpha, img, 1-alpha, 0)

    cv.imshow("Image", res)
    cv.waitKey(40)
