# Programa para saber el numero de veces que rebotara una pelota dependiendo de la altura

# -----------------
# library
# -----------------
import math

# -----------------
# input
# -----------------
h=int(input("Digita la Altura a la que se lanzara la Pelota: "))
q= h/5

# -----------------
# processing & storage
# -----------------
bounce=0

while(h > q):
    bounce += 1
    h= h*0.5
    if(h < q):
        print("N° de veces que reboto la pelota ANTES de llegar a la 5ta parte de la altura inicial: ", bounce)

# -----------------
# output
# -----------------
        print("Awebo :3!! La pelota reboto varias veces >w<!!")