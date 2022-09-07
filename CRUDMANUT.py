#SISTEMA DE CADASTRO PABLO 2022 pratico para manutenção
#base deferencias:https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-


#Biblioteca para construção da janela do app
from tkinter import*
from tkinter import ttk
import sqlite3
root = Tk()

#Gerador de pdf
# from reportlab import *
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import SimpleDocTemplate, Image
# import webbrowser as wb

#classe para criar o formulario GUI        
class app():
#class app(funcs,Relatorios):
    #função para chamar as ações da construção da tela
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela1()
        self.widget()
        #self.frames_da_tela2()
        #self.monta_tabelas()
        #self.select_lista()
        #self.menus()

        root.mainloop()

#função de criação da tela conforme projeto
    def tela (self):
#titulo da janela
        self.root.title("SISTEMA PARA CADASTRAR O.S")

#cor da janela
        self.root.configure(background ='black')
# Geometria da janela
        self.root.geometry("750x600")
# redimensionável sim ou não
#         self.root.resizable(False, False)
        self.root.resizable(True, True)
# Maxima dimensão
        self.root.maxsize(width = 1000, height = 1000)
# minima dimensão
        self.root.minsize(width = 600, height = 600)
# transparencia de 0 a 1
        self.root.attributes('-alpha',1)
# prioridade no empilhamento de janelas.
        self.root.attributes('-topmost', 1)
# iconis https://iconscout.com/icons/service?price=free
        self.root.iconbitmap("settings.ico")

    #Construção do primeiro quadro vai conter os botões e as caixas de texto
    def frames_da_tela1(self):
        # telas sobrepostas frame sup
        self.frame_1 = Frame(self.root, bd = 5,
                             bg = 'Royalblue1',highlightbackground= 'goldenrod',highlightthickness=5)   
        self.frame_1.place(relx= 0.01 , rely= 0.01, relwidth= 0.98, relheight=0.45)
        # telas sobrepostas frame inf    
        self.frame_2 = Frame(self.root, bd=5,
                             bg='Royalblue1', highlightbackground='goldenrod', highlightthickness=5)
        self.frame_2.place(relx=0.01, rely=0.47, relwidth=0.98, relheight=0.45)

    def widget(self):
# botão de limpar
        self.bt_limpar = Button(self.frame_1, text='LIMPAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))#, command = self.limpar_tela)
        self.bt_limpar.place(relx= 0.01, rely=0, relwidth=0.11, relheight=0.15)
# botão de buscar
        self.bt_buscar = Button(self.frame_1, text='BUSCAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))#, command = self.busca_cliente)
        self.bt_buscar.place(relx= 0.2, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de novo
        self.bt_novo = Button(self.frame_1, text='CADASTRAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))#, command = self.add_cliente)
        self.bt_novo.place(relx= 0.4, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de alterar
        self.bt_alterar = Button(self.frame_1, text='ALTERAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))#, command = self.altera_cliente)
        self.bt_alterar.place(relx= 0.6, rely=0.0, relwidth=0.12, relheight=0.15)
# botão de apagar
        # self.bt_apagar = Button(self.frame_1, text='APAGAR',bd = 3, bg = 'royal blue', fg ='White'
        #                        , font = ('verdana',7,'bold'))#, command=self.deleta_cliente )
        # self.bt_apagar.place(relx= 0.85, rely=0.0, relwidth=0.12, relheight=0.15)
# criação label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "NUM O.S",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_codigo.place(relx= 0.0, rely= 0.2)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.0, rely= 0.3)
# criação label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "SOLICITANTE",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_nome.place(relx= 0.3, rely= 0.2)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.30, rely= 0.3)
# criação label e entrada do telefone
        self.lb_maq = Label(self.frame_1, text = "MÁQUINA",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_maq.place(relx= 0.6, rely= 0.2)
        self.maq_entry = Entry(self.frame_1)
        self.maq_entry.place(relx= 0.6, rely= 0.3)
# criação label e entrada do CIDADE
        self.lb_desc = Label(self.frame_1, text = "DESCRIÇÃO DO DEFEITO",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_desc.place(relx= 0.0, rely= 0.45)
        self.desc_entry = Entry(self.frame_1)
        self.desc_entry.place(relx= 0.0, rely= 0.55, relwidth=1, relheight=0.35)
app()