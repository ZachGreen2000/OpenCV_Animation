import cv2
import numpy as np

#frame1 = np.zeros((1024,1024,3), np.uint8)
#first frame stickman
class initial_stickmen:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, -1)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, -1)
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
#second frame stickman
class second_stickman:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, -1)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, -1)
        #arms
        arm_left = (self.x - int(30 * self.scale), self.y + int(30 * self.scale))
        arm_right = (self.x + int(30 * self.scale), self.y + int(30 * self.scale))
        cv2.line(img, (self.x - int(10 * self.scale), self.y + int(30 * self.scale)), arm_left, self.color, self.thickness)
        cv2.line(img, (self.x + int(10 * self.scale), self.y + int(30 * self.scale)), arm_right, self.color, self.thickness)
        #legs
        leg_left = (self.x - int(10 * self.scale), self.y + int(90 * self.scale))
        leg_right = (self.x + int(10 * self.scale), self.y + int(90 * self.scale))
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_left, self.color, self.thickness)
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_right, self.color, self.thickness)
#third stickmen
class third_stickman:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, -1)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, -1)
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
#forth stickmen
class fourth_stickman:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, -1)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, -1)
        #arms
        arm_left = (self.x - int(30 * self.scale), self.y + int(30 * self.scale))
        arm_right = (self.x + int(30 * self.scale), self.y + int(30 * self.scale))
        cv2.line(img, (self.x - int(10 * self.scale), self.y + int(30 * self.scale)), arm_left, self.color, self.thickness)
        cv2.line(img, (self.x + int(10 * self.scale), self.y + int(30 * self.scale)), arm_right, self.color, self.thickness)
        #legs
        leg_left = (self.x - int(10 * self.scale), self.y + int(90 * self.scale))
        leg_right = (self.x + int(10 * self.scale), self.y + int(90 * self.scale))
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_left, self.color, self.thickness)
        cv2.line(img, (self.x, self.y + (int(60 * self.scale))), leg_right, self.color, self.thickness)
#fith stickmen
class fith_stickman:
    def __init__(self, x, y, scale=0, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.thickness = thickness

    def draw(self, img):
        #head
        cv2.circle(img, (self.x, self.y), (int(20 * self.scale)), self.color, -1)
        #body
        cv2.rectangle(img, (self.x - int(10 * self.scale), self.y + int(20 * self.scale)), (self.x + int(10 * self.scale), self.y + int(60 * self.scale)), self.color, -1)
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
#drawing for background
class background:
    def __init__(self, img):
        #block colour
        cv2.rectangle(img, (0,0), (1024,1024), (100, 0, 0), -1)
        #sun
        cv2.circle(img, (900, 10), 100, (200, 200, 200), -1)
        #floor
        cv2.rectangle(img, (0,500), (1024,1024), (100, 100, 100), -1)
        cv2.rectangle(img, (0,500), (1024,900), (60, 60, 60), -1)
        cv2.putText(img, "Zach Green", (820, 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
#for drawing buildings
class buildings():
    def __init__(self, x, y, scale, color,):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color

    def buildings(self, img):
        #buildings
        cv2.rectangle(img, (self.x, self.y), (self.x + int(35 * self.scale), self.y + int(65 * self.scale)), self.color, -1)
        #windows
        cv2.rectangle(img, (self.x + int(5 * self.scale), self.y + int(5 * self.scale)), (self.x + int(12 * self.scale), self.y + int(12 * self.scale)), (255, 222 , 0), -1)
        cv2.rectangle(img, (self.x + int(23 * self.scale), self.y + int(5 * self.scale)), (self.x + int(30 * self.scale), self.y + int(12 * self.scale)), (255, 222 , 0), -1)
        #layer2
        cv2.rectangle(img, (self.x + int(5 * self.scale), self.y + int(15 * self.scale)), (self.x + int(12 * self.scale), self.y + int(22 * self.scale)), (255, 222 , 0), -1)
        cv2.rectangle(img, (self.x + int(23 * self.scale), self.y + int(15 * self.scale)), (self.x + int(30 * self.scale), self.y + int(22 * self.scale)), (255, 222 , 0), -1)
        #layer3
        cv2.rectangle(img, (self.x + int(5 * self.scale), self.y + int(25 * self.scale)), (self.x + int(12 * self.scale), self.y + int(32 * self.scale)), (255, 222 , 0), -1)
        cv2.rectangle(img, (self.x + int(23 * self.scale), self.y + int(25 * self.scale)), (self.x + int(30 * self.scale), self.y + int(32 * self.scale)), (255, 222 , 0), -1)
        #layer4
        cv2.rectangle(img, (self.x + int(5 * self.scale), self.y + int(35 * self.scale)), (self.x + int(12 * self.scale), self.y + int(42 * self.scale)), (255, 222 , 0), -1)
        cv2.rectangle(img, (self.x + int(23 * self.scale), self.y + int(35 * self.scale)), (self.x + int(30 * self.scale), self.y + int(42 * self.scale)), (255, 222 , 0), -1)
        #layer5
        cv2.rectangle(img, (self.x + int(5 * self.scale), self.y + int(45 * self.scale)), (self.x + int(12 * self.scale), self.y + int(52 * self.scale)), (255, 222 , 0), -1)
        cv2.rectangle(img, (self.x + int(23 * self.scale), self.y + int(45 * self.scale)), (self.x + int(30 * self.scale), self.y + int(52 * self.scale)), (255, 222 , 0), -1)
        #door
        cv2.rectangle(img, (self.x + int(13 * self.scale), self.y + int(50 * self.scale)), (self.x + int(22 * self.scale), self.y + int(65 * self.scale)), (35, 35, 130), -1)
#for drawing stars
class star():
    def __init__(self, pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10, color, scale):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
        self.pt4 = pt4
        self.pt5 = pt5
        self.pt6 = pt6
        self.pt7 = pt7
        self.pt8 = pt8
        self.pt9 = pt9
        self.pt10 = pt10
        self.color = color
        self.scale = scale

    def draw_star(self, img):
        points = np.array([[self.pt1], [self.pt2], [self.pt3], [self.pt4], [self.pt5], [self.pt6], [self.pt7], [self.pt8], [self.pt9], [self.pt10]], np.int32)
        cv2.fillPoly(img, [points * self.scale], self.color)

#store stars
stars = [
    star((3,13), (5,10), (2,8), (6,8), (7,5), (8,8), (12,8), (9,10), (11,13), (7,11), color=(240, 240, 240), scale=8),
    star((53,13), (55,10), (52,8), (56,8), (57,5), (58,8), (62,8), (59,10), (61,13), (57,11), color=(240, 240, 240), scale=5),
    star((33,13), (35,10), (32,8), (36,8), (37,5), (38,8), (42,8), (39,10), (41,13), (37,11), color=(240, 240, 240), scale=3),
    star((83,13), (85,10), (82,8), (86,8), (87,5), (88,8), (92,8), (89,10), (91,13), (87,11), color=(240, 240, 240), scale=8),
    star((43,13), (45,10), (42,8), (46,8), (47,5), (48,8), (52,8), (49,10), (51,13), (47,11), color=(240, 240, 240), scale=10)
]
#store buildings
building = [
    buildings(350, 160, scale=10, color = (50, 50 , 50)),
    buildings(700, 90, scale=10, color = (10, 10 , 10)),
    buildings(0, 130, scale=10, color = (80, 80 , 80)),
    buildings(50, 200, scale=10, color = (10, 10 , 10)),
    buildings(450, 200, scale=10, color = (30, 30 , 30)),
    buildings(750, 220, scale=10, color = (80, 80 , 80))
]
#array for stickmen storage
stickmen = [
    initial_stickmen(200, 800, scale=2, color=(0, 255, 0), thickness=4),
    initial_stickmen(800, 800, scale=2, color=(0, 0, 255), thickness=4)
]
#array for frame 2 of stickmen
stickmen2 = [
    second_stickman(250, 800, scale=2, color=(0,255,0), thickness=4),
    second_stickman(750, 800, scale=2, color=(0,0,255), thickness=4),
]
#array for frame 3 of stickmen
stickmen3 = [
    third_stickman(300, 800, scale=2, color=(0,255,0), thickness=4),
    third_stickman(700, 800, scale=2, color=(0,0,255), thickness=4),
]
#array for frame 4 of stickmen
stickmen4 = [
    fourth_stickman(350, 800, scale=2, color=(0,255,0), thickness=4),
    fourth_stickman(650, 800, scale=2, color=(0,0,255), thickness=4),
]
#array for frame 5 of stickmen
stickmen5 = [
    fith_stickman(400, 800, scale=2, color=(0,255,0), thickness=4),
    fith_stickman(600, 800, scale=2, color=(0,0,255), thickness=4),
]
frameCheck = 0 # flag for stickman frame
for _ in range(50):
    frame1 = np.zeros((1024,1024,3), np.uint8)
    #drawing background
    background(frame1)
    #draw stars
    for st in stars:
        st.draw_star(frame1)
        #drawing buildings
    for build in building:
        build.buildings(frame1)
    #checking for stickman frame
    if (frameCheck < 10):
        #draw stickmen
        print ("first stick")
        for stickman in stickmen:
            stickman.draw(frame1)
    elif (frameCheck < 20):
        print ("stick 2")
        for stickman2 in stickmen2:
            stickman2.draw(frame1)
    elif (frameCheck < 30):
        print ("stick 3")
        for stickman3 in stickmen3:
            stickman3.draw(frame1)
    elif (frameCheck < 40):
        print ("stick 4")
        for stickman4 in stickmen4:
            stickman4.draw(frame1)
    elif (frameCheck < 50):
        print ("stick 5")
        for stickman5 in stickmen5:
            stickman5.draw(frame1)
    #show screen
    cv2.imshow('Stickmen Animation', frame1)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
    frameCheck = (frameCheck + 1) % 200
cv2.destroyAllWindows()