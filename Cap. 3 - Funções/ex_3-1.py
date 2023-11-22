# Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a útila letra da string esteja na coluna 70 da tela:

def right_justify(s):
    num_espaços = 70 - len(s)
    print(f"{' ' * num_espaços}{s}")


right_justify("Aline")
right_justify("Pikachu")
right_justify("I'm jealous of the way you're happy without me")