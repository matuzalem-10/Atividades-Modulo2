print("=====Polimorfismo=====")
print()
##1. Crie uma classe Animal com o método falar().
##Depois, crie as classes Cachorro e Gato que herdam de Animal e implementam falar() de forma
##diferente:
##● O cachorro deve imprimir "Au au!"
##● O gato deve imprimir "Miau!"
##● Crie uma lista com vários animais e percorra a lista chamando falar() em cada um.
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

class Galo(Animal):
    def falar(self):
        print("Cocorico!")

animais = [Cachorro(), Gato(), Galo()]
for animal in animais:
    animal.falar()
print()

##2. Crie uma classe Forma com o método area().
##Depois, crie duas classes filhas:
##● Quadrado, que recebe o lado e calcula a área.
##● Círculo, que recebe o raio e calcula a área .
##● Crie uma função que recebe uma lista de formas geométricas e imprime a área de cada uma.
class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        PI = 3.14                 
        return PI * self.raio * self.raio

def imprimir_areas(formas):
    for forma in formas:
        print(f"Área: {forma.area():.2f}")

formas = [
    Quadrado(5),
    Circulo(3),
    Quadrado(4),
    Circulo(10)
]

imprimir_areas(formas)
print()

##3. Crie uma classe Funcionario com um método salario().
##Depois crie duas subclasses:
##● Gerente, que retorna 5000.
##● Estagiario, que retorna 1500.
##● Crie uma lista com funcionários diferentes e mostre o salário de cada um.
class Funcionario:
    def salario(self):
        pass

class Gerente(Funcionario):
    def salario(self):
        return 5000

class Subgerente(Funcionario):
    def salario(self):
        return 3500

class Estagiario(Funcionario):
    def salario(self):
        return 1500

funcionarios = [
    Gerente(),
    Subgerente(),
    Estagiario()
]

print("=== Folha de Pagamento da Empresa ===")
for i, func in enumerate(funcionarios, 1):
    if isinstance(func, Gerente):
        cargo = "Gerente"
    elif isinstance(func, Subgerente):
        cargo = "Subgerente"
    else:
        cargo = "Estagiário"
    
    print(f"Funcionário {i:2d} → {cargo:12s} → R$ {func.salario():,.2f}")
print()
    
##4. Crie uma classe Veiculo com o método mover().
##Depois crie:
##● Carro, que imprime "Dirigindo...".
##● Bicicleta, que imprime "Pedalando...".
##● Avião, que imprime "Voando...".
##● Faça um programa que receba uma lista de veículos e use um loop para chamar o método mover()
##de cada um
class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("Dirigindo...")

class Bicicleta(Veiculo):
    def mover(self):
        print("Pedalando...")

class Aviao(Veiculo):
    def mover(self):
        print("Voando...")

class Navio(Veiculo):
    def mover(self):
        print("Navegando...")

def movimentar_veiculos(veiculos):
    for veiculo in veiculos:
        veiculo.mover()

veiculos = [
    Carro(),
    Bicicleta(),
    Aviao(),
    Navio()
]

movimentar_veiculos(veiculos)
