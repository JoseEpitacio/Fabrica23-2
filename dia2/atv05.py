'''
5. Crie um programa de 0 a 30, mas pare quando encontrar o 20
'''

count = 0

while count <= 30:
    count += 1
    if count == 20:
        print('chegou no 20')
        break
    print(count)