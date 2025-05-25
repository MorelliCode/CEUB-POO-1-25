from pessoa import Pessoa
from funcionario import Funcionario
from hospede import Hospede
from hotel import Hotel
from quarto import Quarto
from reserva import Reserva

list_people = []
for person in range(3):
    new_person = Pessoa(1, "new", "new@gmail.com")
    list_people.append(new_person)

print(list_people)