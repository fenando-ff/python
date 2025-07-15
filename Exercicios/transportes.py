lista_onibus = []
lista_metro = []
lista_trem = []

class Transporte:
    def __init__(self, capacidade, passageiros):
        self._capacidade = capacidade
        self.__passageiros = passageiros
           
    def get_passageiros(self):
        return self.__passageiros
       
class Onibus(Transporte):
    def embarcar(self,qtd):
        if self.get_passageiros() + qtd > self._capacidade:
            print(f"\nCapacidade máxima excedida - capacidade: {self._capacidade}")
        else:
            lista_onibus.append(qtd)
            print("\nEmbarque bem sucedido")
       
class Metro(Transporte):
    def embarcar(self,qtd):
        if self.get_passageiros() + qtd > self._capacidade:
            print(f"\nCapacidade máxima excedida - capacidade: {self._capacidade}")
        else:
            lista_metro.append(qtd)
            print("\nEmbarque bem sucedido")

class Trem(Transporte):
    def embarcar(self,qtd):
        if self.get_passageiros() + qtd > self._capacidade:
            print(f"\nCapacidade máxima excedida - capacidade: {self._capacidade}")
        else:
            lista_trem.append(qtd)
            print("\nEmbarque bem sucedido")
   
while True:
    opcao = int(input("1 - Onibus | 2 - Metro | 3 - Trem | 0 - Sair: "))
    match opcao:
        case 1:
            passageiros = sum(lista_onibus)
            capacidade = 40
            qtd = int(input(f"Capacidade: {capacidade}\nPassageiros: {passageiros}\nDigite a quantidade de passageiros embarcando: "))
            p = Onibus(capacidade,passageiros)
            p.embarcar(qtd)
        case 2:
            passageiros = sum(lista_metro)
            capacidade = 100
            qtd = int(input(f"Capacidade: {capacidade}\nPassageiros: {passageiros}\nDigite a quantidade de passageiros embarcando: "))
            m = Metro(capacidade,passageiros)
            m.embarcar(qtd)
        case 3:
            passageiros = sum(lista_trem)
            capacidade = 80
            qtd = int(input(f"Capacidade: {capacidade}\nPassageiros: {passageiros}\nDigite a quantidade de passageiros embarcando: "))
            t = Trem(capacidade,passageiros)
            t.embarcar(qtd)
        case 0:
            break