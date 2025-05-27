from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self.__reservas = []

    def fazer_reserva(self, reserva):
        for reserva_existente in self.__reservas:
            if str(reserva) == str(reserva_existente):
                print("Essa reserva já existe.")
                return
        self.__reservas.append(reserva)
        print("Reserva feita com sucesso.")
        

    def cancelar_reserva(self, reserva):
        pass

    def consultar_reservas(self):
        print("Você tem as seguintes reservas:")
        if not self.__reservas:
            print("Você não tem reservas no momento.")
        for index, reserva in enumerate(self.__reservas):
            print(f"{index} - {reserva}")

    def __str__(self):
        return "hóspede " + super().__str__()