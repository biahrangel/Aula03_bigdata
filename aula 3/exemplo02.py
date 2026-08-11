#ex2

# uma pessoa deseja comprar ingressos para um evento e possui um valor disponivel para gastar.
# solicite o preco de cada ingresso e valor disponivel. 
# calcule quantos ingressos podem ser comprados e qual sera o troco. 

preco_unitario = float (input('valor do ingresso: R$ '))
valor_disponivel = float (input('valor disponivel: R$ '))

ingressos = int (valor_disponivel // preco_unitario)
troco = int (valor_disponivel % preco_unitario)

print(f'quantidade de ingressos: {ingressos}')
print(f'troco R$: {troco}')
