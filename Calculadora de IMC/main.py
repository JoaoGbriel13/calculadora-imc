#Inputs e usando o metodo try/catch para evitar respostas incorretas e qualquer bug no codigo
try:
    altura = float(input('Insira sua altura atual(Lembre-se de utilizar ponto ao invés da virgula): '))
    peso = float(input('Insira o seu peso atual: '))
except:
    altura = -1
    peso = -1
    if altura or peso < 0 :
        print('Você deve inserir valores validos!')

#Calculo do IMC

imc = round(peso / (altura * altura), 2)
print(f'O seu imc é de {imc}')


#possibilidades

if imc <= 17.0:
  print('Muito abaixo do peso ideal')
elif imc > 17.01 and imc <= 18.49:
  print('Abaixo do peso ideal')
elif imc >= 18.50 and imc <= 24.99 :
  print('Peso normal')
elif imc >= 25.00 and imc <= 29.99 :
  print('Um pouco acima do peso')
elif imc >= 30.00 and imc <= 34.99 :
    print('Obesidade nivel 1')
elif imc >= 35.00 and imc <= 39.99 :
    print('Obesidade nivel 2')
else:
  print('Obsedidade nivel 3(Morbida)')
    


