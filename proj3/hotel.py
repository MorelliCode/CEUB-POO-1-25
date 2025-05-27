class Hotel():
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []
        self.__funcionarios = []
    
    def add_quarto(self, quarto):
        self.__quartos.append(quarto)

    def add_reserva(self, reserva):
        self.__reservas.append(reserva)

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def registar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def remover_quarto(self, quarto):
        pass

    def cancelar_reserva(self, reserva):
        pass

    def listar_quartos(self):
        pass

    def listar_reservas(self):
        pass

    def get_funcionarios(self):
        return self.__funcionarios