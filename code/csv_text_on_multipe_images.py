# COPY TEXT FROM A CSV FILE TO A IMAGE
#Make changes in the next 6 lines.
path1="C:\\Python27"      ### LINE 3- CSV file Location/ Directory.The directory which has the csv file. You have to replace the current directory with your own directory.
your_csv_file='try.csv'     ### LINE 4-You have to change the csv_file name depending on what is your csv file name.
content_list=[0,1,2]        ### LINE 5-You have to add the column numbers depending on your csv file, which have the content that needs to be placed on the image.
image_list=[3]              ### LINE 6-You have to put the column number which contains the image names.
path2='C:\\Python27\\pic2'      ### Line 7- Images Location/ Directory.The dirctory which has the images. You have to replace the current directory with your own directory.
path3='C:\\Python27\\pic3'      ### LINE 8- The directory where you want to save the new images.You have to replace the current directory with your own directory.


#imorting packages and libraries.

import os
import os.path
import csv
from PIL import Image,ImageDraw,ImageFont
import PIL.Image
import PIL.ImageDraw

content1=[]     #creating a list for the content which needs to be copied on the image.
img1=[]     #creating a list for the image names.

os.chdir(path1)        #changing the directory, to where the csv file is stored.
with open (your_csv_file,'rb') as csvfile:      #open the csv file.
    
    reader = csv.reader(csvfile, delimiter=',')
    included_cols = content_list           #content columns. 
    img_cols=image_list                #image column.

    for row in reader:
        content = list(row[i]for i in included_cols)        #selects the content from the csv file. 
        content1.append(content)                #appends the content into the new list.
        for j in img_cols:
            img=(row[j])            #selecting image names in csv file
            img1.append(img)        #appending image names in img1 list.

length2=len(img1)       #length of the img1 list.


images1=[]      #creating new list
images2=[]      #creating new list

os.chdir(path2)      #changing the directory, to where the images are stored. 
length=len([name for name in os.listdir(os.getcwd()) if os.path.isfile(name)])      #length=number of files in the directory.

for i in range(length):
    images1.append(Image.open(os.listdir(os.getcwd())[i]))      #appends the open image to the list.
    images2.append(os.listdir(os.getcwd())[i])              #appends the image name to the list.

z=input ("Enter the value of z:\n 1.TOP CENTER \n 2.TOP LEFT CORNER \n 3.BOTTOM CENTER \n 4.BOTTOM LEFT CORNER \n 5.EXIT \n")     #select a value of z between 1-6, depednig on the case you want.

x=input ("Enter the width of the image:")
y=input ("Enter the height of the images:")

print ("To set the color of text \n")
a=input("Percentage of Red: any number between 0 to 256")
b=input("Percntage of Green: any number between 0 to 256")
c=input("Percntae of Blue: any number between 0 to 256")



if (z==1):
    for j in range(0,length2):
        for i in range(0,length):
            if (img1[j]== images2[i]):      #checks if the image name  from the csv file is present in the directory.
                print ("true")              #if the image name is present in the directory, the it prints true.
                image=images1[i].resize((x,y))      #resizing the image.
                width, height=image.size            #width=width of the image, heigth= height of the image.
                width1=width/2
                height1=height/2
                draw=ImageDraw.Draw(image)          #we have to draw on a specfic image.
                draw.text((width-width1-75,30),str(content1[j]),(a,b,c,0))         #copies the text from the csv file to the image, on the top center
                os.chdir(path3)
                image.save("final000"+str(i)+".jpg")            #save the new image. You can change the new name as whatever you want- image.save("new_name"+str(i)+".jpg")
            else:
                print("Image not found")            #if the image name is not present in the directory.

if (z==2):
    for j in range(0,length2):
        for i in range(0,length):
            if (img1[j]== images2[i]):      #checks if the image name  from the csv file is present in the directory.
                print ("true")              #if the image name is present in the directory, the it prints true.
                image=images1[i].resize((x,y))      #resizing the image.
                width, height=image.size            #width=width of the image, heigth= height of the image.
                draw=ImageDraw.Draw(image)          #we have to draw on a specfic image.
                draw.text((10,10),str(content1[j]),(a,b,c,0))         #copies the text from the csv file to the image, on the top left.
                os.chdir(path3)
                image.save("final000"+str(i)+".jpg")            #save the new image. You can change the new name as whatever you want- image.save("new_name"+str(i)+".jpg")
            else:
                print("Image not found")            #if the image name is not present in the directory.


if (z==3):
    for j in range(0,length2):
        for i in range(0,length):
            if (img1[j]== images2[i]):      #checks if the image name  from the csv file is present in the directory.
                print ("true")              #if the image name is present in the directory, the it prints true.
                image=images1[i].resize((x,y))      #resizing the image.
                width, height=image.size            #width=width of the image, heigth= height of the image.
                width1=width/2
                height1=height/2
                draw=ImageDraw.Draw(image)          #we have to draw on a specfic image.
                draw.text((width-width1-75,height-30),str(content1[j]),(a,b,c,0))         #copies the text from the csv file to the image, on the bottom center
                os.chdir(path3)
                image.save("final000"+str(i)+".jpg")            #save the new image. You can change the new name as whatever you want- image.save("new_name"+str(i)+".jpg")
            else:
                print("Image not found")            #if the image name is not present in the directory.


if (z==4):
    for j in range(0,length2):
        for i in range(0,length):
            if (img1[j]== images2[i]):      #checks if the image name  from the csv file is present in the directory.
                print ("true")              #if the image name is present in the directory, the it prints true.
                image=images1[i].resize((x,y))      #resizing the image.
                width, height=image.size            #width=width of the image, heigth= height of the image.
                width1=width/2
                height1=height/2
                draw=ImageDraw.Draw(image)          #we have to draw on a specfic image.
                draw.text((10,height-30),str(content1[j]),(a,b,c,0))         #copies the text from the csv file to the image, on the bottom left
                os.chdir(path3)
                image.save("final000"+str(i)+".jpg")            #save the new image. You can change the new name as whatever you want- image.save("new_name"+str(i)+".jpg")
            else:
                print("Image not found")            #if the image name is not present in the directory.

if (z==5):
    exit()
