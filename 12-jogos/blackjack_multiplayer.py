# Blackjack para vários jogadores.

import random

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

    apostas_validas = [10, 20, 50, 100, 500, 1000, 5000]

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
            print(f"\n{jogador['nome']} - Chips disponíveis: {jogador['chips']}")
            aposta = int(input(f"Escolha sua aposta {apostas_validas}: "))
            if aposta not in apostas_validas or aposta > jogador["chips"]:
                print("Aposta inválida. Será usada aposta mínima (10).")
                aposta = 10
            jogador["chips"] -= aposta
            apostas.append(aposta)

        # Distribuição inicial
        for jogador in jogadores:
            jogador["mao"] = [baralho.pop(), baralho.pop()]

        print("\n=== Cartas iniciais ===")
        for jogador in jogadores:
            print(f"\n{jogador['nome']}: {jogador['mao']} (Total: {calcular_mao(jogador['mao'])})")
        print(f"Dealer mostra: {dealer['mao'][0]}")

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

    print("\n=== Fim do jogo ===")
    for jogador in jogadores:
        print(f"{jogador['nome']} terminou com {jogador['chips']} chips.")

# Executa o jogo
blackjack_multiplayer()
