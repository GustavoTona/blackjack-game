from baralho import Baralho
from jogador import Jogador

# Criando os baralhos
baralho = Baralho()

# Criando os jogadores
jogador = Jogador("Jogador 1")
dealer = Jogador("Dealer")

# Distribuição das cartas iniciais
for _ in range(2):
    jogador.adicionar_carta(baralho.distribuir())
    dealer.adicionar_carta(baralho.distribuir())

# Mostrando as cartas iniciais dos jogadores
jogador.mostrar_mao()
dealer.mostrar_mao()

# Distribuição de cartas adicionais
for current_jogador in [jogador, dealer]:
    while current_jogador.pontuacao < 21:
        decisao = input(f"Deseja pedir mais cartas, {current_jogador.nome}? (sim/não): ").lower()
        if decisao == 's':
            carta = baralho.distribuir()
            current_jogador.adicionar_carta(carta)
            current_jogador.mostrar_mao()
        elif decisao == 'n':
            break

# Determinação do vencedor
if jogador.pontuacao > 21:
    print(f"{jogador.nome} estourou! {jogador.nome} perdeu.")
elif dealer.pontuacao > 21 or jogador.pontuacao > dealer.pontuacao:
    print(f"{jogador.nome} ganhou!")
elif jogador.pontuacao == dealer.pontuacao:
    print("Empate!")
else:
    print(f"{dealer.nome} ganhou!")

# Atualização do saldo dos jogadores
jogador.saldo += 100 if jogador.pontuacao <= 21 else -100  # Adicionando ou subtraindo 100 do saldo do jogador conforme o resultado
print(f"Saldo final de {jogador.nome}: {jogador.saldo}")
