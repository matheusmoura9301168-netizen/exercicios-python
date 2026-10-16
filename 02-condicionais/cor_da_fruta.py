# Diz a cor de uma fruta com match-case.

def cor_do_fruto():
    fruto = input("Digite o nome de uma fruta: ").lower()

    match fruto:
        case "banana":
            print("A cor da banana é amarela.")
        case "maçã":
            print("A cor da maçã é vermelha ou verde.")
        case "laranja":
            print("A cor da laranja é laranja.")
        case "uva":
            print("A cor da uva é roxa ou verde.")
        case "mamão":
            print("A cor do mamão é alaranjada.")
        case "melancia":
            print("A cor da melancia é verde por fora e vermelha por dentro.")
        case "abacaxi":
            print("A cor do abacaxi é amarela por dentro e marrom/verde por fora.")
        case "manga":
            print("A cor da manga é amarela ou alaranjada.")
        case "coco":
            print("A cor do coco é marrom por fora e branca por dentro.")
        case "limão":
            print("A cor do limão é verde ou amarela.")
        case "goiaba":
            print("A cor da goiaba é verde por fora e rosa ou branca por dentro.")
        case "acerola":
            print("A cor da acerola é vermelha.")
        case "jabuticaba":
            print("A cor da jabuticaba é roxa bem escura.")
        case "pitanga":
            print("A cor da pitanga é vermelha ou alaranjada.")
        case "caju":
            print("A cor do caju é amarela ou vermelha.")
        case "maracujá":
            print("A cor do maracujá é amarela ou roxo por fora e amarela por dentro.")
        case "pera":
            print("A cor da pera é verde ou amarela.")
        case "figo":
            print("A cor do figo é roxa por fora e rosada por dentro.")
        case "kiwi":
            print("A cor do kiwi é marrom por fora e verde por dentro.")
        case "tangerina":
            print("A cor da tangerina é laranja.")
        case "jaca":
            print("A cor da jaca é verde e amarelo por dentro.")
        case "carambola":
            print("A cor da carambola é amarelo.")
        case "cereja":
            print("A cor da cereja é vermelho.")
        case "morango":
            print("A cor do morango é vermelho.")
        case "cacau":
            print("A cor do cacau é marrom por fora e branco por dentro.")
        case "caqui":
            print("A cor do caqui é laranja ou vermelho.")
        case "açai":
            print("A cor do açai é roxo.")
        case "jamelão":
            print("A cor do jamelão é roxo.")
        case "romã":
            print("A cor da romã é vermelho.")
        case "tamarindo":
            print("A cor do tamarindo é marrom.")
        case _:
            print("Fruto não encontrado na lista.")

cor_do_fruto()
