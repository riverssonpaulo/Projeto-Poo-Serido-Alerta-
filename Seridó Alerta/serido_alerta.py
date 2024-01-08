from tkinter import *
import sqlite3

class App:
   def __init__ (self):
        def receber_valores():
           valor_cidade = self.caixacidade.get()
           valor_data = self.caixadata.get()
           valor_hora = self.caixahora.get()
           valor_temperatura = self.caixatemperatura.get()

           banco_temperaturas = sqlite3.connect('banco_temperaturas_seridó.db')
           cursor = banco_temperaturas.cursor()
          
           cursor.execute('''CREATE TABLE tabletemperatura
                  (nome_cidade             TEXT    NOT NULL,
                  data_informada           INT    NOT NULL,
                  hora_informada           INT     NOT NULL,
                  value_temperatura        INT     NOT NULL);''')

           cursor.execute("INSERT INTO tabletemperatura (nome_cidade, data_informada, hora_informada, value_temperatura) VALUES (?, ?, ?, ?)", (valor_cidade, valor_data, valor_hora, valor_temperatura))
               
           banco_temperaturas.close()
           banco_temperaturas.commit()

        def limpar():
            cidade = self.caixacidade
            data = self.caixadata
            hora = self.caixahora
            temperatura = self.caixatemperatura

            cidade.delete(0, END)
            data.delete(0, END)
            hora.delete(0, END)
            temperatura.delete(0, END)

        def verificar():
            valor_cidade = self.caixacidade.get()
            valor_data = self.caixadata.get()
            valor_hora = self.caixahora.get()
            valor_temperatura = self.caixatemperatura.get()

            lista_dicionario = {'cidade': ' ', 'data': ' ', 'horário': ' ', 'temperaruta': ' '}

            for i in valor_cidade:
                if valor_cidade != int:
                    lista_dicionario['cidade'] = valor_cidade
                else:
                    valor_str = str(valor_cidade)
                    lista_dicionario['cidade'] = valor_str

            for i in valor_data:
                if valor_data == str:
                    lista_dicionario['data'] = valor_data
                else:
                    valor_str = str(valor_data)
                    lista_dicionario['data'] = valor_str

            for i in valor_hora:
                if valor_hora == str:
                    lista_dicionario['horário'] = valor_hora
                else:
                    valor_str = str(valor_hora)
                    lista_dicionario['horário'] = valor_str

            for i in valor_temperatura:
                if valor_temperatura == int:
                    lista_dicionario['temperaruta'] = valor_temperatura
                else:
                    valor_int = int(valor_temperatura)
                    lista_dicionario['temperaruta'] = valor_int

            try:
                self.txt['text'] = lista_dicionario
            except:
                print(lista_dicionario)
                
                
        self.janela = Tk()
        self.janela.geometry('600x600')
        self.janela.title('Seridó Alerta')
        self.janela.resizable(False, False)

        self.canvas1 = Canvas(self.janela, bg= 'white', width=600, height= 600)
        self.imagem = PhotoImage(file='logo_seridó_alerta.png').subsample(5)
        self.canvas1.create_image(300,80,image=self.imagem)
        self.canvas1.pack()

        self.txtcidade = Label(self.janela, text= 'Cidade:', font="Corbel 15", bg='white')
        self.txtcidade.place(x=260, y=160)

        self.caixacidade = Entry (self.janela, font="Corbel 13", justify='center')
        self.caixacidade.place(x=200, y= 190, width=190, height=30)

        self.txtdata = Label(self.janela, text= 'Data:', font="Corbel 15", bg='white')
        self.txtdata.place(x=270, y=240)

        self.caixadata = Entry (self.janela, font="Corbel 13", justify='center')
        self.caixadata.place(x=200, y= 270, width=190, height=30)

        self.txthora = Label(self.janela, text= 'Hora:', font="Corbel 15", bg='white')
        self.txthora.place(x=270, y=320)

        self.caixahora = Entry (self.janela, font="Corbel 13", justify='center')
        self.caixahora.place(x=200, y= 350, width=190, height=30)

        self.txtemperatura = Label(self.janela, text= 'Temperatura:', font="Corbel 15", bg='white')
        self.txtemperatura.place(x=235, y=400)

        self.caixatemperatura = Entry (self.janela, font="Corbel 13", justify='center')
        self.caixatemperatura.place(x=200, y= 430, width=190, height=30)

        self.consultar = Button (self.janela, text='Consultar Registro',
        font="Corbel 11", width=20, height=2, fg='white', bg='#000000', borderwidth=0, command=verificar)
        self.consultar.place(x=20, y=500)

        self.consultar = Button (self.janela, text='Limpar Registro',
        font="Corbel 11", width=20, height=2, fg='white', bg='#000000', borderwidth=0, command=limpar)
        self.consultar.place(x=220, y=500)

        self.registrar = Button (self.janela, text='Registrar', font="Corbel 11", width=20, height=2, fg='white', bg='#F9A16E', borderwidth=0, command= receber_valores)
        self.registrar.place(x=420, y=500)

        self.txt = Label(self.janela, font="Corbel 12", bg='white')
        self.txt['text'] = ' '
        self.txt.place(x=20, y=560)

        self.caixacidade.bind("<Return>", lambda e: self.caixadata.focus_set())
        self.caixadata.bind("<Return>", lambda e: self.caixahora.focus_set())
        self.caixahora.bind("<Return>", lambda e: self.caixatemperatura.focus_set())
        
     
        self.janela.mainloop()

        
janela =App()