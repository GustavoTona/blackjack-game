class Jogador:
    def __init__(self, nome, saldo = 1000): # self, você pode acessar atributos e métodos da classe dentro de seus métodos.
        self.mao = [] # inicializa a mao com uma lista vazia
        self.pontuacao = 0 # pontuacao zero 
        self.nome = nome
        self.saldo = saldo

    #Pedir mais uma carta
    def adicionar_carta(self, carta): 
        self.mao.append(carta) #adiciona o elemento especificado ao final da lista
        self.calcular_pontuacao() #atualiza a pontuacao com base nas cartas adicionada
    
    def calcular_pontuacao(self): 
         self.pontuacao = sum(map(int, self.mao))# calcula os pontos somando os valores da carta 

    def mostrar_mao(self):
        print("Cartas na mão de", self.nome + ":", self.mao)
        print("Pontuação de", self.nome + ":", self.pontuacao)