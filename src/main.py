from pessoa import Pessoa
from funcionario import Funcionario
from hospede import Hospede
from hotel import Hotel
from quarto import Quarto
from reserva import Reserva

def start_loop():
    print("-" * 20)
    print("Bem vindo ao hotel Waystone.")
    
    while True:
        print("Digite 1 para hóspede.")
        print("Digite 2 para funcionário.")
        print("Digite 'sair' para fechar o programa.")
        choice = input(">")
        if choice == "1":
            hospede_loop()
        elif choice == "2":
            funcionario_loop()
        elif choice == "sair":
            exit()
        else:
            print("Escolha não reconhecida. Favor tentar novamente.")
            

def hospede_loop():
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
        


waystone = Hotel()

start_loop()