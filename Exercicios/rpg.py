from abc import abstractmethod
import random as R

class Personagem:
    def __init__(self, nome, vida, classe):
        self._nome = nome
        self.__vida = vida
        self.classe = classe
        
    def get_vida(self):
        return self.__vida
    
    def receber_dano(self, dano):
        if dano >= 0:
            return self.__vida - dano
        else:
            print("Digite um dano maior ou igual a zero!")
            
    @abstractmethod
    def atacar(self):
        pass
    
class Guerreiro(Personagem):
    def __init__(self, nome, vida, classe, dano = 15):
        super().__init__(nome, vida, classe = "Guerreiro")
        self._dano = dano
        
    def ver_vida(self):
        print(f"{self.get_vida()}")
        
    def atacar(self):
        tentativa = R.randint(1,20)
        print(tentativa)
        if tentativa == 1:
            print("Erro crítico")
        elif tentativa > 1 and tentativa < 13:
            print("Ataque falhou!")
        else:
            print("Ataque de espada!")
    
class Mago(Personagem):
    def __init__(self, nome, vida, classe, dano = 20):
        super().__init__(nome, vida, classe = "Mago")
        self._dano = dano
        
    def ver_vida(self):
        print(f"{self.get_vida()}")
        
    def atacar(self):
        tentativa = R.randint(1,20)
        print(tentativa)
        if tentativa == 1:
            print("Erro crítico")
        elif tentativa > 1 and tentativa < 15:
            print("A magia falhou ou não fez efeito!")
        else:
            print("Acertou o alvo com magia!")
        
        
    
class Arqueiro(Personagem):
    def __init__(self, nome, vida, classe, dano = 10):
        super().__init__(nome, vida, classe = "Arqueiro")
        self._dano = dano
        
    def ver_vida(self):
        print(f"{self.get_vida()}")
        
    def atacar(self):
        tentativa = R.randint(1,20)
        print(tentativa)
        if tentativa == 1:
            print("Erro crítico")
        elif tentativa > 1 and tentativa < 10:
            print("Errou disparo de flecha!")
        else:
            print("Acertou o alvo com um disparo de flecha!")
    


while True:
    escolha = input("Mago - Guerreiro - Arqueiro\nDigite a classe que irá usar:").lower()

    match escolha:
        case "mago":
            vida = 100
            m = Mago("Felipe",vida,"")
            m.ver_vida()
            m.atacar()
            
g = Guerreiro("Fernando",100,"")
g.ver_vida()


a = Arqueiro("Franci",100,"")
a.atacar()