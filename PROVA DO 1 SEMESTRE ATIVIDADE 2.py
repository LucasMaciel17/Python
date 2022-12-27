entrada_1 = input()
entrada_2 = input()

if entrada_1 == "vertebrado":
    if entrada_2 == "ave":
        print("e uma ave")
    elif entrada_2 == "mamifero":
        print("e uma mamifero")
    else:
        print("vertebrado desconhecido")
elif entrada_1 == " invertebrado":
    if entrada_2 == "inseto":
        print("e um inseto")
    elif entrada_2 == "anelideo":
        print("e um anelideo")
    else:
        print("invertebrado desconhecido")
else:
    print("animal desconhecido")
