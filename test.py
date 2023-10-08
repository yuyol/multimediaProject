from tkinter import *
from functools import partial
import tkinter as tk
from PIL import Image, ImageTk
import math, os
from PixInfo import PixInfo


class test(Frame) :

    # Constructor.
    def __init__(self, master, pixInfo):
        Frame.__init__(self, master)
        self.master = master
        self.pixInfo = pixInfo
        self.colorCode = pixInfo.get_colorCode()
        self.intenCode = pixInfo.get_intenCode()
        # Full-sized images.
        self.imageList = pixInfo.get_imageList()
        # Thumbnail sized images.
        self.photoList = pixInfo.get_photoList()
        # Image size for formatting.
        self.xmax = pixInfo.get_xmax()
        self.ymax = pixInfo.get_ymax()
        global count
        self.count = 0

        # Create Main frame.
        mainFrame = Frame(master)
        mainFrame.pack()

        # Create Picture chooser frame.
        listFrame = Frame(mainFrame, width=300)
        listFrame.pack(side=BOTTOM,fill= X,expand=True)

        # Create Control frame.
        controlFrame = Frame(mainFrame)
        controlFrame.pack(side=RIGHT)

        # Create Preview frame.
        previewFrame = Frame(mainFrame,
                             width=self.xmax + 45, height=self.ymax)
        previewFrame.pack_propagate(0)
        previewFrame.pack(side=LEFT)

        def nextPage():
            print(self.count)
            if self.count != 100:
                for widgets in listFrame.winfo_children():
                    widgets.destroy()

                for i in range(4):
                    for j in range(5):
                        button = tk.Button(listFrame, text="test", image=self.photoList[int(self.count)], width=100, height=50,
                                           command=partial(buttonClicked, self.count))
                        # self.button1.pack(side= LEFT)
                        button.grid(row=i + 1, column=j + 1)
                        self.count += 1

        def previousPage():
            print("before", self.count)
            self.count -= 20

            print("after", self.count)
            if (self.count > 0):
                self.count -= 20
                for widgets in listFrame.winfo_children():
                    widgets.destroy()

                for i in range(4):
                    for j in range(5):
                        button = tk.Button(listFrame, text="test", image=self.photoList[int(self.count)], width=100, height=50,
                                           command=partial(buttonClicked, self.count))
                        # self.button1.pack(side= LEFT)
                        button.grid(row=i + 1, column=j + 1)
                        self.count += 1
            else:
                self.count += 20

        # Layout Controls.
        previousBtn = Button(controlFrame, text="previous page",
                             command=partial(previousPage))
        previousBtn.grid(row=1, column=1)

        nextPageBtn = Button(controlFrame, text="next page",
                    command=partial(nextPage))
        nextPageBtn.grid(row=1, column=2)



        #########################################
        # Layout Picture ListBox in images

        def buttonClicked(idx):
            print(idx)

        # for i in range(len(self.imageList)):

        for i in range(4):
            for j in range(5):
                button = tk.Button(listFrame, text="test", image=self.photoList[int(self.count)], width=100, height=50,
                                   command=partial(buttonClicked,self.count))
                # self.button1.pack(side= LEFT)
                button.grid(row=i+1, column=j + 1)
                self.count+=1






        ##########################################




if __name__ == '__main__':
    root = Tk()
    root.title('Image Analysis Tool')

    # resultWin = Toplevel(root)
    # resultWin.title('Result Viewer')
    # resultWin.protocol('WM_DELETE_WINDOW', lambda: None)

    pixInfo = PixInfo(root)

    test = test(root, pixInfo)


    root.mainloop()