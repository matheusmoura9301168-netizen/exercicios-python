# Menu com jogos de adivinha e blackjack.

import random
import sys


def mostrar_menu():
    print("\n       MENU")
    print("1. Jogo da Adivinha")
    print("2. Jogo da Adivinha 2x")
    print("3. Black jack")
    print("4. Black jack multiplayer")
    print("5. Sair")

    escolha = input()

    match escolha:
        case "1":
            Jogo_adivinha()
        case "2":
            Jogo_adivinha2()
        case "3":
            blackjack()
        case "4":
            blackjack_multiplayer()
        case "5":
            print("FIM")
            sys.exit()




def Jogo_adivinha():
    n = random.randint(1, 1000)
    t = 100
    print("começe com um numero de 0 a 1000: ")

    while t > 0:
        try:
            x = int(input())
        except:
            print("entrada inválida")
            continue
        if x == n:
            print('Acertou')
            print('Pontuação:', t)
            break
        elif x < n:
            print('Maior')
        else:
            print('Menor')
        t -= 1
    else:
        print('Fim das tentativas. Número:', n)




def Jogo_adivinha2():
    # Número secreto de cada jogador
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)


    t = 100
    pontos1 = t
    pontos2 = t
    jogador = 1

    print("Jogo da adivinhação para 2 jogadores!")
    print("Cada jogador tem um número secreto entre 1 e 1000.")
    print("Vocês vão se revezar nos palpites. O jogo termina assim que um número for revelado!\n")

    while t > 0:
        try:
            x = int(input(f"Jogador {jogador}, digite seu palpite: "))
        except:
            print("Entrada inválida, tente novamente.")
            continue

        # Feedback para Jogador 1
        if x == n1:
            print("Jogador", jogador, "acertou o número do Jogador 1!")
            pontos1 += 5  # bônus por ter número revelado
            vencedor = 1 if jogador == 1 else 2
            break
        elif x < n1:
            print("Jogador 1 → O número é MAIOR.")
        else:
            print("Jogador 1 → O número é MENOR.")

        # Feedback para Jogador 2
        if x == n2:
            print("Jogador", jogador, "acertou o número do Jogador 2!")
            pontos2 += 5  # bônus por ter número revelado
            vencedor = 2 if jogador == 2 else 1
            break
        elif x < n2:
            print("Jogador 2 → O número é MAIOR.")
        else:
            print("Jogador 2 → O número é MENOR.")

        # Reduz pontuação de quem jogou
        if jogador == 1:
            pontos1 -= 1
        else:
            pontos2 -= 1

        # Alterna jogador
        jogador = 2 if jogador == 1 else 1
        t -= 1

    else:
        print("Fim das tentativas!")
        print(f"O número do Jogador 1 era: {n1}")
        print(f"O número do Jogador 2 era: {n2}")
        vencedor = None

    # Resultado final
    print("\nResultado Final:")
    print(f"Jogador 1 → {pontos1} pontos")
    print(f"Jogador 2 → {pontos2} pontos")

    if vencedor:
        if pontos1 > pontos2:
            print(f"Jogador 1 é o vencedor!\n O  numero do Jogador 2 é {n2}")
        elif pontos2 > pontos1:
            print(f"Jogador 2 é o vencedor!\n O  numero do Jogador 1 é {n1}")
        else:
            print(f"Empate!\nO jogador 1 numero é {n1}\nO jogador 2 numero é {n2}")




def blackjack():
    # Valores das cartas
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11
    }

    # Criar baralho
    naipes = ["♠", "♥", "♦", "♣"]
    baralho = [f"{valor}{naipe}" for naipe in naipes for valor in valores.keys()]
    random.shuffle(baralho)

    # Função interna para calcular mão
    def calcular_mao(mao):
        total = 0
        ases = 0
        for carta in mao:
            valor = carta[:-1]
            total += valores[valor]
            if valor == "A":
                ases += 1
        while total > 21 and ases:
            total -= 10
            ases -= 1
        return total

    # Distribuição inicial
    jogador = [baralho.pop(), baralho.pop()]
    dealer = [baralho.pop(), baralho.pop()]

    print("=== Bem-vindo ao Blackjack ===")
    print(f"Suas cartas: {jogador} (Total: {calcular_mao(jogador)})")
    print(f"Carta visível do dealer: {dealer[0]}")

    # Turno do jogador
    while calcular_mao(jogador) < 21:
        acao = input("Deseja [H]it (pedir carta) ou [S]tand (parar)? ").upper()
        if acao == "H":
            jogador.append(baralho.pop())
            print(f"Suas cartas: {jogador} (Total: {calcular_mao(jogador)})")
        elif acao == "S":
            break
        else:
            print("Opção inválida. Digite H ou S.")

    if calcular_mao(jogador) > 21:
        print("Você estourou! Dealer vence.")
        return

    # Turno do dealer
    print(f"Cartas do dealer: {dealer} (Total: {calcular_mao(dealer)})")
    while calcular_mao(dealer) < 17:
        dealer.append(baralho.pop())
        print(f"Dealer puxa carta: {dealer[-1]}")
        print(f"Cartas do dealer: {dealer} (Total: {calcular_mao(dealer)})")

    # Resultado final
    total_jogador = calcular_mao(jogador)
    total_dealer = calcular_mao(dealer)

    print("\n=== Resultado Final ===")
    print(f"Jogador: {jogador} (Total: {total_jogador})")
    print(f"Dealer: {dealer} (Total: {total_dealer})")

    if total_dealer > 21 or total_jogador > total_dealer:
        print("Você venceu! ")
    elif total_jogador < total_dealer:
        print("Dealer venceu! ")
    else:
        print("Empate!")


def blackjack_multiplayer():
    # Valores das cartas
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11
    }

    # Função para calcular mão
    def calcular_mao(mao):
        total = 0
        ases = 0
        for carta in mao:
            valor = carta[:-1]
            total += valores[valor]
            if valor == "A":
                ases += 1
        while total > 21 and ases:
            total -= 10
            ases -= 1
        return total

    # Configuração inicial dos jogadores
    num_jogadores = int(input("Quantos jogadores (1-5)? "))
    if num_jogadores < 1 or num_jogadores > 5:
        print("Número inválido de jogadores.")
        return

    jogadores = []
    for i in range(num_jogadores):
        nome = input(f"Digite o nome do Jogador {i+1}: ")
        jogadores.append({"nome": nome, "chips": 2500})

    apostas_validas = [10, 20, 50, 100, 300, 500, 1000, 3000, 5000, 7000 ,10000]

    continuar = True

    while continuar:
        # Criar baralho
        naipes = ["♠", "♥", "♦", "♣"]
        baralho = [f"{valor}{naipe}" for naipe in naipes for valor in valores.keys()]
        random.shuffle(baralho)

        # Dealer
        dealer = {"nome": "Dealer", "mao": [baralho.pop(), baralho.pop()]}

        # Apostas
        apostas = []
        for jogador in jogadores:
            if jogador["chips"] <= 0:
                print(f"{jogador['nome']} está sem chips e não pode jogar.")
                apostas.append(0)
                continue
            print("\n"*30)
            print(f"{jogador['nome']} - Chips disponíveis: {jogador['chips']}")
            aposta = int(input(f"Escolha sua aposta {apostas_validas}: "))
            if aposta not in apostas_validas or aposta > jogador["chips"]:
                print("Aposta inválida. Será usada aposta mínima (10).")
                aposta = 10
            jogador["chips"] -= aposta
            apostas.append(aposta)

        # Distribuição inicial
        for jogador in jogadores:
            jogador["mao"] = [baralho.pop(), baralho.pop()]

        print("\n    Cartas iniciais ")
        for jogador in jogadores:
            print(f"\n{jogador['nome']}: {jogador['mao']} (Total: {calcular_mao(jogador['mao'])})\n")
        print(f"\nDealer mostra: {dealer['mao'][0]}\n")

        # Turno dos jogadores
        for i, jogador in enumerate(jogadores):
            if apostas[i] == 0:  # pulou jogador sem chips
                continue
            while calcular_mao(jogador["mao"]) < 21:
                acao = input(f"{jogador['nome']} - [H]it ou [S]tand? ").upper()
                if acao == "H":
                    jogador["mao"].append(baralho.pop())
                    print(f"{jogador['nome']}: {jogador['mao']} (Total: {calcular_mao(jogador['mao'])})")
                elif acao == "S":
                    break
                else:
                    print("Opção inválida.")

        # Turno do dealer
        print(f"\nDealer: {dealer['mao']} (Total: {calcular_mao(dealer['mao'])})")
        while calcular_mao(dealer["mao"]) < 17:
            dealer["mao"].append(baralho.pop())
            print(f"Dealer puxa carta: {dealer['mao'][-1]}")
            print(f"Dealer: {dealer['mao']} (Total: {calcular_mao(dealer['mao'])})")

        # Resultado final
        total_dealer = calcular_mao(dealer["mao"])
        print("\n=== Resultado Final ===")
        print(f"Dealer: {dealer['mao']} (Total: {total_dealer})")

        for i, jogador in enumerate(jogadores):
            if apostas[i] == 0:
                continue
            total_jogador = calcular_mao(jogador["mao"])
            print(f"\n{jogador['nome']}: {jogador['mao']} (Total: {total_jogador}) | Aposta: {apostas[i]}")

            if total_jogador > 21:
                print("Estourou! Perdeu a aposta.")
            elif total_dealer > 21 or total_jogador > total_dealer:
                ganho = apostas[i] * 2
                jogador["chips"] += ganho
                print(f"Você venceu! Recebeu {ganho} chips. Total: {jogador['chips']}")
            elif total_jogador == total_dealer:
                jogador["chips"] += apostas[i]
                print(f"Empate! Sua aposta foi devolvida. Total: {jogador['chips']}")
            else:
                print(f"Dealer venceu. Total: {jogador['chips']}")

        # Pergunta se querem continuar
        resposta = input("\nDesejam jogar outra rodada? (S/N): ").upper()
        if resposta != "S":
            continuar = False

    print("\n    Fim do jogo ")
    for jogador in jogadores:
        print(f"{jogador['nome']} terminou com {jogador['chips']} chips.")










while True:
    mostrar_menu()
