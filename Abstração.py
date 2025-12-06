'''Você foi contratado para desenvolver um sistema de pagamentos para uma loja online. O sistema deve
atender aos seguintes requisitos:
1. Todo pagamento deve ter um valor e um método obrigatório processar_pagamento().
○ Isso deve ser definido em uma classe abstrata chamada Pagamento.
2. A loja deve aceitar diferentes formas de pagamento (Cartão de Crédito, Pix e Boleto).
○ Cada classe filha deve implementar o método abstrato processar_pagamento() de acordo
com sua forma de pagamento.
3. Para garantir que qualquer forma de pagamento possa ser cancelada, crie uma interface Cancelavel
que tenha o método abstrato cancelar_pagamento().
○ Todas as classes de pagamento devem implementar essa interface.'''

print("=====ABSTRAÇÃO=====")
print()
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class Cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self):
        pass

class CartaoCredito(Pagamento, Cancelavel):
    def __init__(self, valor, numero_cartao, titular):
        super().__init__(valor)
        self.numero_cartao = numero_cartao
        self.titular = titular

    def processar_pagamento(self):
        print(f"Processando R$ {self.valor:.2f} via Cartão de Crédito.")
        print(f"Status: Autorizado para o cartão do titular {self.titular}.")
        return True

    def cancelar_pagamento(self):
        print(f"Estornando R$ {self.valor:.2f} do Cartão de Crédito. A operadora processará o reembolso.")
        return True

class Pix(Pagamento, Cancelavel):
    def __init__(self, valor, chave_destino):
        super().__init__(valor)
        self.chave_destino = chave_destino

    def processar_pagamento(self):
        print(f"Processando R$ {self.valor:.2f} via Pix.")
        print(f"Status: QR Code gerado. Aguardando a confirmação da transferência para a chave {self.chave_destino}.")
        return True

    def cancelar_pagamento(self):
        print(f"Cancelamento/Devolução de R$ {self.valor:.2f} via Pix iniciado. O valor será estornado para a conta de origem.")
        return True

class Boleto(Pagamento, Cancelavel):
    def __init__(self, valor, linha_digitavel):
        super().__init__(valor)
        self.linha_digitavel = linha_digitavel

    def processar_pagamento(self):
        print(f"Processando R$ {self.valor:.2f} via Boleto Bancário.")
        print(f"Status: Boleto gerado com linha digitável: {self.linha_digitavel[:10]}...")
        return True

    def cancelar_pagamento(self):
        print(f"Boleto de R$ {self.valor:.2f} com linha digitável {self.linha_digitavel[:10]}... foi **cancelado/baixado** no sistema bancário.")
        return True

if __name__ == '__main__':
    print("=====Compras=====")

    pagto_cartao = CartaoCredito(valor=150.75, numero_cartao="1234****", titular="Matuzalem Marinho")
    print("\n[Transação 1: Cartão de Crédito]")
    pagto_cartao.processar_pagamento()
    # Cancelamento
    if isinstance(pagto_cartao, Cancelavel):
        pagto_cartao.cancelar_pagamento()
    print("-" * 30)

    # Pix
    pagto_pix = Pix(valor=55.00, chave_destino="9e2010")
    print("\n[Transação 2: Pix]")
    pagto_pix.processar_pagamento()
    print("-" * 30)

    # Boleto
    pagto_boleto = Boleto(valor=320.90, linha_digitavel="341.20")
    print("\n[Transação 3: Boleto]")
    pagto_boleto.processar_pagamento()
    # Cancelamento
    if isinstance(pagto_boleto, Cancelavel):
        pagto_boleto.cancelar_pagamento()
    print("-" * 30)
