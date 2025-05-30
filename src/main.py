from pessoa import Pessoa
from funcionario import Funcionario
from hospede import Hospede
from hotel import Hotel
from quarto import Quarto
from reserva import Reserva

def implement_test_objects():
    test_hospede = Hospede(456, "João Silva", "joao@email.com")
    test_funcionario = Funcionario(123, "Maria Brito", "maria@hotel.com")
    test_quarto = Quarto(1, "casal")
    test_reserva = Reserva(test_hospede, test_quarto)
    test_quarto.reservar()

    waystone.add_quarto(test_quarto)
    waystone.add_hospede(test_hospede)
    test_hospede.fazer_reserva(test_reserva)
    waystone.add_reserva(test_reserva)
    

def start_loop():
    print("-" * 20)
    print("Bem vindo ao hotel Waystone.")
    
    while True:
        print("Digite 1 para hóspede.")
        print("Digite 2 para funcionário.")
        print("Digite 'sair' para fechar o programa.")
        choice = input(">")
        if choice == "1":
            hospede_start_loop()
        elif choice == "2":
            funcionario_loop()
        elif choice == "sair":
            exit()
        else:
            print("Escolha não reconhecida. Favor tentar novamente.")    

def hospede_start_loop():
    while True:
        print("Você selecionou 'hóspede'.")
        print("Você gostaria de:")
        print("1 - log in")
        print("2 - cadastrar")
        print("3 - voltar")
        escolha = input(">")
        if escolha == "1":
            hospede_login()
        elif escolha == "2":
            hospede_cadastrar()
        elif escolha == "3":
            break
        else:
            print("Favor digitar 1-3.")

def hospede_cadastrar():
    while True:
        cpf = ""
        nome = ""
        email = ""
        cpf = int(input("Digite o seu CPF: "))
        for hospede in waystone.get_hospedes():
            if hospede.get_id() == cpf:
                print("Já existe um hóspede com esse CPF. Favor cadastrar outro CPF.")
                continue
        nome = input("Digite o seu nome completo: ")
        email = input("Digite o seu email: ")
        novo_hospede = Hospede(cpf, nome, email)
        waystone.registrar_hospede(novo_hospede)
        print("Você foi cadastrado com sucesso.")
        break
        
def hospede_login():
    global current_user
    while True:
        escolha = input("Digite o seu número de CPF ou 'voltar': ")
        if escolha == "voltar":
            break
        try:
            escolha = int(escolha)
        except:
            print("Favor digitar apenas os números do seu CPF.")
            continue
        for hospede in waystone.get_hospedes():
            if escolha == hospede.get_id():
                current_user = hospede
                print("Hóspede autenticado com sucesso.")
                hospede_loop()
                return
        print("Hóspede não encontrado. Você já fez o cadastro?")

def hospede_loop():
    print(f"Bem vindo, {current_user.get_nome()}.")
    while True:
        opcao = 0
        print("O que você gostaria de fazer?")
        print("1 - Fazer nova reserva")
        print("2 - Cancelar reserva")
        print("3 - Consultar reservas")
        print("9 - Voltar")
        try:
            opcao = int(input(">"))
        except:
            print("Por favor digite o número da sua opção escolhida.")
            continue
        if opcao == 9:
            break
        elif opcao == 1:
            hospede_fazer_reserva()
        elif opcao == 2:
            hospede_cancelar_reserva()
        elif opcao == 3:
            current_user.consultar_reservas()
        else:
            print("Opção não diponível. Tente novamente.")

def hospede_fazer_reserva():
    print("No momento, temos os seguintes quartos disponíveis:")
    for index, quarto in enumerate(waystone.get_quartos()):
        if quarto.esta_disponivel():
            print(index, "-", quarto)
    while True:
        escolha = int(input("Qual o número do quarto que você gostaria de reservar? "))
        



        

waystone = Hotel()
current_user = object()


implement_test_objects()
start_loop()