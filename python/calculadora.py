from tkinter import *
from math import *



class Calculadora:
    def __init__(self, toplevel):

        # Janela
        toplevel.title('Calculadora em Python com Tkinter')
        toplevel.geometry("510x300")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Mensagem
        self.frame7 = Frame(toplevel, pady=12)
        self.frame7.pack()

        # Box 1
        self.frame2 = Frame(toplevel)
        self.frame2.pack()

        # Box 2
        self.frame3 = Frame(toplevel)
        self.frame3.pack()

        # Operações
        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        # Resultado
        self.frame5 = Frame(toplevel)
        self.frame5.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=12)
        self.frame6.pack()

        # Cor e tamanho das letras
        Label(self.frame1,text='', fg='black',
        font=('Verdana','10'), height=1).pack()
        fonte1=('Verdana','10')
        fonte2=('Verdana', '15')

        # Botão somar
        somar=Button(self.frame4,font=fonte1, text='+',command=self.somar)
        somar.pack(side=LEFT)

        # Botão subtrair
        subtrair=Button(self.frame4,font=fonte1, text='-',command=self.subtrair)
        subtrair.pack(side=LEFT)

        # Botão multiplicar
        multiplicar=Button(self.frame4,font=fonte1, text='*',command=self.multiplicar)
        multiplicar.pack(side=LEFT)

        # Botão dividir
        dividir=Button(self.frame4,font=fonte1, text='/',command=self.dividir)
        dividir.pack(side=LEFT)

        # Botão exponeciacao
        exponeciacao=Button(self.frame4,font=fonte1, text='^',command=self.exponeciacao)
        exponeciacao.pack(side=LEFT)

        # Botão porcentagem
        porcentagem=Button(self.frame4,font=fonte1, text='%',command=self.porcentagem)
        porcentagem.pack(side=LEFT)

        # Botão Limpar
        limpar=Button(self.frame6, font=fonte1, text= 'Limpar', command=self.limpar)
        limpar.pack(side=LEFT)

        # Botão Sair
        sair=Button(self.frame6, font=fonte1, text= 'Sair', command=self.sair)
        sair.pack(side=LEFT)

        # Box 1 para entrada de número
        Label(self.frame2,text='Valor 1 :', font=fonte1,width=8).pack(side=LEFT)
        self.valor1=Entry(self.frame2,width=10,font=fonte1)
        self.valor1.focus_force()
        self.valor1.pack(side=LEFT)

        # Box 2 para entrada de número
        Label(self.frame3,text='Valor 2 :',font=fonte1,width=8).pack(side=LEFT)
        self.valor2=Entry(self.frame3,width=10,font=fonte1)
        self.valor2.pack(side=LEFT)

        # Resultado
        Label(self.frame5,text=' = ',font=fonte1,width=8).pack(side=LEFT)
        self.msg=Label(self.frame5,width=10,font=fonte1)
        self.msg.pack(side=LEFT)

        # mensagem
        Label(self.frame7,text='Digite os valores e depois escolha a operação:', font=fonte2,width=50).pack(side=LEFT)

    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 + valor2
        c = float(c)
        self.msg['text']= '%f' %(c)

    def subtrair(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 - valor2
        c = float(c)
        self.msg['text']= '%f' %(c)

    def multiplicar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 * valor2
        c = float(c)
        self.msg['text']= '%f' %(c)

    def dividir(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 / valor2
        c = float(c)
        self.msg['text']= '%f' %(c)

    def exponeciacao(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = valor1 ** valor2
        c = float(c)
        self.msg['text']= '%f' %(c)

    def porcentagem(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        c = (valor1 * valor2) / 100
        c = float(c)
        self.msg['text']= '%f' %(c)

    def limpar(self):
        self.valor1.delete(0, 'end')
        self.valor2.delete(0, 'end')

    def sair(self):
        app.destroy()

app=Tk()
Calculadora(app)
app.mainloop()
