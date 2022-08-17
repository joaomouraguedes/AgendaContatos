from tkinter import *
from tkinter import ttk
from dados import *
from tkinter import messagebox

#---------------------------------------------------------------------------
# GUI

root = Tk()
root.title('Agenda')
root.geometry('460x480')
root['bg'] = '#000000'
root.resizable(False,False)
frame_tabela = Frame(root, width=430, height=250, bg='white', relief="flat")

global tree

#--------------------------------------------------------------------------
# Funções
    # Inserir dados

def inserir():
    nome = textbox1.get()
    telefone = textbox2.get()
    email = textbox3.get()

    dados = [nome, telefone, email]

    if nome == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Preencha todos os campos')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Adicionados com sucesso')

        textbox1.delete(0, 'end')
        textbox2.delete(0, 'end')
        textbox3.delete(0, 'end')

        mostrar_dados()   

    # Atualizar
def atualizar():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']

        nome = tree_lista[0]
        telefone = str(tree_lista[1])
        email = tree_lista[2]

        textbox1.insert(0, nome)
        textbox2.insert(0, telefone)
        textbox3.insert(0, email)

        def confirmar():
            nome = textbox1.get()
            telefone_novo = textbox2.get()
            email = textbox3.get()

            dados = [nome, telefone_novo, email]

            atualizar_dados(dados)

            messagebox.showinfo('Dados', 'Atualizados com sucesso')

            textbox1.delete(0, 'end')
            textbox2.delete(0, 'end')
            textbox3.delete(0, 'end')

            btn5.destroy()

            mostrar_dados() 

        btn5 = Button(root, command=confirmar, text='Confirmar', height=1, width=8)
        btn5.place(x=145, y=120)
    except:
         messagebox.showwarning('Dados', 'Por favor selecione uma informacao na tabela')
         
    #Apagar dados
def remover():
    try:
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']

        telefone = str(tree_lista[1])

        remover_dados(telefone)
        messagebox.showinfo('Dados', 'Apagados com sucesso')

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_dados()

    except:
         messagebox.showwarning('Dados', 'Por favor selecione uma informacao na tabela')

    #Mostrar Dados
def mostrar_dados():

    global tree
    dados_h = ['Nome', 'Telefone', 'E-mail']

    dados = ver_dados()

    tree=ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    #vertical scrollbar
    vsb=ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb=ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Telefone', anchor=NW)
    tree.heading(2,text='E-mail', anchor=NW)

    tree.column(0, width=200,anchor='nw')
    tree.column(1, width=70,anchor='nw')
    tree.column(2, width=150,anchor='nw')

    for item in dados:
        tree.insert('', 'end', values=item)

mostrar_dados()


#---------------------------------------------------------------------------
# Widgets

lbl1 = Label(root, text='Agenda de Contatos', font='arial 20', bg='black', fg='#F0F8FF')
lbl2 = Label(root, text='Nome', font='times 14', bg='black', fg='#F0F8FF')
lbl3 = Label(root, text='Telefone', font='times 14', bg='black', fg='#F0F8FF')
lbl4 = Label(root, text='E-mail', font='times 14', bg='black', fg='#F0F8FF' )
textbox1= Entry(root)
textbox2= Entry(root)
textbox3= Entry(root)
btn1 = Button(root, text='Adicionar', width=10, command=inserir)
btn2 = Button(root, text='Alterar',command=atualizar, width=10)
btn3 = Button(root, text='Apagar', command=remover, width=10)
btn4 = Button(root, text='Ver Dados', command=mostrar_dados, width=10)


#----------------------------------------------------------------------------
# Layout

lbl1.grid(row=0, column=1)
lbl2.grid()
lbl3.grid()
lbl4.grid()
textbox1.grid(row=1, column=1, ipadx=100)
textbox2.grid(row=2, column=1, ipadx=100)
textbox3.grid(row=3, column=1, ipadx=100)
btn1.place(x=40, y=150)
btn2.place(x=140, y=150)
btn3.place(x=240, y=150)
btn4.place(x=340, y=150)
frame_tabela.place(x=10, y=200)



root.mainloop()