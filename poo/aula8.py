class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.class_name = self.__class__.__name__

    def falar(self):
        print(f"{self.class_name} esta falando")


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.class_name} comprando...')

class ClienteVip(Cliente):
    def falar(self):
        super().falar()
        print("aaa")


cliente = ClienteVip("Kaique", 19)
cliente.comprar()
cliente.falar()
