#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e motre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40:
#obesidade mórbida
#imc = peso / pela altura²

peso = float(input('Qual seu peso Kg: '))
altura = float(input('Qual sua altura em m: '))
imc = peso / (altura **2)
print('Seu \033[1:34mIMC é {:.1f}\033[m . '.format(imc))
if imc <= 18.5:
    print('Você está \033[1:31mAbaixo do Peso\033[m')
elif 18.5 <= imc < 25:
    print('Você está no \033[1:32mPeso ideal\033[m')
elif imc <= 30:
    print('Você está em \033[1:31mSobrepeso\033[m. ')
elif imc <= 40:
    print('Você está com \033[1:36mObesidade !\033[m .')
else:
    print('Você está com \033[1:37mObesidade Morbida !\033[m')
#fim
