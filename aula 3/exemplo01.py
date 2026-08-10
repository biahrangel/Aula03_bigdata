# github
print('Github - Aula 03')

# um veiculo percorre 10 km com cada litro de combustivel. 
# considere duas distancias percorridas e calcule a quantidade de combustivel necessaria para realizar o percurso total. 
# apresente a distancia total e o combustivel necessario 

#exemplo01
# entrada

consumo = 10
distancia1 = float (input ('informe a distancia: '))
distancia2 = float (input('Informe a outra distancia: '))

#processamento
distancia_total = distancia1 + distancia2 
combustivel = distancia_total / consumo 

# saida

print(f'distancia total: {distancia_total}' )
print(f'consumo do combustivel: {combustivel} litros')




