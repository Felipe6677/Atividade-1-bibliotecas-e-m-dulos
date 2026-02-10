import random

def gerar_jogo():
    return sorted(random.sample(range(1, 61), 6))

while True:
    print("\n=== MEGA-SENA ===")
    print("1 - Gerar jogo")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "0":
        print("Encerrando...")
        break
    elif op == "1":
        jogo = gerar_jogo()
        print("Números sorteados:", jogo)
    else:
        print("Opção inválida!")