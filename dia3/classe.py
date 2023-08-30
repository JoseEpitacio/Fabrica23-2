from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self): 
        """ Defina na classe filha """

    def andar(self):
        """ Defina na classe filha """

class Lobo(IAnimal):
    def falar(self):
        print("MIM DE PAPAAAAI, AUUUUUUUUUUUUUU")

    def andar(self):
        print("estou andando, AUUUUUUUUUUU")

class Pessoa:

    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self.idade = idade
        self.__humano = True

    def fala_pessoa(self):
        print(f"Eu sou {self._nome}")

lobo = Lobo()
lobo.falar()

pessoa = Pessoa("pita", 19)
pessoa.fala_pessoa()