from lib import interface
from time import sleep

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        interface.cabeçalho('Opção 1')
    elif resposta == 2:
        interface.cabeçalho('Opção 2')
    elif resposta == 3:
        interface.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! digite uma opção válida!\033[m')
    sleep(1.3)
