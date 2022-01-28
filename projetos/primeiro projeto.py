from time import sleep
from random import randint

print("=" * 50)
print(f"{' CAÇA EMOJIS ':=^50}")
print("=" * 50)
print("")

DinheiroTotal = 1000000
Emojis = ("😷", "😎", "😍", "😨", "😈")
Emoji1 = 0
Emoji2 = 0
Emoji3 = 0
ValorGanho = 0
ValorPerdido = 0
ContadorPerdas = 0
ContadorGanhos = 0
R = True

# Loop infinito
# o loop só para se o "R" for falso
while R:
    print("—" * 50)
    print(f"{f'Você tem R${DinheiroTotal}': >50}")
    while True:
        try:
            ValorDaAposta = int(input("Digite o valor da aposta: R$"))
            break
        except:
            print("----> Erro! digite apenas números!")
        else:
            if ValorDaAposta <= 0:
                print("----> O valor não pode ser 0 ou abaixo!")
            elif ValorDaAposta > DinheiroTotal:
                print("----> Valor superior ao seu saldo atual!")
            elif ValorDaAposta <= DinheiroTotal:
                break

    print(f""" \n [😷] {ValorDaAposta} × 10
 [😎] {ValorDaAposta} × 100
 [😍] {ValorDaAposta} × 1000
 [😨] {ValorDaAposta} × 10000
 [😈] {ValorDaAposta} × 100000""")

# Aqui mostra os emojis aleatórios
    print("•" * 50)
    print(f"{'==========': ^50}")
    sleep(1)
    # Aqui é o emoji 1
    Emoji1 = randint(0, 4)
    print(f"{Emojis[Emoji1]: >22}", end = "", flush = True)
    sleep(1)
    # Aqui é o emoji 2
    Emoji2 = randint(0, 4)
    print(f"{Emojis[Emoji2]: >2}", end = "", flush = True)
    sleep(1)
    # Aqui é o emoji 3
    Emoji3 = randint(0, 4)
    print(f"{Emojis[Emoji3]: >2}")
    print(f"{'==========': ^50}")
    print("•" * 50)

    #Se todos os emojis forem iguais roda esse:
    if Emoji1 == Emoji2 == Emoji3:
        ContadorGanhos += 1 

        # Se os emojis iguais forem "😷" roda esse:
        if Emoji1 == 0:
            ValorMais = ValorDaAposta * 10
            DinheiroTotal += ValorMais
            ValorGanho += ValorMais
            print(f"{f'VOCÊ GANHOU R${ValorMais}!': ^50}")

        # Se os emojis iguais forem "😎" roda esse:
        if Emoji1 == 1:
            ValorMais = ValorDaAposta * 100
            DinheiroTotal += ValorMais
            ValorGanho += ValorMais
            print(f"{f'VOCÊ GANHOU R${ValorMais}!': ^50}")

        # Se os emojis iguais forem "😍" roda esse:
        if Emoji1 == 2:
            ValorMais = ValorDaAposta * 1000
            DinheiroTotal += ValorMais
            ValorGanho += ValorMais
            print(f"{f'VOCÊ GANHOU R${ValorMais}!': ^50}")

        # Se os emojis iguais forem "😨" roda esse:
        if Emoji1 == 3:
            ValorMais = ValorDaAposta * 10000
            DinheiroTotal += ValorMais
            ValorGanho += ValorMais
            print(f"{f'VOCÊ GANHOU R${ValorMais}!': ^50}")

        # Se os emojis iguais forem "😈" roda esse:
        if Emoji1 == 4:
            ValorMais = ValorDaAposta * 100000
            DinheiroTotal += ValorMais
            ValorGanho += ValorMais
            print(f"{f'VOCÊ GANHOU R${ValorMais}!': ^50}")

    # Se pelo menos um emoji for diferente roda esse:
    elif Emoji1 != Emoji2 or Emoji2 != Emoji3 or Emoji3 != Emoji1:
        ContadorPerdas += 1
        DinheiroTotal -= ValorDaAposta
        ValorMenos = ValorDaAposta
        ValorPerdido += ValorDaAposta
        print(f"{f'VOCÊ PERDEU R${ValorMenos}!': ^50}")
    print("—" * 50)

    # Se o jogador zerar o seu saldo roda esse:
    if DinheiroTotal == 0:
        print("----> O SEU DINHEIRO ACABOU!")
        sleep(2)
        break

    # Aqui pergunta se o jogador quer continuar
    while True:
        try:
            Resposta = str(input("Quer continuar jogando? ")).upper().strip()[0]
        except:
            print("----> Resposta inválida! Digite apenas 'Não' e 'Sim'.")
        else:
            if Resposta not in "NS" or Resposta == "":
                print("----> Resposta inválida! Digite apenas 'Não' e 'Sim'.")
            elif Resposta == "N":
                R = False
                break
            elif Resposta == "S":
                break

# Tabela final
print(" ")
print("="*50)
print(f"{'JOGO FINALIZADO': ^50}")
print(" ")

# Se o jogador não ganhar roda esse:
if ContadorGanhos == 0:
    print("Você não ganhou nessa partida!")

# Se o jogador ganhar apenas uma vez roda esse:
elif ContadorGanhos == 1:
    print(f"Você ganhou {ContadorGanhos} vez")
    print(f"Você ganhou R${ValorGanho}")

# Se o jogador ganhar mais de uma vez roda esse:
elif ContadorGanhos > 1:
    print(f"Você ganhou {ContadorGanhos} vezes")
    print(f"Você ganhou R${ValorGanho}")
print(" ")

# Se o jogador não perder roda esse:
if ContadorPerdas == 0:
    print("Você não perdeu nessa partida!")

# Se o jogador perder apenas uma vez roda esse:
elif ContadorPerdas == 1:
    print(f"Você perdeu {ContadorPerdas} vez")
    print(f"Você perdeu R${ValorPerdido}")

# Se o jogador perder mais de uma vez roda esse:
elif ContadorPerdas > 1:
    print(f"Você perdeu {ContadorPerdas} vezes")
    print(f"Você perdeu R${ValorPerdido}")
print(" ")

# Aqui mostra o saldo total
print(f"Seu saldo total é de R${DinheiroTotal}", end = " ")
if DinheiroTotal > 1000000:
    print("Saldo positivo!")
elif DinheiroTotal < 1000000:
    if DinheiroTotal == 0:
        print("Saldo zerado!")
    else:
        print("Saldo negativo!")
elif DinheiroTotal == 1000000:
    print("Não houve alteração no seu saldo total!")
print("="*50)
