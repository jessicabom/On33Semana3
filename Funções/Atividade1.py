#essa é uma função (quando você define ali com o def você cria uma função) chamada "soma".
#essa função recebe 2 argumentos: "a" e "b".
#A função retorna a soma desses dois argumentos.
def soma (a, b):
    return a + b

#acima definimos a função e o que ela faz, mas não pedimos que ela retorne nada (não usamos return)
#agora o programa vai dar comandos ao usuário
entrada1 = input("Digite o primeiro número: ")
entrada2 = input("Digite o segundo número: ")

#aqui vem o bloco do try, que vai tentar executar instruções
try:
    #aqui o programa vai tentar converter as entradas do usuário para números (float ou int por exemplo)
    #se as entradas puderem ser convertidas para números, elas serão armazenadas nas variáveis "numero1" e "numero2"
    numero1 = float(entrada1)
    numero2 = float(entrada2)

    #a função "soma" vai ser chamada agora com essas variáveis (que são dois argumentos que a função precisa)
    #é na hora que eu chamo a função que eu adiciono os parâmetros
    #a função "soma" é chamada com "numero1" e "numero2" como argumentos, e o resultado é armazenado na variável resultado
    resultado = soma(numero1, numero2)

    #o resultado da soma é então impresso na tela
    print(f"A soma de {numero1} e { numero2} é: {resultado}")

#caso o usuário não tenha entrado com valores que possam ser convertidos para números float, ou seja, digitou algo inválido
#o bloco except será executado
except ValueError:
    #nesse caso daremos um aviso de erro
    print("Erro! Por favor, insira números válidos")