# uma empresa concedera o reajuste salarial de 18% aos seus funcionarios. 
# solicite o salario atual de um funcionario e calcule o valor do reajuste e o novo salario 
# apresente o salario inicial, o valor do reajuste e o salario reajustado

salario_atual = float (input('salario atual R$: '))
reajuste = salario_atual * 0.18
salario_final = reajuste + salario_atual

print(f'qual o salario atual: {salario_atual} ')
print(f'valor do reajuste: {reajuste} ')
print(f'salario final: {salario_final}')