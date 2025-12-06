print("=====ENCAPSULAMENTO EM PYTHON=====")
print()
##1. Crie uma classe ContaBancaria com um atributo privado __saldo.
##Inicialize o saldo com 0.
##● Crie métodos depositar(valor) e sacar(valor).
##● Crie também um método ver_saldo() que retorne o valor do saldo.
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def ver_saldo(self):
        return self.__saldo


print("===ContaBancaria básica===")
conta = ContaBancaria()
conta.depositar(100)
conta.sacar(30)
print(f"Saldo atual: R${conta.ver_saldo():.2f}")
print()

##2. Crie uma classe Pessoa com os atributos:
##● nome (público)
##● _anoNasceu (protegido)
##Instancie um objeto e mostre que é possível acessar _idade, mas que não é recomendado.
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome              
        self._anoNasceu = ano_nascimento

    def calcular_idade(self, ano_atual=2025):
        return ano_atual - self._anoNasceu


print("===Classe Pessoa===")
p = Pessoa("Ronilson", 1995)
print(f"Nome: {p.nome}")                    
print(f"Ano de nascimento: {p._anoNasceu}")
print(f"Idade aproximada: {p.calcular_idade()} anos")
print()

##3.Modifique a classe ContaBancaria para usar @property:
##● O getter deve retornar o saldo.
##● O setter deve permitir alterar o saldo somente se o valor for maior ou igual a zero.
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            raise ValueError("O saldo não pode ser negativo!")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido.")


print("===ContaBancaria com @property===")
conta2 = ContaBancaria(50)
print(f"Saldo inicial: R${conta2.saldo:.2f}")   
conta2.saldo = 200                          
print(f"Saldo após alteração: R${conta2.saldo:.2f}")
conta2.depositar(100)
print(f"Após depósito: R${conta2.saldo:.2f}")

try:
    conta2.saldo = -50
except ValueError as e:
    print(f"Erro ao tentar saldo negativo: {e}")
print()

##4.Crie uma classe Produto com atributos privados __nome e __preco.
##O nome só pode ser lido, não alterado.
##● O preço pode ser lido e alterado, mas não pode ser negativo.
##● Use @property e @setter.
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        if preco >= 0:
            self.__preco = preco
        else:
            raise ValueError("O preço não pode ser negativo")

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço não pode ser negativo")

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"


print("===Classe Produto===")
produto = Produto("Notebook", 3500.00)
print(produto)
print(f"Nome do produto: {produto.nome}")

produto.preco = 3299.90
print(f"Depois do desconto: {produto}")

try:
    produto.preco = -100
except ValueError as e:
    print(f"Erro: {e}")
