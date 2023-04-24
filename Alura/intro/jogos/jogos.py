import forca
import adivinhacao

print("*********************************")
print("*******Escolhe seu jogo!*********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
