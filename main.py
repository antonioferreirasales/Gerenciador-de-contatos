from funcoes import *
from time import sleep

conn = psycopg2.connect(
    f"host={ip_banco} port={porta_banco} dbname={nome_banco} user={usuario_banco} password={senha_banco}"
)

while True:
    resposta = menu(['Cadastrar um cliente', 'Pesquisar um cliente',
                     'Alterar um cliente', 'Remover um cliente', 'Sair'])

    if resposta == 1:
        nome = input('Digite o nome do cliente: ')
        telefone = input('Digite o número do cliente: ')
        data_nascimento = input('Qual a data de nascimento do cliente: ')
        pergunta_observacao = input('Gostaria de adicionar uma observação? s / n \n')
        if pergunta_observacao == 's':
            observacao = input('Qual observação gostaria de adicionar? \nDigite: ')
        else:
            observacao = None
        cadastra_cliente(nome, telefone, data_nascimento, observacao)
    elif resposta == 2:
        nome = input('Digite o nome do cliente: ')
        procura_cliente(nome)

    elif resposta == 3:
        nome = input('Digite o nome do cliente que você quer alterar: ')
        telefone = input('Digite o novo número de telefone: ')
        altera_cliente(nome, telefone)

    elif resposta == 4:
        nome = input('Digite o nome do cliente que você quer remover: ')
        deleta_cliente(nome)
        print('Cliente removido com sucesso!')

    elif resposta == 5:
        molde('Saindo do sistema')
        break

    else:
        deixa_vermelho('Erro: digite uma opção válida!')
    sleep(1)
cursor.close()
conn.close()