print("=====ORIENTAÇÃO A OBJETOS COM PYTHON - CLASSES, OBJETOS, HERANÇA=====")
print()
#1. Crie uma classe chamada Carro com os atributos marca e modelo. Depois crie dois objetos diferentes dessa classe e imprima os valores.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carro("Ford", "KA")
carro2 = Carro("Honda", "Civic")

print(f"Carro 1: {carro1.marca} {carro1.modelo}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}")

#2. Crie uma classe chamada Cachorro com os atributos nome e idade. Adicione um método que exibe "Au au, meu nome é X e tenho Y anos"
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"Au au, meu nome é {self.nome} e tenho {self.idade} anos")

dog = Cachorro("Ralf", 5)
dog.latir()

#3.Crie uma classe chamada Livro com atributos titulo, autor e ano. Instancie três livros diferentes e mostre suas informações.
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano})"

livro1 = Livro("A culpa é das estrelas", "John Green", 2012)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro3 = Livro("Divina comedia", "Dante Alighieri", 1304)

print(livro1)
print(livro2)
print(livro3)

#4. Adicione à classe Carro um método chamado dirigir() que imprime "O carro está em movimento".
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def dirigir(self):
        print(f"O {self.marca} {self.modelo} está em movimento!")

carro1 = Carro("Fiat", "Palio")
carro1.dirigir()

#5. Na classe Cachorro, adicione um método aniversario() que aumenta a idade em 1 e mostre o novo valor
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        print(f"Au au, meu nome é {self.nome} e tenho {self.idade} anos")
    
    def aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos!")

dog = Cachorro("Ralf", 4)
dog.latir()
dog.aniversario()
dog.latir()

#6. Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione métodos para depositar(valor) e sacar(valor). Garanta que o saldo não fique negativo.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor <= 0:
            print("Valor de saque deve ser positivo")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
    
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta = ContaBancaria("Matuzalem", 500)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.sacar(1500) #tentando sacar o que não tem

#7. Crie uma classe Pessoa com atributos nome e idade. Depois crie uma classe Estudante que herda de Pessoa e adiciona matricula e curso.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    
    def __str__(self):
        return f"Estudante: {self.nome}, {self.idade} anos, Matrícula: {self.matricula}, Curso: {self.curso}"

estudante = Estudante("Chico", 20, "20230507", "Sistemas de Informação")
print(estudante)

#8. Crie uma classe Funcionario que herda de Pessoa e adiciona salario. Crie um método que calcula o 13º salário (um salário extra).
class Funcionario(Pessoa): #Herdando Pessoa da questão anterior
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def calcular_decimo_terceiro(self):
        decimo = self.salario
        print(f"O 13º salário de {self.nome} é R${decimo:.2f}")

func = Funcionario("Maria", 35, 2550)
func.calcular_decimo_terceiro()

#9. Crie uma classe Professor que herda de Funcionario e adiciona a propriedade disciplina. Crie um método que exiba "Professor X leciona Y".
class Professor(Funcionario): #Herdando das questões anteriores
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade, salario)
        self.disciplina = disciplina
    
    def apresentar(self):
        print(f"Professor {self.nome} leciona {self.disciplina}")

prof = Professor("Mario", 40, 11000, "Quimica Geral")
prof.apresentar()

#10. Crie uma classe Artista com um método apresentar() que imprime "Sou artista". Crie uma classe Programador com um método apresentar() que imprime "Sou programador".
#Depois crie uma classe PessoaMultiTalento que herda de ambas e veja qual método é chamado.
class Artista:
    def apresentar(self):
        print("Sou artista")

class Programador:
    def apresentar(self):
        print("Sou programador")

class PessoaMultiTalento(Artista, Programador):
    def apresentar(self):
        print("Sou uma pessoa multitalento!")
        Artista.apresentar(self)   #ou poderia ser Programador.apresentar(self)

p = PessoaMultiTalento()
p.apresentar()

#11.Use super() em todas as classes do exercício anterior para que os métodos sejam chamados em cadeia, seguindo a MRO.
class Artista:
    def apresentar(self):
        print("Sou artista")
        super().apresentar() if hasattr(super(), 'apresentar') else None

class Programador:
    def apresentar(self):
        print("Sou programador")
        super().apresentar() if hasattr(super(), 'apresentar') else None

class PessoaMultiTalento(Artista, Programador):
    def apresentar(self):
        print("Sou uma pessoa multitalento!")
        super().apresentar()

p = PessoaMultiTalento()
p.apresentar()

#12. Modele um sistema escolar simples:
#● Classe Pessoa (nome, idade)
#● Classe Aluno (herda de Pessoa, com matrícula e notas)
#● Classe Professor (herda de Pessoa, com disciplina e salário)
#● Crie métodos para cadastrar notas no aluno e calcular a média.
#● Crie objetos de alunos e professores e exiba os dados formatados
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []
    
    def cadastrar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota {nota} cadastrada para {self.nome}")
            print()
        else:
            print("Nota deve estar entre 0 e 10")
            
    def calcular_media(self):
        if not self.notas:
            return 0
        media = sum(self.notas) / len(self.notas)
        return media
    
    def __str__(self):
        media = self.calcular_media()
        status = "Aprovado" if media >= 7 else "Reprovado"
        return f"Aluno: {self.nome}, {self.idade} anos\nMatrícula: {self.matricula}\nNotas: {self.notas}\nMédia: {media:.2f} - {status}"

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario
    
    def __str__(self):
        return f"Professor: {self.nome}, {self.idade} anos\nDisciplina: {self.disciplina}\nSalário: R${self.salario:.2f}"

prof1 = Professor("Mario", 42, "Português", 4000)
aluno1 = Aluno("Luigi", 17, "20240107")
aluno2 = Aluno("Toad", 16, "20240106")

print(prof1)
print()

aluno1.cadastrar_nota(8.5)
aluno1.cadastrar_nota(7.0)
aluno1.cadastrar_nota(9.0)

aluno2.cadastrar_nota(6.0)
aluno2.cadastrar_nota(5.5)
aluno2.cadastrar_nota(4.0)

print(aluno1)
print()
print(aluno2)
