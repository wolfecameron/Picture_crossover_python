import Image 
import numpy
import random

#this script takes two .png files, merges the pixel values together to mix the pictures, and adds a certain amount of noise the resulting picture
#planning to integrate it with DEAP GA in order to evolve structures based on the initial mixture of the two pictures


#import image being used into library
im = Image.open("image1 file path")
im2 = Image.open("image 2 file path")

#resizes pictures to 50 X 50 pixels
width = 50
height = 50
im3 = im.resize([height, width])
im4 = im2.resize([height,width])
im3.save("resized image1 file path (where to save it)")
im4.save("resized image2 file path (where to save it)")


#creates all initial values for weights 
#used to add noise to each of the pixel values (single weight for each pixel)
weights1 = []
weights2 = []
for i in range(0,3000):
    weights1.append(random.uniform(-1,1))
    weights2.append(random.uniform(-1,1))


#obtains pixel values for two pictures 
pixelMap1 = list(im3.getdata())
pixelMap2 = list(im4.getdata()) 


#adds weights to values of pixels for first image
new_values1 = []
loop1= 0
for tup in pixelMap1:
    sublist1 = list(tup)
    for i in range(0,4):
        r = random.uniform(0,1)
        if r>.5:
            sublist1[i] = int(sublist1[i] + sublist1[i]*weights1[loop1])
        else:
            sublist1[i] = sublist1[i]
    new_values1.append(sublist1)
    loop1 = loop1 + 1


#adds weights to values of pixels for second image
new_values2 = []
loop2 = 0
for tup in pixelMap2:
    sublist2 = list(tup)
    for i in range(0,4):
        r = random.uniform(0,1)
        if r > .5:
            sublist2[i] = int(sublist2[i] + sublist2[i]*weights2[loop2])
        else: 
            sublist2[i] = sublist2[i]
    new_values2.append(sublist2)
    loop2 = loop2 + 1


#adds pixel values of two images together
new_pixels = []
for i in range(0,len(new_values2)):
    x = new_values1[i]
    y = new_values2[i]
    sublist = []
    for z in range(0,4):
        new = (x[z] + y[z])/2
        sublist.append(new)
    new_pixels.append(sublist) 

        
    
    
#eliminates all pixel values greater than 255 or less than 0 (converting to list in process)
#pixel values beyond this range throw errors if converted back to .png file
weighted_values = []
sublist = []
for lists in new_pixels:
    sublist = []
    for i in range(0,4):
        z = lists[i]
        if z < 165:
            z = 0
        else:
            z = 255
        sublist.append(z)
    sublist[1] = sublist[0]
    sublist[2] = sublist[0]
    sublist[3] = sublist[0]
    weighted_values.append(sublist)

	
#eliminates random pixels by checking if the pixels around them have similar values
for x in range(0,2499):
    if x < 3 or x > len(weighted_values)-3:
        weighted_values[x] = weighted_values[x]
    else:
        if weighted_values[x-1][0] == 255 and weighted_values[x+1][0] == 255 and weighted_values[x+2][0] == 255 and weighted_values[x-2][0] == 255:
            weighted_values[x][0] = 255
            weighted_values[x][1] = 255
            weighted_values[x][2] = 255
            weighted_values[x][3] = 255
        else:
            weighted_values[x] = weighted_values[x]
            
  
  
for x in range(0,2499):
    if x ==0 or x == 2499:
        weighted_values[x] = weighted_values[x]
    else:
        if weighted_values[x-1][0] == 0 and weighted_values[x+1][0] == 0:
            weighted_values[x][0] = 0
            weighted_values[x][1] = 0
            weighted_values[x][2] = 0
            weighted_values[x][3] = 0
        else:
            weighted_values[x] = weighted_values[x]


			
for x in range(0,2499):
    if x < 49 or x >2449:
        weighted_values[x] = weighted_values[x]
    else:
        if weighted_values[x-50][0] == 0 and weighted_values[x+50][0] == 0:
            weighted_values[x][0] = 0
            weighted_values[x][1] = 0
            weighted_values[x][2] = 0
            weighted_values[x][3] = 0
        else:
            weighted_values[x] = weighted_values[x]
            
           


#converts list of pixels back into tuple format (format used to create .png files)
final_pixels = []
for lists in weighted_values:
    sublist = []
    for values in lists:
        sublist.append(values)
    tup = (sublist[0],sublist[1],sublist[2],sublist[3]) 
    final_pixels.append(tup)
    


#creates an image with new pixel values
im5 = Image.new('RGB', (50,50))
im5.putdata(final_pixels)
im5.save("File path to store output picture")


