# Exercícios do Módulo 1 - Operações, Variáveis e Input

# Parte 1 - Operações e Variáveis

# Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano. Obs: faça tudo usando variáveis.

# Valores do último ano:

# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00

qtd_coca = 150
qtd_pepsi = 130

coca_unit = 1.50
pepsi_unit = 1.50

custo_loja = 2500
loja = 'Faturamento Hashtag&Drink'

print('='*50)
print('{:=^50}'.format(loja))
print('='*50)

print('')

# Se quiser continuar tudo na mesma linha (Não quebrar a linha de um print para o outro)
# print('Quantidade de vendas de Coca-Cola: {} unidades.'.format(qtd_coca), end = '')

# Se quiser quebrar linha
# print('Quantidade de vendas \n de Coca-Cola: {} unidades.'.format(qtd_coca))


print('Quantidade de vendas de Coca-Cola: {} unidades.'.format(qtd_coca))
print('Quantidade de vendas de Pepsi: {} unidades.'.format(qtd_pepsi))
print('Preço unitário da Coca-Cola: R$ {:.2f}'.format(coca_unit))
print('Preço unitário da Pepsi: R$ {:.2f}'.format(pepsi_unit))
print('Custo da loja: R$ {:.2f}'.format(custo_loja))

# Qual foi o faturamento de Pepsi da Loja?
fat_pepsi = pepsi_unit * qtd_pepsi
print('O faturamento de Pespi foi de R$ {:.2f}'.format(fat_pepsi))

# Qual foi o faturamento de Coca da Loja?
fat_coca = coca_unit * qtd_coca
print('O faturamento de Coca-Cola foi de R$ {:.2f}'.format(fat_coca))

# Qual foi o Lucro da loja?
lucro = (fat_pepsi + fat_coca) - custo_loja
print('O lucro da loja foi de R$ {:.2f}'.format(lucro))

# Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual
margem = lucro / (fat_coca + fat_pepsi)
print('A margem da loja foi de {}'.format(margem))
