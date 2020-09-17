from tkinter import *
import pyperclip
from time import sleep
root = Tk()


class Functions():
    def inserir(self):
        global texto
        texto = self.entrada.get()
        self.entrada.delete( 0, "end" )
        self.lbl_notify['text'] = ' '

    def upper_case(self):
        self.inserir()
        self.entrada.insert(0, texto.upper())
    def lower_case(self):
        self.inserir()
        self.entrada.insert( 0, texto.lower())
    def capitalize_case(self):
        self.inserir()
        self.entrada.insert(0, texto.capitalize())
    def title_case(self):
        self.inserir()
        self.entrada.insert( 0, texto.title())
    def inverter_case(self):
        self.inserir()
        self.entrada.insert( 0, texto.swapcase())
    def clipboard(self):
        texto = self.entrada.get()
        pyperclip.copy(texto)
        self.lbl_notify['text'] = 'Text copied to clipboard!'
    def clear(self):
        self.entrada.delete( 0, "end" )



class Aplicattion(Functions):
    def __init__(self):  # Inicializando tudo
        self.root = root
        self.widgets_tela()
        self.configuracoes_tela()
        root.mainloop()

    def configuracoes_tela(self):  # Função contendo configurações da janela
        self.root.title("Convertor de textos")  # Título da tela
        self.root.configure(bg='#E0E0E0') # Cor de fundo
        self.root.geometry("800x400") #Resolução da tela
        root.minsize( width=800, height=400 )

    def widgets_tela(self):
        self.frame = Frame(root, bg = '#E0E0E0')
        self.frame.place(relx=0.05, rely= 0.35, relheight= 0.6, relwidth=0.9)

        self.label_1 = Label(root, bg = '#142852', text='Digitou algo acidentalmente com o caps lock ligado e está com preguiça de digitar novamente? ',
                             fg= 'white', font=('verdana', 10, 'bold'))
        self.label_1.place(relx=0, rely=0., relheight= 0.25, relwidth=1)

        self.entrada = Entry(self.frame, highlightbackground='#4a8282', highlightthickness=1)
        self.entrada.place(relx=0.025, rely=0.0, relheight= 0.6, relwidth=0.94)



        self.btn_uppercase = Button(self.frame, text= 'UPPER CASE', fg = 'white', bg = '#1e3b7b',
                                    command= self.upper_case)
        self.btn_uppercase.place(relx=0.025, rely=0.7, relheight= 0.12, relwidth=0.11)



        self.btn_lowercase = Button(self.frame, text= 'lower case', fg = 'white', bg = '#1e3b7b',
                                    command=self.lower_case)
        self.btn_lowercase.place(relx=0.14, rely=0.7, relheight= 0.12, relwidth=0.1)



        self.btn_Capitalized = Button(self.frame, text= 'Capitalized case', fg = 'white', bg = '#1e3b7b',
                                      command = self.capitalize_case)

        self.btn_Capitalized.place(relx=0.245, rely=0.7, relheight= 0.12, relwidth=0.15)



        self.btn_Inverte = Button(self.frame, text= 'Inverte case', fg = 'white', bg = '#1e3b7b',
                                  command = self.inverter_case)
        self.btn_Inverte.place(relx=0.4, rely=0.7, relheight= 0.12, relwidth=0.15)



        self.btn_title = Button(self.frame, text= 'Title case', fg = 'white', bg = '#1e3b7b',
                                command=self.title_case )
        self.btn_title.place(relx=0.555, rely=0.7, relheight= 0.12, relwidth=0.1)

        self.btn_title = Button( self.frame, text='Copy to clipboard', fg = 'white', bg = '#1e3b7b',
                                 command=self.clipboard)
        self.btn_title.place( relx=0.66, rely=0.7, relheight=0.12, relwidth=0.15 )

        self.btn_clear = Button( self.frame, text='Clear', fg = 'white', bg = '#1e3b7b',
                                 command=self.clear )
        self.btn_clear.place( relx=0.815, rely=0.7, relheight=0.12, relwidth=0.15 )

        self.lbl_notify = Label(root, bg = '#E0E0E0',fg = 'white', font=('verdana', 8))
        self.lbl_notify.place(relx= 0.073, rely=0.9)


Aplicattion()