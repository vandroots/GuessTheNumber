
from random import randint

tentativas = 10
numero_sorteado = str(randint(1, 60))
tentativa = ""

while(tentativa != "S" and tentativas > 0):
    tentativa = input("Tente adivinhar meu número: ")

    if(tentativa == numero_sorteado):
        print("Parabéns você ganhou :)")
        break
    else:
        print("Tente novamente!")

    tentativas -= 1
    if(tentativas == 0):
        print("O jogo acabou!")
