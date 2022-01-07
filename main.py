from pytube import YouTube
from tkinter import *
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
    def widget(self):
        #---------------------------------------------------------
        self.lbl = Label(self, text="Enter youtube url:")
        self.lbl.grid(row=0,column=1)
        self.urlbox = Entry(self,width=50)
        self.urlbox.grid(row=1,column=1)
        #---------------------------------------------------------
        self.lbl1 = Label(self, text="Enter save path(for examples:C://Users/username/Desktop/videos):")
        self.lbl1.grid(row=2, column=1)
        self.urlbox1 = Entry(self, width=50)
        self.urlbox1.grid(row=3, column=1)
        #---------------------------------------------------------
        #self.lbl2 = Label(self, text="Enter youtube playlist url:")
        #self.lbl2.grid(row=4, column=1)
        #self.playlstbox = Entry(self, width=50)
        #self.playlstbox.grid(row=5, column=1)
        #---------------------------------------------------------
        self.lbl2 = Label(self, text="Enter filename(example:file.mp4):")
        self.lbl2.grid(row=0, column=2)
        self.filename = Entry(self, width=10)
        self.filename.grid(row=1, column=2)
        #---------------------------------------------------------
        self.btn = Button(self)
        self.btn["text"] = "download video"
        self.btn["command"] = self.download
        self.btn["width"] = 14
        self.btn["height"] = 1
        self.btn["bg"] = "black"
        self.btn["fg"] = "white"
        self.btn.grid(row=1, column=3)
        #--------------------------------------------------------
        self.btn1 = Button(self)
        self.btn1["text"] = "browse"
        self.btn1["command"] = self.ch_dir
        self.btn1["width"] = 10
        self.btn1["height"] = 0
        self.btn1["bg"] = "black"
        self.btn1["fg"] = "white"
        self.btn1.grid(row=3, column=2)
        #--------------------------------------------------------
root = Tk()
root.title('video_downloader')
root.iconbitmap('icof.ico')
root.geometry('800x400')
app = App(root)
root.mainloop()
#url = YouTube('https://www.youtube.com/watch?v=co840IiarBs')
#filters = url.streams.filter(progressive=True)
#filters.get_highest_resolution().download(output_path='/home/rmnet/Desktop/youtube_video_downloader', filename='dobl.mp4')
