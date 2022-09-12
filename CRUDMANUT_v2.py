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



#classe crud para as funçoes do bd
class funcs():
        #função para execultar a limpeza das label
        def limpar_tela(self):
                self.codigo_entry.delete(0, END)
                self.solicitante_entry.delete(0, END)
                self.maq_entry.delete(0, END)
                self.desc_entry.delete(0, END)
                self.status_entry.delete(0, END)
        def conecta_bd(self):
                self.conn = sqlite3.connect("cliente_bd")
                self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
        def desconecta_bd(self): 
                self.conn.close(); print("desconectando ao banco de dados")
        def monta_tabelas(self):
                self.conecta_bd()
        # criar tabela
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                                cod INTEGER PRIMARY KEY,
                                solicitante VARCHAR(40) NOT NULL,
                                maq VARCHAR(40),
                                desc VARCHAR(40),
                                status INTERGER(3));""")



                self.conn.commit(); print("banco de dados criado")
                self.desconecta_bd()
        
        def variaveis(self):
                self.codigo = self.codigo_entry.get()
                self.solicitante = self.solicitante_entry.get()
                self.maq = self.maq_entry.get()
                self.desc = self.desc_entry.get()
                self.status = self.status_entry.get()

        def add_cliente(self):
                self.variaveis()
                self.conecta_bd()
                self.cursor.execute(""" INSERT INTO clientes (solicitante, maq, desc, status) 
                                        VALUES (?, ?, ?, ?) """ , (self.solicitante, self.maq, self.desc, self.status))
                self.conn.commit()
                self.desconecta_bd()
                self.select_lista()
                self.limpar_tela()
        
        def select_lista(self):
        
                self.listacli.delete(*self.listacli.get_children())
                self.conecta_bd()
                lista = self.cursor.execute(""" SELECT * FROM clientes """)
                for i in lista:
                        self.listacli.insert("", END, values=i)
                self.desconecta_bd()
        
        def ondoubleclick(self, event):
                self.limpar_tela()
                self.listacli.selection()
                for n in self.listacli.selection():
                        col1, col2, col3, col4 , col5 = self.listacli.item(n, 'values')
                        self.codigo_entry.insert(END, col1)
                        self.solicitante_entry.insert(END, col2)
                        self.maq_entry.insert(END, col3)
                        self.desc_entry.insert(END, col4)
                        self.status_entry.insert(END, col5)

#     def deleta_cliente(self):    
#         self.variaveis()
#         self.conecta_bd()
#         self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
#         self.conn.commit()
#         self.desconecta_bd()
#         self.limpar_tela()
#         self.select_lista()


        #HOLD
#     def altera_cliente(self):
#         self.variaveis()
#         self.conecta_bd()
#         self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
#             WHERE cod = ?""", (self.nome, self.tel, self.cidade, self.codigo))
#         self.conn.commit()
#         self.desconecta_bd()
#         self.select_lista()
#         self.limpar_tela()
    
        def busca_cliente(self):
        
                self.conecta_bd()
                self.listacli.delete(*self.listacli.get_children())
                self.codigo_entry.insert(END, '%')
                nome = self.codigo_entry.get()
                self.cursor.execute(""" SELECT cod, solicitante, maq, desc, status FROM clientes WHERE cod LIKE '%s' ORDER BY cod """ % nome)  
                buscanomecli = self.cursor.fetchall()
                for i in buscanomecli:
                        self.listacli.insert("", END, values=i)
            
                self.limpar_tela()
                self.desconecta_bd()






#classe para criar o formulario GUI        
class app(funcs):
#class app(funcs,Relatorios):
        #função para chamar as ações da construção da tela
        def __init__(self):
                self.root = root
                self.tela()
                self.frames_da_tela1()
                self.widget()
                self.frames_da_tela2()
                self.monta_tabelas()
                self.select_lista()
                #self.menus()

                root.mainloop()

        #função de criação da tela conforme projeto
        def tela (self):
                #titulo da janela
                self.root.title("SISTEMA PARA CADASTRAR O.S")

                #cor da janela
                self.root.configure(background ='black')
                # Geometria da janela
                self.root.geometry("1000x800")
                # redimensionável sim ou não
#               self.root.resizable(False, False)
                self.root.resizable(True, True)
                # Maxima dimensão
                self.root.maxsize(width = 1400, height = 1200)
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
                self.frame_2.place(relx=0.01, rely=0.47, relwidth=0.98, relheight=0.5)

        #Botoes e label e scroolbar
        def widget(self):
                # botão de limpar
                self.bt_limpar = Button(self.frame_1, text='Limpar tela',bd = 3, bg = 'gray26', fg ='goldenrod'
                                        , font = ('verdana',8,'bold'), command = self.limpar_tela)
                self.bt_limpar.place(relx= 0.85, rely=0, relwidth=0.11, relheight=0.15)
                # botão de buscar
                self.bt_buscar = Button(self.frame_1, text='Buscar O.S',bd = 3, bg = 'gray26', fg ='goldenrod', font = ('verdana',8,'bold'), command = self.busca_cliente)
                self.bt_buscar.place(relx= 0.3, rely=0.0, relwidth=0.11, relheight=0.15)
                # botão de novo
                self.bt_novo = Button(self.frame_1, text='Cadastrar O.S',bd = 3, bg = 'gray26', fg ='goldenrod', font = ('verdana',8,'bold'), command = self.add_cliente)
                self.bt_novo.place(relx= 0.0, rely=0, relwidth=0.11, relheight=0.15)
                # botão de alterar
                self.bt_finalizar = Button(self.frame_1, text='Finalizar',bd = 3, bg = 'gray26', fg ='goldenrod', font = ('verdana',8,'bold'))#, command = self.altera_cliente)
                self.bt_finalizar.place(relx= 0.6, rely=0.0, relwidth=0.12, relheight=0.15)
                # botão de apagar não usado pelo usuario
                # self.bt_apagar = Button(self.frame_1, text='APAGAR',bd = 3, bg = 'royal blue', fg ='White'
                #                        , font = ('verdana',7,'bold'))#, command=self.deleta_cliente )
                # self.bt_apagar.place(relx= 0.85, rely=0.0, relwidth=0.12, relheight=0.15)
                # criação label e entrada NUM O.S
                self.lb_codigo = Label(self.frame_1, text = "CÓD O.S",bd = 3, bg = 'sea green', fg ='White', font = ('verdana',7,'bold'))
                self.lb_codigo.place(relx= 0.0, rely= 0.2)
                self.codigo_entry = Entry(self.frame_1)
                self.codigo_entry.place(relx= 0.0, rely= 0.3)
                # criação label e entrada SOLICITANTE
                self.lb_solicitante = Label(self.frame_1, text = "SOLICITANTE",bd = 3, bg = 'sea green', fg ='White', font = ('verdana',7,'bold'))
                self.lb_solicitante.place(relx= 0.3, rely= 0.2)
                self.solicitante_entry = Entry(self.frame_1)
                self.solicitante_entry.place(relx= 0.30, rely= 0.3)
                # criação label e entrada MÁQUINA
                self.lb_maq = Label(self.frame_1, text = "MÁQUINA",bd = 3, bg = 'sea green', fg ='White', font = ('verdana',7,'bold'))
                self.lb_maq.place(relx= 0.6, rely= 0.2)
                self.maq_entry = Entry(self.frame_1)
                self.maq_entry.place(relx= 0.6, rely= 0.3)
                # criação label e entrada DESCRIÇÃO DO DEFEITO 
                self.lb_desc = Label(self.frame_1, text = "DESCRIÇÃO DO DEFEITO",bd = 3, bg = 'sea green', fg ='White', font = ('verdana',7,'bold'))
                self.lb_desc.place(relx= 0.0, rely= 0.45)
                self.desc_entry = Entry(self.frame_1)
                self.desc_entry.place(relx= 0.0, rely= 0.55, relwidth=1, relheight=0.35)

                # criação label e entrada status 
                self.lb_status = Label(self.frame_1, text = "STATUS",bd = 3, bg = 'sea green', fg ='White', font = ('verdana',7,'bold'))
                self.lb_status.place(relx= 0.85, rely= 0.2)
                self.status_entry = Entry(self.frame_1)
                self.status_entry.place(relx= 0.85, rely= 0.3)


        def frames_da_tela2(self):
                self.listacli = ttk.Treeview(self.frame_2, height = 3, column=("col1","col2","col3","col4","col5"))
                self.listacli.heading("#0", text="")
                self.listacli.heading("#1", text="Codigo O.S")
                self.listacli.heading("#2", text="Solicitante")
                self.listacli.heading("#3", text="Máquina")
                self.listacli.heading("#4", text="Descrição")
                self.listacli.heading("#5", text="Status")
                self.listacli.column("#0", width=1)
                self.listacli.column("#1", width=40)
                self.listacli.column("#2", width=100)
                self.listacli.column("#3", width=125)
                self.listacli.column("#4", width=150)
                self.listacli.column("#5", width=175)
                self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
                self.scroollista = Scrollbar(self.frame_2, orient='vertical')
                self.listacli.configure(yscroll=self.scroollista.set)
                self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85 )
                self.listacli.bind("<Double-1>", self.ondoubleclick )
app()