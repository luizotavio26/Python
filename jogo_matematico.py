#%%
import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0  # Inicializa pontos como 0

class Jogo:
    def __init__(self):
        self.s = ["+", "-", "x", "/"]

    def pergunta(self):
        self.n1 = random.randint(0, 99)
        self.n2 = random.randint(1, 99)  # Evita divisão por zero
        simbolo = random.choice(self.s)

        print(f"A equação é: {self.n1} {simbolo} {self.n2} é igual a?", flush=True)

        if simbolo == "+":
            conta = self.n1 + self.n2
        elif simbolo == "-":
            conta = self.n1 - self.n2
        elif simbolo == "x":
            conta = self.n1 * self.n2
        else:
            conta = round(self.n1 / self.n2, 2)  # Mantém 2 casas decimais para divisão

        return conta

    def resposta(self, jogador, is_computador=False):
        resultado_correto = self.pergunta()

        if is_computador:
            # Computador responde automaticamente com alguma chance de erro
            resposta = random.randint(int(resultado_correto - 10), int(resultado_correto + 10))
            print(f"O computador respondeu: {resposta}")
        else:
            try:
                resposta = float(input("Digite a resposta da equação: "))
            except ValueError:
                print("Resposta inválida! O jogo considerará como errada.")
                resposta = None

        if resposta == resultado_correto:
            print(f"Parabéns, {jogador.nome} acertou!")
            jogador.pontos += 1
        else:
            print(f"Você errou, {jogador.nome}. A resposta correta era {resultado_correto}")

def vamosjogar():
    print("Bem-vindo ao jogo!")
    p1 = input("Como você gostaria de ser chamado, Player 1? ")

    while True:
        escolha = input("Se você gostaria de jogar com outro jogador, aperte 1. Se gostaria de jogar contra o computador, aperte 2: ")

        if escolha == "1":
            p2 = input("Como posso chamar o Player 2? ")
            is_computador = False
            break
        elif escolha == "2":
            p2 = "Computador"
            is_computador = True
            break
        else:
            print("Escolha inválida, digite novamente.")

    player1 = Jogador(p1)
    player2 = Jogador(p2)

    qtt = int(input("Quantas rodadas vocês querem jogar? "))

    game = Jogo()  # Criar um único objeto do jogo

    for i in range(qtt):
        print(f"\nTurno de {player1.nome}:")
        game.resposta(player1)

        print(f"\nTurno de {player2.nome}:")
        game.resposta(player2, is_computador=is_computador)

    print("\n--- Resultado Final ---")
    print(f"{player1.nome}: {player1.pontos} pontos")
    print(f"{player2.nome}: {player2.pontos} pontos")

    if player1.pontos == player2.pontos:
        print("Empate!")
    elif player1.pontos > player2.pontos:
        print(f"{player1.nome} venceu!")
    else:
        print(f"{player2.nome} venceu!")

# Inicia o jogo
vamosjogar()

# %%
