from PIL import Image
import os, sys, shutil, datetime, vintage

#TODO -
#Add more image filters
#Add auto watermark facility (Watermark loadble by path)
#Multithreading to make saving process faster
#Add quote facility
    #Text file of quotes added to the bottom center of the picture


path = ("C:/?/?/?/picturestest")
datestr = datetime.date.today().strftime("%d-%m-%y")
makephotosvintage = False
UserInput = ""
UserChosen = False
NumberOfPhotos = 0
NumberOfPhotosResized = 0

if not os.path.exists(path):
    print("Making directory...")
    os.mkdir(path)

if not os.path.exists(path + "/resizedimages"):
    print("Making directory...")
    os.mkdir(path + "/resizedimages")

if not os.path.exists(path + "/resizedimages/" + datestr):
    print("Making directory...")
    os.mkdir(path + "/resizedimages/" + datestr)

NumberOfPhotos =  len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f[0] != '.'])

print("Number of Photos - " + str(NumberOfPhotos))

while (UserChosen == False):
    UserInput = raw_input("Make photos vintage? Y/N")
    if (UserInput.lower() == 'y'):
        makephotosvintage = True
        UserChosen = True
    elif (UserInput.lower() == 'n'):
        makephotosvintage = False
        UserChosen = True
    else:
        print('User\'s input is to be given as (Y/N)\n')


def resize():
    global NumberOfPhotosResized
    for item in os.listdir(path):
        item = path + "/" + item
        print(item)
        if os.path.isfile(item):
            im = Image.open(item)
            width, height = im.size
            f, e = os.path.splitext(item)
            imResize = im.resize((width - 1, height - 1), Image.ANTIALIAS)
            outputfiledirectory = os.path.join(path + "/resizedimages")
            if makephotosvintage == True:
                imResize = vintage.vintage_colors(imResize)
            imResize.save(f + " resized.jpg", 'JPEG', quality=90) #+ f + ' resized.jpg', 'JPEG', quality=90)
            NumberOfPhotosResized += 1
            for xyz in os.listdir(path):
                print(xyz)
                if "resized" in xyz and "resizedimages" not in xyz:
                    shutil.move(path + "/" + xyz, path + "/resizedimages/" + datestr + "/" + xyz)



resize()
print ("Number of Photos resized - " + str(NumberOfPhotosResized))
