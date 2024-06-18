# Atividade 1: Verificação de Idade para Votação
# Objetivo: Verificar se a idade do usuário permite que ele vote.

# Passos:

# Solicite ao usuário que insira sua idade.
# Use uma função para verificar se a idade do usuário é 16 ou mais.
# Use try e except para tratar entradas inválidas.
# Exiba uma mensagem indicando se o usuário pode votar ou não.

def idade_usuario(numero):
    if numero >= 16:
        return "Você já pode votar"
    else:
        return "Você ainda não pode votar"

entrada = input("Digite sua idade em número inteiros: ")

try:
    idade = int(entrada)
    resultado = idade_usuario(idade)
    print(f"{resultado}")

except:
    print("Por favor, digite uma idade válida em números inteiros")