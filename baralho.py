import random

class Baralho:
    # defina os valores iniciais dos atributos do seu objeto.
    # init influencia como o objeto é inicializado
    # init Cria a lista inicial de cartas que compõem o baralho.
    
    def __init__(self): # self, você pode acessar atributos e métodos da classe dentro de seus métodos.
        self.cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11'] * 4 # multiplicar por 4, são 4 baralhos
        # Em seguida o baralho é embaralhado
        self.embaralhar()
    
    def embaralhar(self): # self, você pode acessar atributos e métodos da classe dentro de seus métodos.
        random.shuffle(self.cartas) # utilizado para embaralhar a lista de cartas

    def distribuir(self):
        return self.cartas.pop()
