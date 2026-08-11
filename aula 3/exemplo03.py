#ex03

# uma loja oferece 10% de desconto sobre o valor total da compra.
# solicite o preco do produto e a quantidade comprada
# calculo o valor total, aplique o desconto e informe o valor total 

# entrada 

preco_produto = float (input('preco do produto: '))
quantidade_produto = int (input('quantidade de produto: '))

#processamento 

total = preco_produto * quantidade_produto
desconto = total * 0.1
total_desconto = total - desconto

#saida

print (f'valor total sem desconto: R$ {total:.2f}')
print(f'total do produto com desconto: R$ {total_desconto:.2f}')
print(f'desconto de: R$ {desconto:.2f} ')
