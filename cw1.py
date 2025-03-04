import cv2
import numpy as np

frame1 = np.zeros((1024,1024,3), np.uint8)

class initial_stickmen:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, self.thickness)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, self.thickness)
        #arms
        arm_left = (self.x - int(30 * self.scale), self.y + int(30 * self.scale))
        arm_right = (self.x + int(30 * self.scale), self.y + int(30 * self.scale))
        cv2.line(img, (self.x - int(10 * self.scale), self.y + int(30 * self.scale)), arm_left, self.color, self.thickness)
        cv2.line(img, (self.x + int(10 * self.scale), self.y + int(30 * self.scale)), arm_right, self.color, self.thickness)
        #legs
        leg_left = (self.x - int(30 * self.scale), self.y + int(90 * self.scale))
        leg_right = (self.x + int(30 * self.scale), self.y + int(90 * self.scale))
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_left, self.color, self.thickness)
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_right, self.color, self.thickness)

class background:
    def __init__(self, img):
        #block colour
        cv2.rectangle(img, (0,0), (1024,1024), (255, 0, 0), 1024)
#drawing background
background(frame1)
#array for stickmen storage
stickmen = [
    initial_stickmen(200, 200, scale=5, color=(0, 255, 0), thickness=1)
]

#draw stickmen
for stickman in stickmen:
    stickman.draw(frame1)
#show screen
cv2.imshow('Stickmen Animation', frame1)
cv2.waitKey(0)
cv2.destroyAllWindows()