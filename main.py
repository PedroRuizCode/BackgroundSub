'''         Image processing and computer vision
        Alejandra Avendaño, Carolina Pulido & Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
# import libraries
import numpy as np
import cv2
import tkinter as tk
from boton1 import *
from capture import *

if __name__ == '__main__':
    boton = boton1() #call GUI 1
    path_file = boton.path() #Save path
    voi = boton.bandera() #Select video or image

    shot = capture() #call GUI 2
    cap = shot.enviar() #flag to take a photo

    #Save monitor info
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    A = np.zeros(6, dtype=np.uint8) #Image data vector
    camera = cv2.VideoCapture(0) #Open camera
    vid = cv2.VideoCapture(path_file) #Open video
    while cap:
        ret, image = camera.read() #Load image from camera
        if ret:
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Convert to HSV space
            A[0] = int(np.min(image_hsv[..., 0]) - 12) #Minimum Hue value
            A[1] = int(np.max(image_hsv[..., 0]) + 12) #Maximum Hue value
            A[2] = int(np.min(image_hsv[..., 1])) -10 #Minimum Saturation value
            A[3] = int(np.max(image_hsv[..., 1])) #Maximum Saturation value
            A[4] = int(np.min(image_hsv[..., 2])) - 10 #Minimum Value - value
            A[5] = int(np.max(image_hsv[..., 2])) #Maximum Value - value
            break

    while 1:
        ret, image = camera.read() #Save image
        ret1, image_vid = vid.read()
        if ret:
            if voi == 'A': #background is an image
                fdb1 = cv2.imread(path_file)
                fdb2 = cv2.resize(fdb1, (1280, 720)) #resize
                fdb = cv2.cvtColor(fdb2, cv2.COLOR_BGR2HSV) #Convert to HSV space
            else: #background is a video
                fdb2 = cv2.resize(image_vid, (1280, 720)) #resize
                fdb = cv2.cvtColor(fdb2, cv2.COLOR_BGR2HSV) #Convert to HSV space
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Convert to HSV space
            image_hsv_copy = np.copy(image_hsv) #create a copy

            # Delete green pixels
            image_hsv_copy[np.bitwise_and(np.bitwise_and((A[0] < image_hsv_copy[..., 0]),(image_hsv_copy[..., 0] < A[1])),
                           np.bitwise_and((A[2] < image_hsv_copy[..., 1]), (image_hsv_copy[..., 1] <= A[3])),
                           np.bitwise_and((A[4] < image_hsv_copy[..., 2]), (image_hsv_copy[..., 2] <= A[5])))] = 0

            #Save the mask
            total = np.bitwise_or((image_hsv_copy[...,0] < 1),(image_hsv_copy[...,1] < 1),(image_hsv_copy[...,2] < 1))

            #Morphological operations
            W = 1
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
            mask_eroded = cv2.morphologyEx(np.uint8(total) * 255, cv2.MORPH_OPEN, kernel)
            W = 1
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
            mask_dilated = cv2.morphologyEx(mask_eroded, cv2.MORPH_CLOSE, kernel)
            mask_dilated = mask_dilated.astype(bool)

            # Background substraction
            image_hsv[mask_dilated] = 0 #Delete the background from the camera image
            fdb[np.bitwise_not(mask_dilated)] = 0 #Delete the foreground from the background image
            fim2 = cv2.bitwise_or(image_hsv, fdb, mask=None) #Mix foreground and background edited
            fim3 = cv2.resize(fim2, (screen_width, screen_height - 105)) #resize the video
            fim4 = cv2.cvtColor(fim3, cv2.COLOR_HSV2BGR) #convert to BGR space

            #Uncomment if you want to save the images
            # fim6 = cv2.cvtColor(image_hsv_copy, cv2.COLOR_HSV2BGR)
            # fim7 = cv2.resize(fim6, (screen_width, screen_height - 105))  # resize th video
            # fim8 = cv2.resize(image, (screen_width, screen_height - 105))  # resize th video
            # cv2.imwrite('result.png', fim4)
            # cv2.imwrite('result1.png', fim7)
            # cv2.imwrite('result2.png', fim8)

            cv2.imshow('Final image', fim4) #Show result
            k = cv2.waitKey(1) & 0xFF
            if k == 0x1B: #Press the 'esc' key to stop the algorithm
                break

    camera.release() #Release the camera
    cv2.destroyAllWindows() #Close all windows