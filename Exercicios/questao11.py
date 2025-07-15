class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
       

class Carro(Veiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
   
    def informar_tipo(self,tipo):
        return print(f"Carro - {self.marca} - {self.modelo}")
       
class Moto(Veiculo):  
    def informar_tipo(self):
        return print(f"Moto - {self.marca} - {self.modelo}")
       
class Caminhao(Veiculo):
    def informar_tipo(self):
        return print(f"Caminhão - {self.marca} - {self.modelo}")
   
lista_veiculos = []

while True:
    tipo = input("\nDigite o tipo de veículo ou sair: ").lower()
    match tipo:
        case "carro":
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            v1 = Carro(marca,modelo)
            lista_veiculos.append(v1)
        case "moto":
            marca = input("Digite a marca da moto: ")
            modelo = input("Digite o modelo da moto: ")
            v2 = Moto(marca,modelo)
            lista_veiculos.append(v2)
        case "caminhao":
            marca = input("Digite a marca do caminhão: ")
            modelo = input("Digite o modelo do caminhão: ")
            v3 = Caminhao(marca,modelo)
            lista_veiculos.append(v3)
        case "sair":
            break
            
for item in lista_veiculos:
    item.informar_tipo()