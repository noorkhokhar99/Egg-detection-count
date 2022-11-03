import cv2
import numpy as np
import imutils #importo imutils

sensitivity = 21
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

columnas_huevos = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
espacio = np.array([0,0,0,0,0,0,0,0,0,0,0,0])

cap = cv2.VideoCapture('cintaTransportadora2.mp4') #leo el video de entrada

fgbg =cv2.createBackgroundSubtractorMOG2()  # Sustraccion de fondo - Porque es python 3, sino seria fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)) #Para mejorar la imagen binaria obtenida luego de aplicar la sustraccion de fondo
eggs_counter = 0 #contador de huevos
frame_counter = 0 #contador de capturas

while True:

    ret, imagen = cap.read()

    if not ret:    #si no puede capturar imagen entonces sale del while (es para evitar errores)
        break
    imagen = imutils.resize(imagen, width=640)  # cantidad de pixeles (se puede redimensionar)
    imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #convierto de BGR a HSV
    area_pts = np.array([[55, 50], [imagenHSV.shape[1] - 100, 50], [imagenHSV.shape[1] - 100, 110], [55, 110]])
	#Detectando colores
    maskBlanco = cv2.inRange(imagenHSV, lower_white, upper_white)
    #Las siguientes transformaciones dependen de la iluminacion
    maskBlanco = cv2.morphologyEx(maskBlanco, cv2.MORPH_OPEN, kernel) #transformaciones morfologicas para mejorar la imagen binariav (descarta regiones muy pequeñas de blanco)
    maskBlanco = cv2.morphologyEx(maskBlanco, cv2.MORPH_CLOSE, kernel)
    maskBlanco = cv2.erode(maskBlanco, kernel, iterations=5)
    maskBlanco = cv2.dilate(maskBlanco, None, iterations=3) #5 iteraciones para la dilatacion, es para conectar las areas blancas mas grandes que representan al auto


	#Encontrando contornos
	#OpenCV 4
    cnts = cv2.findContours(maskBlanco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  # para encontrar los contornos presentes en la imagen

    for cnt in cnts:  # se cuentan los contornos encontrados si estan en el area a analizar
        x, y, w, h = cv2.boundingRect(cnt)  # encuentra el ancho y alto del contorno
        if (cv2.contourArea(cnt) > 15) and (50 < (y + h) < 130):  # se compara con sus areas en pixeles (el valor 1500 es a prueba y error) y si esta en el area de analisis
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radio = 2
            if 55 < int(y) < 110:   #dibujo la circunferencia azul solo en el rectangulo de interes
                cv2.circle(imagen, center, radio, (255, 0, 0), 3)   #dibujo el punto en cada huevo
                if 77 < int(y)  < 82:  # si el auto pasa por la linea amarilla, sera contado
                    if (55 < int(x) <= 95) and (espacio[0] == 0): #si pasa por el espacio 1 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[0] = 1
                        columnas_huevos[0] = frame_counter
                    if (95 < int(x) <= 135) and (espacio[1] == 0): #si pasa por el espacio 2 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[1] = 1
                        columnas_huevos[1] = frame_counter
                    if (135 < int(x) <= 175) and (espacio[2] == 0):  # si pasa por el espacio 3 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[2] = 1
                        columnas_huevos[2] = frame_counter
                    if (175 < int(x) <= 215) and (espacio[3] == 0):  # si pasa por el espacio 4 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[3] = 1
                        columnas_huevos[3] = frame_counter
                    if (215 < int(x) <= 255) and (espacio[4] == 0):  # si pasa por el espacio 5 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[4] = 1
                        columnas_huevos[4] = frame_counter
                    if (255 < int(x) <= 295) and (espacio[5] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[5] = 1
                        columnas_huevos[5] = frame_counter
                    if (295 < int(x) <= 335) and (espacio[6] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[6] = 1
                        columnas_huevos[6] = frame_counter
                    if (335 < int(x) <= 375) and (espacio[7] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[7] = 1
                        columnas_huevos[7] = frame_counter
                    if (375 < int(x) <= 415) and (espacio[8] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[8] = 1
                        columnas_huevos[8] = frame_counter
                    if (415 < int(x) <= 455) and (espacio[9] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[9] = 1
                        columnas_huevos[9] = frame_counter
                    if (455 < int(x) <= 495) and (espacio[10] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[10] = 1
                        columnas_huevos[10] = frame_counter
                    if (495 < int(x) <= 540) and (espacio[11] == 0):  # si pasa por el espacio 6 por primera vez
                        eggs_counter = eggs_counter + 1
                        espacio[11] = 1
                        columnas_huevos[11] = frame_counter
                    if radius > 30:
                        radius
                        eggs_counter = eggs_counter + 1
                    cv2.line(imagen, (55, 80), (imagen.shape[1] - 100, 80), (0, 255, 0),3)  # se dibuja una linea verde cuando los autos pasan

    index = 0
    for i in columnas_huevos: #si pasaron 10 frame entonces habilito el contador en dicho espacio
        if((frame_counter - i) > 10):
            espacio[index] = 0
        index = index + 1

    frame_counter = frame_counter + 1
    cv2.drawContours(imagen, [area_pts], -1, (255, 0, 255), 2)  # visualizamos el area determinada anteriormente
    cv2.line(imagen, (55, 50), (55, 110), (0, 255, 255),1)  # linea vertical 1
    #espacio 1: x=95 ; y=80
    cv2.line(imagen, (95, 50), (95, 110), (0, 255, 255), 1)  # linea vertical 2
    #espacio 2: x=135 ; y=80
    cv2.line(imagen, (135, 50), (135, 110), (0, 255, 255),1)  # linea vertical 3
    #espacio 3: x=175 ; y=80
    cv2.line(imagen, (175, 50), (175, 110), (0, 255, 255), 1)  # linea vertical 4
    #espacio 4: x=215 ; y=80
    cv2.line(imagen, (215, 50), (215, 110), (0, 255, 255), 1)  # linea vertical 5
    #espacio 5: x=255 ; y=80
    cv2.line(imagen, (255, 50), (255, 110), (0, 255, 255), 1)  # linea vertical 6
    #espacio 6: x=295 ; y=80
    cv2.line(imagen, (295, 50), (295, 110), (0, 255, 255), 1)  # linea vertical 7
    #espacio 7: x=335 ; y=80
    cv2.line(imagen, (335, 50), (335, 110), (0, 255, 255), 1)  # linea vertical 8
    #espacio 8: x=375 ; y=80
    cv2.line(imagen, (375, 50), (375, 110), (0, 255, 255), 1)  # linea vertical 9
    #espacio 9: x=415 ; y=80
    cv2.line(imagen, (415, 50), (415, 110), (0, 255, 255), 1)  # linea vertical 10
    #espacio 10: x=455 ; y=80
    cv2.line(imagen, (455, 50), (455, 110), (0, 255, 255), 1)  # linea vertical 11
    #espacio 11: x=495 ; y=80
    cv2.line(imagen, (495, 50), (495, 110), (0, 255, 255), 1)  # linea vertical 12
    #espacio 12: x=535 ; y=80
    cv2.line(imagen, (540, 50), (540, 110), (0, 255, 255), 1)  # linea vertical 13
    cv2.line(imagen, (55, 80), (imagen.shape[1] - 100, 80), (0, 255, 255),1)  # linea horizontal amarilla ubicada en 260 (eje y)
    cv2.rectangle(imagen, (imagen.shape[1] - 70, 215), (imagen.shape[1] - 5, 270), (0, 255, 0),2)  # rectangulo donde va el contador, en color verde
    cv2.putText(imagen, str(eggs_counter), (imagen.shape[1] - 55, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    #cv2.putText(imagen, str(frame_counter), (imagen.shape[1] - 200, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.imshow('maskBlanco', maskBlanco)
    cv2.imshow('Imagen', imagen)

    k = cv2.waitKey(70) & 0xFF #el 70 es para que el video se vea mas lento, si disminuye va mas rapido
    if k == 27:  # si apreto la tecla ESC sale.
        break

cap.release()
cv2.destroyAllWindows()
