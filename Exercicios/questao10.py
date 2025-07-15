class Funcionario:
    def __init__(self,_nome,_salario_base):
        self._nome = _nome
        self._salario_base = _salario_base
        
class Gerente(Funcionario):
    def __init__(self, _nome, _salario_base, bonus = 0.2):
        super().__init__(_nome, _salario_base)
        self.bonus = bonus
        
    def salario_total(self, _salario_base, bonus):
        bonus = vendas * bonus
        return _salario_base + bonus
        
class Vendedor(Funcionario):
    def __init__(self, _nome, _salario_base,comissao):
        super().__init__(_nome, _salario_base)
        self.comissao = comissao
    
    def salario_total(self, _salario_base, comissao, vendas):
        comissao = vendas * comissao
        return _salario_base + comissao


nome = input("Digite seu nome: ")
salarioBase = float(input("Digite o salário base: R$"))
bonus = 0.2
comissao = 0.05
vendas = float(input("Digite o valor das vendas: R$"))
F1 = Funcionario(nome,salarioBase)
V1 = Vendedor(salarioBase,comissao,vendas)
print(f"{nome} {V1.salario_total(salarioBase,comissao,vendas)}")