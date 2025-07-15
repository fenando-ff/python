class Transporte:
    def __init__(self, capacidade,passageiros):
        self._capacidade = capacidade
        self.__passageiros = passageiros
        
    def embarcar(self,qtd):
        if self.__passageiros > self._capacidade:
            print("Não há vagas suficientes!")
        else:
            self.__passageiros += qtd
            print("Embarque feito com sucesso!")
        return self.__passageiros
    
class Onibus(Transporte):
    def __init__(self, passageiros):
        super().__init__(40, passageiros)
    
    def embarcar(self, qtd):
        return super().embarcar(qtd)
    
class Metro(Transporte):
    def __init__(self, passageiros):
        super().__init__(100, passageiros)
    
    def embarcar(self, qtd):
        return super().embarcar(qtd)
    
class Trem(Transporte):
    def __init__(self, passageiros):
        super().__init__(80, passageiros)
    
    def embarcar(self, qtd):
        return super().embarcar(qtd)
    

while True:
    opcao = int(input("1- Onibus | 2 - Metro | 3 - Trem | 0 - Sair: "))
    match opcao:
        case 1:
            qtd = int(input("Quantos passageiros querem entrar? : "))
            passageiros = 0
            p = Onibus(passageiros)
            passageiros = p.embarcar(qtd)
        case 0:
            break
