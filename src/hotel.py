class Hotel():
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []
        self.__funcionarios = []
    
    def add_quarto(self, quarto):
        self.__quartos.append(quarto)
        print(f"{quarto} adicionado com sucesso.")

    def add_reserva(self, reserva):
        self.__reservas.append(reserva)
        print(f"{reserva} adicionada com sucesso.")

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)
        print("Hóspede cadastrado com sucesso.")

    def registar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)
        print("Funcionario cadastrado com sucesso.")

    def remover_quarto(self, index_quarto):
        self.__quartos.pop(index_quarto)
        print("Quarto removido com sucesso.")

    def cancelar_reserva(self, reserva):
        self.__reservas.remove(reserva)
        print("Reserva cancelada com sucesso.")

    def get_quartos(self):
        return self.__quartos

    def get_reservas(self):
        return self.__reservas

    def get_funcionarios(self):
        return self.__funcionarios
    
    def get_hospedes(self):
        return self.__hospedes