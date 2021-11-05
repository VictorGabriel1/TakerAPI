import cv2
import numpy as np
from datetime import datetime
#https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html

def taker(var, debug):
    total=0
    i=0

    #Leitura de uma determinada imagem
    img = cv2.imread(var)
    #Converte a imagem para tons de cinza
    imgbin = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    cv2.Canny(imgbin, 50,200)
    imgbin = np.array(255 * (imgbin / 255) ** 1 , dtype='uint8')
    if debug == True:
        cv2.imwrite('images/inputs/Img_Greyscale.png',imgbin)
    #Converte a imagem de tons de cinza para preto e branco binário
    (thresh, imgbw) = cv2.threshold(imgbin, 127, 255, cv2.THRESH_BINARY)
    # Tratamentos de imagem ##############
    if debug == True:
        cv2.imwrite('images/inputs/Img_BW.png',imgbw)
    kernel = np.ones((8, 15), np.uint8)
    kernel2 = np.ones((3,3), np.uint8)

    imgbw = cv2.morphologyEx(imgbw, cv2.MORPH_OPEN, kernel)
    imgbw = cv2.morphologyEx(imgbw, cv2.MORPH_CLOSE, kernel2)
    imgbw = cv2.dilate(imgbw,kernel2,iterations = 1)
    imgbw = cv2.erode(imgbw,kernel,iterations = 1)
    if debug == True:
        cv2.imwrite('images/inputs/Img_Config.png',imgbw)

    #Identifica os contornos de todos os objetos
    contours, hierarchy  = cv2.findContours(imgbw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    minimum_area = 800
    max_area = 10000
    for i in contours:
        area = cv2.contourArea(i)
        #Conta todos os contornos
        if ((area > minimum_area) and (area < max_area)):
            total=total+1;
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(img,(x,y),(x+w,y+h),(200,255,200),2)

    # Finally show the image
    dt = datetime.now()
    dts = dt.strftime("%d-%m-%Y_%H-%M-%S")
    cv2.imwrite(f'images/outputs/{dts}.png', img)


    #Imprime os valores
    return {f'image': dts, 'total': total}
    # print('Total de objetos : ',total)
    # print('--------------------------------------------------------------------------')

    #waitress-serve --port=5000 --call api:create_app >> log.txt &
