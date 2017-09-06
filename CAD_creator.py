import Image 
import numpy
import random

#this script takes a .png photo and outputs an openSCAD script that will create a voxelized CAD representation of the photo

#import image being used into library
im = Image.open("file path for image")

#obtains pixel values 
pixelMap = list(im.getdata())

#converts pixels into list of binary values of 0 or 1, which reveals whether material will be placed in that location or not
normalizedList = []
for tup in pixelMap:
    lists = list(tup)
    newValue = int(((lists[0]+lists[1] + lists[2] + lists[3])/4)/255) 
    if newValue <= .5:
        normalizedList.append(0)
    else:
        normalizedList.append(1)



#creates openSCAD script
#size of boxes that are created can be altered to change the size of the outputted CAD model
#this CAD representation is created in a 50mm by 50mm space
loop = 0
for y in range(0,50):
    for x in range(0,50):
        if normalizedList[loop] == 0:
            print("translate([" + str(x*.25) + "," + str((y*.25)) + ",0])")
            print("cube([.28,.28,10],center = false);")
            loop = loop + 1
        else: 
            loop = loop + 1