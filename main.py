import calculadora

def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

while True:
    menu()
    op = input("Escolha: ")

    if op == "0":
        print("Encerrando...")
        break

    if op not in ["1", "2"]:
        print("Opção inválida!")
        continue

    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if op == "1":
        print("Resultado:", calculadora.soma(n1, n2))
    else:
        print("Resultado:", calculadora.subtracao(n1, n2))