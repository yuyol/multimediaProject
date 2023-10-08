# ImageViewer.py
# Program to start evaluating an image in python
#
# Show the image with:
# os.startfile(imageList[n].filename)
import tkinter
from tkinter import *
from functools import partial
import tkinter as tk
from PIL import Image, ImageTk
import math, os
from PixInfo import PixInfo


# Main app.
class ImageViewer(Frame):
    
    # Constructor.
    def __init__(self, master, pixInfo, resultWin):
        
        Frame.__init__(self, master)
        self.master    = master
        self.pixInfo   = pixInfo
        self.resultWin = resultWin
        self.colorCode = pixInfo.get_colorCode()
        self.intenCode = pixInfo.get_intenCode()
        # Full-sized images.
        self.imageList = pixInfo.get_imageList()
        # Thumbnail sized images.
        self.photoList = pixInfo.get_photoList()
        # Image size for formatting.
        self.xmax = pixInfo.get_xmax()
        self.ymax = pixInfo.get_ymax()
        self.current = 0
        self.currentSelect = 0
        self.arr = [0]*100
        self.dic = {}



        
        # Create Main frame.
        mainFrame = Frame(master)
        # mainFrame.pack(fill=BOTH,expand= True)
        mainFrame.pack()
        
        # Create Picture chooser frame.
        listFrame = Frame(mainFrame,width=300)
        listFrame.pack(side=BOTTOM,fill=X,expand= True)
        
        
        # Create Control frame.
        controlFrame = Frame(mainFrame)
        controlFrame.pack(side=RIGHT)
        
        
        # Create Preview frame.
        previewFrame = Frame(mainFrame,
            width=self.xmax+45, height=self.ymax)
        previewFrame.pack_propagate(0)
        previewFrame.pack(side=LEFT)
        
        
        # Create Results frame.
        self.resultsFrame = Frame(self.resultWin)
        self.resultsFrame.pack(side=BOTTOM)
        self.canvas = Canvas(self.resultsFrame)
        self.resultsScrollbar = Scrollbar(self.resultsFrame)
        self.resultsScrollbar.pack(side=RIGHT, fill=Y)
        
        # initialize arr
        for i in range(100):
            self.arr[i] = i

        # # Layout Picture Listbox.
        # self.listScrollbar = Scrollbar(listFrame)
        # self.listScrollbar.pack(side=RIGHT, fill=Y)
        # self.list = Listbox(listFrame,
        #     yscrollcommand=self.listScrollbar.set,
        #     selectmode=BROWSE,
        #     height=10)
        # for i in range(len(self.imageList)):
        #     self.list.insert(i, self.imageList[i].filename)
        # self.list.pack(side=LEFT, fill=BOTH)
        # self.list.activate(1)
        # self.list.bind('<<ListboxSelect>>', self.update_preview)
        # self.listScrollbar.config(command=self.list.yview)


        def nextPage():
            print(self.current)
            if self.current != 100:
                for widgets in listFrame.winfo_children():
                    widgets.destroy()

                for i in range(4):
                    for j in range(5):
                        button = tk.Button(listFrame, text="test", image=self.photoList[int(self.arr[self.current])], width=100,
                                           height=50,
                                           command=partial(self.buttonClicked, self.arr[self.current]))
                        # self.button1.pack(side= LEFT)
                        button.grid(row=i + 1, column=j + 1)
                        self.current += 1

        def previousPage():
            self.current -= 20
            if (self.current > 0):
                self.current -= 20
                for widgets in listFrame.winfo_children():
                    widgets.destroy()

                for i in range(4):
                    for j in range(5):
                        button = tk.Button(listFrame, text="test", image=self.photoList[int(self.arr[self.current])], width=100,
                                           height=50,
                                           command=partial(self.buttonClicked, self.arr[self.current]))
                        # self.button1.pack(side= LEFT)
                        button.grid(row=i + 1, column=j + 1)
                        self.current += 1
            else:
                self.current += 20

        # Layout Controls.
        button = Button(controlFrame, text="Inspect Pic", 
            fg="red", padx = 10, width=10, 
            command=lambda: self.inspect_pic())
        button.grid(row=0, sticky=E)
        
        # self.b1 = Button(controlFrame, text="Color-Code",
        #     padx = 10, width=10,
        #     command=lambda: self.find_distance(method='CC'))
        # self.b1.grid(row=1, sticky=E)

        b1 = Button(controlFrame, text="Color-Code",
                         padx=10, width=10,
                         command=lambda: self.find_distance(method='CC',master= self,listFrame= listFrame))
        b1.grid(row=1, column=1, sticky=E)
        
        b2 = Button(controlFrame, text="Intensity", 
                        padx = 10, width=10,
                        command=lambda: self.find_distance(method='inten',master= self,listFrame= listFrame))
        b2.grid(row=1, column=2,sticky=E)

        previousBtn = Button(controlFrame, text="previous page",
                             padx = 10, width=10,
                             command=partial(previousPage))
        previousBtn.grid(row=2, column=1)

        nextPageBtn = Button(controlFrame, text="next page",
                             padx = 10, width=10,
                             command=partial(nextPage))
        nextPageBtn.grid(row=2, column=2)
        
        self.resultLbl = Label(controlFrame, text="Results:")
        self.resultLbl.grid(row=3, sticky=W)
        
        
        # Layout Preview.
        self.selectImg = Label(previewFrame,
                        width=100,height=100,bg="black",image=self.photoList[0])
        self.selectImg.pack()

        self.refresh(listFrame)

    # Event "listener" for listbox change.
    def update_preview(self, idx):
        # i = self.list.curselection()[0]
        self.selectImg.configure(
            image=self.photoList[idx])

    def buttonClicked(self, idx):
        self.update_preview(idx)
        self.currentSelect = idx
        print(idx)

    def refresh(self,listFrame):
        self.current = 0
        # Layout Picture List
        for i in range(4):
            for j in range(5):
                button = tk.Button(listFrame, text="test", image=self.photoList[int(self.arr[self.current])], width=100,
                                   height=50,
                                   command=partial(self.buttonClicked, self.arr[self.current]))
                # self.button1.pack(side= LEFT)
                button.grid(row=i + 1, column=j + 1)
                self.current += 1
    
    
    # Find the Manhattan Distance of each image and return a
    # list of distances between image i and each image in the
    # directory uses the comparison method of the passed 
    # binList
    def find_distance(self, method, master,listFrame):
        self.resultFrame = master.resultsFrame

        # your code
        if method == 'inten':
            print("inten")
            for widgets in self.resultFrame.winfo_children():
                widgets.destroy()

            InBin = self.pixInfo.intenCode[self.currentSelect]

            self.dic = {}

            for i in range(100):
                distance = 0
                tmpBin = self.pixInfo.intenCode[i]
                for j in range(26):
                    if j>0:
                        distance += abs((InBin[j]/InBin[0])
                                        -(tmpBin[j]/tmpBin[0]))
                self.dic[i] = distance
            self.dic = sorted(self.dic.items(), key=lambda x:x[1])
            idx = 0
            for key in self.dic:
                self.arr[idx] = key[0]
                idx+=1
            print(self.arr)
            self.refresh(listFrame)


        else:
            print('Cc')
            for widgets in self.resultFrame.winfo_children():
                widgets.destroy()

            CcBin = self.pixInfo.colorCode[self.currentSelect]

            self.dic = {}

            for i in range(100):
                distance = 0
                tmpBin = self.pixInfo.colorCode[i]
                for j in range(65):
                    if j > 0:
                        distance += abs((CcBin[j] / CcBin[0])
                                        - (tmpBin[j] / tmpBin[0]))
                self.dic[i] = distance
            self.dic = sorted(self.dic.items(), key=lambda x: x[1])
            idx = 0
            for key in self.dic:
                self.arr[idx] = key[0]
                idx += 1
            print(self.arr)
            self.refresh(listFrame)
    
    # Update the results window with the sorted results.
    def update_results(self, sortedTup):
        
        cols = int(math.ceil(math.sqrt(len(sortedTup))))
        fullsize = (0, 0, (self.xmax*cols), (self.ymax*cols))

        # Initialize the canvas with dions equal to the
        # number of results.
        self.canvas.delete(ALL)
        self.canvas.config( 
            width=self.xmax*cols, 
            height=self.ymax*cols/2, 
            yscrollcommand=self.resultsScrollbar.set,
            scrollregion=fullsize)
        self.canvas.pack()
        self.resultsScrollbar.config(command=self.canvas.yview)
        
        # your code
        
        
        # Place images on buttons, then on the canvas in order
        # by distance.  Buttons invoke the inspect_pic method.
        rowPos = 0
        while photoRemain:
            
            photoRow = photoRemain[:cols]
            photoRemain = photoRemain[cols:]
            colPos = 0
            for (filename, img) in photoRow:
                
                link = Button(self.canvas, image=img)
                handler = lambda f=filename: self.inspect_pic()
                link.config(command=handler)
                link.pack(side=LEFT, expand=YES)
                self.canvas.create_window(
                    colPos, 
                    rowPos, 
                    anchor=NW,
                    window=link, 
                    width=self.xmax, 
                    height=self.ymax)
                colPos += self.xmax
                
            rowPos += self.ymax
    
    # Open the picture with the default operating system image
    # viewer.
    def inspect_pic(self):
        idx = self.currentSelect
        os.startfile(self.imageList[idx].filename)

if __name__ == '__main__':

    root = Tk()
    root.title('Image Analysis Tool')

    resultWin = Toplevel(root)
    resultWin.title('Result Viewer')
    resultWin.protocol('WM_DELETE_WINDOW', lambda: None)

    pixInfo = PixInfo(root)

    imageViewer = ImageViewer(root, pixInfo, resultWin)

    root.mainloop()