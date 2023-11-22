# Código genérico dos exercícios 3.3.1 e 3.3.2

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

def grade(lin, col):
    linhas(col)
    for i in range(lin):
        colunas(col)
        linhas(col)


grade(6,1)