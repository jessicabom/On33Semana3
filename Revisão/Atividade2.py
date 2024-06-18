# Atividade 2: Cálculo de Média com Verificação de Aprovação
# Objetivo: Calcular a média de três notas e verificar se o aluno foi aprovado.

# Passos:

# Solicite ao usuário que insira três notas.
# Use uma função para calcular a média das notas.
# Use uma função para verificar se a média é suficiente para aprovação (média >= 7).
# Use try e except para tratar entradas inválidas.
# Exiba a média e se o aluno foi aprovado ou não.

# A função 'calcular_media' é definida. Ela recebe três argumentos: 'nota1', 'nota2' e 'nota3'.
# A função retorna a média dessas três notas.

def calcular_media (a, b, c):
    return (a + b + c) / 3

def verificar_aprovacao (valor):
    if valor >= 7:
        return ("O aluno está aprovado!")
    
    else:
        return ("O aluno reprovou")
    
 # O programa pede ao usuário para digitar três notas.   
entrada1 = input("Digite a primeira nota: ")
entrada2 = input("Digite a segunda nota: ")
entrada3 = input("Digite a terceira nota: ")

#As notas são convertidas para números (floats) e armazenadas nas variáveis 'nota1', 'nota2' e 'nota3'.
try:
    nota1 = float(entrada1)
    nota2 = float(entrada2)
    nota3 = float(entrada3)

    #A função 'calcular_media' é chamada com 'nota1', 'nota2' e 'nota3' como argumentos
    # O resultado é armazenado na variável 'media'.
    media = calcular_media(nota1, nota2, nota3)

    #A função 'verificar_aprovacao' é chamada com 'media' como argumento.
    # É aqui que vai ser realizada a verificacao se a média foi o suficiente ou não.
    status = verificar_aprovacao(media)

    # O programa precisa exibir a média do aluno e se ele foi aprovado ou não.
    # Para isso, nós vamos pegar o lugar que onde as funções foram aplicadas, que é a var "media"
    # e a que traz o resultado com base nessa media que é a var "status"
    print(f"A média do aluno é {media}. {status}")

except:
    print("Por favor, digite valores válidos para a média")