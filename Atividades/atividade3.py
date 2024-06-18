nota = float(input("Digite a nota da aluna (de 1 a 10): "))
frequencia = float(input("Digite a frenquencia da aluna (de 0 a 100): "))

if nota >= 7 and nota <=10 or frequencia >= 75:
    print("Você foi aprovada!!!")
elif nota >=1 and nota <=10 and frequencia <= 75:
    print("Não foi dessa vez, baby!")  
else:
    print("ERRO!")