# Programa para confirmar si la contraseña ingresada es la correcta

# -----------------
# input
# -----------------
c1=int(input("Digita la Capital de Pedro: "))
c2=int(input("Digita la Capital de Juan: "))
c3=int(input("Digita la Capital necesaria para el Negocio: "))

# -----------------
# processing & storage
# -----------------
meses=0

while(c1 + c2) < c3:
    c1= c1+0.03*c1
    c2= c2+0.04*c2
    meses + 1

# -----------------
# output
# -----------------
    print("Podran hacer el Negocio en", meses, "meses")
    print("La Capital total de Pedro es: ", round(c1,2))
    print("La Capital total de Juan es: ", round(c2,2))
    print("La Capital total de Ambos es: ", round(c1+c2,2))