from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):  # metod koji kreira glavni prozor i smijesta frejm u njega

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        tk.Tk.iconbitmap(self, default='servis.ico')
        tk.Tk.wm_title(self, 'Servis Automobila')

        container.pack(side="top", fill="both", expand=True)  # postavljanje frejma
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # kreiranje dictionary-a, u koji se smjestaju stranice

        for F in (
        LoginPage, PageOne, PageTwo):  # glavni dio... ovdje se ubacuju stranice... samo dodas naziv klase u kojoj si..
            # ..kreirao glavni prozor
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):  # metod koji prikazuje onaj frejm koji mu proslijedis u glavnom dijelu
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

        tk.Frame.__init__(self, parent)
        userName = tk.Label(self, text="Korisničko ime", font=LARGE_FONT)
        userName.grid(row=0, column=0, sticky=E)
        userEntry = tk.Entry(self, width=17, font=LARGE_FONT, textvariable=user)
        userEntry.grid(row=0, column=1)
        password = tk.Label(self, text="Lozinka", font=LARGE_FONT)
        password.grid(row=1, column=0, sticky=E)
        passEntry = tk.Entry(self, width=17, font=LARGE_FONT, show="*", textvariable=passwd)
        passEntry.grid(row=1, column=1)
        loginButton = tk.Button(self, text="Uloguj se", font=LARGE_FONT,
                                command=loging_check)
        loginButton.place(x=208, y=60)


class PageOne(tk.Frame):  # ovo je drugi... itd.. mozes da imas prozora koliko hoces. :)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Odjava",
                            command=lambda: controller.show_frame(LoginPage))
        button1.grid(column=0, row=0)
        content = ttk.Frame(self, padding=(3, 3, 3, 3))
        unosFrame = ttk.LabelFrame(content, text='Unos podataka')
        toolsFrame = ttk.LabelFrame(content, text='Alatke')

        # kreiranje labela
        labelIme = ttk.Label(unosFrame, text='Ime i Prezime')
        labelMarka = ttk.Label(unosFrame, text='Marka i model')
        labelStatus = ttk.Label(unosFrame, text='Status')
        labelPopravka = ttk.Label(unosFrame, text='Popravka')
        labelDeo = ttk.Label(unosFrame, text='Deo')
        labelCD = ttk.Label(unosFrame, text='Cena Dela')
        labelCP = ttk.Label(unosFrame, text='Cena Popravke')

        deoi = ["Točak", "Guma", "Vijak", "Retrovizor", "Sijalica", "Staklo", "Brisač"]
        statusi = ["Nije stigao na red", "Popravlja se", "Popravljen"]

        class Popravka:
            def __init__(self, pid, deo, cd):
                self.pid = pid
                self.deo = deo
                self.cd = cd

        class Automobil:
            def __init__(self, ime, marka, status, cp, popravka):
                self.ime = ime
                self.popravka = popravka
                self.marka = marka
                self.status = status
                self.cp = cp

        edit1 = StringVar()
        edit2 = StringVar()
        edit3 = StringVar()
        edit4 = StringVar()
        edit5 = StringVar()
        edit6 = StringVar()
        edit7 = StringVar()
        unos1 = StringVar()
        unos2 = StringVar()
        unos3 = StringVar()
        unos4 = StringVar()
        unos5 = StringVar()
        unos6 = StringVar()
        unos7 = StringVar()

        def setuj():
            unos1.set("")
            unos2.set("")
            unos3.set("")
            unos4.set("")
            unos5.set("")
            unos6.set("")
            unos7.set("")

        def unesiLice(*args):  # funkvija za unos podataka u treeview

            ime = unos1.get()
            marka = unos2.get()
            status = unos3.get()
            popravka = unos4.get()
            deo = unos5.get()
            cd = unos6.get()
            cp = unos7.get()

            if ime == "" or marka == "" or status == "" or popravka == "" or deo == "" or cd == "" or cp == "":
                messagebox.showinfo("Greška", "Morate popuniti sva polja!")

            else:
                try:
                    int(cd)
                    int(cp)
                    tree.insert("", 'end', values=(
                    ime.title(), marka.title(), status.title(), popravka.title(), deo.title(), cd, cp))

                    setuj()
                except ValueError:
                    messagebox.showinfo("Greška", "Upišite cene brojem")

        def izbrisiStariItem(tree):  # funkcija (vezana za Edit) koja briše stari item iz tree-a, koji treba biti zamenjen novim
            trenutni = tree.selection()
            if trenutni == '': return
            tree.delete(trenutni)

        def potvrda(tree, entryIme, entryMarka, entryStatus, entryPopravka, entryDeo, entryCD,entryCP):  # funkcija (vezana za Edit) koja ubacuje u tree izmejnene vrednosti
            indeks = tree.index(tree.focus())
            izbrisiStariItem(tree)
            tree.insert('', indeks,
                        values=(entryIme, entryMarka, entryStatus, entryPopravka, entryDeo, int(entryCD), int(entryCP)))

            return True

        # funkcija koja kreira pop up prozor za edit... (kreira labele i entrije u novom prozoru i povezuje ih sa varijablama)
        def edituj():
            try:
                selekcija = tree.item(tree.selection())

                lista = selekcija.get("values")
                ime = lista[0]
                marka = lista[1]
                status = lista[2]
                popravka = lista[3]
                deo = lista[4]
                cd = str(lista[5])
                cp = str(lista[6])

                editWin = tk.Toplevel()
                editWin.title('Edit')

                imelbl = ttk.Label(editWin, text='Ime i Prezime').grid(column=0, row=0, sticky=(E, S, N, W))
                imeEntry = ttk.Entry(editWin, textvariable=edit1).grid(column=1, row=0)
                edit1.set(ime)

                prezimelbl = ttk.Label(editWin, text='Marka i Model').grid(column=0, row=1, sticky=(E, S, N, W))
                prezimeEntry = ttk.Entry(editWin, textvariable=edit2).grid(column=1, row=1)
                edit2.set(marka)

                statuslbl = ttk.Label(editWin, text='Status').grid(column=0, row=2, sticky=(E, S, N, W))
                statusEntry = ttk.Entry(editWin, textvariable=edit3).grid(column=1, row=2)

                edit3.set(status)

                popravkalbl = ttk.Label(editWin, text='Popravka').grid(column=0, row=3, sticky=(E, S, N, W))
                popravkaEntry = ttk.Entry(editWin, textvariable=edit4).grid(column=1, row=3)
                edit4.set(popravka)

                deolbl = ttk.Label(editWin, text='Deo').grid(column=0, row=4, sticky=(E, S, N, W))
                deoEntry = ttk.Entry(editWin, textvariable=edit5).grid(column=1, row=4)

                edit5.set(deo)

                cdlbl = ttk.Label(editWin, text='Cena Dela').grid(column=0, row=5, sticky=(E, S, N, W))
                cdEntry = ttk.Entry(editWin, textvariable=edit6).grid(column=1, row=5)
                edit6.set(cd)

                cplbl = ttk.Label(editWin, text='Cena Popravke').grid(column=0, row=6, sticky=(E, S, N, W))
                cpEntry = ttk.Entry(editWin, textvariable=edit7).grid(column=1, row=6)
                edit7.set(cp)

                def memorisiIZatvori():  # ubacuje izmenjene vrednosti u tree
                    try:
                        int(edit6.get())
                        int(edit7.get())
                        if potvrda(tree, edit1.get(), edit2.get(), edit3.get(), edit4.get(), edit5.get(),
                                   str(edit6.get()), str(edit7.get())):
                            editWin.destroy()
                    except ValueError:
                        messagebox.showinfo("Greška", "Upišite cenu brojem")
                        edituj()

                def cancel():
                    editWin.destroy()

                okDugme = ttk.Button(editWin, text='Ok', command=memorisiIZatvori).grid(column=0, row=7, sticky=E)
                cancelDugme = ttk.Button(editWin, text='Cancel', command=cancel).grid(column=1, row=7, sticky=E)

            except IndexError:
                messagebox.showinfo("Greška", "Upišite cene brojem")

        entryIme = ttk.Entry(unosFrame, textvariable=unos1)
        entryMarka = ttk.Entry(unosFrame, textvariable=unos2)
        entryStatus = ttk.Combobox(unosFrame, textvariable=unos3)
        entryStatus["values"] = (statusi)
        entryPopravka = ttk.Entry(unosFrame, textvariable=unos4)
        entryDeo = ttk.Combobox(unosFrame, textvariable=unos5)
        entryDeo["values"] = (deoi)
        entryCD = ttk.Entry(unosFrame, textvariable=unos6)
        entryCP = ttk.Entry(unosFrame, textvariable=unos7)

        # kreiranje dugmadi
        dodaj = ttk.Button(unosFrame, text='Dodaj', command=unesiLice)

        editd = ttk.Button(toolsFrame, text='Izmeni', command=edituj)
        memorisi = ttk.Button(toolsFrame, text='Sačuvaj')
        ispisiSve = ttk.Button(toolsFrame, text='Učitaj')
        # kreiranje treeviewa

        tree = ttk.Treeview(content)
        tree['show'] = ('headings')
        tree["columns"] = ("prva", "druga", "treca", "cetvrta", "peta", "sesta", "sedma")
        tree.heading("prva", text="Ime I Prezime")
        tree.heading("druga", text="Marka i model")
        tree.heading("treca", text="Status")
        tree.heading("cetvrta", text="Popravka")
        tree.heading("peta", text="Deo")
        tree.heading("sesta", text="Cena dela")
        tree.heading("sedma", text="Cena popravke")
        # scrollbar
        scrollbar = ttk.Scrollbar(content, orient=VERTICAL, command=tree.yview)
        scrollbar.grid(column=3, row=1, sticky=(N, S))
        tree['yscrollcommand'] = scrollbar.set

        # postavljanje widgeta...
        content.grid(column=0, row=0, padx=5, sticky=(N, E, S, W))
        unosFrame.grid(column=0, row=0, padx=7, pady=7, sticky=W)
        toolsFrame.grid(column=1, row=0, sticky=W)

        labelIme.grid(column=1, row=0, sticky=(E))
        labelMarka.grid(column=1, row=1, sticky=(E))
        labelStatus.grid(column=1, row=2, sticky=(E))
        labelPopravka.grid(column=1, row=3, sticky=(E))
        labelDeo.grid(column=1, row=4, sticky=(E))
        labelCD.grid(column=1, row=5, sticky=(E))
        labelCP.grid(column=1, row=6, sticky=(E))

        entryIme.grid(column=2, row=0, sticky=(E, W))
        entryMarka.grid(column=2, row=1, sticky=(E, W))
        entryStatus.grid(column=2, row=2, sticky=(E, W))
        entryPopravka.grid(column=2, row=3, sticky=(E, W))
        entryDeo.grid(column=2, row=4, sticky=(E, W))
        entryCD.grid(column=2, row=5, sticky=(E, W))
        entryCP.grid(column=2, row=6, sticky=(E, W))

        dodaj.grid(column=3, row=0, rowspan=6, sticky=(N, S, E, W))

        editd.grid(column=1, row=0, sticky=(N, S, E, W))
        memorisi.grid(column=1, row=1, sticky=(N, S, E, W))

        ispisiSve.grid(column=0, row=2, columnspan=2, sticky=(N, E, S, W))

        tree.grid(column=0, row=1, columnspan=3, sticky=(E, W))


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = MainWindow()
app.mainloop()