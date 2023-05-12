from credencias import *
import psycopg2
from datetime import datetime

clientes = {}
hora_execucao = datetime.now()

conn = psycopg2.connect(
    f"host={ip_banco} port={porta_banco} dbname={nome_banco} user={usuario_banco} password={senha_banco}"
)
cursor = conn.cursor()


# função para deixar as mensagens vermelhas
def deixa_vermelho(msg):
    print('\033[31m' + msg + '\033[m')


# função para ler e tratar os input do menu
def ler_mensagem(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            deixa_vermelho('Erro: digite uma opção válida!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n


# função apenas para imprimir linhas
def linha(tamanho=42):
    return '-' * tamanho


# função de um molde para texto destacados
def molde(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


# f unção dinâmica para criação do menu
def menu(lista):
    molde('Menu')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = ler_mensagem('Digite sua opção: ')
    return opcao


# cadastrar um cliente com nome e telefone
def cadastra_cliente(nome, telefone, data_nascimento, observacao):
    global telefone_id, telefone_data_atualizacao
    cursor.execute("INSERT INTO telefone ("
                   "telefone_numero, telefone_data_atualizacao, tipo_telefone_id"
                   ") VALUES (%s, %s, 1)", (telefone, hora_execucao))

    cursor.execute(
        "SELECT telefone_id, telefone_data_atualizacao FROM telefone WHERE telefone_numero = %s", (telefone,))
    result = cursor.fetchone()
    if result is not None:
        telefone_id, telefone_data_atualizacao = result
    else:
        deixa_vermelho("Valores são vazios!")

    if observacao == '':
        observacao = None
    cursor.execute("INSERT INTO contato ("
                   "contato_nome, telefone_id, contato_nascimento, contato_observacao, contato_data_criacao, "
                   "contato_data_atualizacao"
                   ") VALUES (%s, %s, %s, %s, %s, %s)",
                   (nome, telefone_id, data_nascimento, observacao, telefone_data_atualizacao, telefone_data_atualizacao,))
    conn.commit()
    print('Cliente cadastrado com sucesso!')


# procurar um cliente pelo nome, mostrando o telefone
def procura_cliente(nome):
    cursor.execute(
        "SELECT c.contato_nome, t.telefone_numero, c.contato_observacao FROM contato c INNER JOIN telefone t ON "
        "c.telefone_id ="
        "t.telefone_id WHERE c.contato_nome = %s"
        , (nome,))
    result = cursor.fetchone()
    contato_nome, contato_telefone, contato_observacao = result
    print(f'Cliente: {contato_nome}, Telefone: {contato_telefone}. || Obs: {contato_observacao}')


# altera o telefone do cliente
def altera_cliente(nome, telefone):
    clientes[nome] = telefone
    print('Cliente alterado com sucesso!')


# deleta um cliente
def deleta_cliente(nome):
    clientes.pop(nome)
