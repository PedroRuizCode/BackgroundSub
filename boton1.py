'''         Image processing and computer vision
        Alejandra Avendaño, Carolina Pulido & Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import tkinter as tk
from tkinter import *
class boton1:
    def __init__(self):
        self.OptionList = ["", "Video", "Imagen"]
        path_file = "imagen.png"
        self.ventana = tk.Tk()
        self.ventana.title("Background Settings")
        self.ventana.configure(background="#212121")
        self.ventana.geometry('680x480')
        self.variable = tk.StringVar(self.ventana)
        self.variable.set(self.OptionList[0])
        self.variable2 = tk.StringVar(self.ventana)
        self.variable2.set(self.OptionList[0])
        self.labelTest1 = tk.Label(text="",font=('Sitka Subheading', 12),background="#212121",foreground='white')
        self.labelTest = tk.Label(text="", font=('Sitka Subheading', 28),background="#212121",foreground='white')
        # labelTest.pack(side="top")
        # labelTest1.pack(side="top")
        self.labelTest.place(x=0, y=0)
        self.labelTest1.place(x=0, y=60)
        self.labelTest.configure(text="SETTINGS MENU")
        self.labelTest1.configure(text="Choose from VIDEO or IMAGE for background settings".format(self.variable.get()))
        self.botImg1 = tk.Button()
        self.botImg2 = tk.Button()
        self.botImg3 = tk.Button()
        self.botImg4 = tk.Button()
        self.botImg5 = tk.Button()
        self.botImg6 = tk.Button()
        self.backImg = tk.Button()
        self.botVideo1 = tk.Button()
        self.botVideo2 = tk.Button()
        self.botVideo3 = tk.Button()
        self.botVideo4 = tk.Button()
        self.backVideo = tk.Button()
        self.closeButton = tk.Button()
        self.saveButton = tk.Button()
        self.image1 = tk.Label()
        self.image2 = tk.Label()
        self.image3 = tk.Label()
        self.image4 = tk.Label()
        self.image5 = tk.Label()
        self.image6 = tk.Label()
        self.imgVid1 = tk.Label()
        self.imgVid2 = tk.Label()
        self.imgVid3 = tk.Label()
        self.imgVid4 = tk.Label()

        self.img1 = tk.PhotoImage(file="images/Comp.png")
        self.img1 = self.img1.subsample(12)
        self.img2 = tk.PhotoImage(file="images/lamp.png")
        self.img2 = self.img2.subsample(12)
        self.img3 = tk.PhotoImage(file="images/mountain.png")
        self.img3 = self.img3.subsample(12)
        self.img4 = tk.PhotoImage(file="images/nave.png")
        self.img4 = self.img4.subsample(12)
        self.img5 = tk.PhotoImage(file="images/office.png")
        self.img5 = self.img5.subsample(12)
        self.img6 = tk.PhotoImage(file="images/sofa.png")
        self.img6 = self.img6.subsample(12)

        self.vid1 = tk.PhotoImage(file="images/beach.png")
        self.vid1 = self.vid1.subsample(8)
        self.vid2 = tk.PhotoImage(file="images/chair.png")
        self.vid2 = self.vid2.subsample(8)
        self. vid3 = tk.PhotoImage(file="images/lights.png")
        self.vid3 = self.vid3.subsample(8)
        self.vid4 = tk.PhotoImage(file="images/star_wars.png")
        self.vid4 = self.vid4.subsample(8)
        self.interfaz()
        self.ventana.mainloop()

    def interfaz(self):
        global opt, opt2

        self.opt = tk.OptionMenu(self.ventana, self.variable, *self.OptionList)
        self.opt.config(width=10, font=('Sitka Subheading', 12), bg="#212121", fg="white")
        self.opt.pack(expand=True)
        self.opt.place(x=10, y=130)
        self.closeButton = tk.Button(self.ventana, width=10, text="Close", command=self.close, bg="#212121", fg="white",font=('Sitka Subheading', 12))
        self.closeButton.pack()
        self.closeButton.place(x=550, y=420)
        self.variable.trace("w", self.callback)


    def callback(self,*args):
        self.xx = self.variable.get()
        # print(variable2.get())
        self.labelTest.configure(text="Settings Menu")
        if (self.xx == "Imagen"):
            self.bot_Image()
            self.flag = "A"
            self.labelTest1.configure(text="Choose an image for background settings")
        elif (self.xx == "Video"):
            self.bot_Video()
            self.flag = "B"
            self.labelTest1.configure(text="Choose a video for background settings")
        else:
            self.labelTest.configure(text="Settings Menu")
            self.labelTest1.configure(text="Choose from VIDEO or IMAGE for background settings".format(self.variable.get()))
            self.clearImg()


    def bot_Image(self):
        self.botImg1, self.botImg2, self.botImg3, self.botImg4, self.botImg5, self.botImg6, self.backImg

        self.botImg1 = tk.Button(self.ventana, text="Imagen 1", image=self.img1, command=self.Imagen1)
        self.botImg2 = tk.Button(self.ventana, text="Imagen 2", image=self.img2, command=self.Imagen2)
        self.botImg3 = tk.Button(self.ventana, text="Imagen 3", image=self.img3, command=self.Imagen3)
        self.botImg4 = tk.Button(self.ventana, text="Imagen 4", image=self.img4, command=self.Imagen4)
        self.botImg5 = tk.Button(self.ventana, text="Imagen 5", image=self.img5, command=self.Imagen5)
        self.botImg6 = tk.Button(self.ventana, text="Imagen 6", image=self.img6, command=self.Imagen6)
        self.backImg = tk.Button(self.ventana, text="Back", command=self.clearImg, bg="#212121", fg="white", width= 10,font=('Sitka Subheading', 12))
        self.botImg1.pack()
        self.botImg2.pack()
        self.botImg3.pack()
        self.botImg4.pack()
        self.botImg5.pack()
        self.botImg6.pack()
        self.backImg.pack()
        self.botImg1.place(x=20, y=200)
        self.botImg2.place(x=190, y=200)
        self.botImg3.place(x=360, y=200)
        self.botImg4.place(x=20, y=302)
        self.botImg5.place(x=190, y=302)
        self.botImg6.place(x=360, y=302)
        self.backImg.place(x=225, y=420)


    def bot_Video(self):
        self.botVideo1, self.botVideo2, self.botVideo3, self.botVideo4, self.backVideo

        self.botVideo1 = tk.Button(self.ventana, text="Video 1", image=self.vid1, command=self.Video1)
        self.botVideo2 = tk.Button(self.ventana, text="Video 2", image=self.vid2, command=self.Video2)
        self.botVideo3 = tk.Button(self.ventana, text="Video 3", image=self.vid3, command=self.Video3)
        self.botVideo4 = tk.Button(self.ventana, text="Video 4", image=self.vid4, command=self.Video4)
        self.backVideo = tk.Button(self.ventana, text="Back", command=self.clearImg, bg="#212121", fg="white", width= 10,font=('Sitka Subheading', 12))
        self.botVideo1.pack()
        self.botVideo2.pack()
        self.botVideo3.pack()
        self.botVideo4.pack()
        self.backVideo.pack()
        self.botVideo1.place(x=20, y=200)
        self.botVideo2.place(x=190, y=200)
        self.botVideo3.place(x=20, y=302)
        self.botVideo4.place(x=190, y=302)
        self.backVideo.place(x=135, y=420)


    def Imagen1(self):
        self.path_file = "images/Comp.png"
        print(self.path_file)


    def Imagen2(self):
        self.path_file = "images/lamp.png"
        print(self.path_file)


    def Imagen3(self):
        self.path_file = "images/mountain.png"
        print(self.path_file)


    def Imagen4(self):
        self.path_file = "images/nave.png"
        print(self.path_file)


    def Imagen5(self):
        self.path_file = "images/office.png"
        print(self.path_file)


    def Imagen6(self):
        self.path_file = "images/sofa.png"
        print(self.path_file)


    def Video1(self):
        self.path_file = "images/beach.mp4"
        print(self.path_file)


    def Video2(self):
        self.path_file = "images/chair.mp4"
        print(self.path_file)


    def Video3(self):
        self.path_file = "images/lights.mp4"
        print(self.path_file)


    def Video4(self):
        self.path_file = "images/start_wars.mp4"
        print(self.path_file)


    def close(self):
        self.ventana.destroy()


    def clearImg(self):
        self.botImg1.place_forget()
        self.botImg2.place_forget()
        self.botImg3.place_forget()
        self.botImg4.place_forget()
        self.botImg5.place_forget()
        self.botImg6.place_forget()
        self.backImg.place_forget()
        self.botVideo1.place_forget()
        self.botVideo2.place_forget()
        self.botVideo3.place_forget()
        self.botVideo4.place_forget()
        self.backVideo.place_forget()
        self.image1.pack_forget()
        self.image2.pack_forget()
        self.image3.pack_forget()
        self.image4.pack_forget()
        self.image5.pack_forget()
        self.image6.pack_forget()
        self.imgVid1.pack_forget()
        self.imgVid2.pack_forget()
        self.imgVid3.pack_forget()
        self.imgVid4.pack_forget()
        self.variable.set(self.OptionList[0])
        self.opt = tk.OptionMenu(self.ventana, self.variable, *self.OptionList)

    def path(self):
        return self.path_file

    def bandera(self):
        return self.flag