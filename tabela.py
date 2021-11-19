from tkinter import *


class Table:

    def __init__(self, root1):

        for i in range(linhas):
            for j in range(colunas):
                self.e = Entry(root1, width=20, fg='black',
                               font=('Arial', 16))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


lst = [("Imc", f"{'Classificação'}"),
       ("menor 18", "Abaixo do peso"),
       ("18,5-24,9", "Peso Normal"),
       ("25-29,9", "Acima do Peso"),
       ("30-34,9", "Obesidade grau 1"),
       ("35-39,9", "Obesidade grau 2"),
       ("maior 40", "Obesidade Morbita")]

linhas = len(lst)
colunas = len(lst[0])

root = Tk()
t = Table(root)
root.mainloop()
