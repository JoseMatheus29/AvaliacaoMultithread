import tkinter
from tkinter import *
import qrcode
import client
lista = list()
link = qrcode.make('scielo.iec.gov.br/scielo.php?script=sci_arttext&pid=S1679-49742012000200015')
link.save('QRcode.png')


def qrcode(img1):
    janelaqrcode = tkinter.Toplevel(app)
    janelaqrcode.geometry("500x500")
    lbl_image = Label(janelaqrcode, image=img1)
    lbl_image.place(x=10, y=40)
    lbltxt = Label(janelaqrcode, text='Scannei o qrcode para saber mais', font="Arial 20")
    lbltxt.place(x=10, y=10)


def enviar():
    lista.append(peso.get())
    lista.append(altura.get())
    imc = client.envia(lista)
    lblimc = Label(app, text=f"{imc}", background='white', foreground='black', font="Arial 15")
    lblimc.place(x=200, y=10)
    return imc


def initabela():
    import tabela
    tab = tabela


app = Tk()
img = PhotoImage(file="QRcode.png")
app.geometry("500x300")
app.title("Calculadora Imc")
app.configure(background='white')
lblpeso = Label(app, text="Peso", background='white', foreground='black', font="Arial 15")
lblpeso.place(x=10, y=10, width=100)
peso = Entry(app)
peso.place(x=10, y=45, width=100)
lblaltura = Label(app, text="Altura", background='white', foreground='black', font="Arial 15")
lblaltura.place(x=10, y=80, width=100)
altura = Entry(app)
altura.place(x=10, y=115, width=100)
Button(app, text='Calcular', command=enviar).place(x=10, y=145, width=100)
Button(app, text='Tabela Imc', command=initabela).place(x=10, y=185, width=100)
Button(app, text='Saiba Mais',  command=lambda: qrcode(img)).place(x=10, y=225, width=100)
app.mainloop()
