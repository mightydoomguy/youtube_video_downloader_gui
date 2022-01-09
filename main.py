from pytube import YouTube
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.filedialog as fd
class App(Frame):
    def __init__(self,video):
        super(App, self).__init__(video)
        self.widget()
        self.grid()
    def download(self):
        url = YouTube(self.urlbox.get())
        filters = url.streams.filter(progressive=True)
        path = self.urlbox1.get()
        file = self.filename.get()
        filename = file + '.mp4'
        filters.get_highest_resolution().download(output_path=path,filename=filename)
    #def download_playlist(self):#Нуждается в доработке поскольку недопилен
     #   url = Playlist(self.urlbox.get())
      #  path = self.urlbox1.get()
       # url.download_all(download_path=path)
    def ch_dir(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        dirctry = str(directory)
        self.urlbox1.insert(0,dirctry)
    def clean(self):
        self.urlbox1.delete(0,END)
        self.urlbox.delete(0,END)
        self.filename.delete(0,END)

    def widget(self):
        #--------------------------------------------
        #self.pb = Progressbar(self,orient='horizontal',mode='determinate',maximum=100,value=0)
        #self.pb['value'] = 100
        #self.pb.grid(row=4,column=3)
        #--------------------------------------------
        #--------------------------------------------
        self.but = LabelFrame(self,text="Buttons",background='#ff3d00')
        self.but.grid(row=0,column=5)
        #---------------------------------------------------------
        self.main = LabelFrame(self, text="MainMenu",background='#ff3d00')
        self.main.grid(row=0, column=1)
        #---------------------------------------------------------
        # --------------------------------------------
        # ---------------------------------------------------------
        self.lbl = Label(self.main, text="Enter youtube url:",background='#ff3d00')
        self.lbl.grid(row=0,column=1)
        self.urlbox = Entry(self.main,width=50)
        self.urlbox.grid(row=1,column=1)
        #---------------------------------------------------------
        self.lbl1 = Label(self.main, text="Enter save path(for examples:C://Users/username/Desktop/videos):",background='#ff3d00')
        self.lbl1.grid(row=2, column=1)
        self.urlbox1 = Entry(self.main, width=50)
        self.urlbox1.grid(row=3, column=1)
        #---------------------------------------------------------
        #self.lbl2 = Label(self, text="Enter youtube playlist url:")
        #self.lbl2.grid(row=4, column=1)
        #self.playlstbox = Entry(self, width=50)
        #self.playlstbox.grid(row=5, column=1)
        #---------------------------------------------------------
        self.lbl2 = Label(self.main, text="Enter filename(example:file.mp4):",background='#ff3d00')
        self.lbl2.grid(row=0, column=2)
        self.filename = Entry(self.main, width=10)
        self.filename.grid(row=1, column=2)
        #---------------------------------------------------------
        self.btn = Button(self.but)
        self.btn["text"] = "download video"
        self.btn["command"] = self.download
        self.btn["width"] = 14
        self.btn["height"] = 1
        self.btn["bg"] = "black"
        self.btn["fg"] = "white"
        self.btn.grid(row=1, column=3,sticky=E)
        #--------------------------------------------------------
        self.btn1 = Button(self.but)
        self.btn1["text"] = "browse"
        self.btn1["command"] = self.ch_dir
        self.btn1["width"] = 10
        self.btn1["height"] = 0
        self.btn1["bg"] = "black"
        self.btn1["fg"] = "white"
        self.btn1.grid(row=3, column=3,sticky=W)
        #--------------------------------------------------------
        self.btn1 = Button(self.but)
        self.btn1["text"] = "clear"
        self.btn1["command"] = self.clean
        self.btn1["width"] = 10
        self.btn1["height"] = 0
        self.btn1["bg"] = "black"
        self.btn1["fg"] = "white"
        self.btn1.grid(row=5, column=3,sticky=W)
root = Tk()
root.title('video_downloader')
root.iconbitmap('icof.ico')
root.configure(background='#ff3d00')
root.geometry('670x120')
#root.configure(background='red')
app = App(root)
root.mainloop()
#url = YouTube('https://www.youtube.com/watch?v=co840IiarBs')
#filters = url.streams.filter(progressive=True)
#filters.get_highest_resolution().download(output_path='/home/rmnet/Desktop/youtube_video_downloader', filename='dobl.mp4')
