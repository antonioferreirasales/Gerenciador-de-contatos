#função para deixar as mensagens vermelhas
def deixaVermelho(msg):
    print('\033[31m'+msg+'\033[m')


#função para ler e tratar os input do menu
def lerMensagem(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            deixaVermelho('Erro: digite uma opção válida!')
            continue
        except(KeyboardInterrupt):
            return 0
        else:
            return n


## função apenas para imprimir linhas
def linha (tamanho=42):
    return '-' * tamanho


#função de um molde para texto destacados
def molde(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


#função dinâmica para criação do menu
def menu(lista):
    molde('Menu')
    c = 1 
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opcao = lerMensagem('Digite sua opção: ')
    return opcao