# Criar uma função que verifica de um número é par ou ímpar
# Usar o try e except para garantir que a entrada seja um número

def verifica_par_impar(numero):
    if numero % 2 == 0:
        return "o número digitado é par"
    else:
        return "o número digitado é ímpar"

# Solicitar  um número ao usuário
entrada = input("Digite um número inteiro: ")

# Bloco do Try para verificação
try:
    #aqui dentro do try eu converto a entrada do usuário para inteiro (é a validação)
    numero = int(entrada)

    #aqui ainda dentro do try eu chamo a função e atribuo a ela que o parâmetro será número
    #é agora que eu valido se é par (if) ou ímpar (else)
    #necessário observar que só aqui eu criei a variável, no bloco da função eu só falo que é um parâmetro
    resultado = verifica_par_impar(numero)

    #aqui ainda dentro do try, agora eu apresento algo ao usuário chamando o número que ele digitou
    # e o resultado do if or else que eu testei logo acima na variável resultado
    print(f"O número {numero} é {resultado}")

#agora eu venho para o else, caso a conversão da entrada do user para int tenha falhado

except ValueError:
    print("Erro! Por favor, insira um número inteiro válido")