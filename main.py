import cv2
import numpy as np
import imutils #import imutils

sensitivity = 21
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

egg_columns = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
space = np.array([0,0,0,0,0,0,0,0,0,0,0,0])

cap = cv2.VideoCapture('cintaTransportadora2.mp4') 

fgbg =cv2.createBackgroundSubtractorMOG2()  
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)) 
eggs_counter = 0 
frame_counter = 0 

while True:

    ret, image = cap.read()

    if not ret:    
        break
    image = imutils.resize(image, width=640)  
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
    area_pts = np.array([[55, 50], [imageHSV.shape[1] - 100, 50], [imageHSV.shape[1] - 100, 110], [55, 110]])
    #Detect colores
    maskWhite = cv2.inRange(imageHSV, lower_white, upper_white)
    maskWhite = cv2.morphologyEx(maskWhite, cv2.MORPH_OPEN, kernel) #
    maskWhite = cv2.morphologyEx(maskWhite, cv2.MORPH_CLOSE, kernel)
    maskWhite = cv2.erode(maskWhite, kernel, iterations=5)
    maskWhite = cv2.dilate(maskWhite, None, iterations=3) #


    #OpenCV 4
    cnts = cv2.findContours(maskWhite, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  #

    for cnt in cnts:  # 
        x, y, w, h = cv2.boundingRect(cnt)  
        if (cv2.contourArea(cnt) > 15) and (50 < (y + h) < 130): 
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radio = 2
            if 55 < int(y) < 110:   
                cv2.circle(image, center, radio, (255, 0, 0), 3)  
                if 77 < int(y)  < 82: 
                    if (55 < int(x) <= 95) and (space[0] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[0] = 1
                        egg_columns[0] = frame_counter
                    if (95 < int(x) <= 135) and (space[1] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[1] = 1
                        egg_columns[1] = frame_counter
                    if (135 < int(x) <= 175) and (space[2] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[2] = 1
                        egg_columns[2] = frame_counter
                    if (175 < int(x) <= 215) and (space[3] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[3] = 1
                        egg_columns[3] = frame_counter
                    if (215 < int(x) <= 255) and (space[4] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[4] = 1
                        egg_columns[4] = frame_counter
                    if (255 < int(x) <= 295) and (space[5] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[5] = 1
                        egg_columns[5] = frame_counter
                    if (295 < int(x) <= 335) and (space[6] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[6] = 1
                        egg_columns[6] = frame_counter
                    if (335 < int(x) <= 375) and (space[7] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[7] = 1
                        egg_columns[7] = frame_counter
                    if (375 < int(x) <= 415) and (space[8] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[8] = 1
                        egg_columns[8] = frame_counter
                    if (415 < int(x) <= 455) and (space[9] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[9] = 1
                        egg_columns[9] = frame_counter
                    if (455 < int(x) <= 495) and (space[10] == 0):  
                        eggs_counter = eggs_counter + 1
                        space[10] = 1
                        egg_columns[10] = frame_counter
                    if (495 < int(x) <= 540) and (space[11] == 0): 
                        eggs_counter = eggs_counter + 1
                        space[11] = 1
                        egg_columns[11] = frame_counter
                    if radius > 30:
                        radius
                        eggs_counter = eggs_counter + 1
                    cv2.line(image, (55, 80), (image.shape[1] - 100, 80), (0, 255, 0),3)  

    index = 0
    for i in egg_columns: #
        if((frame_counter - i) > 10):
            space[index] = 0
        index = index + 1

    frame_counter = frame_counter + 1
    cv2.drawContours(image, [area_pts], -1, (255, 0, 255), 2)  # 
    cv2.line(image, (55, 50), (55, 110), (0, 255, 255),1)  # line vertical 1
    #space 1: x=95 ; y=80
    cv2.line(image, (95, 50), (95, 110), (0, 255, 255), 1)  # line vertical 2
    #space 2: x=135 ; y=80
    cv2.line(image, (135, 50), (135, 110), (0, 255, 255),1)  # line vertical 3
    #space 3: x=175 ; y=80
    cv2.line(image, (175, 50), (175, 110), (0, 255, 255), 1)  # line vertical 4
    #space 4: x=215 ; y=80
    cv2.line(image, (215, 50), (215, 110), (0, 255, 255), 1)  # line vertical 5
    #space 5: x=255 ; y=80
    cv2.line(image, (255, 50), (255, 110), (0, 255, 255), 1)  # line vertical 6
    #space 6: x=295 ; y=80
    cv2.line(image, (295, 50), (295, 110), (0, 255, 255), 1)  # line vertical 7
    #space 7: x=335 ; y=80
    cv2.line(image, (335, 50), (335, 110), (0, 255, 255), 1)  # line vertical 8
    #space 8: x=375 ; y=80
    cv2.line(image, (375, 50), (375, 110), (0, 255, 255), 1)  # line vertical 9
    #space 9: x=415 ; y=80
    cv2.line(image, (415, 50), (415, 110), (0, 255, 255), 1)  # line vertical 10
    #space 10: x=455 ; y=80
    cv2.line(image, (455, 50), (455, 110), (0, 255, 255), 1)  # line vertical 11
    #space 11: x=495 ; y=80
    cv2.line(image, (495, 50), (495, 110), (0, 255, 255), 1)  # line vertical 12
    #space 12: x=535 ; y=80
    cv2.line(image, (540, 50), (540, 110), (0, 255, 255), 1)  # line vertical 13
    cv2.line(image, (55, 80), (image.shape[1] - 100, 80), (0, 255, 255),1)  # 
    cv2.rectangle(image, (image.shape[1] - 70, 215), (image.shape[1] - 5, 270), (0, 255, 0),2)  # rectangulo donde va el contador, en color verde
    cv2.putText(image, str(eggs_counter), (image.shape[1] - 55, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    #cv2.putText(image, str(frame_counter), (image.shape[1] - 200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.imshow('maskWhite', maskWhite)
    cv2.imshow('Image', image)

    k = cv2.waitKey(70) & 0xFF 
    if k == 27:  # 
        break

cap.release()
cv2.destroyAllWindows()