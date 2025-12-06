'''1. Crie uma classe Carro que possui um Motor.
○ O Motor só faz sentido dentro do Carro.
○ Se o Carro deixar de existir, o Motor também deixa.'''
print("=====ASSOCIAÇÃO, AGREGAÇÃO E COMPOSIÇÃO EM PYTHON=====")
print()
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def ligar(self):
        return "Motor ligado com potência de {} Cavalos".format(self.potencia)

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor) 
    
    def iniciar(self):
        return "Carro {} iniciado: {}".format(self.modelo, self.motor.ligar())

'''2. Crie uma classe Professor e uma classe Universidade.
○ A Universidade pode ter vários professores.
○ Mas os Professores também podem existir sem a Universidade.'''
class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def lecionar(self):
        return "{} está lecionando.".format(self.nome)

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = [] 
    
    def adicionar_professor(self, professor):
        self.professores.append(professor)
    
    def listar_professores(self):
        return [prof.nome for prof in self.professores]

'''3. Crie uma classe Autor e uma classe Livro.
○ Um autor pode escrever vários livros.
○ Um livro tem apenas um autor.
○ Os objetos devem ser capazes de interagir sem dependência total (um Autor pode existir sem
Livro e vice-versa).'''
class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        return [livro.titulo for livro in self.livros]

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor  
        autor.adicionar_livro(self) 

# Testes
print("Composição (Carro e Motor)")
carro = Carro("Ford", 86)
print(carro.iniciar())
print()
# Se carro for deletado, motor também é

print("Agregação (Universidade e Professor)")
prof1 = Professor("Sergio")
prof2 = Professor("Maira")
uni = Universidade("UFMA")
uni.adicionar_professor(prof1)
uni.adicionar_professor(prof2)
print("Professores na {}: {}".format(uni.nome, uni.listar_professores()))
print()
# Professores continuam existindo mesmo sem universidade

print("Associação (Autor e Livro)")
autor = Autor("Machado de Assis")
livro1 = Livro("Dom Casmurro", autor)
livro2 = Livro("Memórias Póstumas", autor)
print("Livros do autor {}: {}".format(autor.nome, autor.listar_livros()))
print("Autor do livro {}: {}".format(livro1.titulo, livro1.autor.nome))
# Autor e livros podem existir independentemente, mas estão associados
