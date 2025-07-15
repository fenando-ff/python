from abc import ABC, abstractmethod
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass
    
class PagamentoCartao(Pagamento):
    def processar_pagamento(self,valor):
        print(f"Pagamento de R${valor} processado com cartão")
    
class PagamentoPix(Pagamento):
    def processar_pagamento(self,valor):
        print(f"Pagamento de R${valor} processado via Pix")
    
class PagamentoBoleto(Pagamento):
    def processar_pagamento(self,valor):
        print(f"Boleto de R${valor} gerado com sucesso")
        
lista = []