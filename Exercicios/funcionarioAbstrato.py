from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def __init__(self,nome,salario_base):
        self._nome = nome
        self._salario_base = salario_base

    def calcular_pagamento(self):
        pass

class Assalariado(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_pagamento(self):
        return self._salario_base

    def exibir(self):
        print(f"Nome: {self._nome} - Salário: R${self._salario_base}")

class Comissionado(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    def calcular_pagamento(self,comissao):
        return self._salario_base + comissao
    
    

lista_fucionario = []

while True:
    opcao = int(input("1 - Adicionar Assalariado | 2 - Adicionar comissionado | 3 - Exibir Funcionarios | 0 - Sair\nDigite uma opção acima: "))
    if opcao == 1:
        qtd = int(input("Quantos funcionários quer adicionar? : "))
        for i in range(1, qtd + 1):
            nome = input(f"Digite o nome do {i}º funcionário: ")
            salario = float(input("Digite o salário base: R$"))
            assalariado = Assalariado(nome, salario)
            lista_fucionario.append(assalariado)
    elif opcao == 2:
        qtd = int(input("Quantos funcionários quer adicionar? : "))
        for i in range(1, qtd + 1):
            nome = input(f"Digite o nome do {i}º funcionário: ")
            salario_base = float(input(f"Digite o salário base: R$"))
            comissionado = Comissionado(nome, salario_base)
            lista_fucionario.append(comissionado)
    elif opcao == 3:
        for funcionario in lista_fucionario:
            funcionario.exibir()
    else:
        break