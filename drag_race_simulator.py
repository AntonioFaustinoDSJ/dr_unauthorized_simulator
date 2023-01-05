import tkinter
from aifc import Error
from random import randint
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import tkinter as tk
import tkinter.font as font
import sqlite3 as lite
from tkinter import ttk, messagebox
import json


def nada():
    print()


def conexao_banco():
    caminho = 'C:\\Users\\faust\\PycharmProjects\\drag_race_simulator\\dr_db.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = conexao_banco()


def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


def remove_all():
    labelImg1.destroy()
    labelImg2.destroy()
    button_inic.destroy()
    rodape.destroy()
    personalizacao()


def remove_all0():
    app.title('PERSONALIZAÇÃO DE DESAFIOS')
    lbl_formato.destroy()
    combo_formato.destroy()
    lbl_formafi.destroy()
    combo_formafi.destroy()
    button_queen.destroy()
    button_desaf.destroy()
    lbl_premiere.destroy()
    combo_premiere.destroy()
    lbl_shantay.destroy()
    combo_shantay.destroy()
    lbl_elim.destroy()
    combo_elim.destroy()
    combo_semi.destroy()
    lbl_semi.destroy()
    escolha_desaf()

def remove_all2():
    app.geometry('904x680+265+5')
    app.title('PERSONALIZAÇÃO DE PARTICIPANTES')
    lbl_formato.destroy()
    combo_formato.destroy()
    lbl_formafi.destroy()
    combo_formafi.destroy()
    button_queen.destroy()
    button_desaf.destroy()
    lbl_premiere.destroy()
    combo_premiere.destroy()
    lbl_shantay.destroy()
    combo_shantay.destroy()
    lbl_elim.destroy()
    combo_elim.destroy()
    combo_semi.destroy()
    lbl_semi.destroy()
    criando_combo()


def testar():
    print()


def personalizacao():
    global lbl_formato
    global combo_formato
    global lbl_formafi
    global combo_formafi
    global button_queen
    global button_desaf
    global lbl_premiere
    global combo_premiere
    global lst_formato
    global lst_finale
    global lst_premiere
    global lbl_shantay
    global combo_shantay
    global lbl_elim
    global combo_elim
    global lst_elim
    global lst_shantay
    global lst_semi
    global combo_semi
    global lbl_semi

    app.geometry('820x480+265+150')
    app.title('PERSONALIZAÇÃO DA TEMPORADA')

    # Formato temp
    lst_formato = ["Lip Sync Assassin", "Lip Sync For Your Legacy", "Lip Sync For Your Life", "No-Elimination", ""]

    lbl_formato = Label(app, text='Formato da Competição: ', anchor=S, font=fonte_padrao)
    lbl_formato.place(x=125, y=90, width=325, height=30)

    combo_formato = ttk.Combobox(app, values=lst_formato, state='readonly')
    combo_formato.current(4)
    combo_formato.place(x=450, y=90, width=240, height=30)
    combo_formato.bind('<<ComboboxSelected>>', design_formato)
    combo_formato.config(state=DISABLED)

    # Semi-final
    lst_semi = ["Rumix",
                "Rumix Sem Eliminação",
                "Outro Desafio",
                "Outro Desafio Sem Eliminação",
                ""]

    lbl_semi = Label(app, text='Formato da Semi Final: ', anchor=S, font=fonte_padrao)
    lbl_semi.place(x=130, y=190, width=325, height=30)

    combo_semi = ttk.Combobox(app, values=lst_semi, state='readonly')
    combo_semi.current(4)
    combo_semi.place(x=450, y=190, width=240, height=30)
    combo_semi.bind('<<ComboboxSelected>>', design_semi)
    combo_semi.config(state=DISABLED)

    # Finale
    lst_finale = ["Lip Sync SmackDown",
                  "TOP3 Performances",
                  "TOP3 Rumix/Lip Sync for the Crown",
                  "TOP3 Rumix(Ru Chops Someone)LSFTC",
                  "TOP4 Rumix(Ru Chops Someone)LSFTC",
                  "TOP4 Rumix/Individual Lip-Syncs",
                  "TOP5 Performances/Top2 LSFTC", ""]

    lbl_formafi = Label(app, text='Formato da Final: ', anchor=S, font=fonte_padrao)
    lbl_formafi.place(x=160, y=240, width=325, height=30)

    combo_formafi = ttk.Combobox(app, values=lst_finale, state='readonly')
    combo_formafi.current(7)
    combo_formafi.place(x=450, y=240, width=240, height=30)
    combo_formafi.bind('<<ComboboxSelected>>', design_final)
    combo_formafi.config(state=DISABLED)

    # premiere
    lst_premiere = ["1 Episode Elimination ",
                    "1 Episode No-Elimination",
                    "2 Episodes Fashion Design/Elimination",
                    "2 Episodes Girl Group/No-Elimination",
                    "2 Episodes Talent Show/No-Elimination",
                    "3 Episodes Lip-Syncs/Girl Group/No-Elimination", ""]

    lbl_premiere = Label(app, text='Formato da Premiere: ', anchor=S, font=fonte_padrao)
    lbl_premiere.place(x=138, y=140, width=325, height=30)

    combo_premiere = ttk.Combobox(app, values=lst_premiere, state='readonly')
    combo_premiere.current(6)
    combo_premiere.place(x=450, y=140, width=240, height=30)
    combo_premiere.bind('<<ComboboxSelected>>', design_premiere)
    combo_premiere.config(state=DISABLED)

    # Double Shantay
    lst_shantay = ["Sim", "Não",
                   "Surpresa", " "]

    lbl_shantay = Label(app, text='Double-Shantay: ', anchor=S, font=fonte_padrao)
    lbl_shantay.place(x=165, y=290, width=325, height=30)

    combo_shantay = ttk.Combobox(app, values=lst_shantay, state='readonly')
    combo_shantay.place(x=450, y=290, width=240, height=30)
    combo_shantay.bind('<<ComboboxSelected>>', design_shantay)
    combo_shantay.config(state=DISABLED)
    combo_shantay.current(3)

    # Double Elimination
    lst_elim =["Sim", "Não",
                   "Surpresa", " "]

    lbl_elim = Label(app, text='Double-Elimination: ', anchor=S, font=fonte_padrao)
    lbl_elim.place(x=146, y=340, width=325, height=30)

    combo_elim = ttk.Combobox(app, values=lst_elim, state='readonly')
    combo_elim.current(3)
    combo_elim.place(x=450, y=340, width=240, height=30)
    combo_elim.bind('<<ComboboxSelected>>', design_elim)
    combo_elim.config(state=DISABLED)

    # Participantes

    button_queen = font.Font(family='Cooper Black', size=14, weight='bold')
    button_queen = tkinter.Button(app, text="Queens", font=fonte_padrao, command=remove_all2)
    button_queen.place(x=380, y=20)

    # Desafios

    button_desaf = font.Font(family='Cooper Black', size=14, weight='bold')
    button_desaf = tkinter.Button(app, text="Desafios", font=fonte_padrao, command=remove_all0)
    button_desaf.place(x=375, y=405)
    button_desaf.config(state=DISABLED)


# combobox
def criando_combo():
    global combo_temp
    global lb_temp
    global button_verif
    global button_apagar
    global button_sair

    combo_temp = ttk.Combobox(app, values=lst_seasons, state='readonly')  # creating a combobox
    combo_temp.current(0)
    combo_temp.place(x=285, y=10, width=200, height=30)  # colocando na tela
    combo_temp.bind('<<ComboboxSelected>>', select)

    lb_temp = tk.Label(app, text='Escolha uma temporada: ', font=fonte_padrao)
    lb_temp.grid(row=0, column=1, padx=10, pady=10)

    button_verif = tkinter.Button(app, text="Verificar Escolhas", font=fonte_padrao, command=verificar_escolhas)
    button_verif.place(x=680, y=10, width=215, height=30)

    button_apagar = tkinter.Button(app, text="Deletar Escolhas", font=fonte_padrao, command=reorganizar_id)
    button_apagar.place(x=10, y=640, width=200, height=30)
    button_apagar.config(state=DISABLED)

    button_sair = tkinter.Button(app, text="SALVAR e SAIR", font=fonte_padrao2, command=remove_all3)
    button_sair.place(x=690, y=640, width=200, height=30)

    messagebox.showinfo("Alerta!", "Escolha no mínimo 8 participante e no máximo 16.")


def select(event):  # the function to get triggered each time you choose something
    if combo_temp.get() == lst_seasons[0]:  # if it is the first item
        global tb_temporada
        tb_temporada = 'drus_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), ocultar_but()
    elif combo_temp.get() == lst_seasons[1]:
        tb_temporada = 'drus_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[2]:
        tb_temporada = 'drus_s03'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), ocultar_but()
    elif combo_temp.get() == lst_seasons[3]:
        tb_temporada = 'drus_s04'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), ocultar_but()
    elif combo_temp.get() == lst_seasons[4]:
        tb_temporada = 'drus_s05'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        ocultar_but()
    elif combo_temp.get() == lst_seasons[5]:
        tb_temporada = 'drus_s06'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        ocultar_but()
    elif combo_temp.get() == lst_seasons[9]:
        tb_temporada = 'drus_s10'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        ocultar_but()
    elif combo_temp.get() == lst_seasons[10]:
        tb_temporada = 'drus_s11'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        show_data15(), ocultar_but()
    elif combo_temp.get() == lst_seasons[11]:
        tb_temporada = 'drus_s12'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), ocultar_but()
    elif combo_temp.get() == lst_seasons[12]:
        tb_temporada = 'drus_s13'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), ocultar_but()
    elif combo_temp.get() == lst_seasons[13]:
        tb_temporada = 'drus_s14'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        ocultar_but()
    elif combo_temp.get() == lst_seasons[14]:
        tb_temporada = 'usas_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[15]:
        tb_temporada = 'usas_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[16]:
        tb_temporada = 'usas_s03'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[17]:
        tb_temporada = 'usas_s04'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[18]:
        tb_temporada = 'usas_s05'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[19]:
        tb_temporada = 'usas_s06'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), ocultar_but()
    elif combo_temp.get() == lst_seasons[21]:
        tb_temporada = 'drth_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[24]:
        tb_temporada = 'druk_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[25]:
        tb_temporada = 'druk_s03'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[26]:
        tb_temporada = 'druk_s04'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[27]:
        tb_temporada = 'cdr_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[28]:
        tb_temporada = 'cdr_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[29]:
        tb_temporada = 'cdr_s03'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[31]:
        tb_temporada = 'drhl_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[32]:
        tb_temporada = 'drdw_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[33]:
        tb_temporada = 'drdw_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[34]:
        tb_temporada = 'dre_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[35]:
        tb_temporada = 'dre_s02'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[38]:
        tb_temporada = 'drfr_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), ocultar_but()
    elif combo_temp.get() == lst_seasons[39]:
        tb_temporada = 'drph_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), ocultar_but()
    elif combo_temp.get() == lst_seasons[40]:
        tb_temporada = 'ukvstw_s01'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), ocultar_but()


app = Tk()
app.title('DRAG RACE - UNAUTHORIZED SIMULATOR')
app.geometry('820x480+265+125')  # a,b,c,d altura, largura e os outros dois são a posição que vai aparecer na tela
app.resizable(False, False)

fonte_padrao = font.Font(family='Cooper Black', size=14, weight='bold')
fonte_padrao2 = font.Font(family='Cooper Black', size=12)
fonte_padrao3 = font.Font(family='Cooper Black', size=14)
fonte_padrao4 = font.Font(family='Arial', size=12)

lst_seasons = ["RuPaul's Drag Race - Season 1", "RuPaul's Drag Race - Season 2", "RuPaul's Drag Race - Season 3",
               "RuPaul's Drag Race - Season 4", "RuPaul's Drag Race - Season 5", "RuPaul's Drag Race - Season 6",
               "RuPaul's Drag Race - Season 7", "RuPaul's Drag Race - Season 8", "RuPaul's Drag Race - Season 9",
               "RuPaul's Drag Race - Season 10", "RuPaul's Drag Race - Season 11", "RuPaul's Drag Race - Season 12",
               "RuPaul's Drag Race - Season 13", "RuPaul's Drag Race - Season 14", "RPDR All-Stars - Season 1",
               "RPDR All-Stars - Season 2", "RPDR All-Stars - Season 3", "RPDR All-Stars - Season 4",
               "RPDR All-Stars - Season 5", "RPDR All-Stars - Season 6",
               "RuPaul's Drag Race - All Winners", "Drag Race Thailand - Season 1", "Drag Race Thailand - Season 2",
               "RuPaul's Drag Race UK - Season 1", "RuPaul's Drag Race UK - Season 2",
               "RuPaul's Drag Race UK - Season 3", "RuPaul's Drag Race UK - Season 4",
               "Canada's Drag Race - Season 1", "Canada's Drag Race - Season 2", "Canada's Drag Race - Season 3",
               "Drag Race Holland - Season 1", "Drag Race Holland - Season 2",
               "Drag Race Down Under - Season 1", "Drag Race Down Under - Season 2",
               "Drag Race España - Season 1", "Drag Race España - Season 2",
               "Drag Race Italia - Season 1", "Drag Race Italia - Season 2",
               "Drag Race France - Season 1",
               "Drag Race Philippines - Season 1",
               "UK. vs The World - Season 1", "Canada vs The World - Season 1", " "]

lst_desafios = [" ", "Atuação", "Baile", "Campanha Presidencial", "Canto", "Comercial", "Concurso de Beleza",
                "Dança Burlesca com Auditório", "Dança Coreografada", "Desing de Moda",
                "Discurso de Formatura", "DragLympics",
                "Entrega de Prêmios (Awards)", "Girl Group", "Lip Sync LaLaPaRuza Smackdown", "Make-Over",
                "Painel de Discussão (DragCon)", "Pegadinhas Improvisadas", "Programa de TV (ao-vivo)",
                "Projetar e Apresentar Evento", "Roast",
                "Rumix", "Runway", "Rusical",
                "Show de Talentos", "Snatch Game", "Snatch Game of Love", "Stand-Up"]
lst_escolhas = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
lst_acumulada = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []
lst10 = []
lst11 = []
lst12 = []
lst13 = []
lst14 = []
lst15 = []
lst16 = []

cunt1 = cunt2 = cunt3 = cunt4 = str()
vant1 = vant2 = vant3 = vant4 = str()
check_acumulada = 0
check_acumulada2 = 0

# colocando a logo
img1 = ImageTk.PhotoImage(Image.open("RPDRLogo.png"))
frame = Frame(app)

frame.pack()
frame.place(anchor='center', relx=0.48, rely=0.28)
labelImg1 = Label(frame, image=img1, borderwidth=0)
labelImg1.pack()

# colocando o "simulator"
img2 = ImageTk.PhotoImage(Image.open("unofsimu.png"))
frame = Frame(app)

frame.pack()
frame.place(anchor='center', relx=0.49, rely=0.56)
labelImg2 = Label(frame, image=img2, borderwidth=0)
labelImg2.pack()

# conexão
my_conn = create_engine("sqlite:///C:\\Users\\faust\\PycharmProjects\\drag_race_simulator\\dr_db.db")

# rodapé
rodape = Label(app, text='@ Criado e desenvolvido por Antonio Faustino', foreground='#000', anchor=S)
rodape.place(x=5, y=460, width=250, height=20)

# botão iniciar
buttonFont = font.Font(family='Cooper Black', size=14, weight='bold')
button_inic = tkinter.Button(app, text="INICIAR", font=fonte_padrao, command=remove_all)
button_inic.place(relx=0.43, rely=0.63)

# botão para testes
button_testes = font.Font(family='Cooper Black', size=14, weight='bold')
button_testes = tkinter.Button(app, text="teste", font=fonte_padrao, command=testar)

#DELETANDO UNNOFICIAL SEASON E ELIMINATES_ QUEENS
conn = sqlite3.connect('dr_db.db')
c = conn.cursor()

# delete all rows from table
c.execute('DELETE FROM eliminated_queens;',);
c.execute('DELETE FROM unofficial_season;',);

conn.commit()

conn.close()


##AQUI SEGUEM OS DEFS EXCLUSIVOS DO CHOOSING QUEENS
def id1():
    if tb_temporada != "unofficial_season":
        if var1.get():
            global ctd_id
            global verificador
            ctd_id = "1"
            c1.config(state=DISABLED)
        inserir()

    else:
        ctd_id = "1"
        deletar()


def id2():
    if tb_temporada != "unofficial_season":
        if var2.get():
            global ctd_id
            ctd_id = "2"
            c2.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "2"
        deletar()


def id3():
    if tb_temporada != "unofficial_season":
        if var3.get():
            global ctd_id
            ctd_id = "3"
            c3.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "3"
        deletar()


def id4():
    if tb_temporada != "unofficial_season":
        if var4.get():
            global ctd_id
            ctd_id = "4"
            c4.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "4"
        deletar()


def id5():
    if tb_temporada != "unofficial_season":
        if var5.get():
            global ctd_id
            ctd_id = "5"
            c5.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "5"
        deletar()


def id6():
    if tb_temporada != "unofficial_season":
        if var6.get():
            global ctd_id
            ctd_id = "6"
            c6.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "6"
        deletar()


def id7():
    if tb_temporada != "unofficial_season":
        if var7.get():
            global ctd_id
            ctd_id = "7"
            c7.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "7"
        deletar()


def id8():
    if tb_temporada != "unofficial_season":
        if var8.get():
            global ctd_id
            ctd_id = "8"
            c8.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "8"
        deletar()


def id9():
    if tb_temporada != "unofficial_season":
        if var9.get():
            global ctd_id
            ctd_id = "9"
            c9.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "9"
        deletar()


def id10():
    if tb_temporada != "unofficial_season":
        if var10.get():
            global ctd_id
            ctd_id = "10"
            c10.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "10"
        deletar()


def id11():
    if tb_temporada != "unofficial_season":
        if var11.get():
            global ctd_id
            ctd_id = "11"
            c11.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "11"
        deletar()


def id12():
    if tb_temporada != "unofficial_season":
        if var12.get():
            global ctd_id
            ctd_id = "12"
            c12.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "12"
        deletar()


def id13():
    if tb_temporada != "unofficial_season":
        if var13.get():
            global ctd_id
            ctd_id = "13"
            c13.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "13"
        deletar()


def id14():
    if tb_temporada != "unofficial_season":
        if var14.get():
            global ctd_id
            ctd_id = "14"
            c14.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "14"
        deletar()


def id15():
    if tb_temporada != "unofficial_season":
        if var15.get():
            global ctd_id
            ctd_id = "15"
            c15.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "15"
        deletar()


def id16():
    if tb_temporada != "unofficial_season":
        if var16.get():
            global ctd_id
            ctd_id = "16"
            c16.config(state=DISABLED)
        inserir()
    else:
        ctd_id = "16"
        deletar()


def inserir():
    try:
        sqliteconnection = sqlite3.connect('dr_db.db')
        cursor = sqliteconnection.cursor()

        sqlite_insert_query = """insert into unofficial_season (PHOTO, NAME_QUEENS, CHARISMA, UNIQUENESS, NERVE, TALENT,
        ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV, MAQUIAG, MODA, PERFORM, LP, 
        FAVORITA, JUSTICA, NADA) 
        select PHOTO, NAME_QUEENS, CHARISMA, UNIQUENESS, NERVE, TALENT, ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV,
        MAQUIAG, MODA, PERFORM, LP, FAVORITA, JUSTICA, NADA from """ + tb_temporada + """
        where ID_QUEENS=""" + ctd_id + """"""

        cursor.execute(sqlite_insert_query)
        sqliteconnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteconnection:
            sqliteconnection.close()


def deletar():
    try:
        sqliteconnection = sqlite3.connect('dr_db.db')
        cursor = sqliteconnection.cursor()

        sqlite_insert_query = "delete from unofficial_season where ID_QUEENS = '" + ctd_id + "'"

        cursor.execute(sqlite_insert_query)
        sqliteconnection.commit()
        print("Record deleted successfully from SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data into sqlite table", error)
    finally:
        if sqliteconnection:
            sqliteconnection.close()


def reorganizar_id():
    qcheck = "SELECT ID_QUEENS FROM unofficial_season "
    bsc_qcheck = consulta(vcon, qcheck)

    my_conn = lite.connect('dr_db.db')
    new_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    ctd_alter = 0
    for values in bsc_qcheck:
        with my_conn:
            cur = my_conn.cursor()
            old_value = str(values)[1:-2]
            cur.execute("UPDATE unofficial_season SET ID_QUEENS = '" + new_values[
                ctd_alter] + "' WHERE ID_QUEENS = '" + old_value + "'")
            ctd_alter += 1

    # parte que limpa e reimprime depois de reorganizar
    clear_cb(), limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), \
    show_data6(), show_data7(), show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), \
    show_data14(), show_data15(), show_data16()


def checkbox():
    global c1, var1
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=1"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var1 = tk.IntVar()
    c1 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var1, onvalue=1, offvalue=0, command=id1)
    c1.place(x=0, y=215)


def checkbox2():
    global c2, var2
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=2"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var2 = tk.IntVar()
    c2 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var2, onvalue=1, offvalue=0, command=id2)
    c2.place(x=150, y=215)


def checkbox3():
    global c3, var3
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=3"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var3 = tk.IntVar()
    c3 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var3, onvalue=1, offvalue=0, command=id3)
    c3.place(x=300, y=215)


def checkbox4():
    global c4, var4
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=4"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var4 = tk.IntVar()
    c4 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var4, onvalue=1, offvalue=0, command=id4)
    c4.place(x=450, y=215)


def checkbox5():
    global c5, var5
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=5"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var5 = tk.IntVar()
    c5 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var5, onvalue=1, offvalue=0, command=id5)
    c5.place(x=600, y=215)


def checkbox6():
    global c6, var6
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=6"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var6 = tk.IntVar()
    c6 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var6, onvalue=1, offvalue=0, command=id6)
    c6.place(x=750, y=215)


def checkbox7():
    global c7, var7
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=7"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var7 = tk.IntVar()
    c7 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var7, onvalue=1, offvalue=0, command=id7)
    c7.place(x=0, y=405)


def checkbox8():
    global c8, var8
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=8"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var8 = tk.IntVar()
    c8 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var8, onvalue=1, offvalue=0, command=id8)
    c8.place(x=150, y=405)


def checkbox9():
    global c9, var9
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=9"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var9 = tk.IntVar()
    c9 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var9, onvalue=1, offvalue=0, command=id9)
    c9.place(x=300, y=405)


def checkbox10():
    global c10, var10
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=10"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var10 = tk.IntVar()
    c10 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var10, onvalue=1, offvalue=0, command=id10)
    c10.place(x=450, y=405)


def checkbox11():
    global c11, var11
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=11"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var11 = tk.IntVar()
    c11 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var11, onvalue=1, offvalue=0, command=id11)
    c11.place(x=600, y=405)


def checkbox12():
    global c12, var12
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=12"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var12 = tk.IntVar()
    c12 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var12, onvalue=1, offvalue=0, command=id12)
    c12.place(x=750, y=405)


def checkbox13():
    global c13, var13
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=13"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var13 = tk.IntVar()
    c13 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var13, onvalue=1, offvalue=0, command=id13)
    c13.place(x=0, y=595)


def checkbox14():
    global c14, var14
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=14"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var14 = tk.IntVar()
    c14 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var14, onvalue=1, offvalue=0, command=id14)
    c14.place(x=150, y=595)


def checkbox15():
    global c15, var15
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=15"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var15 = tk.IntVar()
    c15 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var15, onvalue=1, offvalue=0, command=id15)
    c15.place(x=300, y=595)


def checkbox16():
    global c16, var16
    qcheck = "SELECT NAME_QUEENS FROM '" + tb_temporada + "' WHERE ID_QUEENS=16"
    bsc_qcheck = consulta(vcon, qcheck)
    bsc_qcheck2 = json.dumps(bsc_qcheck)
    bsc_qcheck3 = bsc_qcheck2.replace("[", "").replace("]", "").replace('"', "")

    var16 = tk.IntVar()
    c16 = tk.Checkbutton(app, text=bsc_qcheck3, variable=var16, onvalue=1, offvalue=0, command=id16)
    c16.place(x=450, y=595)


# _____________ SHOW DATAS_____________
def show_data():
    global l1
    l1 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img  # Image variable to display
    my_data = 1  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img = ImageTk.PhotoImage(data=r_set[0])  # create image
        l1.config(image=img)  # display image
        l1.place(x=0, y=60)
        checkbox()


def show_data2():
    global l2
    l2 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img2  # Image variable to display
    my_data = 2  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img2 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l2.config(image=img2)  # display image
        l2.place(x=150, y=60)
        checkbox2()


def show_data3():
    global l3
    l3 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img3  # Image variable to display
    my_data = 3  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img3 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l3.config(image=img3)  # display image
        l3.place(x=300, y=60)
        checkbox3()


def show_data4():
    global l4
    l4 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img4  # Image variable to display
    my_data = 4  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img4 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l4.config(image=img4)  # display image
        l4.place(x=450, y=60)
        checkbox4()


def show_data5():
    global l5
    l5 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img5  # Image variable to display
    my_data = 5  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img5 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l5.config(image=img5)  # display image
        l5.place(x=600, y=60)
        checkbox5()


def show_data6():
    global l6
    l6 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img6  # Image variable to display
    my_data = 6  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img6 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l6.config(image=img6)  # display image
        l6.place(x=750, y=60)
        checkbox6()


def show_data7():
    global l7
    l7 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img7  # Image variable to display
    my_data = 7  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img7 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l7.config(image=img7)  # display image
        l7.place(x=0, y=250)
        checkbox7()


def show_data8():
    global l8
    l8 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img8  # Image variable to display
    my_data = 8  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img8 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l8.config(image=img8)  # display image
        l8.place(x=150, y=250)
        checkbox8()


def show_data9():
    global l9
    l9 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img9  # Image variable to display
    my_data = 9  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img9 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l9.config(image=img9)  # display image
        l9.place(x=300, y=250)
        checkbox9()


def show_data10():
    global l10
    l10 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img10  # Image variable to display
    my_data = 10  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img10 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l10.config(image=img10)  # display image
        l10.place(x=450, y=250)
        checkbox10()


def show_data11():
    global l11
    l11 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img11  # Image variable to display
    my_data = 11  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img11 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l11.config(image=img11)  # display image
        l11.place(x=600, y=250)
        checkbox11()


def show_data12():
    global l12
    l12 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img12  # Image variable to display
    my_data = 12  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img12 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l12.config(image=img12)  # display image
        l12.place(x=750, y=250)
        checkbox12()


def show_data13():
    global l13
    l13 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img13  # Image variable to display
    my_data = 13  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img13 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l13.config(image=img13)  # display image
        l13.place(x=0, y=440)
        checkbox13()


def show_data14():
    global l14
    l14 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img14  # Image variable to display
    my_data = 14  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img14 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l14.config(image=img14)  # display image
        l14.place(x=150, y=440)
        checkbox14()


def show_data15():
    global l15
    l15 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img15  # Image variable to display
    my_data = 15  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img15 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l15.config(image=img15)  # display image
        l15.place(x=300, y=440)
        checkbox15()


def show_data16():
    global l16
    l16 = tk.Label(app)
    q = "SELECT PHOTO FROM '" + tb_temporada + "' WHERE ID_QUEENS=?"
    global img16  # Image variable to display
    my_data = 16  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        img16 = ImageTk.PhotoImage(data=r_set[0])  # create image
        l16.config(image=img16)  # display image
        l16.place(x=450, y=440)
        checkbox16()


# _____________ SHOW DATAS_____________


def limpar():
    if 'l1' and 'c1' in globals():
        l1.destroy()
        c1.destroy()
    if 'l2' and 'c2' in globals():
        l2.destroy()
        c2.destroy()
    if 'l3' and 'c3' in globals():
        l3.destroy()
        c3.destroy()
    if 'l4' and 'c4' in globals():
        l4.destroy()
        c4.destroy()
    if 'l5' and 'c5' in globals():
        l5.destroy()
        c5.destroy()
    if 'l6' and 'c6' in globals():
        l6.destroy()
        c6.destroy()
    if 'l7' and 'c7' in globals():
        l7.destroy()
        c7.destroy()
    if 'l8' and 'c8' in globals():
        l8.destroy()
        c8.destroy()
    if 'l9' and 'c9' in globals():
        l9.destroy()
        c9.destroy()
    if 'l10' and 'c10' in globals():
        l10.destroy()
        c10.destroy()
    if 'l11' and 'c11' in globals():
        l11.destroy()
        c11.destroy()
    if 'l12' and 'c12' in globals():
        l12.destroy()
        c12.destroy()
    if 'l13' and 'c13' in globals():
        l13.destroy()
        c13.destroy()
    if 'l14' and 'c14' in globals():
        l14.destroy()
        c14.destroy()
    if 'l15' and 'c15' in globals():
        l15.destroy()
        c15.destroy()
    if 'l16' and 'c16' in globals():
        l16.destroy()
        c16.destroy()


def clear_cb():
    combo_temp.set('')


def verificar_escolhas():
    global tb_temporada

    tb_temporada = 'unofficial_season'
    but_apagar(), clear_cb(), limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(),
    show_data6(), show_data7(), show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(),
    show_data14(), show_data15(), show_data16()


def but_apagar():
    button_apagar.config(state=NORMAL)


def ocultar_but():
    button_apagar.config(state=DISABLED)


def remove_all3():
    cont = "SELECT ID_QUEENS FROM unofficial_season "
    bsc_cont = consulta(vcon, cont)

    if len(bsc_cont) < 8:
        messagebox.showerror("Quantidade Insuficiente", "Escolha pelo menos 8 participantes.")
    elif len(bsc_cont) > 16:
        messagebox.showerror("Quantidade Excedente", "Escolha menos que 16 participantes.")
    else:
        combo_temp.destroy()
        lb_temp.destroy()
        button_verif.destroy()
        button_apagar.destroy()
        button_sair.destroy()
        limpar()
        personalizacao()
        combo_formato.config(state=NORMAL)
        combo_semi.config(state=NORMAL)
        combo_formafi.config(state=NORMAL)
        combo_premiere.config(state=NORMAL)
        combo_shantay.config(state=NORMAL)
        combo_elim.config(state=NORMAL)


# --------------------------------- DESING DO FORMATO --------------------------------------


def design_formato(event):
    global chave_formato
    if combo_formato.get() == lst_formato[1]: #lip sync for your legacy
        chave_formato = 1
        print(chave_formato) #loló apagar
    elif combo_formato.get() == lst_formato[2]: #lip sync for your life
        chave_formato = 2
        print(chave_formato) #loló apagar


def design_premiere(event):
    global chave_premiere
    if combo_premiere.get() == lst_premiere[0]:
        chave_premiere = 0
        print(chave_premiere)
    elif combo_premiere.get() == lst_premiere[1]:
        chave_premiere = 1
        print(chave_premiere)
    elif combo_premiere.get() == lst_premiere[2]:
        chave_premiere = 2
        print(chave_premiere)
    elif combo_premiere.get() == lst_premiere[3]:
        chave_premiere = 3
        print(chave_premiere)
    elif combo_premiere.get() == lst_premiere[4]:
        chave_premiere = 4
        print(chave_premiere)
    elif combo_premiere.get() == lst_premiere[5]:
        chave_premiere = 5
        print(chave_premiere)
    else:
        chave_premiere = 999


def design_final(event):
    global chave_finale
    if combo_formafi.get() == lst_finale[0]:
        chave_finale = 0
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[1]:
        chave_finale = 1
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[2]:
        chave_finale = 2
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[3]:
        chave_finale = 3
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[4]:
        chave_finale = 4
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[5]:
        chave_finale = 5
        print(chave_finale)
    elif combo_formafi.get() == lst_finale[6]:
        chave_finale = 6
        print(chave_finale)
    else:
        chave_finale = 999


def design_elim(event):
    global chave_elim
    if (combo_elim.get()) and (combo_formato.get()) and (combo_premiere.get()) \
            and (combo_formafi.get()) and (combo_shantay.get()) and (combo_semi.get()):
        button_desaf.config(state=NORMAL) #bloqueia o botão desafios
    else:
        print()
    if combo_elim.get() == lst_elim[0]: #sim
        chave_elim = 0
        print(chave_elim)
    elif combo_elim.get() == lst_elim[2]: #surpresa
        chave_elim = 2
        print(chave_elim)
    elif combo_elim.get() == lst_elim[1]: #nao
        chave_elim = 1
        print(chave_elim)
    else:
        chave_elim = 999


def design_shantay(event):
    global chave_shantay
    if combo_shantay.get() == lst_shantay[0]:  # add 1
        chave_shantay = 0
        print(chave_shantay)
    elif combo_shantay.get() == lst_shantay[2]:  # surpresa
        chave_shantay = 2
        print(chave_shantay)
    else:
        chave_shantay = 999


def design_semi(event):
    global chave_semi
    if combo_semi.get() == lst_semi[1]:  # add 1
        chave_semi = 1
        print(chave_semi)
    elif combo_semi.get() == lst_semi[0]:  # add 0
        chave_semi = 0
        print(chave_semi)
    elif combo_semi.get() == lst_semi[2]:  # add 0
        chave_semi = 2
        print(chave_semi)
    elif combo_semi.get() == lst_semi[3]:  # add 0
        chave_semi = 3
        print(chave_semi)
    else:
        chave_shantay = 999


def double_shantay():
    global dbshantay

    if (chave_shantay == 0) or (randsh == 1):
        dbshantay = randint(2, num_ep)
        if dbshantay == num_ep:
            dbshantay -= 1 #n deixo a db cair na semi final
        if (dbshantay == 2) or (dbshantay == 3) or (dbshantay == 4):
            dbshantay = 5
        print('') #lolo apagar
        print(f'double shantay vai ser no episódio: {dbshantay - 1}')


# --------------------------------- DESING DE DESAFIOS -------------------------------------


def escolha_desaf():
    app.geometry('755x530+265+125')
    global combo_ep1
    global lbl_ep1
    global combo_ep2
    global lbl_ep2
    global combo_ep3
    global lbl_ep3
    global combo_ep4
    global lbl_ep4
    global combo_ep5
    global lbl_ep5
    global combo_ep6
    global lbl_ep6
    global combo_ep7
    global lbl_ep7
    global combo_ep8
    global lbl_ep8
    global combo_ep9
    global lbl_ep9
    global combo_ep10
    global lbl_ep10
    global combo_ep11
    global lbl_ep11
    global combo_ep12
    global lbl_ep12
    global combo_ep13
    global lbl_ep13
    global combo_ep14
    global lbl_ep14
    global combo_ep15
    global lbl_ep15
    global combo_ep16
    global lbl_ep16
    global combo_ep17
    global lbl_ep17
    global combo_ep18
    global lbl_ep18
    global combo_ep19
    global lbl_ep19
    global but_voltd
    global num_ep
    global button_avan
    global randsh

    # COMBOS DOS DESAFIOS
    combo_ep1 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep1.current(0)
    combo_ep1.place(x=150, y=30, width=190, height=30)  # colocando na tela
    combo_ep1.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep1 = tk.Label(app, text='Episódio 1: ', font=fonte_padrao)
    lbl_ep1.place(x=10, y=30)

    combo_ep2 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep2.current(0)
    combo_ep2.place(x=150, y=80, width=190, height=30)  # colocando na tela
    combo_ep2.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep2 = tk.Label(app, text='Episódio 2: ', font=fonte_padrao)
    lbl_ep2.place(x=10, y=80)

    combo_ep3 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep3.current(0)
    combo_ep3.place(x=150, y=130, width=190, height=30)  # colocando na tela
    combo_ep3.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep3 = tk.Label(app, text='Episódio 3: ', font=fonte_padrao)
    lbl_ep3.place(x=10, y=130)

    combo_ep4 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep4.current(0)
    combo_ep4.place(x=150, y=180, width=190, height=30)  # colocando na tela
    combo_ep4.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep4 = tk.Label(app, text='Episódio 4: ', font=fonte_padrao)
    lbl_ep4.place(x=10, y=180)

    combo_ep5 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep5.current(0)
    combo_ep5.place(x=150, y=230, width=190, height=30)  # colocando na tela
    combo_ep5.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep5 = tk.Label(app, text='Episódio 5: ', font=fonte_padrao)
    lbl_ep5.place(x=10, y=230)

    combo_ep6 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep6.current(0)
    combo_ep6.place(x=150, y=280, width=190, height=30)  # colocando na tela
    combo_ep6.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep6 = tk.Label(app, text='Episódio 6: ', font=fonte_padrao)
    lbl_ep6.place(x=10, y=280)

    combo_ep7 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep7.current(0)
    combo_ep7.place(x=150, y=330, width=190, height=30)  # colocando na tela
    combo_ep7.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep7 = tk.Label(app, text='Episódio 7: ', font=fonte_padrao)
    lbl_ep7.place(x=10, y=330)

    combo_ep8 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep8.current(0)
    combo_ep8.place(x=150, y=380, width=190, height=30)  # colocando na tela
    combo_ep8.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep8 = tk.Label(app, text='Episódio 8: ', font=fonte_padrao)
    lbl_ep8.place(x=10, y=380)

    combo_ep9 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep9.current(0)
    combo_ep9.place(x=150, y=430, width=190, height=30)  # colocando na tela
    combo_ep9.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep9 = tk.Label(app, text='Episódio 9: ', font=fonte_padrao)
    lbl_ep9.place(x=10, y=430)

    combo_ep10 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep10.current(0)
    combo_ep10.place(x=150, y=480, width=190, height=30)  # colocando na tela
    combo_ep10.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep10 = tk.Label(app, text='Episódio 10: ', font=fonte_padrao)
    lbl_ep10.place(x=10, y=480)

    combo_ep11 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep11.current(0)
    combo_ep11.place(x=525, y=30, width=190, height=30)  # colocando na tela
    combo_ep11.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep11 = tk.Label(app, text='Episódio 11: ', font=fonte_padrao)
    lbl_ep11.place(x=375, y=30)

    combo_ep12 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep12.current(0)
    combo_ep12.place(x=525, y=80, width=190, height=30)  # colocando na tela
    combo_ep12.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep12 = tk.Label(app, text='Episódio 12: ', font=fonte_padrao)
    lbl_ep12.place(x=375, y=80)

    combo_ep13 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep13.current(0)
    combo_ep13.place(x=525, y=130, width=190, height=30)  # colocando na tela
    combo_ep13.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep13 = tk.Label(app, text='Episódio 13: ', font=fonte_padrao)
    lbl_ep13.place(x=375, y=130)

    combo_ep14 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep14.current(0)
    combo_ep14.place(x=525, y=180, width=190, height=30)  # colocando na tela
    combo_ep14.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep14 = tk.Label(app, text='Episódio 14: ', font=fonte_padrao)
    lbl_ep14.place(x=375, y=180)

    combo_ep15 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep15.current(0)
    combo_ep15.place(x=525, y=230, width=190, height=30)  # colocando na tela
    combo_ep15.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep15 = tk.Label(app, text='Episódio 15: ', font=fonte_padrao)
    lbl_ep15.place(x=375, y=230)

    combo_ep16 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep16.current(0)
    combo_ep16.place(x=525, y=280, width=190, height=30)  # colocando na tela
    combo_ep16.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep16 = tk.Label(app, text='Episódio 16: ', font=fonte_padrao)
    lbl_ep16.place(x=375, y=280)

    combo_ep17 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep17.current(0)
    combo_ep17.place(x=525, y=330, width=190, height=30)  # colocando na tela
    combo_ep17.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep17 = tk.Label(app, text='Episódio 17: ', font=fonte_padrao)
    lbl_ep17.place(x=375, y=330)

    combo_ep18 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep18.current(0)
    combo_ep18.place(x=525, y=380, width=190, height=30)  # colocando na tela
    combo_ep18.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep18 = tk.Label(app, text='Episódio 18: ', font=fonte_padrao)
    lbl_ep18.place(x=375, y=380)

    combo_ep19 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep19.current(0)
    combo_ep19.place(x=525, y=430, width=190, height=30)  # colocando na tela
    combo_ep19.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep19 = tk.Label(app, text='Episódio 19: ', font=fonte_padrao)
    lbl_ep19.place(x=375, y=430)

    # BOTÃO VOLTAR DESAFIOS
    # but_voltd = tkinter.Button(app, text="Voltar", font=fonte_padrao, command=remove_all4)
    # but_voltd.place(x=610, y=490)

    # BOTÃO AVANÇAR DESAFIOS
    button_avan = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=remove_all5)
    button_avan.place(x=545, y=475, width=190)

    # FIXANDO A PREMIERE
    if chave_premiere == 2:  # design com eliminação
        combo_ep1.current(9)
        combo_ep2.current(9)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[9]
        lst_escolhas[1] = lst_desafios[9]

    if chave_premiere == 3:  # girl group - no elim
        combo_ep1.current(13)
        combo_ep2.current(13)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[13]
        lst_escolhas[1] = lst_desafios[13]

    if chave_premiere == 4:  # show de talentos - no elim
        combo_ep1.current(24)
        combo_ep2.current(24)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[24]
        lst_escolhas[1] = lst_desafios[24]

    if chave_premiere == 5:  # premiere tripla - no elim
        combo_ep1.current(14)
        combo_ep2.current(24)
        combo_ep3.current(24)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        combo_ep3.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[14]
        lst_escolhas[1] = lst_desafios[24]
        lst_escolhas[2] = lst_desafios[24]

    # DEFININDO N# DE EPISÓDIOS
    check_queens = 'SELECT NAME_QUEENS from unofficial_season'
    total_queens = consulta(vcon, check_queens)

    # formato da final
    if (chave_finale == 0) or (chave_finale == 4) or (chave_finale == 5):  # ls smackdown
        num_ep = len(total_queens) - 4
    if (chave_finale == 1) or (chave_finale == 2) or (chave_finale == 3):
        num_ep = len(total_queens) - 3
    if chave_finale == 6:
        num_ep = len(total_queens) - 5

    # premiere
    if chave_premiere == 1:  # premiere qualquer - no elim
        num_ep += 1
    if chave_premiere == 3:  # girl group - no elim
        num_ep += 2
    if chave_premiere == 4:  # show de talentos - no elim
        num_ep += 2
    if chave_premiere == 5:  # premiere tripla
        num_ep += 3

    # double-shantay
    if chave_shantay == 0: #sim
        num_ep += 1
        double_shantay()

    if chave_shantay == 2: #surpresa
        randsh = randint(0, 1)
        num_ep += randsh
        if randsh == 1:
            print('Haverá double-shantay')
            double_shantay()
        else:
            print('Não haverá double-shantay')

    # double-elim
    if chave_elim == 0:
        num_ep -= 1
    if chave_elim == 2:
        randelim = randint(0, 1)
        num_ep -= randelim
        if randelim == 0:
            print('Não haverá double-elimination')
        else:
            print('Haverá double-eliminations')

    # semi-final
    if chave_semi == 1:
        num_ep += 1
    if chave_semi == 3:
        num_ep += 1

    print(f'Número de episódios será: {num_ep} + 1 da Final')

    # OCULTANDO COMBOS E LBLS
    # o menor numero possivel de episódios é 3 + F e o máximo 18 + F
    if num_ep == 4:
        combo_ep5.config(state=DISABLED)
        combo_ep6.config(state=DISABLED)
        combo_ep7.config(state=DISABLED)
        combo_ep8.config(state=DISABLED)
        combo_ep9.config(state=DISABLED)
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 5:
        combo_ep6.config(state=DISABLED)
        combo_ep7.config(state=DISABLED)
        combo_ep8.config(state=DISABLED)
        combo_ep9.config(state=DISABLED)
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 6:
        combo_ep7.config(state=DISABLED)
        combo_ep8.config(state=DISABLED)
        combo_ep9.config(state=DISABLED)
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 7:
        combo_ep8.config(state=DISABLED)
        combo_ep9.config(state=DISABLED)
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 8:
        combo_ep9.config(state=DISABLED)
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 9:
        combo_ep10.config(state=DISABLED)
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 10:
        combo_ep11.config(state=DISABLED)
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 11:
        combo_ep12.config(state=DISABLED)
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 12:
        combo_ep13.config(state=DISABLED)
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 13:
        combo_ep14.config(state=DISABLED)
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 14:
        combo_ep15.config(state=DISABLED)
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 15:
        combo_ep16.config(state=DISABLED)
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 16:
        combo_ep17.config(state=DISABLED)
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 17:
        combo_ep18.config(state=DISABLED)
        combo_ep19.config(state=DISABLED)
    elif num_ep == 18:
        combo_ep19.config(state=DISABLED)

    # gerador da semifinal e final
    if (chave_semi == 1) or (chave_semi == 0):  # verif isso do desaf sem nada
        if num_ep == 2:
            combo_ep2.current(21)
            combo_ep2.config(state=DISABLED)
            combo_ep3.set('GRAND FINALE')
            lst_escolhas[2] = 'GRAND FINALE'
        elif num_ep == 3:
            combo_ep3.current(21)
            combo_ep3.config(state=DISABLED)
            combo_ep4.set('GRAND FINALE')
            lst_escolhas[3] = 'GRAND FINALE'
        elif num_ep == 4:
            combo_ep4.current(21)
            combo_ep4.config(state=DISABLED)
            combo_ep5.set('GRAND FINALE')
            lst_escolhas[4] = 'GRAND FINALE'
        elif num_ep == 5:
            combo_ep5.current(21)
            combo_ep5.config(state=DISABLED)
            combo_ep6.set('GRAND FINALE')
            lst_escolhas[5] = 'GRAND FINALE'
        elif num_ep == 6:
            combo_ep6.current(21)
            combo_ep6.config(state=DISABLED)
            combo_ep7.set('GRAND FINALE')
            lst_escolhas[6] = 'GRAND FINALE'
        elif num_ep == 7:
            combo_ep7.current(21)
            combo_ep7.config(state=DISABLED)
            combo_ep8.set('GRAND FINALE')
            lst_escolhas[7] = 'GRAND FINALE'
        elif num_ep == 8:
            combo_ep8.current(21)
            combo_ep8.config(state=DISABLED)
            combo_ep9.set('GRAND FINALE')
            lst_escolhas[8] = 'GRAND FINALE'
        elif num_ep == 9:
            combo_ep9.current(21)
            combo_ep9.config(state=DISABLED)
            combo_ep10.set('GRAND FINALE')
            lst_escolhas[9] = 'GRAND FINALE'
        elif num_ep == 10:
            combo_ep10.current(21)
            combo_ep10.config(state=DISABLED)
            combo_ep11.set('GRAND FINALE')
            lst_escolhas[10] = 'GRAND FINALE'
        elif num_ep == 11:
            combo_ep11.current(21)
            combo_ep11.config(state=DISABLED)
            combo_ep12.set('GRAND FINALE')
            lst_escolhas[11] = 'GRAND FINALE'
        elif num_ep == 12:
            combo_ep12.current(21)
            combo_ep12.config(state=DISABLED)
            combo_ep13.set('GRAND FINALE')
            lst_escolhas[12] = 'GRAND FINALE'
        elif num_ep == 13:
            combo_ep13.current(21)
            combo_ep13.config(state=DISABLED)
            combo_ep14.set('GRAND FINALE')
            lst_escolhas[13] = 'GRAND FINALE'
        elif num_ep == 14:
            combo_ep14.current(21)
            combo_ep14.config(state=DISABLED)
            combo_ep15.set('GRAND FINALE')
            lst_escolhas[14] = 'GRAND FINALE'
        elif num_ep == 15:
            combo_ep15.current(21)
            combo_ep15.config(state=DISABLED)
            combo_ep16.set('GRAND FINALE')
            lst_escolhas[15] = 'GRAND FINALE'
        elif num_ep == 16:
            combo_ep16.current(21)
            combo_ep16.config(state=DISABLED)
            combo_ep17.set('GRAND FINALE')
            lst_escolhas[16] = 'GRAND FINALE'
        elif num_ep == 17:
            combo_ep17.current(21)
            combo_ep17.config(state=DISABLED)
            combo_ep18.set('GRAND FINALE')
            lst_escolhas[17] = 'GRAND FINALE'
        elif num_ep == 18:
            combo_ep18.current(21)
            combo_ep18.config(state=DISABLED)
            combo_ep19.set('GRAND FINALE')
            lst_escolhas[18] = 'GRAND FINALE'

    if (chave_semi == 3) or (chave_semi == 2):
        if num_ep == 2:
            combo_ep3.set('GRAND FINALE')
            combo_ep3.config(state=DISABLED)
            lst_escolhas[2] = 'GRAND FINALE'
        elif num_ep == 3:
            combo_ep4.set('GRAND FINALE')
            combo_ep4.config(state=DISABLED)
            lst_escolhas[3] = 'GRAND FINALE'
        elif num_ep == 4:
            combo_ep5.set('GRAND FINALE')
            combo_ep5.config(state=DISABLED)
            lst_escolhas[4] = 'GRAND FINALE'
        elif num_ep == 5:
            combo_ep6.set('GRAND FINALE')
            combo_ep6.config(state=DISABLED)
            lst_escolhas[5] = 'GRAND FINALE'
        elif num_ep == 6:
            combo_ep7.set('GRAND FINALE')
            combo_ep7.config(state=DISABLED)
            lst_escolhas[6] = 'GRAND FINALE'
        elif num_ep == 7:
            combo_ep8.set('GRAND FINALE')
            combo_ep8.config(state=DISABLED)
            lst_escolhas[7] = 'GRAND FINALE'
        elif num_ep == 8:
            combo_ep9.set('GRAND FINALE')
            combo_ep9.config(state=DISABLED)
            lst_escolhas[8] = 'GRAND FINALE'
        elif num_ep == 9:
            combo_ep10.set('GRAND FINALE')
            combo_ep10.config(state=DISABLED)
            lst_escolhas[9] = 'GRAND FINALE'
        elif num_ep == 10:
            combo_ep11.set('GRAND FINALE')
            combo_ep11.config(state=DISABLED)
            lst_escolhas[10] = 'GRAND FINALE'
        elif num_ep == 11:
            combo_ep12.set('GRAND FINALE')
            combo_ep12.config(state=DISABLED)
            lst_escolhas[11] = 'GRAND FINALE'
        elif num_ep == 12:
            combo_ep13.set('GRAND FINALE')
            combo_ep13.config(state=DISABLED)
            lst_escolhas[12] = 'GRAND FINALE'
        elif num_ep == 13:
            combo_ep14.set('GRAND FINALE')
            combo_ep14.config(state=DISABLED)
            lst_escolhas[13] = 'GRAND FINALE'
        elif num_ep == 14:
            combo_ep15.set('GRAND FINALE')
            combo_ep15.config(state=DISABLED)
            lst_escolhas[14] = 'GRAND FINALE'
        elif num_ep == 15:
            combo_ep16.set('GRAND FINALE')
            combo_ep16.config(state=DISABLED)
            lst_escolhas[15] = 'GRAND FINALE'
        elif num_ep == 16:
            combo_ep17.set('GRAND FINALE')
            combo_ep17.config(state=DISABLED)
            lst_escolhas[16] = 'GRAND FINALE'
        elif num_ep == 17:
            combo_ep18.set('GRAND FINALE')
            combo_ep18.config(state=DISABLED)
            lst_escolhas[17] = 'GRAND FINALE'
        elif num_ep == 18:
            combo_ep19.set('GRAND FINALE')
            combo_ep19.config(state=DISABLED)
            lst_escolhas[18] = 'GRAND FINALE'


def ordem_desaf(event):
    # SALVANDO OS DESAF NA LISTA
    for check in range(0, 27):
        if combo_ep1.get() == lst_desafios[check]:
            lst_escolhas[0] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep2.get() == lst_desafios[check]:
            lst_escolhas[1] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep3.get() == lst_desafios[check]:
            lst_escolhas[2] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep4.get() == lst_desafios[check]:
            lst_escolhas[3] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep5.get() == lst_desafios[check]:
            lst_escolhas[4] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep6.get() == lst_desafios[check]:
            lst_escolhas[5] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep7.get() == lst_desafios[check]:
            lst_escolhas[6] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep8.get() == lst_desafios[check]:
            lst_escolhas[7] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep9.get() == lst_desafios[check]:
            lst_escolhas[8] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep10.get() == lst_desafios[check]:
            lst_escolhas[9] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep11.get() == lst_desafios[check]:
            lst_escolhas[10] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep12.get() == lst_desafios[check]:
            lst_escolhas[11] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep13.get() == lst_desafios[check]:
            lst_escolhas[12] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep14.get() == lst_desafios[check]:
            lst_escolhas[13] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep15.get() == lst_desafios[check]:
            lst_escolhas[14] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep16.get() == lst_desafios[check]:
            lst_escolhas[15] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep17.get() == lst_desafios[check]:
            lst_escolhas[16] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep18.get() == lst_desafios[check]:
            lst_escolhas[17] = lst_desafios[check]

    for check in range(0, 27):
        if combo_ep19.get() == lst_desafios[check]:
            lst_escolhas[18] = lst_desafios[check]

    print(lst_escolhas)


def remove_all4():
    combo_ep1.destroy()
    lbl_ep1.destroy()
    combo_ep2.destroy()
    lbl_ep2.destroy()
    combo_ep3.destroy()
    lbl_ep3.destroy()
    combo_ep4.destroy()
    lbl_ep4.destroy()
    combo_ep5.destroy()
    lbl_ep5.destroy()
    combo_ep6.destroy()
    lbl_ep6.destroy()
    combo_ep7.destroy()
    lbl_ep7.destroy()
    combo_ep8.destroy()
    lbl_ep8.destroy()
    combo_ep9.destroy()
    lbl_ep9.destroy()
    combo_ep10.destroy()
    lbl_ep10.destroy()
    combo_ep11.destroy()
    lbl_ep11.destroy()
    combo_ep12.destroy()
    lbl_ep12.destroy()
    combo_ep13.destroy()
    lbl_ep13.destroy()
    combo_ep14.destroy()
    lbl_ep14.destroy()
    combo_ep15.destroy()
    lbl_ep15.destroy()
    combo_ep16.destroy()
    lbl_ep16.destroy()
    combo_ep17.destroy()
    lbl_ep17.destroy()
    combo_ep18.destroy()
    lbl_ep18.destroy()
    combo_ep19.destroy()
    lbl_ep19.destroy()
    but_voltd.destroy()
    personalizacao()


def remove_all5():
    global nep
    global button_avanep
    nep = 0

    combo_ep1.destroy()
    lbl_ep1.destroy()
    combo_ep2.destroy()
    lbl_ep2.destroy()
    combo_ep3.destroy()
    lbl_ep3.destroy()
    combo_ep4.destroy()
    lbl_ep4.destroy()
    combo_ep5.destroy()
    lbl_ep5.destroy()
    combo_ep6.destroy()
    lbl_ep6.destroy()
    combo_ep7.destroy()
    lbl_ep7.destroy()
    combo_ep8.destroy()
    lbl_ep8.destroy()
    combo_ep9.destroy()
    lbl_ep9.destroy()
    combo_ep10.destroy()
    lbl_ep10.destroy()
    combo_ep11.destroy()
    lbl_ep11.destroy()
    combo_ep12.destroy()
    lbl_ep12.destroy()
    combo_ep13.destroy()
    lbl_ep13.destroy()
    combo_ep14.destroy()
    lbl_ep14.destroy()
    combo_ep15.destroy()
    lbl_ep15.destroy()
    combo_ep16.destroy()
    lbl_ep16.destroy()
    combo_ep17.destroy()
    lbl_ep17.destroy()
    combo_ep18.destroy()
    lbl_ep18.destroy()
    combo_ep19.destroy()
    lbl_ep19.destroy()
    button_avan.destroy()

    app.title('DRAG RACE - UNAUTHORIZED SIMULATOR')
    # loló também verificar se soma aumenta ao passar dos episódios
    control = 0
    nep += 1
    avan_ep()

    # BOTÃO AVANÇAR ENTRE EPISÓDIOS
    button_avanep = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=avan_epX)
    button_avanep.place(x=545, y=475, width=190)
    button_avanep.config(state=DISABLED)


def soma_cunt():
    global sumCUNT
    global resultado_final
    global lst_resultados
    lst_resultados = []

    sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
    bscName = consulta(vcon, sqlNAME)

    for check in range(1, len(bscName) + 1):
        checkstr = str(check)

        sqlCUNT = """SELECT 
                       """ + cunt1 + """, 
                       """ + cunt2 + """, 
                       """ + cunt3 + """, 
                       """ + cunt4 + """,
                       """ + vant1 + """, 
                       """ + vant2 + """, 
                       """ + vant3 + """, 
                       """ + vant4 + """
                       FROM unofficial_season 
                       WHERE ID_QUEENS= """ + checkstr + """ """
        bscCUNT = consulta(vcon, sqlCUNT)
        sumCUNT = sum(list(map(sum, list(bscCUNT))))  # soma os valores

        dado1 = randint(0, 6)
        dado2 = randint(0, 6)
        dado = dado1 + dado2

        resultado_final = sumCUNT + dado

        lst_resultados.append(resultado_final)

        # apagar depois loló
        print(f'O C.U.N.T. de {bscName[check - 1]} é {bscCUNT}')
        print("e a soma destes valores é: " + str(sumCUNT))
        print(f'O valor aleatorio foi {dado}')
        print(f'O resultado final desta pariticipante é {resultado_final}')
        print(f'Esta é a queen de número {check}')
        # apagar até aqui


# --------------------------------- TODOS OS DESAFIOS -------------------------------------

def num_episodio():
    global lbl_nep
    global lbl_nmep

    lbl_nep = tk.Label(app, text="EPISÓDIO: ",
                       font=fonte_padrao)
    lbl_nep.place(x=10, y=20)

    nmep = str(nep)

    lbl_nmep = tk.Label(app, text=nmep + "  -  " + lst_escolhas[nep - 1],
                        font=fonte_padrao)
    lbl_nmep.place(x=135, y=20)


def visu_resu():
    global button_visu

    # BOTÃO VISUALIZAR RESULTADOS
    button_visu = tkinter.Button(app, text="Visualizar Resultados", font=fonte_padrao3, command=tops_n_bottons)
    button_visu.place(x=10, y=180)


def show_de_talentos():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste desafio, as participantes de Drag Race Unauthorized",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="Simulator deverão revelar suas habilidades em uma incrível",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="performance de Show de Talentos!",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N.T
    # tipo:

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'NADA'
    vant2 = 'NADA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def girl_group():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Para o desafio principal deste episódio, as Queens serão divididas",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="em times onde deverão escrever um solo e coreografar uma ",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="performance para a música 'Break Up Bye Bye'!",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N.T
    # tipo: Canto, dança e Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'PERFORM'
    vant2 = 'CANTO'
    vant3 = 'DANCA'
    vant4 = 'NADA'

    soma_cunt()


def rumix():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste episódio, as Queens deverão apresentar um medley de músicas ",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="de RuPaul's Drag Race Live, em homenagem à hospedagem do show em ",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="LAS VEGAS! Este desafio será coreografado pelo fabuloso Jamal Sims",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N.T
    # tipo: Canto, dança e Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'PERFORM'
    vant2 = 'CANTO'
    vant3 = 'DANCA'
    vant4 = 'NADA'

    soma_cunt()


def atuacao():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Luz, câmera e AÇÃO! Esta semana nossas participantes usarão suas",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="habilidades de atuação na comédia: 'Gay's Anatomy' ",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="Que vença a melhor Drag Queen!",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.N.T.T
    # tipo: Canto, dança e Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'TALENT'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'ATUACAO'
    vant2 = 'COMEDIA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def baile():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Nesta semana as Queens foram desafiadas a construir um look",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="usando APENAS materiais de um brechó! Além disso elas deverão",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="desfilar com mais outros 2 looks trazidos de casa.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: U.T.T.
    # tipo: Costura, moda, maquiag

    cunt1 = 'UNIQUENESS'
    cunt2 = 'TALENT'
    cunt3 = 'TALENT'
    cunt4 = 'NADA'

    vant1 = 'COSTURA'
    vant2 = 'MODA'
    vant3 = 'MAQUIAG'
    vant4 = 'NADA'

    soma_cunt()


def snatch_game():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="É a hora do SNATCH GAME! Hoje as participantes deverão",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="se montar como uma celebridade e também deverão fazer",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="RuPaul rir, neste desafio que exige muita improvisação.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.N.T.
    # tipo: IMPROV, COMEDIA, MAQUIAG

    cunt1 = 'CHARISMA'
    cunt2 = 'NERVE'
    cunt3 = 'TALENT'
    cunt4 = 'NADA'

    vant1 = 'IMPROV'
    vant2 = 'COMEDIA'
    vant3 = 'MAQUIAG'
    vant4 = 'COMEDIA'

    soma_cunt()


def rusical():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Para o desafio de hoje as Queens irão performar AO VIVO",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="o espetáculo Shade: The Rusical. Este desafio exigirá",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="habilidades de canto e atuação.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.N.T.T.
    # tipo: Canto, Atuação e Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'NERVE'
    cunt3 = 'TALENT'
    cunt4 = 'NADA'

    vant1 = 'ATUACAO'
    vant2 = 'CANTO'
    vant3 = 'PERFORM'
    vant4 = 'DANCA'

    soma_cunt()


def roast():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="No desafio desta semana, haverá o imperdível 'RuPaul Roast',",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="onde as queens terão que preparar e apresentar piadas aos",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="jurados sobre a própria RuPaul.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N.N.
    # tipo: COMEDIA, IMPROV

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'COMEDIA'
    vant2 = 'IMPROV'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def design():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste desafio cada participante recebeu uma caixa, cada uma",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="contendo materiais como plástico, couro ou metal. A partir",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="destes materiais cada Queen deverá construir um look babadeiro.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: U.U.T.
    # tipo: moda, costura

    cunt1 = 'UNIQUENESS'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'TALENT'
    cunt4 = 'NADA'

    vant1 = 'MODA'
    vant2 = 'COSTURA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def comercial():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste desafio cada Queen deverá roterizar um comercial",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="para vender sua prórpia marca de Perfumes. ",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="Este desafio exige habilidades criativas e de improviso.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.C.U.N.
    # tipo: moda, costura

    cunt1 = 'CHARISMA'
    cunt2 = 'NERVE'
    cunt3 = 'UNIQUENESS'
    cunt4 = 'NADA'

    vant1 = 'ATUACAO'
    vant2 = 'IMPROV'
    vant3 = 'IMPROV'
    vant4 = 'COMEDIA'

    soma_cunt()


def make_over():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Nesta semana, nossas participantes receberão a tarefa de",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="montar pela primeira vez veteranos de guerra LGBTQA+",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="do nosso país.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.U.T.
    # tipo: moda, costura

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'TALENT'
    cunt4 = 'NADA'

    vant1 = 'MAQUIAG'
    vant2 = 'MAQUIAG'
    vant3 = 'COSTURA'
    vant4 = 'MODA'

    soma_cunt()


def morning_show():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste episódios as Drag Queens serão desafiadas a",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="apresentar o programa 'Morning Glory'. Este desafio",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="exigirá muito improviso e personalidade",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N
    # tipo: IMPROV, IMPROV, ATUACAO, COMEDIA

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'IMPROV'
    vant2 = 'IMPROV'
    vant3 = 'ATUACAO'
    vant4 = 'COMEDIA'

    soma_cunt()


def draglympic():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Neste desafio as Queens irão competir em grupos em",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="uma batalha de Cheerleaders! Este desafio exigirá",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="muita energia e carisma",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: c.n.t.
    # tipo: danca, perform

    cunt1 = 'CHARISMA'
    cunt2 = 'TALENT'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'PERFORM'
    vant2 = 'DANCA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def danca_core():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Separadas em times, as Drag Queens deverão performar",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="em um documentário de dança sobre a era Disco, passando",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="por eras, como 'Studio 54', 'Disco Sucks' e 'Disco n' Sex'.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: c.n.t.
    # tipo: danca, perform, atuacao

    cunt1 = 'CHARISMA'
    cunt2 = 'TALENT'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'PERFORM'
    vant2 = 'DANCA'
    vant3 = 'ATUACAO'
    vant4 = 'DANCA'

    soma_cunt()


def runway():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Nesta semana, nossas participantes deverão desfilar",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="com um look em homenagem à um programa da BBC e outro",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="look que mostre quem elas são como Drag Queens.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.U.
    # tipo: moda, costura

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'UNIQUENESS'
    cunt4 = 'NADA'

    vant1 = 'MODA'
    vant2 = 'NADA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def canto():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Para o desafio desta semana, as competidoras gravarão a ",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="música 'Can I Get an Amen' inspirada em 'We are the World'. ",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="Com participação especial da própria RuPaul!",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.U.N.T
    # tipo: Canto, dança e Performance

    cunt1 = 'TALENT'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'PERFORM'
    vant2 = 'CANTO'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def stand_up():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="No desafio desta semana, as Queens foram desafiadas",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="a apresentar um show de Stand-Up diante os jurados",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="e a um auditório ao-vivo!",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)

    visu_resu()

    # exigencias: C.N.T.
    # tipo: COMEDIA, IMPROV

    cunt1 = 'CHARISMA'
    cunt2 = 'TALENT'
    cunt3 = 'NERVE'
    cunt4 = 'NADA'

    vant1 = 'COMEDIA'
    vant2 = 'IMPROV'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()


def lipsync_smack():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global lbl_dsc4
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    global button_visusmack

    button_ls.destroy()

    num_episodio()

    lbl_dsc1 = tk.Label(app, text="Chegou o momento de coroar nossa campeã! Porém elas deverão",
                        font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)

    lbl_dsc2 = tk.Label(app, text="lutar em um incrível Lip Sync SmackDown pela coroa!",
                        font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text="Competidores, aqueçam os motores.",
                        font=fonte_padrao)
    lbl_dsc3.place(x=10, y=160)
    lbl_dsc4 = tk.Label(app, text="E que vença a melhor DRAG QUEEN!",
                        font=fonte_padrao)
    lbl_dsc4.place(x=10, y=190)

    # exigencias: C.U.N.T.
    # tipo: Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'LP'
    vant2 = 'NADA'
    vant3 = 'NADA'
    vant4 = 'NADA'

    soma_cunt()
    sqlFAV = 'SELECT FAVORITA FROM unofficial_season'
    bscFAV = consulta(vcon, sqlFAV)
    contador = 0
    for value in bscFAV:
        cnv = str(value)[1:-2]
        if cnv == '1':
            val_fav = randint(1, 5)
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav {val_fav} e o valor acu {val_acu}')
        else:
            val_fav = 0
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav da {val_fav} e o valor acu {val_acu}')
    print(f'A lista de acu corrigida é: {lst_acumulada}')
    print(f'A lista resultados corrigida é: {lst_resultados}')

    # BOTÃO VISUALIZAR RESULTADOS DO SMACKDOWN
    button_visusmack = tkinter.Button(app, text="Visualizar Resultados", font=fonte_padrao3, command=lipsync_smack2)
    button_visusmack.place(x=10, y=230)


def lipsync_smack2():
    global lbl_smack
    global button_avansd
    global combinacao
    global valuex
    global valuey
    global queen_a
    global queen_b
    global queen_c
    global queen_d
    global queen_f

    global cntxt1
    global cntxt2
    global cntxt3
    global cntxt4
    global cntf

    global lst_finalista
    global ctd_id
    lst_finalista = []

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_dsc4.destroy()
    button_ls.destroy()
    button_visusmack.destroy()

    lbl_smack = tk.Label(app, text="A roleta girou e a primeira dupla a dublar por um lugar na final é:",
                         font=fonte_padrao)
    lbl_smack.place(x=10, y=50)

    # BOTÃO PARA AVANÇAR DENTRE O SMACKDOWN
    button_avansd = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=lipsync_smack3)
    button_avansd.place(x=545, y=475, width=190)

    # Indicador do nome das participantes entre A, B, C e D

    sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
    bscName = consulta(vcon, sqlNAME)

    queen_a = str(bscName[0])
    cntxt1 = "1"

    queen_b = str(bscName[1])
    cntxt2 = "2"

    queen_c = str(bscName[2])
    cntxt3 = "3"

    queen_d = str(bscName[3])
    cntxt4 = "4"

    combinacao = randint(1, 3)
    # 1 = A x B e C x D
    # 2 = A x C e B x D
    # 3 = A x D e B x C
    # n esquecer o valor de x e y onde a foto aparece deve vir daqui

    # Aque teremos o efeito da roleta ao formas as duplas
    if combinacao == 1:
        valuex = 10
        valuey = 80
        qn_a()
        valuex = 290
        valuey = 80
        qn_b()
        if lst_resultados[1] >= lst_resultados[0]:
            valuex = 150
            valuey = 260
            lst_finalista.append("2")
            queen_f = queen_b
            cntf = "2"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("1")
            queen_f = queen_a
            cntf = "1"
            qn_f()

    elif combinacao == 2:
        valuex = 10
        valuey = 80
        qn_a()
        valuex = 290
        valuey = 80
        qn_c()
        if lst_resultados[2] >= lst_resultados[0]:
            valuex = 150
            valuey = 260
            lst_finalista.append("3")
            queen_f = queen_c
            cntf = "3"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("1")
            queen_f = queen_a
            cntf = "1"
            qn_f()

    elif combinacao == 3:
        valuex = 10
        valuey = 80
        qn_a()
        valuex = 290
        valuey = 80
        qn_d()
        if lst_resultados[3] >= lst_resultados[0]:
            valuex = 150
            valuey = 260
            lst_finalista.append("4")
            queen_f = queen_d
            cntf = "4"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("1")
            queen_f = queen_a
            cntf = "1"
            qn_f()


def lipsync_smack3():
    if combinacao == 1:
        lbl_qa.destroy()
        f_qa.destroy()
        lbl_qb.destroy()
        f_qb.destroy()
        lbl_qf.destroy()
        f_qf.destroy()
    elif combinacao == 2:
        lbl_qa.destroy()
        f_qa.destroy()
        lbl_qc.destroy()
        f_qc.destroy()
        lbl_qf.destroy()
        f_qf.destroy()
    else:
        lbl_qa.destroy()
        f_qa.destroy()
        lbl_qd.destroy()
        f_qd.destroy()
        lbl_qf.destroy()
        f_qf.destroy()

    button_avansd.destroy()
    lbl_smack.destroy()

    global valuex
    global valuey
    global queen_f
    global cntf
    global button_avansd2
    global lbl_smack2
    global ctd_id

    lbl_smack2 = tk.Label(app, text="A próxima dupla de competidoras a dublar pela coroa é:",
                          font=fonte_padrao)
    lbl_smack2.place(x=10, y=50)

    # Aque teremos o efeito da roleta ao formas as duplas
    if combinacao == 1:
        valuex = 10
        valuey = 80
        qn_c()
        valuex = 290
        valuey = 80
        qn_d()
        if lst_resultados[3] >= lst_resultados[2]:
            valuex = 150
            valuey = 260
            queen_f = queen_d
            lst_finalista.append("4")
            cntf = "4"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("3")
            queen_f = queen_c
            cntf = "3"
            qn_f()

    elif combinacao == 2:
        valuex = 10
        valuey = 80
        qn_b()
        valuex = 290
        valuey = 80
        qn_d()
        if lst_resultados[3] >= lst_resultados[1]:
            valuex = 150
            valuey = 260
            lst_finalista.append("4")
            queen_f = queen_d
            cntf = "4"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("2")
            queen_f = queen_b
            cntf = "2"
            qn_f()

    elif combinacao == 3:
        valuex = 10
        valuey = 80
        qn_b()
        valuex = 290
        valuey = 80
        qn_c()
        if lst_resultados[2] >= lst_resultados[1]:
            valuex = 150
            valuey = 260
            lst_finalista.append("3")
            queen_f = queen_c
            cntf = "3"
            qn_f()
        else:
            valuex = 150
            valuey = 260
            lst_finalista.append("2")
            queen_f = queen_b
            cntf = "2"
            qn_f()

    # BOTÃO PARA AVANÇAR DENTRE O SMACKDOWN2
    button_avansd2 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=lipsync_smack4)
    button_avansd2.place(x=545, y=475, width=190)


def lipsync_smack4():
    global lbl_smack3
    global lbl_smack4
    global lbl_smack5
    global valuex
    global valuey
    global button_avansd3

    if combinacao == 1:
        lbl_qc.destroy()
        f_qc.destroy()
        lbl_qd.destroy()
        f_qd.destroy()
        lbl_qf.destroy()
        f_qf.destroy()
    elif combinacao == 2:
        lbl_qb.destroy()
        f_qb.destroy()
        lbl_qd.destroy()
        f_qd.destroy()
        lbl_qf.destroy()
        f_qf.destroy()
    else:
        lbl_qb.destroy()
        f_qb.destroy()
        lbl_qc.destroy()
        f_qc.destroy()
        lbl_qf.destroy()
        f_qf.destroy()
    lbl_smack2.destroy()
    button_ls.destroy()

    lbl_smack3 = tk.Label(app, text="Estamos diante do ÚLTIMO lip sync desta temporada de",
                          font=fonte_padrao)
    lbl_smack3.place(x=10, y=50)
    lbl_smack4 = tk.Label(app, text="DRAG RACE - UNAUTHORIZED SIMULATOR",
                          font=fonte_padrao)
    lbl_smack4.place(x=10, y=80)
    lbl_smack5 = tk.Label(app, text="que a melhor Drag Queen VENÇA!",
                          font=fonte_padrao)
    lbl_smack5.place(x=10, y=300)

    if lst_finalista[0] == "1":
        valuex = 10
        valuey = 110
        qn_a()
    elif lst_finalista[0] == "2":
        valuex = 10
        valuey = 110
        qn_b()
    elif lst_finalista[0] == "3":
        valuex = 10
        valuey = 110
        qn_c()
    elif lst_finalista[0] == "4":
        valuex = 10
        valuey = 110
        qn_d()

    if lst_finalista[1] == "1":
        valuex = 290
        valuey = 110
        qn_a()
    elif lst_finalista[1] == "2":
        valuex = 290
        valuey = 110
        qn_b()
    elif lst_finalista[1] == "3":
        valuex = 290
        valuey = 110
        qn_c()
    elif lst_finalista[1] == "4":
        valuex = 290
        valuey = 110
        qn_d()

    # BOTÃO PARA AVANÇAR DENTRE O SMACKDOWN3
    button_avansd3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=lipsync_smack5)
    button_avansd3.place(x=545, y=475, width=190)


def lipsync_smack5():
    global button_avansd4
    global campea
    global lbl_smack6
    global lbl_smack7
    global lbl_smack8

    if lst_finalista[0] == "1":
        lbl_qa.destroy()
        f_qa.destroy()
    elif lst_finalista[0] == "2":
        lbl_qb.destroy()
        f_qb.destroy()
    elif lst_finalista[0] == "3":
        lbl_qc.destroy()
        f_qc.destroy()
    elif lst_finalista[0] == "4":
        lbl_qd.destroy()
        f_qd.destroy()

    if lst_finalista[1] == "1":
        lbl_qa.destroy()
        f_qa.destroy()
    elif lst_finalista[1] == "2":
        lbl_qb.destroy()
        f_qb.destroy()
    elif lst_finalista[1] == "3":
        lbl_qc.destroy()
        f_qc.destroy()
    elif lst_finalista[1] == "4":
        lbl_qd.destroy()
        f_qd.destroy()

    lbl_smack3.destroy()
    lbl_smack4.destroy()
    lbl_smack5.destroy()
    button_ls.destroy()
    button_avansd3.destroy()

    lbl_smack6 = tk.Label(app, text="Após dublarem com unhas e dentes, reveal após reveal...",
                          font=fonte_padrao)
    lbl_smack6.place(x=40, y=150)
    lbl_smack7 = tk.Label(app, text="A campeã de Drag Race - Unauthorized Simulator...",
                          font=fonte_padrao)
    lbl_smack7.place(x=100, y=190)
    lbl_smack8 = tk.Label(app, text="A nova Drag Super Star da Internet é...",
                          font=fonte_padrao)
    lbl_smack8.place(x=130, y=230)

    soma_cunt()
    sqlFAV = 'SELECT FAVORITA FROM unofficial_season'
    bscFAV = consulta(vcon, sqlFAV)
    contador = 0
    for value in bscFAV:
        cnv = str(value)[1:-2]
        if cnv == '1':
            val_fav = randint(1, 5)
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav {val_fav} e o valor acu {val_acu}')
        else:
            val_fav = 0
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav da {val_fav} e o valor acu {val_acu}')
    print(f'A lista corrigida é: {lst_acumulada}')
    print(f'A lista resultados corrigida é: {lst_resultados}')
    # lst_finalista possui os ids das top2
    # lst_resultados possui os valores do top4
    if lst_finalista[0] == "1":
        final_a = lst_resultados[0]
        campea0 = "1"
    elif lst_finalista[0] == "2":
        final_a = lst_resultados[1]
        campea0 = "2"
    elif lst_finalista[0] == "3":
        final_a = lst_resultados[2]
        campea0 = "3"
    elif lst_finalista[0] == "4":
        final_a = lst_resultados[3]
        campea0 = "4"

    if lst_finalista[1] == "1":
        final_b = lst_resultados[0]
        campea1 = "1"
    elif lst_finalista[1] == "2":
        final_b = lst_resultados[1]
        campea1 = "2"
    elif lst_finalista[1] == "3":
        final_b = lst_resultados[2]
        campea1 = "3"
    elif lst_finalista[1] == "4":
        final_b = lst_resultados[3]
        campea1 = "4"

    # definindo a campeã
    if final_b >= final_a:
        campea = campea1
    else:
        campea = campea0

    # BOTÃO PARA AVANÇAR DENTRE O SMACKDOWN4
    button_avansd4 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=lipsync_smack6)
    button_avansd4.place(x=545, y=475, width=190)


def lipsync_smack6():  # mostra a campea
    lbl_smack6.destroy()
    lbl_smack7.destroy()
    lbl_smack8.destroy()

    valuex = 300
    valuey = 240

    if campea == "1":
        qn_a()
    elif campea == "2":
        qn_b()
    elif campea == "3":
        qn_c()
    elif campea == "4":
        qn_d()

    button_fechartudo()


def top3_perform():
    global lbl_dsc1
    global lbl_dsc2
    global lbl_dsc3
    global lbl_dsc4
    global lbl_dsc5
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4

    global button_visutop3

    button_ls.destroy()

    num_episodio()

    if (chave_finale == 1) or (chave_finale == 6):
        txt1 = "Antes de coroar nossa campeã, nossas competidoras deverão "
        txt2 = "se apresentar em um incrível show e irão protagonizar "
        txt3 = "uma performance feita especialmente para elas! "
        vtg1 = "PERFORM"
        vtg2 = "NADA"
        vtg3 = "NADA"
        vtg4 = "NADA"
    elif (chave_finale == 2) or (chave_finale == 3) or (chave_finale == 4) or (chave_finale == 5):
        txt1 = "Antes de coroar nossa campeã, nossas competidoras serão"
        txt2 = "desafiadas a protagonizar um vídeo-clipe de uma música"
        txt3 = "inédita da RuPaul, com participação especial da própria!"
        vtg1 = "PERFORM"
        vtg2 = "CANTO"
        vtg3 = "DANCA"
        vtg4 = "NADA"

    lbl_dsc1 = tk.Label(app, text=txt1, font=fonte_padrao)
    lbl_dsc1.place(x=10, y=80)
    lbl_dsc2 = tk.Label(app, text=txt2, font=fonte_padrao)
    lbl_dsc2.place(x=10, y=110)
    lbl_dsc3 = tk.Label(app, text=txt3, font=fonte_padrao)
    lbl_dsc3.place(x=10, y=140)
    lbl_dsc4 = tk.Label(app, text="Competidores, aqueçam os motores.",
                        font=fonte_padrao)
    lbl_dsc4.place(x=10, y=190)
    lbl_dsc5 = tk.Label(app, text="E que vença a melhor DRAG QUEEN!",
                        font=fonte_padrao)
    lbl_dsc5.place(x=10, y=220)

    # exigencias: C.U.N.T.
    # tipo: Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = vtg1
    vant2 = vtg2
    vant3 = vtg3
    vant4 = vtg4

    soma_cunt()
    sqlFAV = 'SELECT FAVORITA FROM unofficial_season'
    bscFAV = consulta(vcon, sqlFAV)
    contador = 0
    for value in bscFAV:
        cnv = str(value)[1:-2]
        if cnv == '1':
            val_fav = randint(1, 5)
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav {val_fav} e o valor acu {val_acu}')
        else:
            val_fav = 0
            val_acu = lst_acumulada[contador]
            val = val_fav + val_acu
            lst_resultados[contador] += val
            contador += 1
            # loló apagar
            print('**************')
            print(f'valor de fav da {val_fav} e o valor acu {val_acu}')
    print(f'A lista de acu corrigida é: {lst_acumulada}')
    print(f'A lista resultados corrigida é: {lst_resultados}')

    # BOTÃO VISUALIZAR TOP 3
    if (chave_finale == 1) or (chave_finale == 2) or (chave_finale == 6):
        button_visutop3 = tkinter.Button(app, text="Visualizar Finalistas", font=fonte_padrao3, command=top3_perform2)
        button_visutop3.place(x=10, y=250)
    elif chave_finale == 3:
        button_visutop3 = tkinter.Button(app, text="Visualizar Finalistas", font=fonte_padrao3, command=top3_top2)
        button_visutop3.place(x=10, y=250)
    elif chave_finale == 4:
        button_visutop3 = tkinter.Button(app, text="Visualizar Finalistas", font=fonte_padrao3, command=top4_rumix)
        button_visutop3.place(x=10, y=250)
    elif chave_finale == 5:
        button_visutop3 = tkinter.Button(app, text="Visualizar Finalistas", font=fonte_padrao3, command=top4_individual)
        button_visutop3.place(x=10, y=250)


def top3_perform2():
    global queen_a
    global queen_b
    global queen_c
    global lbl_dsc6
    global lbl_dsc7
    global lbl_dsc8
    global cntxt1
    global campeatop3

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_dsc4.destroy()
    lbl_dsc5.destroy()
    button_visutop3.destroy()

    if (chave_finale == 1) or (chave_finale == 2):
        button_avantop3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top3_perform3)
        button_avantop3.place(x=545, y=475, width=190)
        txt1 = "A campeã de Drag Race - Unauthorized Simulator,"
        txt2 = "A nova Drag Super Star da Internet é..."
    elif chave_finale == 6:
        button_avantop3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top5_top2)
        button_avantop3.place(x=545, y=475, width=190)
        txt1 = "RuPaul ainda não tomou sua decisão e precisará ver as Queens "
        txt2 = "do TOP2 lutarem mais uma vez em um Lip Sync pela coroa! " #top2 pela coroa

    lbl_dsc6 = tk.Label(app, text="Após apresentarem uma performance de tirar o fôlego",
                        font=fonte_padrao)
    lbl_dsc6.place(x=10, y=80)
    lbl_dsc7 = tk.Label(app, text=txt1, font=fonte_padrao)
    lbl_dsc7.place(x=10, y=110)
    lbl_dsc8 = tk.Label(app, text=txt2, font=fonte_padrao)
    lbl_dsc8.place(x=10, y=140)

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    if (chave_finale == 1) or (chave_finale == 2):
        qn1_top3() #imprimi a queen da lista 1
        qn2_top3()
        qn3_top3()
    elif chave_finale == 6:
        qn1_top5()
        qn2_top5()
        qn3_top5()
        qn4_top5()
        qn5_top5()

    #definindo campea
    if (chave_finale == 1) or (chave_finale == 2):
        if (lst_resultados[2] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[1]):
            campeatop3 = "3"
        elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[1] >= lst_resultados[2]):
            campeatop3 = "2"
        elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[0] >= lst_resultados[2]):
            campeatop3 = "1"
    elif chave_finale == 6:
        if (lst_resultados[4] >= lst_resultados[0]) and (lst_resultados[4] >= lst_resultados[1]) and \
                (lst_resultados[4] >= lst_resultados[2]) and (lst_resultados[4] >= lst_resultados[3]):
            campeatop3 = "5"
        elif (lst_resultados[3] >= lst_resultados[0]) and (lst_resultados[3] >= lst_resultados[1]) and \
                (lst_resultados[3] >= lst_resultados[2]) and (lst_resultados[3] >= lst_resultados[4]):
            campeatop3 = "4"
        elif (lst_resultados[2] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[1]) and \
                (lst_resultados[2] >= lst_resultados[3]) and (lst_resultados[2] >= lst_resultados[4]):
            campeatop3 = "3"
        elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[1] >= lst_resultados[2]) and \
                (lst_resultados[1] >= lst_resultados[3]) and (lst_resultados[1] >= lst_resultados[4]):
            campeatop3 = "2"
        elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[0] >= lst_resultados[2]) and \
                (lst_resultados[0] >= lst_resultados[3]) and (lst_resultados[0] >= lst_resultados[4]):
            campeatop3 = "1"


def top3_perform3():
    lbl_dsc6.destroy()
    lbl_dsc7.destroy()
    lbl_dsc8.destroy()
    f_qa.destroy()
    f_qb.destroy()
    f_qc.destroy()
    lbl_qa.destroy()
    lbl_qb.destroy()
    lbl_qc.destroy()

    #lolo apagar isso
    print()
    print(f'A lista de resultados finais é {lst_resultados}')

    qnwin_top3()

    button_fechartudo()


def top3_top2():
    global queen_a
    global queen_b
    global queen_c
    global lbl_dsc6
    global lbl_dsc7
    global lbl_dsc8
    global lbl_fulana
    global cntxt1
    global campeatop3
    global button_avantop3

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_dsc4.destroy()
    lbl_dsc5.destroy()
    button_visutop3.destroy()

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    if (lst_resultados[0] >= lst_resultados[2]) and (lst_resultados[1] >= lst_resultados[2]):
        fulana = str(lstname[2])
    elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[2] >= lst_resultados[1]):
        fulana = str(lstname[1])
    elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[0]):
        fulana = str(lstname[0])

    lbl_dsc6 = tk.Label(app, text="Após apresentarem uma performance de tirar o fôlego,",
                        font=fonte_padrao)
    lbl_dsc6.place(x=10, y=80)
    lbl_dsc7 = tk.Label(app, text="RuPaul decide que haverá apenas um TOP2 e que",
                        font=fonte_padrao)
    lbl_dsc7.place(x=10, y=110)
    lbl_fulana = tk.Label(app, text=fulana[2:-3],
                        font=fonte_padrao, bg='yellow', fg='blue')
    lbl_fulana.place(x=540, y=110)
    lbl_dsc8 = tk.Label(app, text="não irá dublar pela coroa.",
                        font=fonte_padrao)
    lbl_dsc8.place(x=10, y=140)

    qn1_top3() #imprimi a queen da lista 1

    qn2_top3()

    qn3_top3()

    button_avantop3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top3_top2_2)
    button_avantop3.place(x=545, y=475, width=190)

    #definindo campea
    if (lst_resultados[2] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[1]):
        campeatop3 = "3"
    elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[1] >= lst_resultados[2]):
        campeatop3 = "2"
    elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[0] >= lst_resultados[2]):
        campeatop3 = "1"


def top3_top2_2():
    global lbl_dsc9
    global lbl_dsc10
    global lbl_dsc11
    global button_avantop3_2
    global contab

    lbl_dsc6.destroy()
    lbl_dsc7.destroy()
    lbl_dsc8.destroy()
    f_qa.destroy()
    f_qb.destroy()
    f_qc.destroy()
    lbl_qa.destroy()
    lbl_qb.destroy()
    lbl_qc.destroy()
    lbl_fulana.destroy()
    button_avantop3.destroy()

    lbl_dsc9 = tk.Label(app, text="Após um lip sync de estremecer a passarela, RuPaul tem sua decisão!",
                        font=fonte_padrao)
    lbl_dsc9.place(x=10, y=80)
    lbl_dsc10 = tk.Label(app, text="A campeã de Drag Race - Unauthorized Simulator...",
                        font=fonte_padrao)
    lbl_dsc10.place(x=10, y=110)
    lbl_dsc11 = tk.Label(app, text="A nova Drag Super Star da Internet é...",
                        font=fonte_padrao)
    lbl_dsc11.place(x=10, y=140)

    if (lst_resultados[0] >= lst_resultados[2]) and (lst_resultados[1] >= lst_resultados[2]):
        contab = 0
        qn1_top3()
        qn2_top3()
    elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[2] >= lst_resultados[1]):
        contab = 1
        qn1_top3()
        qn3_top3()
    elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[0]):
        contab = 2
        qn2_top3()
        qn3_top3()

    button_avantop3_2 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top3_top2_3)
    button_avantop3_2.place(x=545, y=475, width=190)


def top3_top2_3():
    lbl_dsc9.destroy()
    lbl_dsc10.destroy()
    lbl_dsc11.destroy()
    button_avantop3_2.destroy()

    f_qa.destroy()
    f_qb.destroy()
    f_qc.destroy()
    lbl_qa.destroy()
    lbl_qb.destroy()
    lbl_qc.destroy()

    qnwin_top3()

    button_fechartudo()


def top4_individual():
    global queen_a
    global queen_b
    global queen_c
    global lbl_dsc6
    global lbl_dsc7
    global lbl_dsc8
    global cntxt1
    global campeatop3
    global button_avantop4_top3

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_dsc4.destroy()
    lbl_dsc5.destroy()
    button_visutop3.destroy()

    lbl_dsc6 = tk.Label(app, text="Após apresentarem uma performance sensacional e looks de",
                        font=fonte_padrao)
    lbl_dsc6.place(x=10, y=80)
    lbl_dsc7 = tk.Label(app, text="tirar o fôlego, RuPaul decide que cada finalista deverá",
                        font=fonte_padrao)
    lbl_dsc7.place(x=10, y=110)
    lbl_dsc8 = tk.Label(app, text="dublar SOZINHA pela coroa!",
                        font=fonte_padrao)
    lbl_dsc8.place(x=10, y=140)

    qn1_top4() #imprimi a queen da lista 1

    qn2_top4()

    qn3_top4()

    qn4_top4()

    button_avantop4_top3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top4_rumix2)
    button_avantop4_top3.place(x=545, y=475, width=190)

    #definindo campea
    if (lst_resultados[3] >= lst_resultados[0]) and (lst_resultados[3] >= lst_resultados[1]) and \
            (lst_resultados[3] >= lst_resultados[2]):
        campeatop3 = "4"
    elif (lst_resultados[2] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[1]) and \
            (lst_resultados[2] >= lst_resultados[3]):
        campeatop3 = "3"
    elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[1] >= lst_resultados[2]) and \
            (lst_resultados[1] >= lst_resultados[3]):
        campeatop3 = "2"
    elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[0] >= lst_resultados[2]) and \
            (lst_resultados[0] >= lst_resultados[3]):
        campeatop3 = "1"


def top4_rumix():
    global queen_a
    global queen_b
    global queen_c
    global lbl_dsc6
    global lbl_dsc7
    global lbl_dsc8
    global lbl_fulana
    global cntxt1
    global campeatop3
    global button_avantop4_top3

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_dsc4.destroy()
    lbl_dsc5.destroy()
    button_visutop3.destroy()

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    if (lst_resultados[0] >= lst_resultados[3]) and \
        (lst_resultados[1] >= lst_resultados[3]) and \
        (lst_resultados[2] >= lst_resultados[3]):
        fulana = str(lstname[3])
    elif (lst_resultados[0] >= lst_resultados[2]) and \
        (lst_resultados[1] >= lst_resultados[2]) and \
        (lst_resultados[3] >= lst_resultados[2]):
        fulana = str(lstname[2])
    elif (lst_resultados[0] >= lst_resultados[1]) and \
        (lst_resultados[2] >= lst_resultados[1]) and \
        (lst_resultados[3] >= lst_resultados[1]):
        fulana = str(lstname[1])
    elif (lst_resultados[1] >= lst_resultados[0]) and \
        (lst_resultados[2] >= lst_resultados[0]) and \
        (lst_resultados[3] >= lst_resultados[0]):
        fulana = str(lstname[0])

    lbl_dsc6 = tk.Label(app, text="Após apresentarem uma performance de tirar o fôlego,",
                        font=fonte_padrao)
    lbl_dsc6.place(x=10, y=80)
    lbl_dsc7 = tk.Label(app, text="RuPaul decide que haverá apenas um TOP3 e que",
                        font=fonte_padrao)
    lbl_dsc7.place(x=10, y=110)
    lbl_fulana = tk.Label(app, text=fulana[2:-3],
                        font=fonte_padrao, bg='yellow', fg='blue')
    lbl_fulana.place(x=540, y=110)
    lbl_dsc8 = tk.Label(app, text="não irá dublar pela coroa.",
                        font=fonte_padrao)
    lbl_dsc8.place(x=10, y=140)

    qn1_top4() #imprimi a queen da lista 1

    qn2_top4()

    qn3_top4()

    qn4_top4()

    button_avantop4_top3 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top4_rumix2)
    button_avantop4_top3.place(x=545, y=475, width=190)

    #definindo campea
    if (lst_resultados[3] >= lst_resultados[0]) and (lst_resultados[3] >= lst_resultados[1]) and \
            (lst_resultados[3] >= lst_resultados[2]):
        campeatop3 = "4"
    elif (lst_resultados[2] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[1]) and \
            (lst_resultados[2] >= lst_resultados[3]):
        campeatop3 = "3"
    elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[1] >= lst_resultados[2]) and \
            (lst_resultados[1] >= lst_resultados[3]):
        campeatop3 = "2"
    elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[0] >= lst_resultados[2]) and \
            (lst_resultados[0] >= lst_resultados[3]):
        campeatop3 = "1"


def top4_rumix2():
    global lbl_dsc9
    global lbl_dsc10
    global lbl_dsc11
    global button_avantop4_top3_2

    lbl_dsc6.destroy()
    lbl_dsc7.destroy()
    lbl_dsc8.destroy()
    f_qa.destroy()
    f_qb.destroy()
    f_qc.destroy()
    f_qd.destroy()
    lbl_qa.destroy()
    lbl_qb.destroy()
    lbl_qc.destroy()
    lbl_qd.destroy()
    button_avantop4_top3.destroy()



    lbl_dsc9 = tk.Label(app, text="Após um lip sync de estremecer a passarela, RuPaul tem sua decisão!",
                        font=fonte_padrao)
    lbl_dsc9.place(x=10, y=80)
    lbl_dsc10 = tk.Label(app, text="A campeã de Drag Race - Unauthorized Simulator...",
                        font=fonte_padrao)
    lbl_dsc10.place(x=10, y=110)
    lbl_dsc11 = tk.Label(app, text="A nova Drag Super Star da Internet é...",
                        font=fonte_padrao)
    lbl_dsc11.place(x=10, y=140)

    if chave_finale == 4: #apaga a fulana qd rupaul elimina alguem
        lbl_fulana.destroy()
        if (lst_resultados[0] >= lst_resultados[3]) and (lst_resultados[1] >= lst_resultados[3]) and \
                (lst_resultados[2] >= lst_resultados[3]):
            qn1_top4()
            qn2_top4()
            qn3_top4()
        elif (lst_resultados[0] >= lst_resultados[2]) and (lst_resultados[1] >= lst_resultados[2]) and \
                (lst_resultados[3] >= lst_resultados[2]):
            qn1_top4()
            qn2_top4()
            qn4_top4()
        elif (lst_resultados[0] >= lst_resultados[1]) and (lst_resultados[2] >= lst_resultados[1]) and \
                (lst_resultados[3] >= lst_resultados[1]):
            qn1_top4()
            qn3_top4()
            qn4_top4()
        elif (lst_resultados[1] >= lst_resultados[0]) and (lst_resultados[2] >= lst_resultados[0]) and \
                (lst_resultados[3] >= lst_resultados[0]):
            qn2_top4()
            qn3_top4()
            qn4_top4()
    else:
        qn1_top4()
        qn2_top4()
        qn3_top4()
        qn4_top4()

    button_avantop4_top3_2 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top4_rumix3)
    button_avantop4_top3_2.place(x=545, y=475, width=190)


def top4_rumix3():

    lbl_dsc9.destroy()
    lbl_dsc10.destroy()
    lbl_dsc11.destroy()
    button_avantop4_top3_2.destroy()

    if chave_finale == 6:
        f_qtop1.destroy()
        lbl_qtop1.destroy()
        f_qtop2.destroy()
        lbl_qtop2.destroy()
    else:
        f_qa.destroy()
        f_qb.destroy()
        f_qc.destroy()
        f_qd.destroy()
        lbl_qa.destroy()
        lbl_qb.destroy()
        lbl_qc.destroy()
        lbl_qd.destroy()


    qnwin_top3()
    button_fechartudo()


def top5_top2():
    global lbl_dsc9
    global lbl_dsc10
    global lbl_dsc11
    global button_avantop4_top3_2
    global top5a
    global top5b
    global posia
    global posib

    lbl_dsc6.destroy()
    lbl_dsc7.destroy()
    lbl_dsc8.destroy()
    f_qa.destroy()
    f_qb.destroy()
    f_qc.destroy()
    f_qd.destroy()
    f_qe.destroy()
    lbl_qa.destroy()
    lbl_qb.destroy()
    lbl_qc.destroy()
    lbl_qd.destroy()
    lbl_qe.destroy()

    lbl_dsc9 = tk.Label(app, text="Após um Lip Sync que deixou os jurados boquiabertos,",
                        font=fonte_padrao)
    lbl_dsc9.place(x=10, y=80)
    lbl_dsc10 = tk.Label(app, text="A campeã de Drag Race - Unauthorized Simulator...",
                        font=fonte_padrao)
    lbl_dsc10.place(x=10, y=110)
    lbl_dsc11 = tk.Label(app, text="A nova Drag Super Star da Internet é...",
                        font=fonte_padrao)
    lbl_dsc11.place(x=10, y=140)

    # criando lista auxiliar organizada
    lst_organizada2 = lst_resultados[:]

    for check in range(len(lst_organizada2)):
        for check2 in range(len(lst_organizada2)):
            if lst_organizada2[check] <= lst_organizada2[check2]:
                aux = lst_organizada2[check]
                lst_organizada2[check] = lst_organizada2[check2]
                lst_organizada2[check2] = aux

    print('************') #lolo apagar
    print(f'Lista original antes do aliviador: {lst_resultados}')
    print(f'Lista organizada antes do aliviador: {lst_organizada2}')

    # aliviador de empates
    aliviador = 20
    for caliv in range(0, len(lst_organizada2)):
        for caliv2 in range(0, len(lst_organizada2)):
            if lst_organizada2[caliv] == lst_resultados[caliv2]:
                lst_organizada2[caliv] += aliviador
                lst_resultados[caliv2] += aliviador
                break
        aliviador += 20

    print('************') #lolo apagar
    print(f'Lista original depois do aliviador: {lst_resultados}')
    print(f'Lista organizada depois do aliviador: {lst_organizada2}')

    # verificar quem é o top2
    for ctop5 in range(0, 5):
        if lst_resultados[ctop5] == lst_organizada2[-1]:
            posia = ctop5
            if ctop5 == 0:
                top5a = "1"
            elif ctop5 == 1:
                top5a = "2"
            elif ctop5 == 2:
                top5a = "3"
            elif ctop5 == 3:
                top5a = "4"
            elif ctop5 == 4:
                top5a = "5"

    for ctop5 in range(0, 5):
        if lst_resultados[ctop5] == lst_organizada2[-2]:
            posib = ctop5
            if ctop5 == 0:
                top5b = "1"
            elif ctop5 == 1:
                top5b = "2"
            elif ctop5 == 2:
                top5b = "3"
            elif ctop5 == 3:
                top5b = "4"
            elif ctop5 == 4:
                top5b = "5"

    top2_top5a()
    top2_top5b()

    button_avantop4_top3_2 = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=top4_rumix3)
    button_avantop4_top3_2.place(x=545, y=475, width=190)


def grand_finale():
    if chave_finale == 0:  # representa a escolha de ls smackdown para a finale
        lipsync_smack()
    else: #todos os outros estilo de finale
        top3_perform()


def qn_a():
    global lbl_qa
    global valuex
    global valuey
    global f_qa

    lbl_qa = tk.Label(app, text=queen_a[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qa.place(x=valuex, y=valuey + 155)

    f_qa = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqa  # Image variable to display
    my_data = cntxt1  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqa = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qa.config(image=imgqa)  # display image
        f_qa.place(x=valuex, y=valuey)


def qn_b():
    global lbl_qb
    global valuex
    global valuey
    global f_qb

    lbl_qb = tk.Label(app, text=queen_b[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qb.place(x=valuex, y=valuey + 155)

    f_qb = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqb  # Image variable to display
    my_data = cntxt2  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqb = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qb.config(image=imgqb)  # display image
        f_qb.place(x=valuex, y=valuey)


def qn_c():
    global lbl_qc
    global valuex
    global valuey
    global f_qc

    lbl_qc = tk.Label(app, text=queen_c[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qc.place(x=valuex, y=valuey + 155)

    f_qc = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqc  # Image variable to display
    my_data = cntxt3  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqc = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qc.config(image=imgqc)  # display image
        f_qc.place(x=valuex, y=valuey)


def qn_d():
    global lbl_qd
    global valuex
    global valuey
    global f_qd

    lbl_qd = tk.Label(app, text=queen_d[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qd.place(x=valuex, y=valuey + 155)

    f_qd = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqd  # Image variable to display
    my_data = cntxt4  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqd = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qd.config(image=imgqd)  # display image
        f_qd.place(x=valuex, y=valuey)


def qn_f():
    global lbl_qf
    global valuex
    global valuey
    global f_qf

    lbl_qf = tk.Label(app, text="AVANÇOU PARA O LIP SYNC FINAL", font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qf.place(x=valuex - 20, y=valuey + 155)

    f_qf = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqf  # Image variable to display
    my_data = cntf  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqf = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qf.config(image=imgqf)  # display image
        f_qf.place(x=valuex, y=valuey)


def qn1_top3():
    global lbl_qa
    global valuex
    global valuey
    global f_qa

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv = str(lstname[0])
    lbl_qa = tk.Label(app, text=namecv[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qa.place(x=10, y=345)

    f_qa = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqa  # Image variable to display
    my_data = "1" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqa = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qa.config(image=imgqa)  # display image
        f_qa.place(x=10, y=190)


def qn2_top3():
    global lbl_qb
    global valuex
    global valuey
    global f_qb

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv2 = str(lstname[1])
    lbl_qb = tk.Label(app, text=namecv2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qb.place(x=290, y=345)

    f_qb = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqb  # Image variable to display
    my_data = "2" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqb = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qb.config(image=imgqb)  # display image
        f_qb.place(x=290, y=190)


def qn3_top3():
    global lbl_qc
    global valuex
    global valuey
    global f_qc

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv3 = str(lstname[2])
    lbl_qc = tk.Label(app, text=namecv3[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qc.place(x=570, y=345)

    f_qc = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqc  # Image variable to display
    my_data = "3" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqc = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qc.config(image=imgqc)  # display image
        f_qc.place(x=570, y=190)


def qn1_top5():
    global lbl_qa
    global valuex
    global valuey
    global f_qa

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv = str(lstname[0])
    lbl_qa = tk.Label(app, text=namecv[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qa.place(x=0, y=345)

    f_qa = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqa  # Image variable to display
    my_data = "1" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqa = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qa.config(image=imgqa)  # display image
        f_qa.place(x=0, y=190)


def qn2_top5():
    global lbl_qb
    global valuex
    global valuey
    global f_qb

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv2 = str(lstname[1])
    lbl_qb = tk.Label(app, text=namecv2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qb.place(x=150, y=345)

    f_qb = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqb  # Image variable to display
    my_data = "2" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqb = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qb.config(image=imgqb)  # display image
        f_qb.place(x=150, y=190)


def qn3_top5():
    global lbl_qc
    global valuex
    global valuey
    global f_qc

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv3 = str(lstname[2])
    lbl_qc = tk.Label(app, text=namecv3[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qc.place(x=300, y=345)

    f_qc = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqc  # Image variable to display
    my_data = "3" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqc = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qc.config(image=imgqc)  # display image
        f_qc.place(x=300, y=190)


def qn4_top5():
    global lbl_qd
    global f_qd

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv4 = str(lstname[3])
    lbl_qd = tk.Label(app, text=namecv4[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qd.place(x=450, y=345)

    f_qd = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqd  # Image variable to display
    my_data = "4" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqd = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qd.config(image=imgqd)  # display image
        f_qd.place(x=450, y=190)


def qn5_top5():
    global lbl_qe
    global f_qe

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv5 = str(lstname[4])
    lbl_qe = tk.Label(app, text=namecv5[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qe.place(x=600, y=345)

    f_qe = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqe  # Image variable to display
    my_data = "5" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqe = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qe.config(image=imgqe)  # display image
        f_qe.place(x=600, y=190)


def qn1_top4():
    global lbl_qa
    global valuex
    global valuey
    global f_qa

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv = str(lstname[0])
    lbl_qa = tk.Label(app, text=namecv[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qa.place(x=10, y=345)

    f_qa = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqa  # Image variable to display
    my_data = "1" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqa = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qa.config(image=imgqa)  # display image
        f_qa.place(x=10, y=190)


def qn2_top4():
    global lbl_qb
    global valuex
    global valuey
    global f_qb

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv2 = str(lstname[1])
    lbl_qb = tk.Label(app, text=namecv2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qb.place(x=200, y=345)

    f_qb = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqb  # Image variable to display
    my_data = "2" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqb = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qb.config(image=imgqb)  # display image
        f_qb.place(x=200, y=190)


def qn3_top4():
    global lbl_qc
    global valuex
    global valuey
    global f_qc

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv3 = str(lstname[2])
    lbl_qc = tk.Label(app, text=namecv3[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qc.place(x=395, y=345)

    f_qc = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqc  # Image variable to display
    my_data = "3" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqc = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qc.config(image=imgqc)  # display image
        f_qc.place(x=395, y=190)


def qn4_top4():
    global lbl_qd
    global valuex
    global valuey
    global f_qd

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    namecv4 = str(lstname[3])
    lbl_qd = tk.Label(app, text=namecv4[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qd.place(x=590, y=345)

    f_qd = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqd  # Image variable to display
    my_data = "4" # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqd = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qd.config(image=imgqd)  # display image
        f_qd.place(x=590, y=190)


def top2_top5a():
    global lbl_qtop1
    global valuex
    global valuey
    global f_qtop1

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    nametop1 = str(lstname[posia])
    lbl_qtop1 = tk.Label(app, text=nametop1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qtop1.place(x=160, y=190+155)

    f_qtop1 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqtop1 # Image variable to display
    my_data = top5a # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqtop1 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qtop1.config(image=imgqtop1)  # display image
        f_qtop1.place(x=160, y=190)


def top2_top5b():
    global lbl_qtop2
    global valuex
    global valuey
    global f_qtop2

    name = "SELECT NAME_QUEENS FROM unofficial_season"
    lstname = consulta(vcon, name)

    nametop2 = str(lstname[posib])
    lbl_qtop2 = tk.Label(app, text=nametop2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qtop2.place(x=440, y=190+155)

    f_qtop2 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqtop2  # Image variable to display
    my_data = top5b # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqtop2 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qtop2.config(image=imgqtop2)  # display image
        f_qtop2.place(x=440, y=190)


def qnwin_top3():

    name = "SELECT NAME_QUEENS FROM unofficial_season WHERE ID_QUEENS = "+campeatop3+" "
    lstname = consulta(vcon, name)

    namecvwin = str(lstname)
    lbl_qw = tk.Label(app, text=namecvwin[3:-4], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_qw.place(x=295, y=140+155)

    f_qw = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgqw # Image variable to display
    my_data = campeatop3 # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgqw = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_qw.config(image=imgqw)  # display image
        f_qw.place(x=295, y=140)


# --------------------------------- TOPS AND BOTTONS --------------------------------------


def show_top1():
    global f_top1
    global lbl_lp1
    global lst_acumulada
    global check_acumulada

    f_top1 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgtop1  # Image variable to display
    my_data = cntxt1  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgtop1 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_top1.config(image=imgtop1)  # display image
        if check_ls1 == 1:
            lbl_lp1 = tk.Label(app, text=top1[2:-3], font=fonte_padrao4, fg='blue', bg='yellow')
            lbl_lp1.place(x=440, y=215)
            f_top1.place(x=440, y=60)
        else:
            f_top1.place(x=valuex, y=valuey)

    if chave_formato == 1:
        print('') #LOLÓ APAGAR
        print('O VERIF DA SOMA 1 FUNCIONOU')
        lst_acumulada[cntxt1 - 1] += 1
        print('')  # LOLÓ APAGAR
        print('SOMA 1 FUNCIONOU')
    else:
        lst_acumulada[cntxt1 - 1] += 2


def show_top2():
    global f_top2
    global lbl_lp2
    global check_acumulada2

    f_top2 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgtop2  # Image variable to display
    my_data = cntxt2  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgtop2 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_top2.config(image=imgtop2)  # display image
        if check_ls2 == 1:
            lbl_lp2 = tk.Label(app, text=top2[2:-3], font=fonte_padrao4, fg='blue', bg='yellow')
            lbl_lp2.place(x=140, y=215)
            f_top2.place(x=140, y=60)
        else:
            f_top2.place(x=valuex, y=valuey)

    if chave_formato == 1: #só adiciona +2 aqui pro lsfylg
        print('') #LOLÓ APAGAR
        print('O VERIF DA SOMA 1 FUNCIONOU')
        lst_acumulada[cntxt2 - 1] += 1
        print('')  # LOLÓ APAGAR
        print('SOMA 1 FUNCIONOU')


def show_top3():
    global f_top3
    f_top3 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgtop3  # Image variable to display
    my_data = cntxt3  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgtop3 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_top3.config(image=imgtop3)  # display image
        f_top3.place(x=590, y=60)


def show_btm1():
    global f_btm1
    global lbl_lp1

    f_btm1 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgbtm1  # Image variable to display
    my_data = cntxb1  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgbtm1 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_btm1.config(image=imgbtm1)  # display image
        if check_ls1 == 1:
            lbl_lp1 = tk.Label(app, text=btm1[2:-3], font=fonte_padrao4, fg='white', bg='red')
            lbl_lp1.place(x=440, y=215)
            f_btm1.place(x=440, y=60)
        else:
            f_btm1.place(x=valuex, y=valuey)


def show_btm2():
    global f_btm2
    global lbl_lp2

    f_btm2 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgbtm2  # Image variable to display
    my_data = cntxb2  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgbtm2 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_btm2.config(image=imgbtm2)  # display image
        if check_ls2 == 1:
            lbl_lp2 = tk.Label(app, text=btm2[2:-3], font=fonte_padrao4, fg='white', bg='red')
            lbl_lp2.place(x=140, y=215)
            f_btm2.place(x=140, y=60)
        else:
            f_btm2.place(x=valuex, y=valuey)


def show_btm3():
    global f_btm3

    f_btm3 = tk.Label(app)
    q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
    global imgbtm3  # Image variable to display
    my_data = cntxb3  # ID of the row to display
    try:
        my_cursor = my_conn.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        imgbtm3 = ImageTk.PhotoImage(data=r_set[0])  # create image
        f_btm3.config(image=imgbtm3)  # display image
        f_btm3.place(x=590, y=260)


def reorganizar_elim():
    qcheck = "SELECT ID_QUEENS FROM '" + tab_elim + "'"
    bsc_qcheck = consulta(vcon, qcheck)

    my_conn = lite.connect('dr_db.db')
    new_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    ctd_alter = 0
    for values in bsc_qcheck:
        with my_conn:
            cur = my_conn.cursor()
            old_value = str(values)[1:-2]
            cur.execute("UPDATE '" + tab_elim + "' SET ID_QUEENS = '" + new_values[
                ctd_alter] + "' WHERE ID_QUEENS = '" + old_value + "'")
            ctd_alter += 1


def inserir_eliminida():
    try:
        sqliteconnection = sqlite3.connect('dr_db.db')
        cursor = sqliteconnection.cursor()

        sqlite_insert_query = """insert into eliminated_queens (PHOTO, NAME_QUEENS, CHARISMA, UNIQUENESS, NERVE, TALENT,
        ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV, MAQUIAG, MODA, PERFORM, LP, 
        FAVORITA, JUSTICA, NADA) 
        select PHOTO, NAME_QUEENS, CHARISMA, UNIQUENESS, NERVE, TALENT, ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV,
        MAQUIAG, MODA, PERFORM, LP, FAVORITA, JUSTICA, NADA from unofficial_season
        where ID_QUEENS=""" + ctd_id + """"""

        cursor.execute(sqlite_insert_query)
        sqliteconnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteconnection:
            sqliteconnection.close()


def soma_ls():
    global sumCUNT
    global resultado_final
    global resultado_ls1
    global resultado_ls2
    global eliminada
    global lsfylg
    global chop1
    global chop2
    global venclegacy

    sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
    bscName = consulta(vcon, sqlNAME)

    sqlFAV = 'SELECT FAVORITA FROM unofficial_season'
    bscFAV = consulta(vcon, sqlFAV)
    print('')
    print('lista de fav: ', bscFAV)
    print(bscFAV[1])

    if chave_formato == 1:
        for check in lst_ll:  # lst_ll um lista contendo os valores de ID bo top 2
            checkstr = str(check)

            sqlCUNT = """SELECT 
                           """ + cunt1 + """, 
                           """ + cunt2 + """, 
                           """ + cunt3 + """, 
                           """ + cunt4 + """,
                           """ + vant1 + """, 
                           """ + vant2 + """, 
                           """ + vant3 + """, 
                           """ + vant4 + """
                           FROM unofficial_season 
                           WHERE ID_QUEENS= """ + checkstr + """ """
            bscCUNT = consulta(vcon, sqlCUNT)
            sumCUNT = sum(list(map(sum, list(bscCUNT))))  # soma os valores

            dado1 = randint(0, 6)
            dado2 = randint(0, 6)
            dado = dado1 + dado2

            cnv = str(bscFAV[check - 1])[
                  1:-2]  # nesta linha eu converto o valor da lista para str e corto as caracteres em excesso
            if cnv == '1':
                val_fav = randint(1, 5)
                # loló apagar
                print()
                print(f'Esta queen é favorita e tirou {val_fav}')
            else:
                val_fav = 0
                # loló apagar
                print()
                print('Esta queen NÃO é favorita')

            resultado_ls = sumCUNT + dado + val_fav

            if check == lst_ll[0]:
                resultado_ls1 = resultado_ls
                # apagar depois loló
                print(f'O resultado final desta pariticipante é {resultado_ls1}')

            if check == lst_ll[1]:
                resultado_ls2 = resultado_ls
                # apagar depois loló
                print(f'O resultado final desta pariticipante é {resultado_ls2}')

            # apagar depois loló
            print(f'A lista de top 2 é {lst_ll}')
            print(f'O C.U.N.T. de {bscName[check - 1]} é {bscCUNT}')
            print("e a soma destes valores é: " + str(sumCUNT))
            print(f'O valor aleatorio foi {dado}')
            print(f'Esta é a queen de número {check}')
            print(f'lista de resultados {resultado_ls}')
            # apagar até aqui

        # Determinação da campeã do Lip Sync
        if resultado_ls1 > resultado_ls2:
            lsfylg = lst_ll[0]
            # loló apagar depois
            print(f'A vencedora do LS: {top1}')

        elif resultado_ls2 >= resultado_ls1:
            lsfylg = lst_ll[1]
            # loló apagar depois
            print(f'A vencedora do LS: {top2}')

        lsfylgstr = str(lsfylg)
        sqlNAMElg = 'SELECT NAME_QUEENS FROM unofficial_season WHERE ID_QUEENS = '+lsfylgstr+''
        venclegacy = consulta(vcon, sqlNAMElg)

        # Determinação da prioridade do btm2
            #determinando a melhor track record dentro do btm2
            #chop2 é a pior
        if lst_acumulada[lst_ls[0] - 1] > lst_acumulada[lst_ls[1] - 1]:
            chop1 = lst_ls[0]
            chop2 = lst_ls[1]
        elif lst_acumulada[lst_ls[1] - 1] > lst_acumulada[lst_ls[0] - 1]:
            chop1 = lst_ls[1]
            chop2 = lst_ls[0]
        else:
            aleat = randint(0, 1)
            if aleat == 0:
                chop1 = lst_ls[1]
                chop2 = lst_ls[0]
            else:
                chop1 = lst_ls[0]
                chop2 = lst_ls[1]

        #determinando justiça
        sqlJUS = 'SELECT JUSTICA FROM unofficial_season'
        bscJUS = consulta(vcon, sqlJUS)
        jus = str(bscJUS[lsfylg - 1])[1:-2] #verifica a jus da campea e corta o valor
        if jus == "100":
            print(" a justiça da campea é 100%") #loló apagar
            eliminada = chop2
        elif jus == "75":
            print(" a justiça da campea é 75%") #loló apagar
            alejus = randint(1, 4)
            if alejus < 4:
                eliminada = chop2
            else:
                eliminada = chop1
        elif jus == "50":
            print(" a justiça da campea é 50%") #loló apagar
            alejus = randint(1, 4)
            if alejus < 3:
                eliminada = chop2
            else:
                eliminada = chop1
        elif jus == "25":
            print(" a justiça da campea é 25%") #loló apagar
            alejus = randint(1, 4)
            if alejus < 2:
                eliminada = chop2
            else:
                eliminada = chop1
        elif jus == "0":
            print(" a justiça da campea é 0%") #loló apagar
            eliminada = chop1

    elif chave_formato == 2:
        for check in lst_ls:  # lst_ls é um lista contendo os valores de ID bo bottom 2
            checkstr = str(check)

            sqlCUNT = """SELECT 
                           """ + cunt1 + """, 
                           """ + cunt2 + """, 
                           """ + cunt3 + """, 
                           """ + cunt4 + """,
                           """ + vant1 + """, 
                           """ + vant2 + """, 
                           """ + vant3 + """, 
                           """ + vant4 + """
                           FROM unofficial_season 
                           WHERE ID_QUEENS= """ + checkstr + """ """
            bscCUNT = consulta(vcon, sqlCUNT)
            sumCUNT = sum(list(map(sum, list(bscCUNT))))  # soma os valores

            dado1 = randint(0, 6)
            dado2 = randint(0, 6)
            dado = dado1 + dado2

            cnv = str(bscFAV[check - 1])[
                  1:-2]  # nesta linha eu converto o valor da lista para str e corto as caracteres em excesso
            if cnv == '1':
                val_fav = randint(1, 5)
                # loló apagar
                print()
                print(f'Esta queen é favorita e tirou {val_fav}')
            else:
                val_fav = 0
                # loló apagar
                print()
                print('Esta queen NÃO é favorita')

            resultado_ls = sumCUNT + dado + lst_acumulada[check - 1] + val_fav

            if check == lst_ls[0]:
                resultado_ls1 = resultado_ls
                # apagar depois loló
                print(f'O resultado final desta pariticipante é {resultado_ls1}')
                print(f' ela tinha {lst_acumulada[check - 1]} acumulado')

            if check == lst_ls[1]:
                resultado_ls2 = resultado_ls
                # apagar depois loló
                print(f'O resultado final desta pariticipante é {resultado_ls2}')
                print(f' ela tinha {lst_acumulada[check - 1]} acumulado')

            # apagar depois loló
            print(f'A lista de bottom 2 é {lst_ls}')
            print(f'O C.U.N.T. de {bscName[check - 1]} é {bscCUNT}')
            print("e a soma destes valores é: " + str(sumCUNT))
            print(f'O valor aleatorio foi {dado}')
            print(f'Esta é a queen de número {check}')
            print(f'lista de resultados {resultado_ls}')
            # apagar até aqui

        # Determinação da eliminada
        if resultado_ls1 > resultado_ls2:
            eliminada = lst_ls[1]
            # loló apagar depois
            print(f'A queen eliminada será: {btm2}')

        elif resultado_ls2 >= resultado_ls1:
            eliminada = lst_ls[0]
            # loló apagar depois
            print(f'A queen eliminada será: {btm1}')


def eliminacao():
    global cunt1
    global cunt2
    global cunt3
    global cunt4

    global vant1
    global vant2
    global vant3
    global vant4
    # matematica da eliminação
    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'LP'
    vant2 = 'NADA'
    vant3 = 'NADA'
    vant4 = 'NADA'


def remove_all6():  # resultado do lip sync esta aqui
    global check_ls1
    global check_ls2
    global lbl_nmep
    global f_eliminada
    global lbl_elim
    global f_lsfylg
    global lbl_venc
    global ctd_id
    global tab_elim
    global valuex
    global valuey
    global verifdb

    check_ls1 = 1
    check_ls2 = 1

    f_top1.destroy()
    f_top2.destroy()
    f_top3.destroy()
    f_btm1.destroy()
    f_btm2.destroy()
    f_btm3.destroy()
    lbl_top1.destroy()
    lbl_top2.destroy()
    lbl_top3.destroy()
    lbl_btm1.destroy()
    lbl_btm2.destroy()
    lbl_btm3.destroy()
    lbl_nmep.destroy()
    button_avanep.config(state=NORMAL)
    button_ls.config(state=DISABLED)

    if chave_formato == 1:
        lbl_nmep = tk.Label(app, text="LIP SYNC FOR YOUR LEGACY", font=fonte_padrao)
        lbl_nmep.place(x=135, y=20)

        show_top1()
        show_top2()

        eliminacao()
        soma_ls()

        lsfylgstr = str(lsfylg) #traduz o nome da lista pra str

        f_lsfylg = tk.Label(app) #imprime a campea do lip sync
        q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
        global img_lsfylg  # Image variable to display
        my_data = lsfylgstr  # ID of the row to display
        try:
            my_cursor = my_conn.execute(q, my_data)
            r_set = my_cursor.fetchone()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            img_lsfylg = ImageTk.PhotoImage(data=r_set[0])  # create image
            f_lsfylg.config(image=img_lsfylg)  # display image
            f_lsfylg.place(x=300, y=250)
            lbl_venc = tk.Label(app, text='VENCEDORA', font=fonte_padrao4, fg='blue', bg='yellow')
            lbl_venc.place(x=330, y=405)

            button_visulegacy()

    elif chave_formato == 2:
        lbl_nmep = tk.Label(app, text="LIP SYNC FOR YOUR LIFE", font=fonte_padrao)
        lbl_nmep.place(x=135, y=20)

        if dbshantay == nep:
            show_btm1()
            show_btm2()
            messagebox.showinfo('SHANTAY YOU BOTH STAY!', \
                                'Após um Lip Sync incrível, RuPaul decide salvar ambas.')
            verifdb = 0

        elif (chave_premiere == 1) and (nep == 2): #equivalente ao ep 1 sem eliminação
            messagebox.showinfo('NO ONE IS GOING HOME!',
                                'Para celebrar a Premiere, RuPaul decide não eliminar ninguém nesta semana.')
            verifdb = 3
        else: #a outra opção é dbshantay ser == 0, sendo impossivel ter 0 episodios, ele segue normal
            show_btm1()
            show_btm2()

            eliminacao()
            soma_ls()

            verifdb = 1

            eliminadastr = str(eliminada) #converte o n# de id da eliminada para str (esse valor é feito no soma_ls())

            f_eliminada = tk.Label(app)
            q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
            global img_eliminada  # Image variable to display
            my_data = eliminadastr  # ID of the row to display
            try:
                my_cursor = my_conn.execute(q, my_data)
                r_set = my_cursor.fetchone()
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
            else:
                img_eliminada = ImageTk.PhotoImage(data=r_set[0])  # create image
                f_eliminada.config(image=img_eliminada)  # display image
                f_eliminada.place(x=300, y=250)
                lbl_elim = tk.Label(app, text='ELIMINADA', font=fonte_padrao4, fg='white', bg='red')
                lbl_elim.place(x=330, y=405)

                # BOTTOM 2 ENTRANDO NA LISTA ACUMULADA (recebendo -2 pontos)
                lst_acumulada[lst_ls[0] - 1] -= 2
                lst_acumulada[lst_ls[1] - 1] -= 2
                lst_acumulada.pop(eliminada - 1) #apagando a eliminada da lst
                # loló apagar depois
                print()
                print(f'A lista de valores acumulados é: {lst_acumulada}')

            ctd_id = eliminadastr

            # COPIAR A ELIMINADA PARA A TABELA DE ELIMINADAS
            inserir_eliminida()
            tab_elim = "eliminated_queens"
            reorganizar_elim()

            # DELETAR A ELIMINADA
            deletar()
            tab_elim = "unofficial_season"
            reorganizar_elim()


def tops_n_bottons():
    global top1
    global top2
    global top3
    global bottom1
    global bottom2
    global bottom3
    global lbl_top1
    global lbl_top2
    global lbl_top3
    global lbl_btm1
    global lbl_btm2
    global lbl_btm3
    global value_foto
    global cntxt1
    global cntxt2
    global cntxt3
    global cntxt4
    global cntxb1
    global cntxb2
    global cntxb3
    global check_ls1
    global check_ls2
    global btm1
    global btm2
    global btm3
    global lst_ls
    global lst_ll
    global valuex
    global valuey
    lst_ls = [] #lst com as btm2
    lst_ll = [] #lst com as top2

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    button_visu.destroy()
    check_ls1 = 0
    check_ls2 = 0

    # matematica que verifica tops e bottoms:
    # criando lista auxiliar organizada
    lst_organizada = lst_resultados[:]

    for check in range(len(lst_organizada)):
        for check2 in range(len(lst_organizada)):
            if lst_organizada[check] <= lst_organizada[check2]:
                aux = lst_organizada[check]
                lst_organizada[check] = lst_organizada[check2]
                lst_organizada[check2] = aux

    print('************') #lolo apagar
    print(f'Lista original antes do aliviador: {lst_resultados}')
    print(f'Lista organizada antes do aliviador: {lst_organizada}')

    # aliviador de empates
    aliviador = 20
    for caliv in range(0, len(lst_organizada)):
        for caliv2 in range(0, len(lst_organizada)):
            if lst_organizada[caliv] == lst_resultados[caliv2]:
                lst_organizada[caliv] += aliviador
                lst_resultados[caliv2] += aliviador
                break
        aliviador += 20

    print('************') #lolo apagar
    print(f'Lista original depois do aliviador: {lst_resultados}')
    print(f'Lista organizada depois do aliviador: {lst_organizada}')

    # Indicador do nome dos tops and bottoms
    # top1
    cntt1 = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 1] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            top1 = str(bscName[cntt1])
            cntxt1 = cntt1 + 1
            lst_ll.append(cntxt1)  # lista de tops2
        cntt1 += 1

    # top2
    cntt2 = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 2] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            top2 = str(bscName[cntt2])
            cntxt2 = cntt2 + 1
            lst_ll.append(cntxt2)  # lista de tops2
        cntt2 += 1

    # top3
    cntt3 = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 3] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            top3 = str(bscName[cntt3])
            cntxt3 = cntt3 + 1
        cntt3 += 1

    # btm1
    cntb1 = 0
    for value in lst_resultados:
        if lst_organizada[0] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm1 = str(bscName[cntb1])
            cntxb1 = cntb1 + 1
            lst_ls.append(cntxb1) #lista de btm
        cntb1 += 1

    # btm2
    cntb2 = 0
    for value in lst_resultados:
        if lst_organizada[1] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm2 = str(bscName[cntb2])
            cntxb2 = cntb2 + 1
            lst_ls.append(cntxb2)
        cntb2 += 1

    # btm3
    cntb3 = 0
    for value in lst_resultados:
        if lst_organizada[2] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm3 = str(bscName[cntb3])
            cntxb3 = cntb3 + 1
        cntb3 += 1

    # verificar o tamho do cast pra decidir se serão top3/btm3 ou top2/btm2
    sqlLeng = 'SELECT NAME_QUEENS FROM unofficial_season'
    bscLeng = consulta(vcon, sqlLeng)

    if len(bscLeng) >= 7:
        # lbls para escrever tops e bottoms e imprimir foto
        if (chave_formato == 1) or (chave_formato == 3):
            lbl_top1 = tk.Label(app, text='TOP 2: ' + top1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
        else:
            lbl_top1 = tk.Label(app, text='WINNER: ' + top1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')

        lbl_top1.place(x=10, y=215)
        valuex = 10
        valuey = 60
        show_top1()

        if (chave_formato == 1) or (chave_formato == 3):
            lbl_top2 = tk.Label(app, text='TOP 2: ' + top2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
        else:
            lbl_top2 = tk.Label(app, text='HIGH: ' + top2[2:-3], font=fonte_padrao4, fg='blue')
        lbl_top2.place(x=290, y=215)
        valuex = 290
        valuey = 60
        show_top2()

        lbl_top3 = tk.Label(app, text='HIGH: ' + top3[2:-3], font=fonte_padrao4, fg='blue')
        lbl_top3.place(x=560, y=215)  # o X tem que ser 30 menos pra n sair da tela
        show_top3()

        lbl_btm1 = tk.Label(app, text='BOTTOM 2: ' + btm1[2:-3], font=fonte_padrao4, fg='white', bg='red')
        lbl_btm1.place(x=10, y=415)
        valuex = 10
        valuey = 260
        show_btm1()

        lbl_btm2 = tk.Label(app, text='BOTTOM 2: ' + btm2[2:-3], font=fonte_padrao4, fg='white', bg='red')
        lbl_btm2.place(x=290, y=415)
        valuex = 290
        valuey = 260
        show_btm2()

        lbl_btm3 = tk.Label(app, text='LOW: ' + btm3[2:-3], font=fonte_padrao4, fg='blue')
        lbl_btm3.place(x=560, y=415)
        show_btm3()

    else:
        if (chave_formato == 1) or (chave_formato == 3):
            lbl_top1 = tk.Label(app, text='TOP 2: ' + top1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
        else:
            lbl_top1 = tk.Label(app, text='WINNER: ' + top1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
        lbl_top1.place(x=160, y=215)
        valuex = 160
        valuey = 60
        show_top1()

        if (chave_formato == 1) or (chave_formato == 3):
            lbl_top2 = tk.Label(app, text='TOP 2: ' + top2[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
        else:
            lbl_top2 = tk.Label(app, text='HIGH: ' + top2[2:-3], font=fonte_padrao4, fg='blue')
        lbl_top2.place(x=440, y=215)
        valuex = 440
        valuey = 60
        show_top2()

        lbl_btm1 = tk.Label(app, text='BOTTOM 2: ' + btm1[2:-3], font=fonte_padrao4, fg='white', bg='red')
        lbl_btm1.place(x=160, y=415)
        valuex = 160
        valuey = 260
        show_btm1()

        lbl_btm2 = tk.Label(app, text='BOTTOM 2: ' + btm2[2:-3], font=fonte_padrao4, fg='white', bg='red')
        lbl_btm2.place(x=440, y=415)
        valuex = 440
        valuey = 260
        show_btm2()

    # BOTÃO LIP-SYNC
    global button_ls

    button_ls = tkinter.Button(app, text="LIP SYNC", font=fonte_padrao, command=remove_all6) #esse botão chama o lipsync
    button_ls.place(x=10, y=475, width=190)
    button_ls.config(state=NORMAL)


def button_visulegacy():
    global button_legacy

    button_legacy = tkinter.Button(app, text="DECISÃO", font=fonte_padrao, command=remove_all7)
    button_legacy.place(x=545, y=475, width=190)


def remove_all7():
    global lbl_chop
    global lbl_elim
    global f_eliminada
    global tab_elim
    global ctd_id
    global verifdb

    button_legacy.destroy()

    if chave_formato == 1:
        f_lsfylg.destroy()
        lbl_venc.destroy()
        f_top1.destroy()
        f_top2.destroy()
        lbl_lp1.destroy()
        lbl_lp2.destroy()

    venclegacystr = str(venclegacy)
    lbl_chop = tk.Label(app, text=venclegacystr[3:-4] + ' decidiu eliminar...', font=fonte_padrao)
    lbl_chop.place(x=100, y=100)

    # BOTTOM 2 ENTRANDO NA LISTA ACUMULADA (recebendo -2 pontos)
    lst_acumulada[lst_ls[0] - 1] -= 2
    lst_acumulada[lst_ls[1] - 1] -= 2

    # loló apagar depois
    print()
    print(f'A lista de valores acumulados é: {lst_acumulada}')

    if dbshantay == nep:
        messagebox.showinfo('ESPERE! ESPERE!',
            f'RuPaul decide que ninguém irá para casa hoje! {venclegacystr[3:-4]} não revela o nome da eliminada')
        verifdb = 0
    elif (chave_premiere == 1) and (nep == 2):
        messagebox.showinfo('NO ONE IS GOING HOME!',
        f'Para celebrar a Premiere, não haverá eliminação! {venclegacystr[3:-4]} não revela o nome da eliminada')
        verifdb = 0
    else:
        verifdb = 1
        eliminadastr = str(eliminada)
        ctd_id = eliminadastr

        #imprimindo foto da eliminada
        nome_elim = "SELECT NAME_QUEENS FROM unofficial_season WHERE ID_QUEENS = "+eliminadastr+""
        nome_elim2 = consulta(vcon, nome_elim)
        nome_elim3 = str(nome_elim2)

        f_eliminada = tk.Label(app)
        q = "SELECT PHOTO FROM unofficial_season WHERE ID_QUEENS=?"
        global img_eliminada  # Image variable to display
        my_data = eliminadastr  # ID of the row to display
        try:
            my_cursor = my_conn.execute(q, my_data)
            r_set = my_cursor.fetchone()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            img_eliminada = ImageTk.PhotoImage(data=r_set[0])  # create image
            f_eliminada.config(image=img_eliminada)  # display image
            f_eliminada.place(x=300, y=150)
            lbl_elim = tk.Label(app, text=nome_elim3[3:-4], font=fonte_padrao4, fg='white', bg='red')
            lbl_elim.place(x=330, y=305)

        lst_acumulada.pop(eliminada - 1)  # apagando a eliminada da lst

        # COPIAR A ELIMINADA PARA A TABELA DE ELIMINADAS
        inserir_eliminida()
        tab_elim = "eliminated_queens"
        reorganizar_elim()

        # DELETAR A ELIMINADA
        deletar()
        tab_elim = "unofficial_season"
        reorganizar_elim()


# --------------------------------- AVANÇAR EPISODIOS --------------------------------------
def avan_ep():
    global nep

    if lst_escolhas[nep - 1] == 'Show de Talentos':
        show_de_talentos()
    elif lst_escolhas[nep - 1] == 'Girl Group':
        girl_group()
    elif lst_escolhas[nep - 1] == 'Rumix':
        rumix()
    elif lst_escolhas[nep - 1] == 'Atuação':
        atuacao()
    elif lst_escolhas[nep - 1] == 'Baile':
        baile()
    elif lst_escolhas[nep - 1] == 'Snatch Game':
        snatch_game()
    elif lst_escolhas[nep - 1] == 'Rusical':
        rusical()
    elif lst_escolhas[nep - 1] == 'Roast':
        roast()
    elif lst_escolhas[nep - 1] == 'Desing de Moda':
        design()
    elif lst_escolhas[nep - 1] == 'Comercial':
        comercial()
    elif lst_escolhas[nep - 1] == 'Make-Over':
        make_over()
    elif lst_escolhas[nep - 1] == 'Programa de TV (ao-vivo)':
        morning_show()
    elif lst_escolhas[nep - 1] == 'DragLympics':
        draglympic()
    elif lst_escolhas[nep - 1] == 'Dança Coreografada':
        danca_core()
    elif lst_escolhas[nep - 1] == 'Runway':
        runway()
    elif lst_escolhas[nep - 1] == "Canto":
        canto()
    elif lst_escolhas[nep - 1] == "Stand-Up":
        stand_up()
    elif lst_escolhas[nep - 1] == 'GRAND FINALE':
        grand_finale()
    nep += 1


def avan_epX():
    global nep

    lbl_nmep.destroy()

    if chave_formato == 1:
        lbl_chop.destroy()
        if verifdb == 1:
            lbl_elim.destroy()
            f_eliminada.destroy()

    elif chave_formato == 2:
        if (verifdb == 0) or (verifdb == 1):
            f_btm1.destroy()
            f_btm2.destroy()
            lbl_lp1.destroy()
            lbl_lp2.destroy()
        if verifdb == 1:
            f_eliminada.destroy()
            lbl_elim.destroy()

    button_avanep.config(state=DISABLED)

    avan_ep()


# ____________________________________________________________________________________________
def button_fechartudo():
    button_fechar = tkinter.Button(app, text="SAIR", font=fonte_padrao, command=app.destroy)
    button_fechar.place(x=545, y=475, width=190)


def disable_event():
    pass


app.mainloop()
