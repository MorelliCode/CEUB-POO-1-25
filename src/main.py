import os
from funcionario import Funcionario
from hospede import Hospede
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel

def initialize_test_objects():
    test_funcionario = Funcionario(123, "Maria", "maria@email.com")
    test_hospede = Hospede(456, "João", "joao@email.com")
    test_quarto_1 = Quarto(1, "casal")
    test_quarto_2 = Quarto(2, "solteiro")

    waystone.add_quarto(test_quarto_1)
    waystone.add_quarto(test_quarto_2)
    waystone.registrar_hospede(test_hospede)
    waystone.registar_funcionario(test_funcionario)
    
    test_reserva = Reserva(test_hospede, test_quarto_1)

    test_hospede.fazer_reserva(test_reserva)
    waystone.add_reserva(test_reserva)
    test_quarto_1.reservar()

def loop_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print(divider)
        print("Bem vindo ao Hotel Waystone.")
        print("1 - Hóspedes")
        print("2 - Funcionários")
        print("3 - Sair")
    
        choice = input(">")
    
        if choice == "1":
            loop_hospede_start()
        elif choice == "2":
            loop_funcionario_start()
        elif choice == "3":
            exit()
        else:
            print("Favor escolher um número entre 1-3.")

def loop_funcionario_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print("Você selecionou 'Funcionário'.")
        print("1 - Log in")
        print("2 - Cadastrar")
        print("3 - Voltar")
    
        choice = input(">")
    
        if choice == "1":
            loop_funcionario_login()
        elif choice == "2":
            loop_funcionario_cadastrar()
        elif choice == "3":
            break
        else:
            print("Favor escolher um número entre 1-3.")

def loop_funcionario_cadastrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Você escolheu 'Cadastrar'.")
    
    while True:
        ja_cadastrado = False
    
        print("Digite o seu número de funcionario, ou 'voltar' para voltar à tela anterior.")
    
        numero_funcionario = input(">")
    
        if numero_funcionario == "voltar":
            break
        try:
            numero_funcionario = int(numero_funcionario)
        except:
            print("Favor digitar o seu número de funcionario, ou 'voltar'.")
            continue
    
        for funcionario in waystone.get_funcionarios():
            if numero_funcionario == funcionario.get_id():
                print("Funcionario já cadastrado.")
                ja_cadastrado = True
                break
    
        if ja_cadastrado:
            continue
    
        print("Digite o seu nome completo:")
    
        nome = input(">")
    
        print("Digite o seu email corporativo:")
    
        email = input(">")
    
        new_funcionario = Funcionario(numero_funcionario, nome, email)
        waystone.registar_funcionario(new_funcionario)
    
        break

def loop_funcionario_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    global current_user
    
    while True:
        print("Favor informar o seu número de funcionário, ou 'voltar' para voltar à tela anterior.")
    
        choice = input(">")
    
        if choice == "voltar":
            break
    
        for funcionario in waystone.get_funcionarios():
            if choice == str(funcionario.get_id()):
                current_user = funcionario
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Funcionário autenticado com sucesso.")
                loop_funcionario()
                return
        print("Funcionário não encontrado. Você já fez o cadastro?")
        
def loop_funcionario():
    print(f"Bem vindo, {current_user.get_nome()}.")
    print("O que você gostaria de fazer?")
    
    while True:
        print("1 - Adicionar quarto")
        print("2 - Remover quarto")
        print("3 - Registrar hóspede")
        print("4 - Cancelar reserva")
        print("9 - Voltar")
    
        choice = input(">")
    
        if choice == "9":
            break
        elif choice == "1":
            loop_adicionar_quarto()
        elif choice == "2":
            loop_remover_quarto()
        elif choice == "3":
            loop_registrar_hospede()
        elif choice == "4":
            loop_funcionario_cancelar_reserva()
        else:
            print("Escolha não reconhecida. Tente novamente.")

def loop_adicionar_quarto():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        ja_cadastrado = False
    
        print("Favor digitar o número do quarto (ou 'voltar'):")
    
        numero_quarto = input(">")
    
        if numero_quarto == "voltar":
            break
        try:
            numero_quarto = int(numero_quarto)
        except:
            print("Favor digitar apenas números ou 'voltar'.")
            continue
    
        for quarto in waystone.get_quartos():
            if numero_quarto == quarto.get_numero():
                print("Este quarto já está cadastrado.")
                ja_cadastrado = True
                break
    
        if ja_cadastrado:
            continue
    
        tipo_quarto = input("Este quarto é de casal ou solteiro? ")
    
        new_quarto = Quarto(numero_quarto, tipo_quarto)
        current_user.add_quarto(waystone, new_quarto)
        break

def loop_remover_quarto():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print(divider)

        if not waystone.get_quartos():
            print("Não existem quartos registrados.")
            print(divider)
            break
    
        print("No momento, possuímos os seguintes quartos:")
    
        for index, quarto in enumerate(waystone.get_quartos()):
            print(index, "-", quarto)

        print(divider)

        choice = input("Qual quarto você deseja remover (ou escreva 'voltar' para voltar a tela anterior)? ")
    
        if choice == "voltar":
            break
        try:
            current_user.remover_quarto(waystone, int(choice))
        except:
            print(f"Você precisa escolher um número de 0 a {len(waystone.get_quartos()) - 1}. Ou escreva 'voltar' para voltar à tela anterior")

def loop_registrar_hospede():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Você escolheu 'Registrar hóspede'.")
    
    while True:
        ja_cadastrado = False
    
        print("Digite o CPF do hóspede, ou 'voltar' para voltar.")
    
        cpf = input(">")
    
        if cpf == "voltar":
            break
        try:
            cpf = int(cpf)
        except:
            print("Favor digitar o número de CPF ou 'voltar'.")
            continue
    
        for hospede in waystone.get_hospedes():
            if cpf == hospede.get_id():
                print("Hóspede já cadastrado")
                ja_cadastrado = True
                break
    
        if ja_cadastrado == True:
            continue
    
        print("Digite o nome completo do hóspede.")
    
        nome = input(">")
    
        print("Digite o email do hóspede.")
    
        email = input(">")
    
        new_hospede = Hospede(cpf, nome, email)
        current_user.registrar_hospede(waystone, new_hospede)
        break

def loop_funcionario_cancelar_reserva():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Você escolheu 'Cancelar reserva'.")
    
    while True:
        print(divider)

        reservas = [reserva for reserva in waystone.get_reservas()]
    
        if not reservas:
            print("Não existem reservas registradas no momento.")
            print(divider)
            break
    
        print("No momento, possuímos as seguintes reservas:")
    
        for index, reserva in enumerate(reservas):
            print(index, "-", reserva)

        print(divider)
        print("Qual reserva você deseja cancelar (ou escreva 'voltar' para voltar para a tela anterior)?")
    
        choice = input(">")
    
        if choice == "voltar":
            break
        try:
            reservas[int(choice)].get_quarto().liberar()
            reservas[int(choice)].get_hospede().cancelar_reserva(reservas[int(choice)])
        except:
            print(f"Você precisa escolher um número de 0 a {len(reservas) - 1}. Ou escreva 'voltar' para voltar a tela anterior")
            continue
    
        current_user.cancelar_reserva(waystone, reservas[int(choice)])

def loop_hospede_start():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print("Você selecionou 'Hóspede'.")
        print("1 - Log in")
        print("2 - Cadastrar")
        print("3 - Voltar")
    
        choice = input(">")
    
        if choice == "1":
            loop_hospede_login()
        elif choice == "2":
            loop_hospede_cadastrar()
        elif choice == "3":
            break
        else:
            print("Favor escolher um número entre 1-3.")

def loop_hospede_cadastrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Você escolheu 'Cadastrar'.")
    
    while True:
        ja_cadastrado = False
    
        print("Digite o seu número de CPF, ou 'voltar' para voltar à tela anterior.")
    
        cpf = input(">")
    
        if cpf == "voltar":
            break
        try:
            cpf = int(cpf)
        except:
            print("Favor digitar o seu número de CPF, ou 'voltar'.")
            continue
    
        for hospede in waystone.get_hospedes():
            if cpf == hospede.get_id():
                print("Hóspede já cadastrado.")
                ja_cadastrado = True
                break
    
        if ja_cadastrado:
            continue
    
        print("Digite o seu nome completo:")
    
        nome = input(">")
    
        print("Digite o seu email pessoal:")
    
        email = input(">")
    
        new_hospede = Hospede(cpf, nome, email)
        waystone.registrar_hospede(new_hospede)
        break

def loop_hospede_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global current_user
    
    while True:
        print("Favor informar o seu número de CPF, ou 'voltar' para voltar à tela anterior.")
    
        choice = input(">")
    
        if choice == "voltar":
            break
    
        for hospede in waystone.get_hospedes():
            if choice == str(hospede.get_id()):
                current_user = hospede
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hóspede autenticado com sucesso.")
                loop_hospede()
                return
    
        print("Hóspede não encontrado. Você já fez o cadastro?")

def loop_hospede():
    print(f"Bem vindo, {current_user.get_nome()}.")
    print("O que você gostaria de fazer?")
    
    while True:
        print("1 - Fazer reserva")
        print("2 - Cancelar reserva")
        print("3 - Consultar reservas")
        print("9 - Voltar")
    
        choice = input(">")
    
        if choice == "9":
            break
        elif choice == "1":
            loop_hospede_fazer_reserva()
        elif choice == "2":
            loop_hospede_cancelar_reserva()
        elif choice == "3":
            hospede_consultar_reservas()
        else:
            print("Escolha não reconhecida. Tente novamente.")

def loop_hospede_fazer_reserva():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print(divider)

        quartos_disponíveis = [quarto for quarto in waystone.get_quartos() if quarto.esta_disponivel()]
        if not quartos_disponíveis:
            print("Não há quartos disponíveis no momento.")
            print(divider)
            break
    
        print("No momento, os seguintes quartos estão disponíveis:")
    
        for index, quarto in enumerate(quartos_disponíveis):
            print(index, "-", quarto)
    
        print(divider)
        print("Qual quarto você gostaria de reservar (ou digite 'voltar' para voltar)?")
    
        choice = input(">")
    
        if choice == "voltar":
            break
        try:
            choice = int(choice)
        except:
            print(f"Favor escolher um número entre 0 e {len(quartos_disponíveis)}, ou 'voltar'.")
            continue
    
        try:
            new_reserva = Reserva(current_user, quartos_disponíveis[choice])
        except:
            print(f"Favor escolher um número entre 0 e {len(quartos_disponíveis)}, ou 'voltar'.")
            continue
    
        current_user.fazer_reserva(new_reserva)
        waystone.add_reserva(new_reserva)
        quartos_disponíveis[choice].reservar()
        break
        
def loop_hospede_cancelar_reserva():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print(divider)

        reservas = [reserva for reserva in current_user.consultar_reservas()]
    
        if not reservas:
            print("Não há reservas no seu nome.")
            print(divider)
            break
    
        print("No momento, você tem as seguintes reservas:")
    
        for index, reserva in enumerate(reservas):
            print(index, "-", reserva)
    
        print(divider)
        print("Qual reserva você gostaria de cancelar (ou digite 'voltar' para voltar)?")
    
        choice = input(">")
    
        if choice == "voltar":
            break
        try:
            choice = int(choice)
        except:
            print(f"Favor escolher um número entre 0 e {len(reservas)}, ou 'voltar'.")
            continue
    
        try:
            current_user.cancelar_reserva(reservas[choice])
        except:
            print(f"Favor escolher um número entre 0 e {len(reservas) - 1}, ou 'voltar'.")
            continue
    
        waystone.cancelar_reserva(reservas[choice])
        reservas[choice].get_quarto().liberar()

def hospede_consultar_reservas():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    reservas = [reserva for reserva in current_user.consultar_reservas()]
    
    print(divider)

    if not reservas:
        print("Não há reservas no seu nome.")
        print(divider)
        return
    
    print("No momento, você tem as seguintes reservas:")
    
    for index, reserva in enumerate(reservas):
        print(index, "-", reserva)

    print(divider)

divider = "-" * 30
waystone = Hotel()
current_user = object()

initialize_test_objects()
loop_start()