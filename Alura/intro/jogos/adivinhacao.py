import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101, 1))
    total_de_tentativas = 3

    print("Qual o nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")

    nivel = input("Defina o nível: ")

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    pontos = 600

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if acertou:
            print("Você acertou e fez {} !".format(pontos))
            break
        else:
            if maior:
                print("Seu chute foi maior que o número secreto!")
            elif menor:
                print("Seu chute foi menor que o número secreto!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo")


if __name__ == "__main__":
    jogar()
