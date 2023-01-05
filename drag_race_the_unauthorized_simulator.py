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


def open():
    print()


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
    lst_formato = ["Lip-Sync Assassin", "Lip-Sync For Your Legacy", "Lip-Sync For Your Life", "No-Elimination", ""]

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
    lst_finale = ["Lip-Sync SmackDown",
                  "TOP 3 Performances",
                  "TOP 3 Rumix/Lip-Sync for the Crown",
                  "TOP 3 Rumix (Ru Chops Someone) TOP 2 LSFTC",
                  "TOP 4 Rumix/Individual Lip-Syncs",
                  "TOP 5 Performances/Top 2 LSFTC", ""]

    lbl_formafi = Label(app, text='Formato da Final: ', anchor=S, font=fonte_padrao)
    lbl_formafi.place(x=160, y=240, width=325, height=30)

    combo_formafi = ttk.Combobox(app, values=lst_finale, state='readonly')
    combo_formafi.current(6)
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
    lst_shantay = ["Surpresa", "Não",
                   "Sim",
                   ""]

    lbl_shantay = Label(app, text='Double-Shantay: ', anchor=S, font=fonte_padrao)
    lbl_shantay.place(x=165, y=290, width=325, height=30)

    combo_shantay = ttk.Combobox(app, values=lst_shantay, state='readonly')
    combo_shantay.current(3)
    combo_shantay.place(x=450, y=290, width=240, height=30)
    combo_shantay.bind('<<ComboboxSelected>>', design_shantay)
    combo_shantay.config(state=DISABLED)

    # Double Elimination
    lst_elim = ["Surpresa",
                "Sim",
                "Não", ""]

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
    elif combo_temp.get() == lst_seasons[1]:  # if it is the second item
        print('Option 2 is selected')
    elif combo_temp.get() == lst_seasons[2]:  # if it is the second item
        print('Option 2 is selected')
    elif combo_temp.get() == lst_seasons[3]:  # if it is the second item
        print('Option 2 is selected')
    elif combo_temp.get() == lst_seasons[4]:
        tb_temporada = 'drus_s14'
        limpar(), show_data(), show_data2(), show_data3(), show_data4(), show_data5(), show_data6(), show_data7(),
        show_data8(), show_data9(), show_data10(), show_data11(), show_data12(), show_data13(), show_data14(),
        ocultar_but()


app = Tk()
app.title('DRAG RACE - UNOFFICIAL SIMULATOR')
app.geometry('820x480+265+125')  # a,b,c,d altura, largura e os outros dois são a posição que vai aparecer na tela
app.resizable(False, False)

fonte_padrao = font.Font(family='Cooper Black', size=14, weight='bold')
fonte_padrao2 = font.Font(family='Cooper Black', size=12)
fonte_padrao3 = font.Font(family='Cooper Black', size=14)
fonte_padrao4 = font.Font(family='Arial', size=12)

lst_seasons = ["RuPaul's Drag Race - Season 1", "RuPaul's Drag Race - Season 2", "RuPaul's Drag Race - Season 3",
               "RuPaul's Drag Race - Season 4", "RuPaul's Drag Race - Season 14", " "]  # creating option list
lst_desafios = ["Atuação", "Baile", "Campanha Presidencial", "Comercial", "Concurso de Beleza", "Dança Coreografada",
                "Desing de Moda", "Discurso de Formatura", "DragLympics", "Entrega de Prêmios (Awards)", "Girl Group",
                "Make-Over", "Painel de Discussão (DragCon)", "Programa de TV (ao-vivo)",
                "Projetar e Apresentar Evento",
                "Roast", "Rumix", "Rusical", "Show de Talentos", "Snatch Game", "Snatch Game of Love", "Stand-Up",
                "Lip-Sync LaLaPaRuza Smackdown", " "]
lst_escolhas = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

cunt1 = cunt2 = cunt3 = cunt4 = str()
vant1 = vant2 = vant3 = vant4 = str()

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


# button_testes.place(x=745, y=440)


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
        ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV, MAQUIAG, MODA, PERFORM, LP_DANC, LP_EMOTIV, LP_TEATRAL, 
        FAVORITA, JUSTICA) 
        select PHOTO, NAME_QUEENS, CHARISMA, UNIQUENESS, NERVE, TALENT, ATUACAO, CANTO, COMEDIA, COSTURA, DANCA, IMPROV,
        MAQUIAG, MODA, PERFORM, LP_DANC, LP_EMOTIV, LP_TEATRAL, FAVORITA, JUSTICA from """ + tb_temporada + """
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
    if combo_formato.get() == lst_formato[2]:
        chave_formato = 2
        print(chave_formato)


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
        button_desaf.config(state=NORMAL)
    else:
        print()
    if combo_elim.get() == lst_elim[1]:
        chave_elim = 1
        print(chave_elim)
    elif combo_elim.get() == lst_elim[0]:
        chave_elim = 0
        print(chave_elim)
    elif combo_elim.get() == lst_elim[2]:
        chave_elim = 2
        print(chave_elim)
    else:
        chave_elim = 999


def design_shantay(event):
    global chave_shantay
    if combo_shantay.get() == lst_shantay[2]:  # add 1
        chave_shantay = 2
        print(chave_shantay)
    elif combo_shantay.get() == lst_shantay[0]:  # add 1
        chave_shantay = 0
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

    # COMBOS DOS DESAFIOS
    combo_ep1 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep1.current(23)
    combo_ep1.place(x=150, y=30, width=190, height=30)  # colocando na tela
    combo_ep1.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep1 = tk.Label(app, text='Episódio 1: ', font=fonte_padrao)
    lbl_ep1.place(x=10, y=30)

    combo_ep2 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep2.current(23)
    combo_ep2.place(x=150, y=80, width=190, height=30)  # colocando na tela
    combo_ep2.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep2 = tk.Label(app, text='Episódio 2: ', font=fonte_padrao)
    lbl_ep2.place(x=10, y=80)

    combo_ep3 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep3.current(23)
    combo_ep3.place(x=150, y=130, width=190, height=30)  # colocando na tela
    combo_ep3.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep3 = tk.Label(app, text='Episódio 3: ', font=fonte_padrao)
    lbl_ep3.place(x=10, y=130)

    combo_ep4 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep4.current(23)
    combo_ep4.place(x=150, y=180, width=190, height=30)  # colocando na tela
    combo_ep4.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep4 = tk.Label(app, text='Episódio 4: ', font=fonte_padrao)
    lbl_ep4.place(x=10, y=180)

    combo_ep5 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep5.current(23)
    combo_ep5.place(x=150, y=230, width=190, height=30)  # colocando na tela
    combo_ep5.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep5 = tk.Label(app, text='Episódio 5: ', font=fonte_padrao)
    lbl_ep5.place(x=10, y=230)

    combo_ep6 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep6.current(23)
    combo_ep6.place(x=150, y=280, width=190, height=30)  # colocando na tela
    combo_ep6.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep6 = tk.Label(app, text='Episódio 6: ', font=fonte_padrao)
    lbl_ep6.place(x=10, y=280)

    combo_ep7 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep7.current(23)
    combo_ep7.place(x=150, y=330, width=190, height=30)  # colocando na tela
    combo_ep7.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep7 = tk.Label(app, text='Episódio 7: ', font=fonte_padrao)
    lbl_ep7.place(x=10, y=330)

    combo_ep8 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep8.current(23)
    combo_ep8.place(x=150, y=380, width=190, height=30)  # colocando na tela
    combo_ep8.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep8 = tk.Label(app, text='Episódio 8: ', font=fonte_padrao)
    lbl_ep8.place(x=10, y=380)

    combo_ep9 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep9.current(23)
    combo_ep9.place(x=150, y=430, width=190, height=30)  # colocando na tela
    combo_ep9.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep9 = tk.Label(app, text='Episódio 9: ', font=fonte_padrao)
    lbl_ep9.place(x=10, y=430)

    combo_ep10 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep10.current(23)
    combo_ep10.place(x=150, y=480, width=190, height=30)  # colocando na tela
    combo_ep10.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep10 = tk.Label(app, text='Episódio 10: ', font=fonte_padrao)
    lbl_ep10.place(x=10, y=480)

    combo_ep11 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep11.current(23)
    combo_ep11.place(x=525, y=30, width=190, height=30)  # colocando na tela
    combo_ep11.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep11 = tk.Label(app, text='Episódio 11: ', font=fonte_padrao)
    lbl_ep11.place(x=375, y=30)

    combo_ep12 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep12.current(23)
    combo_ep12.place(x=525, y=80, width=190, height=30)  # colocando na tela
    combo_ep12.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep12 = tk.Label(app, text='Episódio 12: ', font=fonte_padrao)
    lbl_ep12.place(x=375, y=80)

    combo_ep13 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep13.current(23)
    combo_ep13.place(x=525, y=130, width=190, height=30)  # colocando na tela
    combo_ep13.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep13 = tk.Label(app, text='Episódio 13: ', font=fonte_padrao)
    lbl_ep13.place(x=375, y=130)

    combo_ep14 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep14.current(23)
    combo_ep14.place(x=525, y=180, width=190, height=30)  # colocando na tela
    combo_ep14.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep14 = tk.Label(app, text='Episódio 14: ', font=fonte_padrao)
    lbl_ep14.place(x=375, y=180)

    combo_ep15 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep15.current(23)
    combo_ep15.place(x=525, y=230, width=190, height=30)  # colocando na tela
    combo_ep15.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep15 = tk.Label(app, text='Episódio 15: ', font=fonte_padrao)
    lbl_ep15.place(x=375, y=230)

    combo_ep16 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep16.current(23)
    combo_ep16.place(x=525, y=280, width=190, height=30)  # colocando na tela
    combo_ep16.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep16 = tk.Label(app, text='Episódio 16: ', font=fonte_padrao)
    lbl_ep16.place(x=375, y=280)

    combo_ep17 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep17.current(23)
    combo_ep17.place(x=525, y=330, width=190, height=30)  # colocando na tela
    combo_ep17.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep17 = tk.Label(app, text='Episódio 17: ', font=fonte_padrao)
    lbl_ep17.place(x=375, y=330)

    combo_ep18 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep18.current(23)
    combo_ep18.place(x=525, y=380, width=190, height=30)  # colocando na tela
    combo_ep18.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep18 = tk.Label(app, text='Episódio 18: ', font=fonte_padrao)
    lbl_ep18.place(x=375, y=380)

    combo_ep19 = ttk.Combobox(app, values=lst_desafios, state='readonly')  # creating a combobox
    combo_ep19.current(23)
    combo_ep19.place(x=525, y=430, width=190, height=30)  # colocando na tela
    combo_ep19.bind('<<ComboboxSelected>>', ordem_desaf)

    lbl_ep19 = tk.Label(app, text='Episódio 19: ', font=fonte_padrao)
    lbl_ep19.place(x=375, y=430)

    # BOTÃO VOLTAR DESAFIOS
    #but_voltd = tkinter.Button(app, text="Voltar", font=fonte_padrao, command=remove_all4)
    #but_voltd.place(x=610, y=490)

    # BOTÃO AVANÇAR DESAFIOS
    button_avan = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=remove_all5)
    button_avan.place(x=525, y=475, width=190)


    # FIXANDO A PREMIERE
    if chave_premiere == 2:  # design com eliminação
        combo_ep1.current(6)
        combo_ep2.current(6)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[6]
        lst_escolhas[1] = lst_desafios[6]

    if chave_premiere == 3:  # girl group - no elim
        combo_ep1.current(10)
        combo_ep2.current(10)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[10]
        lst_escolhas[1] = lst_desafios[10]

    if chave_premiere == 4:  # show de talentos - no elim
        combo_ep1.current(18)
        combo_ep2.current(18)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[18]
        lst_escolhas[1] = lst_desafios[18]

    if chave_premiere == 5:  # premiere tripla - no elim
        combo_ep1.current(22)
        combo_ep2.current(18)
        combo_ep3.current(18)
        combo_ep1.config(state=DISABLED)
        combo_ep2.config(state=DISABLED)
        combo_ep3.config(state=DISABLED)
        lst_escolhas[0] = lst_desafios[22]
        lst_escolhas[1] = lst_desafios[18]
        lst_escolhas[2] = lst_desafios[18]

    # DEFININDO N# DE EPISÓDIOS
    check_queens = 'SELECT NAME_QUEENS from unofficial_season'
    total_queens = consulta(vcon, check_queens)

    # formato da final
    if (chave_finale == 0) or (chave_finale == 4):  # ls smackdown
        num_ep = len(total_queens) - 4
    if (chave_finale == 1) or (chave_finale == 2) or (chave_finale == 3):
        num_ep = len(total_queens) - 3
    if chave_finale == 5:
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
    if chave_shantay == 2:
        num_ep += 1
    if chave_shantay == 0:
        randsh = randint(0, 1)
        num_ep += randsh
        if randsh == 0:
            print('Não haverá double-shantay')
        else:
            print('Haverá double-shantay')

    # double-elim
    if chave_elim == 1:
        num_ep -= 1
    if chave_elim == 0:
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
            combo_ep2.current(16)
            combo_ep2.config(state=DISABLED)
            combo_ep3.set('GRAND FINALE')
            lst_escolhas[2] = 'GRAND FINALE'
        elif num_ep == 3:
            combo_ep3.current(16)
            combo_ep3.config(state=DISABLED)
            combo_ep4.set('GRAND FINALE')
            lst_escolhas[3] = 'GRAND FINALE'
        elif num_ep == 4:
            combo_ep4.current(16)
            combo_ep4.config(state=DISABLED)
            combo_ep5.set('GRAND FINALE')
            lst_escolhas[4] = 'GRAND FINALE'
        elif num_ep == 5:
            combo_ep5.current(16)
            combo_ep5.config(state=DISABLED)
            combo_ep6.set('GRAND FINALE')
            lst_escolhas[5] = 'GRAND FINALE'
        elif num_ep == 6:
            combo_ep6.current(16)
            combo_ep6.config(state=DISABLED)
            combo_ep7.set('GRAND FINALE')
            lst_escolhas[6] = 'GRAND FINALE'
        elif num_ep == 7:
            combo_ep7.current(16)
            combo_ep7.config(state=DISABLED)
            combo_ep8.set('GRAND FINALE')
            lst_escolhas[7] = 'GRAND FINALE'
        elif num_ep == 8:
            combo_ep8.current(16)
            combo_ep8.config(state=DISABLED)
            combo_ep9.set('GRAND FINALE')
            lst_escolhas[8] = 'GRAND FINALE'
        elif num_ep == 9:
            combo_ep9.current(16)
            combo_ep9.config(state=DISABLED)
            combo_ep10.set('GRAND FINALE')
            lst_escolhas[9] = 'GRAND FINALE'
        elif num_ep == 10:
            combo_ep10.current(16)
            combo_ep10.config(state=DISABLED)
            combo_ep11.set('GRAND FINALE')
            lst_escolhas[10] = 'GRAND FINALE'
        elif num_ep == 11:
            combo_ep11.current(16)
            combo_ep11.config(state=DISABLED)
            combo_ep12.set('GRAND FINALE')
            lst_escolhas[11] = 'GRAND FINALE'
        elif num_ep == 12:
            combo_ep12.current(16)
            combo_ep12.config(state=DISABLED)
            combo_ep13.set('GRAND FINALE')
            lst_escolhas[12] = 'GRAND FINALE'
        elif num_ep == 13:
            combo_ep13.current(16)
            combo_ep13.config(state=DISABLED)
            combo_ep14.set('GRAND FINALE')
            lst_escolhas[13] = 'GRAND FINALE'
        elif num_ep == 14:
            combo_ep14.current(16)
            combo_ep14.config(state=DISABLED)
            combo_ep15.set('GRAND FINALE')
            lst_escolhas[14] = 'GRAND FINALE'
        elif num_ep == 15:
            combo_ep15.current(16)
            combo_ep15.config(state=DISABLED)
            combo_ep16.set('GRAND FINALE')
            lst_escolhas[15] = 'GRAND FINALE'
        elif num_ep == 16:
            combo_ep16.current(16)
            combo_ep16.config(state=DISABLED)
            combo_ep17.set('GRAND FINALE')
            lst_escolhas[16] = 'GRAND FINALE'
        elif num_ep == 17:
            combo_ep17.current(16)
            combo_ep17.config(state=DISABLED)
            combo_ep18.set('GRAND FINALE')
            lst_escolhas[17] = 'GRAND FINALE'
        elif num_ep == 18:
            combo_ep18.current(16)
            combo_ep18.config(state=DISABLED)
            combo_ep19.set('GRAND FINALE')
            lst_escolhas[18] = 'GRAND FINALE'

    if (chave_semi == 3) or (chave_semi == 2):
        if num_ep == 2:
            combo_ep3.set('GRAND FINALE')
            combo_ep3.config(state=DISABLED)
        elif num_ep == 3:
            combo_ep4.set('GRAND FINALE')
            combo_ep4.config(state=DISABLED)
        elif num_ep == 4:
            combo_ep5.set('GRAND FINALE')
            combo_ep5.config(state=DISABLED)
        elif num_ep == 5:
            combo_ep6.set('GRAND FINALE')
            combo_ep6.config(state=DISABLED)
        elif num_ep == 6:
            combo_ep7.set('GRAND FINALE')
            combo_ep7.config(state=DISABLED)
        elif num_ep == 7:
            combo_ep8.set('GRAND FINALE')
            combo_ep8.config(state=DISABLED)
        elif num_ep == 8:
            combo_ep9.set('GRAND FINALE')
            combo_ep9.config(state=DISABLED)
        elif num_ep == 9:
            combo_ep10.set('GRAND FINALE')
            combo_ep10.config(state=DISABLED)
        elif num_ep == 10:
            combo_ep11.set('GRAND FINALE')
            combo_ep11.config(state=DISABLED)
        elif num_ep == 11:
            combo_ep12.set('GRAND FINALE')
            combo_ep12.config(state=DISABLED)
        elif num_ep == 12:
            combo_ep13.set('GRAND FINALE')
            combo_ep13.config(state=DISABLED)
        elif num_ep == 13:
            combo_ep14.set('GRAND FINALE')
            combo_ep14.config(state=DISABLED)
        elif num_ep == 14:
            combo_ep15.set('GRAND FINALE')
            combo_ep15.config(state=DISABLED)
        elif num_ep == 15:
            combo_ep16.set('GRAND FINALE')
            combo_ep16.config(state=DISABLED)
        elif num_ep == 16:
            combo_ep17.set('GRAND FINALE')
            combo_ep17.config(state=DISABLED)
        elif num_ep == 17:
            combo_ep18.set('GRAND FINALE')
            combo_ep18.config(state=DISABLED)
        elif num_ep == 18:
            combo_ep19.set('GRAND FINALE')
            combo_ep19.config(state=DISABLED)


def ordem_desaf(event):
    # SALVANDO OS DESAF NA LISTA
    for check in range(0, 23):
        if combo_ep1.get() == lst_desafios[check]:
            lst_escolhas[0] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep2.get() == lst_desafios[check]:
            lst_escolhas[1] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep3.get() == lst_desafios[check]:
            lst_escolhas[2] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep4.get() == lst_desafios[check]:
            lst_escolhas[3] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep5.get() == lst_desafios[check]:
            lst_escolhas[4] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep6.get() == lst_desafios[check]:
            lst_escolhas[5] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep7.get() == lst_desafios[check]:
            lst_escolhas[6] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep8.get() == lst_desafios[check]:
            lst_escolhas[7] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep9.get() == lst_desafios[check]:
            lst_escolhas[8] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep10.get() == lst_desafios[check]:
            lst_escolhas[9] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep11.get() == lst_desafios[check]:
            lst_escolhas[10] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep12.get() == lst_desafios[check]:
            lst_escolhas[11] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep13.get() == lst_desafios[check]:
            lst_escolhas[12] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep14.get() == lst_desafios[check]:
            lst_escolhas[13] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep15.get() == lst_desafios[check]:
            lst_escolhas[14] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep16.get() == lst_desafios[check]:
            lst_escolhas[15] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep17.get() == lst_desafios[check]:
            lst_escolhas[16] = lst_desafios[check]

    for check in range(0, 23):
        if combo_ep18.get() == lst_desafios[check]:
            lst_escolhas[17] = lst_desafios[check]

    for check in range(0, 23):
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
    #loló também verificar se soma aumenta ao passar dos episódios
    nep += 1
    avan_ep()

    # BOTÃO AVANÇAR ENTRE EPISÓDIOS
    button_avanep = tkinter.Button(app, text="AVANÇAR", font=fonte_padrao, command=avan_epX)
    button_avanep.place(x=525, y=475, width=190)


def avan_ep():
    global nep

    if lst_escolhas[nep-1] == 'Show de Talentos':
        show_de_talentos()
    if lst_escolhas[nep-1] == 'Girl Group':
        girl_group()
    nep += 1


def avan_epX():
    global nep

    lbl_dsc1.destroy()
    lbl_dsc2.destroy()
    lbl_dsc3.destroy()
    lbl_nmep.destroy()

    if lst_escolhas[nep-1] == 'Show de Talentos':
        show_de_talentos()
    if lst_escolhas[nep-1] == 'Girl Group':
        girl_group()
    nep += 1


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

        #aliviador de empates
        if check >= 2:
            for value in range(0, len(lst_resultados)):
                if resultado_final == lst_resultados[value]:
                    resultado_final += 1

        if check >= 2:
            for value in reversed(range(len(lst_resultados), 0)):
                if resultado_final == lst_resultados[value]:
                    resultado_final += 1

        lst_resultados.append(resultado_final)

        print(f'depois do aliviador {lst_resultados}')

        # apagar depois loló
        print(f'O C.U.N.T. de {bscName[check - 1]} é {bscCUNT}')
        print("e a soma destes valores é: " + str(sumCUNT))
        print(f'O valor aleatorio foi {dado}')
        print(f'O resultado final desta pariticipante é {resultado_final}')
        print(f'Esta é a queen de número {check}')
        print(f'lista de resultados {lst_resultados}')
        # apagar até aqui



# --------------------------------- TODOS OS DESAFIOS -------------------------------------

def num_episodio():
    global lbl_nep
    global lbl_nmep

    lbl_nep = tk.Label(app, text="EPISÓDIO: ",
                        font=fonte_padrao)
    lbl_nep.place(x=10, y=20)

    nmep = str(nep)

    lbl_nmep = tk.Label(app, text=nmep + "  -  " + lst_escolhas[nep-1],
                       font=fonte_padrao)
    lbl_nmep.place(x=135, y=20)


def visu_resu():
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

    lbl_dsc1 = tk.Label(app, text ="Neste desafio, as participantes de Drag Race Unauthorized",
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
    # tipo: Performance

    cunt1 = 'CHARISMA'
    cunt2 = 'UNIQUENESS'
    cunt3 = 'NERVE'
    cunt4 = 'TALENT'

    vant1 = 'PERFORM'
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


# --------------------------------- TOPS AND BOTTONS --------------------------------------
def foto_tnb():
    if cntx == 1:
        show_data()
    elif cntx == 2:
        show_data2()
    elif cntx == 3:
        show_data3()
    elif cntx == 4:
        show_data4()
    elif cntx == 5:
        show_data5()
    elif cntx == 6:
        show_data6()
    elif cntx == 7:
        show_data7()
    elif cntx == 8:
        show_data8()
    elif cntx == 9:
        show_data9()
    elif cntx == 10:
        show_data10()
    elif cntx == 11:
        show_data11()
    elif cntx == 12:
        show_data12()
    elif cntx == 13:
        show_data13()
    elif cntx == 14:
        show_data14()
    elif cntx == 15:
        show_data15()
    elif cntx == 16:
        show_data16()


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
    global cntx

    #matematica que verifica tops e bottoms:
    #criando lista auxiliar organizada
    lst_organizada = lst_resultados[:]

    for check in range(len(lst_organizada)):
        for check2 in range(len(lst_organizada)):
            if lst_organizada[check] <= lst_organizada[check2]:
                aux = lst_organizada[check]
                lst_organizada[check] = lst_organizada[check2]
                lst_organizada[check2] = aux

    #Indicador do nome dos tops and bottoms
    #top1
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 1] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
           # print()
           # print(f'O nome da Queen com o valor final da lista {lst_organizada[len(lst_organizada)-1]} é {bscName[cnt1]}')
            top1 = str(bscName[cntx])
        cntx += 1

    #top2
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 2] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            top2 = str(bscName[cntx])
        cntx += 1

    #top3
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[len(lst_organizada) - 3] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            top3 = str(bscName[cntx])
        cntx += 1

    #btm1
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[0] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm1 = str(bscName[cntx])
        cntx += 1

    #btm2
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[1] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm2 = str(bscName[cntx])
        cntx += 1

    #btm3
    cntx = 0
    for value in lst_resultados:
        if lst_organizada[2] == value:
            sqlNAME = 'SELECT NAME_QUEENS FROM unofficial_season'
            bscName = consulta(vcon, sqlNAME)
            btm3 = str(bscName[cntx])
        cntx += 1

    #lbls para tops e bottoms
    #para não esquecer, o codigo da foto vai ser recolocado todas as vezes value_foto = cnt e foto_tnb()
    lbl_top1 = tk.Label(app, text='WINNER: ' + top1[2:-3], font=fonte_padrao4, bg='yellow', fg='blue')
    lbl_top1.place(x=10, y=280)

    lbl_top2 = tk.Label(app, text='HIGH: ' + top2[2:-3], font=fonte_padrao4, fg='blue')
    lbl_top2.place(x=10, y=310)

    lbl_top3 = tk.Label(app, text='HIGH: ' + top3[2:-3], font=fonte_padrao4, fg='blue')
    lbl_top3.place(x=10, y=340)

    lbl_btm1 = tk.Label(app, text='BOTTOM 2: ' + btm1[2:-3], font=fonte_padrao4, fg='white', bg='red')
    lbl_btm1.place(x=10, y=370)

    lbl_btm2 = tk.Label(app, text='BOTTOM 2: ' + btm2[2:-3], font=fonte_padrao4, fg='white', bg='red')
    lbl_btm2.place(x=10, y=400)

    lbl_btm3 = tk.Label(app, text='LOW: ' + btm3[2:-3], font=fonte_padrao4, fg='blue')
    lbl_btm3.place(x=10, y=430)

    #loló apagar isso depois
    print()
    print(f'A lista normal é {lst_resultados}')
    print(f'A lista organizada é {lst_organizada}')


app.mainloop()
