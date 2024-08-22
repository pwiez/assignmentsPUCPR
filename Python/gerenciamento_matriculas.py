'''
ALUNO: PEDRO FERNANDO WIEZEL
CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
'''

'''Primeiro exercício realizado no curso de ADS.'''

import platform
import os
import json

sistemaoperacional = platform.system() #coleta de qual sistema operacional está sendo usado

#definição das listas a serem mexidas depois pelo programa
listaestudantes = []
listadisciplinas = []
listaprofessores = []
listaturmas = []
listamatriculas = []

#FUNÇÕES DE CADASTRO USANDO ARQUIVOS .JSON
def recuperar_cadastro(setorescolhido):

        if setorescolhido == 'estudante':
                try:
                        with open('listaestudantes.json', encoding='utf-8') as f:
                                listaestudantes = json.load(f)
                except FileNotFoundError:
                        listaestudantes = []
                return listaestudantes

        elif setorescolhido == 'disciplina':
                try:
                        with open('listadisciplinas.json', encoding='utf-8') as f:
                                listadisciplinas= json.load(f)
                except FileNotFoundError:
                        listadisciplinas = []
                return listadisciplinas

        elif setorescolhido == 'professor':
                try:
                        with open('listaprofessores.json', encoding='utf-8') as f:
                                listaprofessores= json.load(f)
                except FileNotFoundError:
                        listaprofessores = []
                return listaprofessores

        elif setorescolhido == 'turma':
                try:
                        with open('listaturmas.json', encoding='utf-8') as f:
                                listaturmas= json.load(f)
                except FileNotFoundError:
                        listaturmas = []
                return listaturmas

        elif setorescolhido == 'matricula':
                try:
                        with open('listamatriculas.json', encoding='utf-8') as f:
                                listamatriculas= json.load(f)
                except FileNotFoundError:
                        listamatriculas = []
                return listamatriculas

def gravar_cadastro(setorescolhido, lista):

        if setorescolhido == 'estudante':
                with open('listaestudantes.json', 'w') as f:
                        json.dump(lista, f)
        elif setorescolhido == 'disciplina':
                with open('listadisciplinas.json', 'w') as f:
                        json.dump(lista, f)
        elif setorescolhido == 'professor':
                with open('listaprofessores.json', 'w') as f:
                        json.dump(lista, f)
        elif setorescolhido == 'turma':
                with open('listaturmas.json', 'w') as f:
                        json.dump(lista, f)
        elif setorescolhido == 'matricula':
                with open('listamatriculas.json', 'w') as f:
                        json.dump(lista, f)

#FUNÇÕES DE MENUS
def menu_principal():

        '''
        Imprime o menu principal e retorna o valor escolhido, ou seja, o setor cadastral.
        Também é feita a validação do dado inserido por meio de try-except,
        para que o programa não aceite uma letra nem um número fora das opções.
        '''

        limpar_tela()
        print("Bem vindo ao Sistema de Gerenciamento de Estudantes!\n")
        print("----------------MENU PRINCIPAL----------------")
        print("\n[1] - Gerenciar Estudantes")
        print("[2] - Gerenciar Disciplinas")
        print("[3] - Gerenciar Professores")
        print("[4] - Gerenciar Turmas")
        print("[5] - Gerenciar Matrículas")
        print("[0] - Sair")


        while True:
                try:
                        opcao = int(input("\nSelecione o setor cadastral desejado: "))
                        if opcao > -1 and opcao < 6:
                                break
                        else:
                                print("\nEscolha um dos valores apresentados!")
                except ValueError:
                        print("\nValor inválido! Selecione um número!")

        return opcao

def menu_de_operacoes(setorescolhido):

        '''
        Parecido com o menu principal, retorna o valor escolhido referente à operação selecionada.
        Imprime o menu respectivo à opção escolhida pelo usuário no menu principal.
        Também é feita a validação do dado inserido por meio de try-except,
        para que o programa não aceite uma letra nem um número fora das opções.
        '''

        opcao = 0

        while True:
                if setorescolhido != "professor": #por questões de escrita fiz essa divisão
                        limpar_tela()
                        print("***** [OPERAÇÕES DE GERENCIAMENTO DE " + setorescolhido.upper() + "S] *****\n")
                        print("[1] - Incluir " + setorescolhido.lower() + "(s)")
                        print("[2] - Listar " + setorescolhido.lower() + "s")
                        print("[3] - Atualizar lista de " + setorescolhido.lower() + "s")
                        print("[4] - Excluir " + setorescolhido.lower() + "(s)")
                        print("[0] - Voltar ao menu principal\n")
                else:
                        limpar_tela()
                        print("***** [OPERAÇÕES DE GERENCIAMENTO DE " + setorescolhido.upper() + "ES] *****\n")
                        print("[1] - Incluir " + setorescolhido.lower() + "(es)")
                        print("[2] - Listar " + setorescolhido.lower() + "es")
                        print("[3] - Atualizar lista de " + setorescolhido.lower() + "es")
                        print("[4] - Excluir " + setorescolhido.lower() + "(es)")
                        print("[0] - Voltar ao menu principal\n")

                while True:
                        try:
                                opcao = int(input("Selecione a operação desejada: "))
                                if opcao > -1 and opcao < 5:
                                        limpar_tela()
                                        break
                                else:
                                        print("\nEscolha um dos valores apresentados!\n")
                        except ValueError:
                                print("\nValor inválido! Selecione um número!\n")

                if opcao == 1: incluir(setorescolhido)
                elif opcao == 2: listar(setorescolhido)
                elif opcao == 3: editar(setorescolhido)
                elif opcao == 4: excluir(setorescolhido)
                else: return

#FUNÇÕES OPERACIONAIS
def incluir(setorescolhido):

        '''
        A operação realizada é igual para cada um dos setores. Ele valida o dado quando é um int a ser inserido
        e depois adiciona esse valor na lista por meio de append usando as defs recuperar e gravar cadastro,
        atualizando a lista. A verificação de código repetido é feita para matrículas e turmas.
        '''

        if setorescolhido == "estudante":

                estudante = {'codigo_estudante': 0 ,
                        'nome_estudante': '',
                        'cpf_estudante': ''}

                while True:
                        try:
                                estudante['codigo_estudante'] = int(input("Qual o código do/da " + setorescolhido.lower() + "? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                estudante['nome_estudante'] = (input("Qual o nome do/da " + setorescolhido.lower() + "? "))
                estudante['cpf_estudante'] = input("Qual o CPF do/da " + setorescolhido.lower() + "? ")

                listaestudantes = recuperar_cadastro(setorescolhido)
                listaestudantes.append(estudante)
                gravar_cadastro(setorescolhido, listaestudantes)

                input("\n" + setorescolhido.title() + " cadastrado(a) com sucesso. \n\nAperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "disciplina":

                disciplina = {'codigo_disciplina': '',
                        'nome_disciplina': ''}

                while True:
                        try:
                                disciplina['codigo_disciplina'] = int(input("Qual o código da " + setorescolhido.lower() + "? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                disciplina['nome_disciplina'] = (input("Qual o nome da " + setorescolhido.lower() + "? "))

                listadisciplinas = recuperar_cadastro(setorescolhido)
                listadisciplinas.append(disciplina)
                gravar_cadastro(setorescolhido, listadisciplinas)

                input("\n" + setorescolhido.title() + " cadastrada com sucesso. \n\nAperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "professor":

                professor = {'codigo_professor': '',
                        'nome_professor': '',
                        'cpf_professor': ''}

                while True:
                        try:
                                professor['codigo_professor'] = int(input("Qual o código do(a) " + setorescolhido.lower() + "(a)? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                professor['nome_professor'] = input("Qual o nome do(a) " + setorescolhido.lower() + "(a)? ")
                professor['cpf_professor'] = input("Qual o CPF do(a) " + setorescolhido.lower() + "(a)? ")

                listaprofessores = recuperar_cadastro(setorescolhido)
                listaprofessores.append(professor)
                gravar_cadastro(setorescolhido, listaprofessores)

                input("\n" + setorescolhido.title() + "(a) cadastrado(a) com sucesso. \n\nAperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "turma":

                turma = {'codigo_turma': '',
                        'codigo_professor': '',
                        'codigo_disciplina': ''}

                while True:
                        listaturmas = recuperar_cadastro(setorescolhido)
                        try:
                                codigo = int(input("Qual o código da " + setorescolhido.lower() + "? "))
                                if any(
                                turma.get('codigo_turma') == codigo
                                for turma in listaturmas
                                ):
                                        print("\nEsse código de turma já foi utilizado!")
                                        input("\nAperte Enter para tentar de novo...")
                                        limpar_tela()
                                else:
                                        turma['codigo_turma'] = codigo
                                        break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")
                while True:
                        try:
                                turma['codigo_professor'] = int(input("Qual o código do(a) professor(a) da " + setorescolhido.lower() + "? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")
                while True:
                        try:
                                turma['codigo_disciplina'] = int(input("Qual o código da disciplina da " + setorescolhido.lower() + "? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                listaturmas = recuperar_cadastro(setorescolhido)
                listaturmas.append(turma)
                gravar_cadastro(setorescolhido, listaturmas)

                input("\n" + setorescolhido.title() + "a cadastrada com sucesso. \n\nAperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "matricula":

                matricula = {'codigo_turma': '',
                        'codigo_estudante_matriculado': ''}

                while True:
                        listamatriculas = recuperar_cadastro(setorescolhido)
                        try:
                                codigo = int(input("Qual o código da " + setorescolhido.lower() + "? "))
                                if any(
                                        matricula.get('codigo_turma') == codigo
                                        for matricula in listamatriculas
                                ):
                                        print("\nEsse código de matrícula já foi utilizado!")
                                        input("\nAperte Enter para tentar de novo...")
                                        limpar_tela()
                                else:
                                        matricula['codigo_turma'] = codigo
                                        break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                while True:
                        try:
                                matricula["codigo_estudante_matriculado"] = int(input("Qual o código do(a) estudante dessa " + setorescolhido.lower() + "? "))
                                break
                        except ValueError:
                                limpar_tela()
                                print("Valor inválido. Insira um número!\n")

                listamatriculas = recuperar_cadastro(setorescolhido)
                listamatriculas.append(matricula)
                gravar_cadastro(setorescolhido, listamatriculas)

                input("\n" + setorescolhido.title() + " cadastrada com sucesso. \n\nAperte Enter para retornar ao menu de operações...")
def listar(setorescolhido):

        '''
        Aqui ele simplesmente percorre cada lista de dicionários imprimindo os valores, verificando
        se existem valores, é claro.
        '''

        if setorescolhido == "estudante": #Listar

                listaestudantes = recuperar_cadastro("estudante")

                if len(listaestudantes) < 1:
                        limpar_tela()
                        input("Nenhum(a) " + setorescolhido.lower() + " cadastrado(a)! \n\nAperte Enter para retornar ao menu de operações...")

                else:
                        print(setorescolhido.title() + "s cadastrados(as): \n")
                        for i in listaestudantes:
                                for key,value in i.items():
                                        if(key == 'codigo_estudante'):
                                                print(f"CÓDIGO:", value, end = ' || ')
                                        elif(key == 'nome_estudante'):
                                                print(f"NOME:", value, end = ' || ')
                                        elif(key == 'cpf_estudante'):
                                                print(f"CPF:", value, end = '')
                                print("\n")
                        input("Aperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "disciplina": #Listar

                listadisciplinas = recuperar_cadastro("disciplina")

                if len(listadisciplinas) < 1:
                        limpar_tela()
                        input("Nenhuma " + setorescolhido.lower() + " cadastrada. \n\nAperte Enter para retornar ao menu de operações...")

                else:
                        print(setorescolhido.title() + "s cadastradas: \n")
                        for i in listadisciplinas:
                                for key,value in i.items():
                                        if(key == 'codigo_disciplina'):
                                                print(f"CÓDIGO:", value, end = ' || ')
                                        elif(key == 'nome_disciplina'):
                                                print(f"NOME:", value, end = ' || ')

                                print("\n")
                        input("Aperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "professor": #Listar

                listaprofessores = recuperar_cadastro("professor")

                if len(listaprofessores) < 1:
                        limpar_tela()
                        input("Nenhum(a) " + setorescolhido.lower() + "(a) cadastrado(a)! \n\nAperte Enter para retornar ao menu de operações...")

                else:
                        print(setorescolhido.title() + "es(as) cadastrados(as): \n")
                        for i in listaprofessores:
                                for key,value in i.items():
                                        if(key == 'codigo_professor'):
                                                print(f"CÓDIGO:", value, end = ' || ')
                                        elif(key == 'nome_professor'):
                                                print(f"NOME:", value, end = ' || ')
                                        elif(key == 'cpf_professor'):
                                                print(f"CPF:", value, end = ' || ')

                                print("\n")
                        input("Aperte Enter para retornar ao menu de operações...")

        elif setorescolhido == "turma": #Listar

                listaturmas = recuperar_cadastro("turma")

                if len(listaturmas) < 1:
                        limpar_tela()
                        input("Nenhuma " + setorescolhido.lower() + " cadastrada! \n\nAperte Enter para retornar ao menu de operações...")

                else:
                        print(setorescolhido.title() + "s cadastradas: \n")
                        for i in listaturmas:
                                for key,value in i.items():
                                        if(key == 'codigo_turma'):
                                                print(f"CÓDIGO DA TURMA:", value, end = ' || ')
                                        elif(key == 'codigo_professor'):
                                                print(f"CÓDIGO DO PROFESSOR:", value, end = ' || ')
                                        elif(key == 'codigo_disciplina'):
                                                print(f"CÓDIGO DA DISCIPLINA:", value, end = ' || ')

                                print("\n")
                        input("Aperte Enter para retornar ao menu de operações...")

        elif setorescolhido == 'matricula':

                listamatriculas = recuperar_cadastro("matricula")

                if len(listamatriculas) < 1:
                        limpar_tela()
                        input("Nenhuma " + setorescolhido.lower() + " cadastrada! \n\nAperte Enter para retornar ao menu de operações...")

                else:
                        print(setorescolhido.title() + "s cadastradas: \n")
                        for i in listamatriculas:
                                for key,value in i.items():
                                        if(key == 'codigo_turma'):
                                                print(f"CÓDIGO DA TURMA:", value, end = ' || ')
                                        elif(key == 'codigo_estudante_matriculado'):
                                                print(f"CÓDIGO DO(A) ESTUDANTE MATRICULADO(A):", value, end = ' || ')

                                print("\n")
                        input("Aperte Enter para retornar ao menu de operações...")
def editar(setorescolhido):

        '''
        Aqui, eu usei loops para ver se o código que a pessoa insere
        está nos valores da lista de dicionários. Se sim ele
        prossegue com a modificação. Se não consta, ele fala que não existe aquele código ali.

        Ele verifica se os códigos já foram usados em turma e código antes da inclusão, também.
        '''

        if setorescolhido == 'estudante':

                listaestudantes = recuperar_cadastro(setorescolhido)
                estudanteconsta = False

                if len(listaestudantes) < 1:
                        limpar_tela()
                        print("Nenhum(a) estudante cadastrado(a)!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                limpar_tela()
                                try:
                                        print("Códigos dos estudantes cadastrados: \n")
                                        for i in listaestudantes:
                                                print(f"| {i['codigo_estudante']}", end = ' | ')
                                        print("\n")
                                        codigoparaeditar = int(input("Qual o código do(a) " + setorescolhido.lower() + " que você quer editar? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                                        input("Aperte Enter para tentar novamente...")
                        for i in listaestudantes:
                                if(i['codigo_estudante'] == codigoparaeditar):
                                        limpar_tela()
                                        while True:
                                                try:
                                                        i['codigo_estudante'] = int(input("Qual o novo código do(a) " + setorescolhido.lower() + "? "))
                                                        break
                                                except ValueError:
                                                        limpar_tela()
                                                        print("Valor inválido. Insira um número!\n")
                                        i['nome_estudante'] = input("Qual o novo nome do(a) " + setorescolhido.lower() + "? ")
                                        i['cpf_estudante'] = input("Qual o novo CPF do(a) " + setorescolhido.lower() + "? ")
                                        estudanteconsta = True
                                        limpar_tela()
                                        print("Cadastro editado com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listaestudantes)
                                        break
                        if(estudanteconsta == False):
                                limpar_tela()
                                print("Estudante não encontrado(a)!")
                                input("\nAperte Enter para tentar novamente...")
                                editar(setorescolhido)

        elif setorescolhido == 'disciplina':

            listadisciplinas = recuperar_cadastro(setorescolhido)
            disciplinaconsta = False

            if len(listadisciplinas) < 1:
                    limpar_tela()
                    print("Nenhuma disciplina cadastrada!\n")
                    input("Aperte Enter para retornar ao menu de operações...")
                    return
            else:
                    while True:
                            limpar_tela()
                            try:
                                    print("Código(s) das disciplinas cadastradas: \n")
                                    for i in listadisciplinas:
                                            print(f"| {i['codigo_disciplina']}", end = ' | ')
                                    print("\n")
                                    codigoparaeditar = int(input("Qual o código da " + setorescolhido.lower() + " que você quer editar? "))
                                    break
                            except ValueError:
                                    limpar_tela()
                                    print("Insira um código válido!\n")
                                    input("Aperte Enter para tentar novamente...")
                    for i in listadisciplinas:
                            if(i['codigo_disciplina'] == codigoparaeditar):
                                    limpar_tela()
                                    while True:
                                            try:
                                                    i['codigo_disciplina'] = int(input("Qual o novo código da " + setorescolhido.lower() + "? "))
                                                    break
                                            except ValueError:
                                                    limpar_tela()
                                                    print("Valor inválido. Insira um número!\n")
                                    i['nome_disciplina'] = input("Qual o novo nome da " + setorescolhido.lower() + "? ")
                                    disciplinaconsta = True
                                    limpar_tela()
                                    print("Cadastro editado com sucesso!")
                                    input("\nAperte Enter para retornar ao menu de operações...")
                                    gravar_cadastro(setorescolhido, listadisciplinas)
                                    break
                    if(disciplinaconsta == False):
                            limpar_tela()
                            print("Disciplina não encontrada!")
                            input("\nAperte Enter para tentar novamente...")
                            editar(setorescolhido)

        elif setorescolhido == 'professor':

            listaprofessores = recuperar_cadastro(setorescolhido)
            professorconsta = False

            if len(listaprofessores) < 1:
                    limpar_tela()
                    print("Nenhum(a) professor(a) cadastrado(a)!\n")
                    input("Aperte Enter para retornar ao menu de operações...")
                    return
            else:
                    while True:
                            limpar_tela()
                            try:
                                    print("Códigos dos(as) professores(as) cadastrados(as): \n")
                                    for i in listaprofessores:
                                            print(f"| {i['codigo_professor']}", end = ' | ')
                                    print("\n")
                                    codigoparaeditar = int(input("Qual o código do(a) " + setorescolhido.lower() + "(a) que você quer editar? "))
                                    break
                            except ValueError:
                                    limpar_tela()
                                    print("Insira um código válido!\n")
                                    input("Aperte Enter para tentar novamente...")
                    for i in listaprofessores:
                            if(i['codigo_professor'] == codigoparaeditar):
                                    limpar_tela()
                                    while True:
                                            try:
                                                    i['codigo_professor'] = int(input("Qual o novo código do(a) " + setorescolhido.lower() + "(a)? "))
                                                    break
                                            except ValueError:
                                                    limpar_tela()
                                                    print("Valor inválido. Insira um número!\n")
                                    i['nome_professor'] = input("Qual o novo nome do(a) " + setorescolhido.lower() + "(a)? ")
                                    i['cpf_professor'] = input("Qual o novo CPF do(a) " + setorescolhido.lower() + "(a)? ")
                                    professorconsta = True
                                    limpar_tela()
                                    print("Cadastro editado com sucesso!")
                                    input("\nAperte Enter para retornar ao menu de operações...")
                                    gravar_cadastro(setorescolhido, listaprofessores)
                                    break
                    if(professorconsta == False):
                            limpar_tela()
                            print("Professor(a) não encontrado(a)!")
                            input("\nAperte Enter para tentar novamente...")
                            editar(setorescolhido)

        elif setorescolhido == 'turma':

            listaturmas = recuperar_cadastro(setorescolhido)
            turmaconsta = False

            if len(listaturmas) < 1:
                    limpar_tela()
                    print("Nenhuma turma cadastrada!\n")
                    input("Aperte Enter para retornar ao menu de operações...")
                    return
            else:
                    while True:
                            limpar_tela()
                            try:
                                    print("Códigos das turmas cadastradas): \n")
                                    for i in listaturmas:
                                            print(f"| {i['codigo_turma']}", end = ' | ')
                                    print("\n")
                                    codigoparaeditar = int(input("Qual o código da " + setorescolhido.lower() + " que você quer editar? "))
                                    break
                            except ValueError:
                                    limpar_tela()
                                    print("Insira um código válido!\n")
                                    input("Aperte Enter para tentar novamente...")
                    for i in listaturmas:
                            if(i['codigo_turma'] == codigoparaeditar):
                                    limpar_tela()
                                    while True:
                                            try:
                                                codigo = int(input("Qual o novo código da " + setorescolhido.lower() + "? "))
                                                if any(
                                                        turma.get('codigo_turma') == codigo
                                                        for turma in listaturmas
                                                ):
                                                        print("\nEsse código de turma já foi utilizado!")
                                                        input("\nAperte Enter para tentar de novo...")
                                                        limpar_tela()
                                                else:
                                                        i['codigo_turma'] = codigo
                                                        break
                                            except ValueError:
                                                    limpar_tela()
                                                    print("Valor inválido. Insira um número!\n")
                                    i['nome_turma'] = input("Qual o novo nome da " + setorescolhido.lower() + "? ")
                                    while True:
                                            try:
                                                i['codigo_disciplina'] = int(input("Qual o novo código da disciplina da " + setorescolhido.lower() + "? "))
                                                break
                                            except ValueError:
                                                limpar_tela()
                                                print("Valor inválido. Insira um número!\n")
                                    turmaconsta = True
                                    limpar_tela()
                                    print("Cadastro editado com sucesso!")
                                    input("\nAperte Enter para retornar ao menu de operações...")
                                    gravar_cadastro(setorescolhido, listaturmas)
                                    break
                    if(turmaconsta == False):
                            limpar_tela()
                            print("Turma não encontrada!")
                            input("\nAperte Enter para tentar novamente...")
                            editar(setorescolhido)

        elif setorescolhido == 'matricula':

            listamatriculas = recuperar_cadastro(setorescolhido)
            matriculaconsta = False

            if len(listamatriculas) < 1:
                    limpar_tela()
                    print("Nenhuma matrícula cadastrada!\n")
                    input("Aperte Enter para retornar ao menu de operações...")
                    return
            else:
                    while True:
                            limpar_tela()
                            try:
                                    print("Códigos das matrículas cadastradas): \n")
                                    for i in listamatriculas:
                                            print(f"| {i['codigo_turma']}", end = ' | ')
                                    print("\n")
                                    codigoparaeditar = int(input("Qual o código da " + setorescolhido.lower() + " que você quer editar? "))
                                    break
                            except ValueError:
                                    limpar_tela()
                                    print("Insira um código válido!\n")
                                    input("Aperte Enter para tentar novamente...")
                    for i in listamatriculas:
                            if(i['codigo_turma'] == codigoparaeditar):
                                limpar_tela()
                                while True:
                                        try:
                                                codigo = int(input("Qual o novo código da turma da " + setorescolhido.lower() + "? "))
                                                if any(
                                                        matricula.get('codigo_turma') == codigo
                                                        for matricula in listamatriculas
                                                ):
                                                        print("\nEsse código de matrícula já foi utilizado!")
                                                        input("\nAperte Enter para tentar de novo...")
                                                        limpar_tela()
                                                else:
                                                        i['codigo_turma'] = codigo
                                                        break
                                        except ValueError:
                                                limpar_tela()
                                                print("Valor inválido. Insira um número!\n")
                                while True:
                                        try:
                                                i['codigo_estudante_matriculado'] = int(input("Qual o novo código do estudante dessa " + setorescolhido.lower() + "? "))
                                                break
                                        except ValueError:
                                                limpar_tela()
                                                print("Valor inválido. Insira um número!\n")
                                matriculaconsta = True
                                limpar_tela()
                                print("Cadastro editado com sucesso!")
                                input("\nAperte Enter para retornar ao menu de operações...")
                                gravar_cadastro(setorescolhido, listamatriculas)
                                break
                    if(matriculaconsta == False):
                            limpar_tela()
                            print("Matrícula não encontrada!")
                            input("\nAperte Enter para tentar novamente...")
                            editar(setorescolhido)

def excluir(setorescolhido):

        '''
        Aqui a ideia é igual a da def editar, na verdade. A mesma lógica dos loops serve para ver
        se algo pode ser excluído, só retirando as operações de mudança das chaves dos dicts.
        '''
        if setorescolhido == "estudante":

                listaestudantes = recuperar_cadastro(setorescolhido)
                estudanteexcluido = False

                if len(listaestudantes) < 1:
                        limpar_tela()
                        print("Nenhum(a) estudante cadastrado(a)!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                try:
                                        print("Código(s) dos estudantes cadastrados: \n")
                                        for i in listaestudantes:
                                                print(f"| {i['codigo_estudante']}", end = ' | ')
                                        print("\n")
                                        codigoparaexcluir = int(input("Qual o código do(a) " + setorescolhido.lower() + " que você quer excluir? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                        for i in listaestudantes:
                                if(i['codigo_estudante'] == codigoparaexcluir):
                                        listaestudantes.remove(i)
                                        estudanteexcluido = True
                                        limpar_tela()
                                        print("Estudante removido(a) com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listaestudantes)
                                        break
                        if(estudanteexcluido == False):
                                limpar_tela()
                                print("Estudante não encontrado(a)!")
                                input("\nAperte Enter para tentar novamente...")
                                excluir(setorescolhido)

        elif setorescolhido == "disciplina":

                listadisciplinas = recuperar_cadastro(setorescolhido)
                disciplinaexcluida = False

                if len(listadisciplinas) < 1:
                        limpar_tela()
                        print("Nenhuma disciplina cadastrada!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                try:
                                        print("Códigos das disciplinas cadastradas: \n")
                                        for i in listadisciplinas:
                                                print(f"| {i['codigo_disciplina']}", end = ' | ')
                                        print("\n")
                                        codigoparaexcluir = int(input("Qual o código da " + setorescolhido.lower() + " que você quer excluir? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                        for i in listadisciplinas:
                                if(i['codigo_disciplina'] == codigoparaexcluir):
                                        listadisciplinas.remove(i)
                                        disciplinaexcluida = True
                                        limpar_tela()
                                        print("Disciplina removida com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listadisciplinas)
                                        break
                        if(disciplinaexcluida == False):
                                limpar_tela()
                                print("Disciplina não encontrada!")
                                input("\nAperte Enter para tentar novamente...")
                                excluir(setorescolhido)

        elif setorescolhido == "professor":

                listaprofessores = recuperar_cadastro(setorescolhido)
                professorexcluido = False

                if len(listaprofessores) < 1:
                        limpar_tela()
                        print("Nenhum(a) professor(a) cadastrado(a)!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                try:
                                        print("Código dos professores cadastrados: \n")
                                        for i in listaprofessores:
                                                print(f"| {i['codigo_professor']}", end = ' | ')
                                        print("\n")
                                        codigoparaexcluir = int(input("Qual o código do(a) " + setorescolhido.lower() + "(a) que você quer excluir? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                        for i in listaprofessores:
                                if(i['codigo_professor'] == codigoparaexcluir):
                                        listaprofessores.remove(i)
                                        professorexcluido = True
                                        limpar_tela()
                                        print("Professor(a) removido(a) com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listaprofessores)
                                        break
                        if(professorexcluido == False):
                                limpar_tela()
                                print("Professor(a) não encontrado(a)!")
                                input("\nAperte Enter para tentar novamente...")
                                excluir(setorescolhido)

        elif setorescolhido == "turma":

                listaturmas = recuperar_cadastro(setorescolhido)
                turmaexcluida = False

                if len(listaturmas) < 1:
                        limpar_tela()
                        print("Nenhuma turma cadastrada!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                try:
                                        print("Códigos das turmas cadastrados: \n")
                                        for i in listaturmas:
                                                print(f"| {i['codigo_turma']}", end = ' | ')
                                        print("\n")
                                        codigoparaexcluir = int(input("Qual o código da " + setorescolhido.lower() + " que você quer excluir? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                        for i in listaturmas:
                                if(i['codigo_turma'] == codigoparaexcluir):
                                        listaturmas.remove(i)
                                        turmaexcluida = True
                                        limpar_tela()
                                        print("Turma removida com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listaturmas)
                                        break
                        if(turmaexcluida == False):
                                limpar_tela()
                                print("Turma não encontrada!")
                                input("\nAperte Enter para tentar novamente...")
                                excluir(setorescolhido)

        elif setorescolhido == "matricula":

                listamatriculas = recuperar_cadastro(setorescolhido)
                matriculaexcluida = False

                if len(listamatriculas) < 1:
                        limpar_tela()
                        print("Nenhuma matrícula cadastrada!\n")
                        input("Aperte Enter para retornar ao menu de operações...")
                        return
                else:
                        while True:
                                try:
                                        print("Código das turmas com matrículas cadastradas: \n")
                                        for i in listamatriculas:
                                                print(f"| {i['codigo_turma']}", end = ' | ')
                                        print("\n")
                                        codigoparaexcluir = int(input("Qual o código da " + setorescolhido.lower() + " que você quer excluir? "))
                                        break
                                except ValueError:
                                        limpar_tela()
                                        print("Insira um código válido!\n")
                        for i in listamatriculas:
                                if(i['codigo_turma'] == codigoparaexcluir):
                                        listamatriculas.remove(i)
                                        matriculaexcluida = True
                                        limpar_tela()
                                        print("Matrícula removida com sucesso!")
                                        input("\nAperte Enter para retornar ao menu de operações...")
                                        gravar_cadastro(setorescolhido, listamatriculas)
                                        break
                        if(matriculaexcluida == False):
                                limpar_tela()
                                print("Matrícula não encontrada!")
                                input("\nAperte Enter para tentar novamente...")
                                excluir(setorescolhido)
def limpar_tela():

        '''
        Função para limpar a tela, usando o os.system para limpar o terminal.
        Quis aprender a fazer por questões de organização e limpeza do terminal.
        '''

        if sistemaoperacional == "Windows":
                os.system("cls")
        else:
                os.system("clear")

#EXECUÇÃO
while True:

        opcaomenuprincipal = menu_principal()

        if opcaomenuprincipal == 0:
                limpar_tela()
                print("Saindo do sistema!")
                break #fim da execução
        elif opcaomenuprincipal == 1:
                setorescolhido = "estudante"
                menu_de_operacoes(setorescolhido)
        elif opcaomenuprincipal == 2:
                setorescolhido = "disciplina"
                menu_de_operacoes(setorescolhido)
        elif opcaomenuprincipal == 3:
                setorescolhido = "professor"
                menu_de_operacoes(setorescolhido)
        elif opcaomenuprincipal== 4:
                setorescolhido = "turma"
                menu_de_operacoes(setorescolhido)
        elif opcaomenuprincipal == 5:
                setorescolhido = "matricula"
                menu_de_operacoes(setorescolhido)
