# PixInfo.py
# Program to start evaluating an image in python

from PIL import Image, ImageTk
import glob, os, math


# Pixel Info class.
class PixInfo:
    
    # Constructor.
    def __init__(self, master):
    
        self.master = master
        self.imageList = []
        self.photoList = []
        self.xmax = 0
        self.ymax = 0
        self.colorCode = []
        self.intenCode = []

        count = 1
        
        # Add each image (for evaluation) into a list, 
        # and a Photo from the image (for the GUI) in a list.
        for infile in glob.glob('images/*.jpg'):
            
            file, ext = os.path.splitext(infile)
            im = Image.open(infile)

            # Resize the image for thumbnails.
            imSize = im.size

            x = imSize[0]/4
            y = imSize[1]/4
            imResize = im.resize((int(x), int(y)), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(imResize)
            
            
            # Find the max height and width of the set of pics.
            if x > self.xmax:
              self.xmax = x
            if y > self.ymax:
              self.ymax = y
            
            
            # Add the images to the lists.
            self.imageList.append(im)
            self.photoList.append(photo)


        # Create a list of pixel data for each image and add it
        # to a list.
        for im in self.imageList[:]:
            pixList = list(im.getdata())
            CcBins, InBins = self.encode(pixList)
            if im.filename.endswith('43.jpg'):
                # print(im.size[0])
                # print(im.size[1])
                print(InBins)
            self.colorCode.append(CcBins)
            self.intenCode.append(InBins)
            

    # Bin function returns an array of bins for each 
    # image, both Intensity and Color-Code methods.
    def encode(self, pixlist):
        
        # 2D array initilazation for bins, initialized
        # to zero.
        CcBins = [0]*65
        InBins = [0]*26
        
                    
           #your code
        #intensity:
        InBins[0] = len(pixlist)
        for pix in pixlist:
            H = pix[0] * 0.299 + pix[1] * 0.587 + pix[2] * 0.114
            H /= 10
            H = int(H)
            if H>=25:
                InBins[25] += 1
            else:
                InBins[H+1] += 1

        #color code:
        CcBins[0] = len(pixlist)
        for pix in pixlist:
            R = pix[0]
            G = pix[1]
            B = pix[2]
            H = ((R>>6)<<4) + ((G>>6)<<2) + (B>>6)
            CcBins[H+1] += 1
        # Return the list of binary digits, one digit for each
        # pixel.
        return CcBins, InBins
    
    
    # Accessor functions:
    def get_imageList(self):
        return self.imageList
    
    def get_photoList(self):
        return self.photoList
    
    def get_xmax(self):
        return self.xmax
    
    def get_ymax(self):
        return self.ymax
    
    def get_colorCode(self):
        return self.colorCode
        
    def get_intenCode(self):
        return self.intenCode
    
    
