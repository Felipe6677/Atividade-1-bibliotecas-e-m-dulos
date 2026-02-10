import random
def jogar():
    opcoes=["pedra","papel","tesoura"]
    while True:
        print("===JO KEN PO===")
        print("1-Pedra")
        print("2-Papel")
        print("3-Tesoura")
        print("0-Sair")
        escolha=input("Escolha:")
        if escolha=="0":
            print("Saindo...")
            break
        if escolha not in ["1","2","3"]:
            print("Opção inválida!")
            continue
        usuario=opcoes[int(escolha)-1]
        computador=random.choice(opcoes)
        print("Você:",usuario)
        print("Computador:",computador)
        if usuario==computador:
            print("Empate!")
        elif (usuario=="pedra" and computador=="tesoura") or (usuario=="papel" and computador=="pedra") or (usuario=="tesoura" and computador=="papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")
            
            jogar()