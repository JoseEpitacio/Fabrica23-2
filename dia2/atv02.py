'''
2. crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)
'''

idade = input("Digite a sua idade: ")
idade_int = 0

try:
    idade_int = int(idade)
except ValueError:
    raise ValueError("Idade digitada inválida, digite novamente.")

if idade_int >= 18:
      print("Você está apto a retirar a CNH.")
else:
      print("Você ainda não pode retirar a CNH.")