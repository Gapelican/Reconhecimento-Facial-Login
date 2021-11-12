import cv2
import os
import shutil

def tirarFoto(nome_foto):
    cam = 0
    frames = 30
    camera = cv2.VideoCapture(cam)

    def pega_img():
        retval, im = camera.read()
        return im

    for i in range(frames):
        # vai amazenar os 30 fps 
        temp = pega_img()
    print("Tirando a foto...")

    camera = pega_img()
    file = nome_foto + '.png'
    cv2.imwrite(file, camera)

    #deletar camera
    del camera
    print("imagem capturada")


    caminho_original = r'C:\dev\python\aps\{}'.format(file)
    caminho_destino = r'C:\dev\python\aps\img\{}'.format(file)

    shutil.move(caminho_original, caminho_destino)
    

