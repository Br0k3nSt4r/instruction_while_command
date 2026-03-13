# Programa para confirmar si la contraseña ingresada es la correcta

# -----------------
# input
# -----------------
password=input("Digita la Contraseña: ")

# -----------------
# processing & storage
# -----------------
correct_password="python123"

while(password != correct_password):
    print("ERROR!: Contraseña INCORRECTA")
    password=input("Vuelve a digitar la Contraseña: ")

# -----------------
# output
# -----------------
    if(password == correct_password):
        print("ACCESO CONCEDIDO")