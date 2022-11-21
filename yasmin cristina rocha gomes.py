import sqlite3

connect = sqlite3.connect('clientes.db')

from sql import banco #importa a classe Banco


a = banco()

a.criar_tabela()

while True:
    print('Escolha um candidato:\n')
    print('1- Inserir \n2- Pesquisar \n3- Aterar \n4- Deletar')
    opcao = int(input('-> '))


    if opcao == 1:
        nome = str(input("Escolha uma pessoa: "))
        cpf = str(input("informe o cpf do escolhida: "))
        a.adicione (nome,cpf)

    elif opcao ==2:
        id = input("apresente o id: ")
        a.ler(id)

    elif opcao ==3:
        id = input('Entre com o ID da pessoa que deseja alterar: \n')
        nome = input('insire com o novo nome: \n')
        cpf = input('insire o novo cpf: \n')
        a.alterar(id, nome, cpf)

    elif opcao ==4:
        id = input('insira o ID da pessoa que deseja excluir: \n')
        a.excluir(id)