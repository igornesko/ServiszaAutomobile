from tkinter import *
import tkinter as tk
from tkinter import messagebox

LARGE_FONT= ("Verdana", 11)



class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):   #metod koji kreira glavni prozor i smijesta frejm u njega

        ttk.__init__(self, *args, **kwargs)
        container = ttk.Frame(self)
        ttk.iconbitmap(self, default='servis.ico')
        ttk.wm_title(self, 'Servis Automobila')

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
        frame.ttkraise()
        if cont == LoginPage:
            self.geometry('320x120+700+350')
        elif cont == PageOne:
            self.geometry('1000x1000')

class LoginPage(ttk.Frame):

    def __init__(self, parent, controller):

        user = StringVar()
        passwd = StringVar()
        def loging_check():
            useru="user"
            userp="user"
            adminu = 'admin'
            adminp = 'admin'
            if passwd.get() == adminu and user.get() == adminp:
                controller.show_frame(PageOne)

            elif passwd.get()==useru and user.get()==userp:
                controller.show_frame(PageTwo)
            else:
                messagebox.showinfo("Greska", "Sifra ili korisnicko ime nisu tacni!\nPokusajte ponovo!")


        ttk.Frame.__init__(self,parent)
        userName = ttk.Label(self, text="Korisničko ime", font=LARGE_FONT)
        userName.grid(row=0, column=0, sticky=E)
        userEntry = ttk.Entry(self, width=17, font=LARGE_FONT, textvariable=user)
        userEntry.grid(row=0, column=1)
        password = ttk.Label(self, text="Lozinka", font=LARGE_FONT)
        password.grid(row=1, column=0, sticky=E)
        passEntry = ttk.Entry(self, width=17, font=LARGE_FONT, show="*",textvariable=passwd)
        passEntry.grid(row=1, column=1)
        loginButton = ttk.Button(self, text="Prijava", font=LARGE_FONT,
                                command=loging_check)
        loginButton.place(x=208, y=60)




class PageOne(ttk.Frame): # ovo je drugi... itd.. mozes da imas prozora koliko hoces. :)

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        odjava = ttk.Button(self, text="Odjava",
                            command=lambda: controller.show_frame(LoginPage),font=LARGE_FONT)
        odjava.grid(column=0, row=0)
        ime=StringVar()
        model=StringVar()
        opis=StringVar()
        status=StringVar()

        labelai=ttk.Label(self,text="Ime i Prezime", font=LARGE_FONT)
        labelai.grid(column=0,row=1)
        labelam = ttk.Label(self, text="Model automobila", font=LARGE_FONT)
        labelam.grid(column=0, row=2)
        labelao = ttk.Label(self, text="Opis kvara", font=LARGE_FONT)
        labelao.grid(column=0, row=3)
        labelas = ttk.Label(self, text="Status", font=LARGE_FONT)
        labelas.grid(column=0, row=4)
        unosi = ttk.Entry(self,  font=LARGE_FONT, textvariable=ime)
        unosi.grid(column=1, row=1)
        unosm = ttk.Entry(self,  font=LARGE_FONT,textvariable=model)
        unosm.grid(column=1, row=2)
        unoso = ttk.Entry(self,  font=LARGE_FONT,textvariable=opis)
        unoso.grid(column=1, row=3)
        unoss = ttk.Entry(self,  font=LARGE_FONT,textvariable=status)
        unoss.grid(column=1, row=4)
        donjiDeo = ttk.Frame(self, width=200, height=200)
        donjiDeo.grid(column=1, row=6)
        labelain = ttk.Label(donjiDeo, text="Informacije", bg="blue", fg="white",  font=LARGE_FONT,width=100)
        labelain.grid(column=0, row=0,columnspan=2)
        lista=ttk.list(donjiDeo,font=LARGE_FONT,width=100)
        lista.grid(column=0, row=1,columnspan=2)

# tree = ttk.Treeview()
# tree['show']=('headings')
# tree["columns"]=("prva","druga", "treca", "cetvrta")
# tree.heading("prva", text="Kategorija")
# tree.heading("druga", text="Iznos")
# tree.heading("treca", text="Datum")
# tree.heading("cetvrta", text="Uneo korisnik:")
# tree.grid(column=1, row=10, columnspan=2, sticky=(E,W))




class PageTwo(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(LoginPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = MainWindow()
app.mainloop()
