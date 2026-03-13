#-------
# libraries
#-------
import random

#-------
# input
#-------
print("La computadora ha generado un número entre 1 y 100")
computer_number = random.randint(1,100)
user_number = 0

#-----------
# processing & storage
#-----------
while(user_number!=computer_number):
    user_number=int(input("¿Qué número será?: "))

    if(user_number<computer_number):
        print("El Numero a adivinar era mas grande")
    elif(user_number>computer_number):
        print("El Numero a adivinar era mas pequeño")

#-----------
# output
#-----------
print("C0NGR4TULA4T10NS!! Adivinaste el NUMERO")