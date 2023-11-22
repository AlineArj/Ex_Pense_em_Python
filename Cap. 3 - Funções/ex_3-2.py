# 1. Digite este exemplo em um script e teste-o.

# def do_twice(f):
#     f()
#     f()

# def print_spam():
#     print('Já fui campeã da liga Pokemon!!')


# do_twice(print_spam)

# 2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame a funçao duas vezes, passando o valor como um argumento.

# def do_twice(f, n):
#     f(n)
#     f(n)

# def print_spam(n):
#     print(f'Já fui campeã da liga Pokemon {n} vezes!!')


# do_twice(print_spam, 3)

# 3. Copie a definição de print_twice que aparece anteriormente nesse capítulo no seu script

# def do_twice(f, n):
#     f(n)
#     f(n)

# def print_spam(bruce):
#     print(bruce * 4)
#     print(bruce * 4)


# do_twice(print_spam, 'salsicha ')

# 4. Use a versão alterada de do_twice para chamar print_twice duas vezes passando 'spam' como argumento.

# def do_twice(n):
#     print_spam(n)
#     print_spam(n)

# def print_spam(bruce):
#     print(bruce * 4)
#     print(bruce * 4)


# do_twice('spam ')

# 5. Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo dessa função, não quatro

def do_four(f,texto):
    repeat(f, texto)
    repeat(f, texto)

def repeat(f, tex):
    f(tex)
    f(tex)
    
def print_f(t):
    print(t)


do_four(print_f, 'Espero ter entendido ;-; ')