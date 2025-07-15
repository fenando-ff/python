while True:
    X = float(input("Digite o valor da coordenada X: "))
    Y = float(input("Digite o valor da coordenada Y: "))


    if X == 0 or Y == 0: 
        break

    if X > 0 and Y > 0:
        print("COORDENADAS PERTENCEM AO QUADRANTE Q1")
    elif X < 0 and Y > 0:
        print("COORDENADAS PERTENCEM AO QUADRANTE Q2")
    elif X < 0 and Y < 0:
        print("COORDENADAS PERTENCEM AO QUADRANTE Q3")
    else:
        print("COORDENADAS PERTENCEM AO QUADRANTE Q4")

