from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import math

class FrmTabung:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Tinggi:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  

        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=3, column=1, padx=5, pady=5) 

        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=0, padx=5, pady=5)


    # fungsi "onHitung" berfungsi untuk menghitung Volume Tabung
    def onHitung(self, event=None):
        Jarijari = int(self.txtJarijari.get())
        Tinggi = int(self.txtTinggi.get())
        Volume = math.pi * Jarijari**2 * Tinggi
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(Volume))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTabung(root, "Program Volume Tabung")
    root.mainloop() 