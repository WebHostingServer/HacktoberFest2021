import cv2
import pytesseract
import os
import numpy as np
#from matplotlib import pyplot as plt
import re
  
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
link = r'C:\Users\suyash\Desktop\FROST HACK\Frost Hack Video\Shape6.jpeg'
img1 = cv2.imread(link)
cv2.imshow("imput", img1)
img = cv2.resize(img1,(500,500),interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)  
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

liobj = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
      
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
      
    # Cropping the text block for giving input to OCR
    cropped = img[y:y + h, x:x + w]
      
    # Open the file in append mode
    file = open("recognized.txt", "a")
   
    
    # Apply OCR on the cropped image
    text1 = pytesseract.image_to_string(cropped)
    file.write(text1)
    #file.write("\n")  
    #print(text)
    #print(text1)
file.close()     
blank = np.zeros(img.shape, dtype='uint8')
# converting image into grayscale image



hgt = img1.shape[0]
wdt = img1.shape[1]
if hgt>500 & wdt>500:
    img = cv2.resize(img1, (500,500), interpolation = cv2.INTER_AREA)
elif hgt<500 & wdt<500:
    img = cv2.resize(img1, (500,500), interpolation=cv2.INTER) 
elif hgt>500 & wdt<500:
     img = cv2.resize(img1, (500,500), interpolation = cv2.INTER_AREA)
     img = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
     pass 
elif hgt<500 & wdt>500:
     img = cv2.resize(img1, (500,500), interpolation = cv2.INTER_AREA)
     img = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
     pass      
blank = np.zeros(img.shape, dtype='uint8')          
#cv2.imshow("black", blank)

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
#threshold = cv2.erode(threshold1, (7,7), iterations=4)
#cv2.imshow("hello", threshold)

# using a findContours() function
contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(blank, contours, -1, (0,0,255), 1)
#cv2.imshow("draw", blank)
i = 0

# list for storing names of shapes
for contour in contours:
    
    Area = cv2.contourArea(contour)
    if Area > 2000:
        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1                #Ye part samj nahi aya
            continue

        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)
        
        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            
        i+=1
        if i%2 == 1:
            liobj.append([x,y])
        else:
            pass

        img = cv2.line(img, (x,y), (x, y+int(h/1.5)) , (255,0,0), 3)
        img = cv2.line(img, (x,y+int(h/1.5)), (x-int(x/10),y+int(h/1.8)),(255,0,0), 3)
        img = cv2.line(img, (x,y+int(h/1.5)), (x+int(x/10),y+int(h/1.8)) ,(255,0,0),3)
        img = cv2.putText(img, "mg", (x-20,y+int(h/1.5)+20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 1)
        img = cv2.line(img, (x,y), (x, y-int(h/1.5)) , (0,0,255), 3)
        img = cv2.line(img, (x,y-int(h/1.5)), (x+int(x/10),y-int(h/1.8)),(0,0,255), 3)
        img = cv2.line(img, (x,y-int(h/1.5)), (x-int(x/10),y-int(h/1.8)) ,(0,0,255),3)
        img = cv2.putText(img, "N", (x-20,y-int(h/1.5)-20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 1)
        #cv2.imshow('arrow', img)    

        # putting shape name at center of each shape and drawContours() function
        if len(approx) == 3:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 4:
            cv2.drawContours(img, [contour], -1, (0,255, 255), 1)
            cv2.putText(img, 'Quadrilateral', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 255), 2)
            
        elif len(approx) == 5:
            cv2.drawContours(img, [contour], 0, (0, 255,0), 1)
            cv2.putText(img, 'Pentagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0, 255),2)
        elif len(approx) == 6:
            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
            cv2.putText(img, 'Hexagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        elif len(approx) == 8:
            cv2.drawContours(img, [contour],0, (255,0,0), 1)
            cv2.putText(img, 'Octagon', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0,0 ), 2)    
        else:
            cv2.drawContours(img, [contour],0 , ( 255, 255,0), 1)
            cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, ( 255, 255,0), 2)
# displaying the image after drawing contours
cv2.imshow('shapes', img)
print(liobj)

f = open("recognized.txt", "r")
read = f.read()
read = read.replace(" ", "")
read = read.replace("\n", "")
read = read.replace("", "")
print(read)
f.close()
os.remove("recognized.txt")
digit = re.compile('\D')
n = digit.split(read)
num = []
for i in n:
    if i != '':
        num.append(i)
        
digit = re.compile('\d')
a = digit.split(read)
alpha = []
for i in a:
    if i != '':
        alpha.append(i)
print(num)        
print(alpha)
kg = []
keyset = []
for i in alpha:
    if i.upper() == 'KG':
        kg.append(i)
if len(liobj) == 1:
    keyset.append(str(liobj[0])+";" + str(num[0])) 
elif len(liobj) == 2:
    if len(kg) == 1:
        if liobj[0][1]>liobj[1][1]:
            keyset.append(str(liobj[1])+";"+str(num[0]))
        else:
            keyset.append(str(liobj[0])+";"+str(num[0]))
    elif len(kg) == 2:
        if liobj[0][1]>liobj[1][1]:
            keyset.append(str(liobj[1])+";"+str(num[0]))
            keyset.append(str(liobj[0])+";" + str(num[0]))
        else:
            keyset.append(str(liobj[0])+";"+str(num[1]))
            keyset.append(str(liobj[1])+";" + str(num[1]))  
else:
    pass
print(keyset[0])
if len(keyset) == 1:
    s = keyset[0]
    key = s.split(";")
    img = cv2.putText(img, "   ="+str(int(key[1])*10)+" N", (x-20,y+int(h/1.5)+20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 1)
    img = cv2.putText(img, "  ="+str(int(key[1])*10)+" N", (x-20,y-int(h/1.5)-20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 1)
    img = cv2.putText(img, "N=mg="+str(int(key[1])*10)+" N", (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (30, 120, 255), 1)


elif len(keyset) == 2:
    nor = 0
    l=-1

    for i in range(2):
        l +=1
        kyu = keyset[i]
        #print(kyu)
        key = kyu.split(";")
        x =  key[0]
        nor += int(key[1])
        st = re.compile('\D')
        dig = st.split(x)
        dhinchak = []
        for i in dig:
            if i != '':
                dhinchak.append(i)
        x = dhinchak[0]
        y =dhinchak[1]
        
        if l==0:
            img = cv2.putText(img,"BODY1: n=mg="+str(int(nor)*10)+" N", (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (30, 120, 255), 1)
        else:
            img = cv2.putText(img,"BODY2: Mg+mg=N="+str(int(nor)*10)+" N", (10,475), cv2.FONT_HERSHEY_COMPLEX, 0.5, (30, 120, 255), 1)
        img = cv2.putText(img, "   ="+str(int(key[1])*10)+" N", (int(x)-20,int(y)+int(h/1.5)+20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 1)
        img = cv2.putText(img, "  ="+str(int(nor)*10)+" N", (int(x)-20,int(y)-int(h/1.5)-20) ,cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 1)

cv2.imshow("end", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
