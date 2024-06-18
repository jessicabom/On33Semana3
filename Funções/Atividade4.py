# Crie uma função que conta o número de caracteres em uma string fornecida pelo usuário. 
# Use try e except para garantir que a entrada seja uma string.

def contar_caracteres(texto):
    return len(texto)

entrada = input("Digite uma frase ou um texto: ")

try:
#nesse caso eu não preciso fazer um teste para ver se é um texto tipo converter em float ou int
# posso ir direto para o que era o "resultado" nas funções anteriores e já chamar a função    
    resultado = contar_caracteres(entrada)
    print(f"A entrada {entrada} possui {resultado} caractéres")

except TypeError:
    print("Erro! Por favor, digite uma entrada de texto válida")