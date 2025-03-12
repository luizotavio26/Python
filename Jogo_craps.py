'''
8- Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo funciona da seguinte maneira:
O jogador lança dois dados, resultando em um valor entre 2 e 12.

Na primeira jogada:
- Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado de 'natural').
- Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado de 'craps').
- Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o Ponto do jogador.

Caso um 'Ponto' tenha sido estabelecido, o jogador continua lançando os dados:
- Se tirar o mesmo valor do Ponto, ele vence.
- Se tirar um 7 antes de repetir o Ponto, ele perde.
Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.

'''
#%%

import random

def jogardados():
    dado = random.randint(1,6)
    return dado

def jogar():
    dado1 = jogardados()
    dado2 = jogardados()
    print(dado1, dado2)
    pontos = 0
    if dado1+dado2 == 7 or dado1+dado2  == 11:
        print("Você venceu automaticamente, 'natural'")

    elif dado1+dado2 == 2 or dado1+dado2 == 3 or dado1+dado2 == 12:
        print("Você perdeu imediatamente, 'craps'")

    else:
        while True:
            pontos=dado1+dado2
            print(f"Você fez {pontos} nessa jogada")
            dado1 = jogardados()
            dado2 = jogardados()
            print(dado1, dado2)
            if dado1+dado2 == pontos:
                print("Você venceu")
                break
            elif dado1+dado2 == 7:
                print("Você perdeu")
                break

joao = jogar()
# %%
