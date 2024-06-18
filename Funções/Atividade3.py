# Crie uma função que converte uma temperatura de graus Celsius para Fahrenheit. 
# Use try e except para garantir que a entrada seja um número.
#Para converter para Farenheit você multiplica por 9/5 e soma 32
def conversao_celsius_farenheit(numero):
    return numero * 9/5 + 32

# Solicito ao user que entre com um valor em graus celsius
entrada = input("Digite a temperatura em graus Celsius: ")

#bloco do Try
try:
    #primeiro testa se a entrada pode ser convertida para float
    temperaturaCelsius = float(entrada)

    #agora o try traz um resultado
    resultado = conversao_celsius_farenheit(temperaturaCelsius)

    #trago um resultado ao user
    print(f"{entrada}ºC equivalem a {resultado}F")

#bloco do except
except ValueError:
    print("Erro! Por favor, insira um valor de temperatura válido")