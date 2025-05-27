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

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def registar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def remover_quarto(self, index_quarto):
        self.__quartos.pop(index_quarto)
        print("Quarto removido com sucesso.")

    def cancelar_reserva(self, reserva):
        pass

    def get_quartos(self):
        return self.__quartos

    def listar_reservas(self):
        pass

    def get_funcionarios(self):
        return self.__funcionarios