from funcoes import*

while True:
    resposta = menu(['Cadastrar um cliente', 'Pesquisar um cliente', 'Alterar um cliente', 'Sair'])
    if resposta == 1:
        print('Cadastrando um cliente')
    elif resposta == 2:
        print('Pesquisando um cliente')
    elif resposta == 3:
        print('Alterando um cliente')
    elif resposta == 4:
        molde('Saindo do sistema')
        break
    else:
        deixaVermelho('Erro: digite uma opção válida!')
