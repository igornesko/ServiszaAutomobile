import tkinter as tk
from tkinter import *

LARGE_FONT= ("Verdana", 12)


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):   #metod koji kreira glavni prozor i smijesta frejm u njega
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #kreiranje frejma
        
        container.pack(side="top", fill="both", expand = True) #postavljanje frejma
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
            
        self.frames = {}  #kreiranje dictionary-a, u koji se smjestaju stranice

        for F in (StartPage, PageOne, PageTwo):  #glavni dio... ovdje se ubacuju stranice... samo dodas naziv klase u kojoj si..
                                                 #..kreirao glavni prozor
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont): #metod koji prikazuje onaj frejm koji mu proslijedis u glavnom dijelu
        frame = self.frames[cont]
        frame.tkraise()
        if cont == StartPage:
            self.geometry('200x300')
        elif cont == PageOne:
            self.geometry('500x500')
            
        
class StartPage(tk.Frame):  # ovo je klassa prvog prozora koji se otvori kada pokrenes program...

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        global geo
        geo = '200x200'
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame): # ovo je drugi... itd.. mozes da imas prozora koliko hoces. :) 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = MainWindow()
app.mainloop()
