# Escreva uma função que desenhe uma grade como a seguinte:
#           + - - - - + - - - - +
#           |         |         |
#           |         |         |
#           |         |         |
#           |         |         |
#           + - - - - + - - - - +
#           |         |         |
#           |         |         |
#           |         |         |
#           |         |         |
#           + - - - - + - - - - +
  
def linhas(col):
    print(f"+", end="")
    print(f"{' - ' * 4}+" * col)

def colunas(col):
    print(f"|", end="")
    print(f"{' ' * 12}|" * col)

    print(f"|", end="")
    print(f"{' ' * 12}|" * col)

    print(f"|", end="")
    print(f"{' ' * 12}|" * col)

    print(f"|", end="")
    print(f"{' ' * 12}|" * col)

# Nota do livro: Este exercício deve ser feito usando-se apenas instruções e outros recursos que aprendemos até agora. 

def grade(col):
    linhas(col)
    colunas(col)
    linhas(col)
    colunas(col)
    linhas(col)


grade(2)