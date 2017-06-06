import tkinter as tk
from tkinter import *
from tkinter import messagebox
LARGE_FONT= ("Verdana", 12)



class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):   #metod koji kreira glavni prozor i smijesta frejm u njega
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        tk.Tk.iconbitmap(self, default='servis.ico')
        tk.Tk.wm_title(self, 'Servis Automobila')
        
        container.pack(side="top", fill="both", expand = True) #postavljanje frejma
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
            
        self.frames = {}  #kreiranje dictionary-a, u koji se smjestaju stranice

        for F in (LoginPage, PageOne, PageTwo):  #glavni dio... ovdje se ubacuju stranice... samo dodas naziv klase u kojoj si..
                                                 #..kreirao glavni prozor
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont): #metod koji prikazuje onaj frejm koji mu proslijedis u glavnom dijelu
        frame = self.frames[cont]
        frame.tkraise()
        if cont == LoginPage:
            self.geometry('320x120+700+350')
        elif cont == PageOne:
            self.geometry('500x500')
        
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        global user
        global passwd
        user = StringVar()
        passwd = StringVar()
        def loging_check():
            global user
            global passwd
            pasword = 'admin'
            username = 'admin'
            if passwd.get() == pasword and user.get() == username:
                controller.show_frame(PageOne)
            else:
                messagebox.showinfo("Greska", "Sifra ili korisnicko ime nisu tacni!\nPokusajte ponovo!")

        tk.Frame.__init__(self,parent)
        userName = tk.Label(self, text="Korisničko ime", font=LARGE_FONT)
        userName.grid(row=0, column=0, sticky=E)
        userEntry = tk.Entry(self, width=17, font=LARGE_FONT, textvariable=user)
        userEntry.grid(row=0, column=1)
        password = tk.Label(self, text="Lozinka", font=LARGE_FONT)
        password.grid(row=1, column=0, sticky=E)
        passEntry = tk.Entry(self, width=17, font=LARGE_FONT, show="*",textvariable=passwd)
        passEntry.grid(row=1, column=1)
        loginButton = tk.Button(self, text="Uloguj se", font=LARGE_FONT,
                                command=loging_check)
        loginButton.place(x=208, y=60)
        


class PageOne(tk.Frame): # ovo je drugi... itd.. mozes da imas prozora koliko hoces. :) 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(LoginPage))
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
