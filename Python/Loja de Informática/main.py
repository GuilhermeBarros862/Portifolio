lista_de_pecas = []  # Cria uma lista para que as peças possam ser adicionadas
codigo = 0  # Cria um código exclusivo para as peças

# Definição de Funções
def cadastrar_componentes(codigo):  # Função para cadastrar peças
    peca = {}  # Cria um dicionário para que os dados possam ser adicionados na lista
    print('Você escolheu a opção de cadastrar uma peça!')

    while True:
        try:  # Tratamento de erro para caso o usuário digite uma letra onde deveria ser um número
            peca['Codigo'] = codigo  # Cadastra o código exclusivo da peça
            peca['Categoria'] = str(input('Qual a CATEGORIA da peça? ')).upper()  # Cadastra as informações que foram pedidas
            peca['Fabricante'] = str(input('Qual a FABRICANTE da peça? ')).upper()
            peca['Nome'] = str(input('Qual o NOME da peça? (Obs.: Não digitar partes do nome que é a categoria e fabricante)')).upper()
            peca['Valor'] = float(input('Qual o VALOR da peça? '))
            peca['Quantidade'] = int(input('Qual a QUANTIDADE de peças? '))
            print(f'\nCódigo da peça = {codigo}')  # Informa o código ao usuário
            lista_de_pecas.append(peca)  # Adiciona a peça a lista de peças
            break

        except:  # Caso o erro se confirme, informa o usuário sobre tal
            print('Favor digitar no campo "VALOR" um valor numérico!')
            continue

def consulta_de_pecas():  # Função para consultar peças
    while True:
        print('Você escolheu a opção de consultar peças!\n')

        tipo_consulta = str(input('1 - Consultar TODAS AS PEÇAS\n'
                                  '2 - Consultar por CATEGORIA e FABRICANTE\n'
                                  '3 - Consultar por NOME\n'
                                  '4 - Consultar por CÓDIGO\n'
                                  '5 - Sair\n'
                                  '>> '))

        if tipo_consulta == '1':  # Verifica a opção escolhida pelo usuário
            print('-' * 24)
            for peca in lista_de_pecas:  # Verifica cada peça para as apresentar na consulta
                print(f'Nome: {peca["Categoria"]} {peca["Fabricante"]} {peca["Nome"]}\n'  # Imprime na tela as informações da peça
                      f'Código: {peca["Codigo"]}\n'
                      f'Categoria: {peca["Categoria"]}\n'
                      f'Fabricante: {peca["Fabricante"]}\n'
                      f'Valor: {peca["Valor"]}\n'
                      f'Quantidade: {peca["Quantidade"]}')
                print('-' * 24)
                continue

        elif tipo_consulta == '2':
            consulta_categoria = str(input('Qual a CATEGORIA das peças? '))  # Pergunta a categoria da peça a ser consultada
            consulta_fabricante = str(input('Qual o FABRICANTE das peças? '))  # Pergunta a fabricante da peça a ser consultada
            encontrado = False  # Verifica se a peça existe
            print('-' * 34)
            for peca in lista_de_pecas:
                if str(peca['Categoria']) == consulta_categoria and peca['Fabricante'] == consulta_fabricante:
                    print(f'Nome: {peca["Nome"]}\n'
                          f'Código: {peca["Codigo"]}\n'
                          f'Categoria: {peca["Categoria"]}\n'
                          f'Fabricante: {peca["Fabricante"]}\n'
                          f'Valor: {peca["Valor"]}\n'
                          f'Quantidade: {peca["Quantidade"]}')
                    print('-' * 34)
                    encontrado = True  # Confirma que a peça está na lista
                    continue

                if not encontrado:  # Caso a peça não seja encontrada informa ao usuário
                    print('')
                    print('Categoria e/ou Fabricante não encontrada!')
                    print('')
                    continue

        elif tipo_consulta == '3':
            consulta_nome = str(input('Qual o NOME da peça? '))  # Pergunta o nome da peça a ser consultada
            encontrado = False
            print('-' * 34)
            for peca in lista_de_pecas:
                if str(peca['Nome']) == consulta_nome:
                    print(f'Nome: {peca["Nome"]}\n'
                          f'Código: {peca["Codigo"]}\n'
                          f'Categoria: {peca["Categoria"]}\n'
                          f'Fabricante: {peca["Fabricante"]}\n'
                          f'Valor: {peca["Valor"]}'
                          f'Quantidade: {peca["Quantidade"]}')
                    print('-' * 34)
                    encontrado = True
                    continue

                if not encontrado:
                    print('')
                    print('Nome não encontrado!')
                    print('')
                    continue

        elif tipo_consulta == '4':
            consulta_codigo = str(input('Qual o CÓDIGO da peça? '))  # Pergunta o código da peça a ser consultada
            encontrado = False
            print('-' * 34)
            for peca in lista_de_pecas:
                if str(peca['Codigo']) == consulta_codigo:
                    print(f'Nome: {peca["Nome"]}'
                          f'Código: {peca["Codigo"]}'
                          f'Categoria: {peca["Categoria"]}'
                          f'Fabricante: {peca["Fabricante"]}'
                          f'Valor: {peca["Valor"]}'
                          f'Quantidade: {peca["Quantidade"]}')
                    encontrado = True
                    print('-' * 34)
                    continue

                if not encontrado:
                    print('')
                    print('Código não encontrado')
                    print('')
                    continue

        elif tipo_consulta == '5':  # Opção para voltar ao programa principal
            print('Voltando...')
            break

        else:
            print('')
            print('Opção não válida! Tente novamente!')  # Informa que o usuário escolheu uma opção inválida
            print('')

def remove_peca():  # Função para remover uma peça
    print('Você selecionou a opção de remover peça!')
    print('')
    remover_peca = str(input('Digite o código da peça a ser removida'))
    encontrado = False

    for peca in lista_de_pecas:
        if remover_peca == peca['Codigo']:
            encontrado = True
            lista_de_pecas.remove(peca)  # Remove a peça da lista
            print('Peça Removida!')
    if not encontrado:
        print('')
        print('Peça não encontrada!')

def editar_pecas():  # Função para editar uma informação duma peça
    print('Você escolheu a opção de editar uma peça!')

    while True:
        peca_pra_editar = str(input('O que você irá fazer?\n'
                                    '1 - Editar NOME da peça\n'
                                    '2 - Editar FABRICANTE da peça\n'
                                    '3 - Editar VALOR da peça\n'
                                    '4 - Editar QUANTIDADE da peça\n'
                                    '5 - Sair...\n'
                                    '>> '))  # Pergunta a informação que será editada

        if peca_pra_editar == '1':
            codigo_pra_editar = str(input('Qual o código da peça? '))
            encontrado = False

            for peca in lista_de_pecas:
                if codigo_pra_editar == str(peca['Codigo']):  # Verifica se o código informado é de alguma peça
                    print(f'{peca["Categoria"]} {peca["Fabricante"]} {peca["Nome"]}')  # Informa as informações da peça
                    peca['Nome'] = str(input('Qual o novo NOME da peça?'))
                    print('NOME da peça editado!')
                    encontrado = True
                    continue

                if not encontrado:
                    print('')
                    print('Peça não encontrada!')
                    print('')

        elif peca_pra_editar == '2':
            codigo_pra_editar = str(input('Qual o código da peça? '))
            encontrado = False

            for peca in lista_de_pecas:
                if codigo_pra_editar == str(peca['Codigo']):
                    print(f'{peca["Categoria"]} {peca["Fabricante"]} {peca["Nome"]}')
                    peca['Fabricante'] = str(input('Qual o novo FABRICANTE da peça?'))
                    print('FABRICANTE da peça editado!')
                    encontrado = True
                    continue

                if not encontrado:
                    print('')
                    print('Peça não encontrada!')
                    print('')

        elif peca_pra_editar == '3':
            codigo_pra_editar = str(input('Qual o código da peça? '))
            encontrado = False

            for peca in lista_de_pecas:
                if codigo_pra_editar == str(peca['Codigo']):
                    print(f'{peca["Categoria"]} {peca["Fabricante"]} {peca["Nome"]}')
                    print(f'{peca["Valor"]}')
                    peca['Valor'] = str(input('Qual o novo VALOR da peça?'))
                    print('VALOR da peça editado!')
                    encontrado = True
                    continue

                if not encontrado:
                    print('')
                    print('Peça não encontrada!')
                    print('')

        elif peca_pra_editar == '4':
            codigo_pra_editar = str(input('Qual o código da peça? '))
            encontrado = False

            for peca in lista_de_pecas:
                if codigo_pra_editar == str(peca['Codigo']):
                    print(f'{peca["Categoria"]} {peca["Fabricante"]} {peca["Nome"]}')
                    print(f'{peca["Quantidade"]}')
                    peca['Quantidade'] = str(input('Qual a nova QUANTIDADE da peça?'))
                    print('QUANTIDADE da peça editado!')
                    encontrado = True
                    continue

                if not encontrado:
                    print('')
                    print('Peça não encontrada!')
                    print('')

        elif peca_pra_editar == '5':
            print('Voltando...')
            break

        else:
            print('Opção Inválida, tente novamente!')


# Programa Principal
print('Gerenciador de Peças da Loja de Informática')

while True:
    opcao = str(input('O que você irá fazer?\n'
                      '1 - Cadastrar Peça e Quantidade\n'
                      '2 - Consultar Peças\n'
                      '3 - Remover Peças\n'
                      '4 - Editar peças\n'
                      '5 - Sair do Programa\n'
                      '>> '))  # O usuário o que irá fazer

    if opcao == '1':  # Verifica a opção escolhida pelo usuário
        codigo = codigo + 1
        print('')
        cadastrar_componentes(codigo)  # Chama a função
        print('')
        continue

    elif opcao == '2':
        print('')
        consulta_de_pecas()
        print('')
        continue

    elif opcao == '3':
        print('')
        remove_peca()
        print('')
        continue

    elif opcao == '4':
        print('')
        editar_pecas()
        print('')
        continue

    elif opcao == '5':
        print('')
        break  # Fecha o programa

print('Fim do Programa')