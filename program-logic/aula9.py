num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# numeros e positivos (12)

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('nao')

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print('ERROR')