import csv

lista = []

#funcão adicionar dados
def adicionar_dados(i):
    with open('Tkinter\Agenda\dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

adicionar_dados(lista)

#função ver dados
def ver_dados():
    dados=[]
    with open('Tkinter\Agenda\dados.csv') as file:
           ler_csv = csv.reader(file)
           for linha in ler_csv:
                dados.append(linha)
    return dados

#funcao remover dados
def remover_dados(i):
    def adicionar_novalista(j):
        with open('Tkinter\Agenda\dados.csv', 'w', newline='') as file:
            escrever=csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista=[]
    telefone = i
    with open('Tkinter\Agenda\dados.csv', 'r') as file:
        ler_csv=csv.reader(file) 
        
        for linha in ler_csv:
            nova_lista.append (linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)

    adicionar_novalista(nova_lista)

#funcao atualizar dados
def atualizar_dados(i):
    def adicionar_novalista(j):
        with open('Tkinter\Agenda\dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()

    nova_lista=[]
    telefone = i[0]
    with open('Tkinter\Agenda\dados.csv', 'r') as file:
        ler_csv=csv.reader(file)
              
        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[0]
                    telefone = i[1]
                    email = i[2]

                    dados = [nome, telefone, email]
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados

    adicionar_novalista(nova_lista)

#atualizar_dados()

