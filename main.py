'''         Image processing and computer vision
        Alejandra Avendaño, Carolina Pulido & Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import numpy as np
import cv2
from matplotlib import pyplot
if __name__ == '__main__':
    path_file = '/home/pedroruiz54/Escritorio/pr/imagenes/Mario.mp4' #path of the ubication of the video
    path_file1 = '/home/pedroruiz54/Escritorio/pr/imagenes/sp1.jpg'  # path of the ubication of the image
    fdb = cv2.imread(path_file1)

    camera = cv2.VideoCapture(0) #Open camera
    vid = cv2.VideoCapture(path_file) #Open video
    ret = True
    while ret:
        ret, image = camera.read()
        ret1, image_vid = vid.read()
        if ret:
            fdb = cv2.resize(image_vid, (640, 480)) #resize th video
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Convert to HSV space

            image_hsv_1 = image_hsv[0:80, 0:80, :] #create a sample of the real image
            hist = cv2.calcHist([image_hsv_1], [0], None, [180], [0, 180]) #Histrgram of H component
            pyplot.plot(hist, color='red') #Plot the histogram
            pyplot.xlim([0, 180])
            max_val = hist.max() #max val of the histogram
            max_pos = int(hist.argmax()) #position of the maximun in the histogram
            mask1 = cv2.inRange(image_hsv, (0, 0, 0), (max_pos - 10, 255, 255)) #color mask
            mask2 = cv2.inRange(image_hsv, (max_pos + 10, 0, 0), (179, 255, 255)) #color mask
            total = cv2.add(mask1, mask2) #Sum of the masks

            #Morphological operations
            W = 1
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
            mask_eroded = cv2.morphologyEx(total, cv2.MORPH_OPEN, kernel)
            W = 2
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
            mask_dilated = cv2.morphologyEx(mask_eroded, cv2.MORPH_CLOSE, kernel)

            # Background substraction
            fim = cv2.bitwise_and(image, image, mask=mask_dilated)
            fim1 = cv2.bitwise_and(fdb, fdb, mask=cv2.bitwise_not(mask_dilated))
            fim2 = cv2.bitwise_or(fim, fim1, mask=None)

            #Show images
            cv2.imshow("Image", image)
            cv2.imshow("Color mask", total)
            cv2.imshow("Eroded", mask_eroded)
            cv2.imshow("Dilated", mask_dilated)
            cv2.imshow("Final image", fim2)

            #Uncomment if you want save the images
            # cv2.imwrite('/home/pedroruiz54/Escritorio/pr/camera/results/original.png', image)
            # cv2.imwrite('/home/pedroruiz54/Escritorio/pr/camera/results/total.png', total)
            # cv2.imwrite('/home/pedroruiz54/Escritorio/pr/camera/results/eroded.png', mask_eroded)
            # cv2.imwrite('/home/pedroruiz54/Escritorio/pr/camera/results/dilated.png', mask_dilated)
            # cv2.imwrite('/home/pedroruiz54/Escritorio/pr/camera/results/result.png', fim2)
            k = cv2.waitKey(10) & 0xFF
            if k == 0x1B: #Press the 'esc' key to stop the algorithm
                break

    camera.release() #Release the camera
    cv2.destroyAllWindows() #Close all windows