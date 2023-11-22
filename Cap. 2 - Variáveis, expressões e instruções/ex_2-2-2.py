# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

preco_livro = 24.95
desconto = 0.4
copias = 60

# Considerei que + de 10 cópias vendidas é considerado atacado.
if copias > 10:
    total_livros = preco_livro * (1 - desconto) * copias
    total_frete = 3 + (copias - 1) * 0.75
else:
    total_livros = preco_livro * copias
    total_frete = 3 + (copias - 1) * 0.75

print(f"Total: R$ {total_livros+total_frete:.2f}")