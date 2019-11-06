import argparse
import cv2
import imutils
import numpy as np
from PIL import Image
import pytesseract
import os

#get args file path
ap = argparse.ArgumentParser()
# ap.add_argument("-i","--image",required = True,help = "Path to image")
ap.add_argument("-p","--preprocess",type=str,default="thresh",help="type of preprocessing to be done")
args = vars(ap.parse_args())


#processing the image and show its data
image = cv2.imread("ex3.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray,3)


filename = "{}.png".format(os.getpid())
cv2.imwrite(filename,gray)

dissect = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

cv2.imshow("image",image)
cv2.imshow("output",gray)
print(dissect)
cv2.waitKey(0)