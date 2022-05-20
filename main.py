from funcoes import*
from time import sleep
while True:
    resposta = menu(['Cadastrar um cliente', 'Pesquisar um cliente',
                    'Alterar um cliente', 'Remover um cliente', 'Sair'])

    if resposta == 1:
        nome = input('Digite o nome do cliente: ')
        telefone = int(input('Digite o número do cliente: '))
        cadastraCliente(nome, telefone)

    elif resposta == 2:
        nome = input('Digite o nome do cliente: ')
        procuraCliente(nome)

    elif resposta == 3:
        nome = input('Digite o nome do cliente que você quer alterar: ')
        telefone = input('Digite o novo número de telefone: ')
        alteraCliente(nome, telefone)

    elif resposta == 4:
        nome = input('Digite o nome do cliente que você quer remover: ')
        deletaCliente(nome)
        print('Cliente removido com sucesso!')

    elif resposta == 5:
        molde('Saindo do sistema')
        break

    else:
        deixaVermelho('Erro: digite uma opção válida!')
    sleep(1)
