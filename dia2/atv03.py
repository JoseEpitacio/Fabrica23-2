'''
3. Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. mostre que ele foi multado. a multa é de 7R$ por cada km acima do limite
'''

limite_velocidade = 80
velocidade = input("Digite a velocidade do carro: ")
velocidade_int = 0
multa = 0.0

try: 
    velocidade_int = int(velocidade)
except ValueError:
    raise ValueError("Velocidade inválida! Digite novamente.")

if velocidade_int > limite_velocidade:
    multa = (velocidade_int - limite_velocidade) * 7.0
    print(f"O carro passou a uma velocidade de {velocidade_int}, num radar de {limite_velocidade} KM/H. Por isso foi aplicada uma multa de R${multa}")
else:
    print(f"O carro não excedeu o limite de 80 KM/H ({velocidade_int} KM/H)")