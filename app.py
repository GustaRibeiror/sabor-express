import os
restaurantes = [
      {'nome': 'praça', 'categoria': 'japonesa', 'ativo': False},
      {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo':True},
      {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def nome_programa():
      '''
      função que irá exibir o nome do nosso aplicativo
      '''


      print(""""
            
      █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
      ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
            """)

def exibir_opcoes():
      '''
      função que exibe todas as opções do menu principal
      '''

      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Alternar Status do Restaurante')
      print('4. Sair\n')

def finalizar_sistema():
    '''
    exibe mensagem de finalização do aplicativo
    '''
    print('Sistema Finalizado.')

def voltar_ao_menu():
      ''' Solicita uma tecla para voltar ao menu principal 
    
      Outputs:
      - Retorna ao menu principal
      '''
      input('\nDigite uma tecla para voltar ao menu principal: \n')
      main()

def exibir_subtitulo(texto):


      os.system('cls')
      linha = '*' * len(texto)
      print(linha)
      print(texto)
      print(linha)

      print('\n')


def opcao_invalida():
      ''' 
      Exibe mensagem de opção inválida e retorna ao menu principal 
      Outputs:
      - Retorna ao menu principal
      '''

      print('Opção inválida\n')
      voltar_ao_menu()

def cadastrar_restaurante():
      '''
      Essa função é responsável por cadastrar um novo restaurante

      inputs:
      - Nome
      - Categoria

      outputs:
      - Adiciona um novo restaurante a lista de restaurantes

      '''


      exibir_subtitulo('CADASTRANDO RESTAURANTES')

      novo_restaurante = input('Digite o nome do restaurante: ')
      categoria = input(f'Digite a categoria do restaurante {novo_restaurante}: ')
      dados_restaurante = {'nome': novo_restaurante, 'categoria': categoria, 'ativo': False}

      restaurantes.append(dados_restaurante)
      print(f'O restaurante {novo_restaurante} foi cadastrado com sucesso!')

      escolha = ''
      while escolha not in ['S', 'N']:
            escolha = input('\nDeseja cadastrar mais um restaurante (S/N):   \n').upper().strip()[0]
            if escolha not in ['s', 'n']:
                  print('Resposta inválida. Digite "S" para continuar cadastrando ou "N" para voltar ao menu principal')
      if escolha == 'S':
            cadastrar_restaurante()
      else: 
            main()
            
def listar_restaurante():
      '''
      Essa função lista todos os reataurantes cadastrados

      Inputs:
      - None

      Outputs:
      - Listagem dos restaurantes
      '''


      exibir_subtitulo('LISTANDO RESTAURANTES')

      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante =  'Ativado' if restaurante['ativo'] else 'Desativado'

            print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
      
      voltar_ao_menu()

def alterar_restaurante():
      '''
      Essa função altera o status dos restaurants (ativado/desativo)

      Inputs:
      - Nome do restaurante

      Outputs:
       - Alteração do status do restaurante
      '''


      exibir_subtitulo('ALTERANDO RESTAURANTES')

      nome_restaurante = input('Digite o nome do restaurante a ser alterado o estado: ')
      encontrado_restaurante = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  encontrado_restaurante = True
                  restaurante['ativo'] = not restaurante['ativo']
                  print(f'O estado do restaurante {nome_restaurante} foi ativado com sucesso!') if restaurante['ativo'] == True else print(f'O estado do restaurante {nome_restaurante} foi desativado com sucesso!')
      if encontrado_restaurante == False:
            print(f'O restaurante {nome_restaurante} não foi encontrado.')
      voltar_ao_menu()


def escolher_opcao():
      '''
      Essa função armazena a opção escolhida do menu e leva o usuário ao local que ele escolheu

      Inputs:
      - Número da escolha

      Outputs:
      - Leva o usuário para o local da opção escolhida
      '''


      try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            if opcao_escolhida == 1: 
                  cadastrar_restaurante()
            elif opcao_escolhida == 2: 
                  listar_restaurante()
            elif opcao_escolhida == 3: 
                  alterar_restaurante()
            elif opcao_escolhida == 4: 
                  finalizar_sistema()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()
      
def main():
      ''' Função principal que inicia o programa '''

      os.system('cls')
      nome_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      main()
