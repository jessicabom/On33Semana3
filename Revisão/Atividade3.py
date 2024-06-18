# Atividade 3: Conversor de Medidas
# Objetivo: Criar um programa que converte diferentes 
# unidades de medida (metros para quilômetros, gramas para quilogramas, etc.).

# Passos:

# Solicite ao usuário que insira um valor e escolha uma unidade de medida.
# Verifique se a unidade de medida é válida.
# Use funções para realizar a conversão.
# Exiba o resultado da conversão.
# A função 'metros_para_kilometros' é definida. Ela recebe um argumento chamado 'metros'.
# A função retorna a conversão de metros para quilômetros.

def converte_metros_para_km (valor):
    return valor / 1000

def converte_gramas_para_kg (valor):
    return valor / 1000

def conversao (valor, unidade):
    if unidade == "metros":
        return converte_metros_para_km(valor)
    elif unidade == "gramas":
        return converte_gramas_para_kg(valor)
    else:
        return "Unidade inválida"
    

try:
    valor_digitado = float(input("Digite o valor a ser convertido: "))
    unidade = input("Digite a unidade: metros ou gramas: ")
    resultado = conversao(valor_digitado, unidade)
    print(f"O resultado da conversão é: {resultado}")

except:
    print("Por favor, siga corretamente as instruções do programa e digite valores válidos")
