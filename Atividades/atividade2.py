notaDaAluna = float(input("Insira a nota da Aluna (de 1 a 10): "))
frequenciaDaAluna = float(input("Insira a frequência da Aluna (de 0 a 100): "))

if notaDaAluna >= 7 and frequenciaDaAluna >= 75:
    print("A aluna está aprovada")
elif notaDaAluna >= 7 and frequenciaDaAluna < 75:
    print("A aluna está reprovada por faltas")
elif notaDaAluna <7 and frequenciaDaAluna >= 75:
    print("A aluna está reprovada por nota")
else:
    print("A aluna reprovou por nota e por faltas")