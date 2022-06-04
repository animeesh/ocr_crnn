import cv2
from FaceDetection import FaceDetector
import pyglet.media  #for sound
import os

cap = cv2.VideoCapture(0) #webcam

if not cap.isOpened():
    print("Camera can't open!!!")
    exit()

#detector = PoseDetector()
detector = FaceDetector()
#sound = pyglet.media.load("alarm.wav", streaming=False)  #sound
people = False
img_count, breakcount = 0, 0

path = '/Users/animeshkumarnayak/PycharmProjects/smartcctv-main/face_croping/img/'
caption = "People Detected!!!"

while True: 
    success, img = cap.read()
    img, bboxs, bbox = detector.findFaces(img)
    #print("bbox :",bbox)
    img_name = f'image_{img_count}.png'

    if bboxs:
        cv2.rectangle(img, (120, 20), (470, 80), (0, 250, 145), cv2.FILLED)
        cv2.putText(img, "BOXES DETECTED!!!", (130, 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        breakcount += 1


        if breakcount >= 20:
            if people == False:
                img_count += 1
                #sound.play()
                if bbox != 0:
                    imgRoi = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
                    cv2.imshow("ROI", imgRoi)
                    cv2.imwrite(os.path.join(path, img_name), imgRoi)
                    files = {'photo': open(path + img_name, 'rb')}
                    # print("files:",files)
                    print("filename: ", img_name)
                    #cv2.imwrite(img_path, cropped_img)
                else:
                    continue
                people = not people
    else:
        breakcount = 0
        if people:
            people = not people

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

