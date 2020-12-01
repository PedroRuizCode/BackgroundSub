'''         Image processing and computer vision
        Alejandra Avendaño, Carolina Pulido & Pedro Ruiz
               Electronic engineering students
              Pontificia Universidad Javeriana
                      Bogotá - 2020
'''
import tkinter as tk
from tkinter import *
class capture:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.img1 = tk.PhotoImage(file="images/icon.png")
        self.img1 = self.img1.subsample(6)
        self.ventana1.title("Background Settings")
        self.ventana1.configure(background="#212121")
        self.ventana1.geometry('270x200')
        self.labelTest = tk.Label(text="", font=('Sitka Subheading', 23), background="#212121", foreground='white')
        self.labelTest1= tk.Label(text="", font=('Sitka Subheading', 10), background="#212121", foreground='white')
        self.labelTest.place(x=30, y=0)
        self.labelTest1.place(x=0, y=60)
        self.labelTest.configure(text="SCREENSHOT")
        self.labelTest1.configure(text="Push the button to capture the image")
        self.Capture_photo = tk.Button(self.ventana1, image=self.img1, command=self.Capture_button, bg="#212121", fg="white")
        self.Capture_photo.pack()
        self.Capture_photo.place(x=75, y=90)
        self.Capture_photo = tk.Button()
        self.Capture_button()
        self.ventana1.mainloop()

    def Capture_button(self):
        self.photo = 1
        self.Capture_photo1 = tk.Button(self.ventana1, text="Close", command=self.Close, bg="#212121",
                                       fg="white")
        self.Capture_photo1.pack()
        self.Capture_photo1.place(x=195, y=160)

    def enviar(self):
        return self.photo

    def Close(self):
        self.ventana1.destroy()