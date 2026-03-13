# Programa para restar los HP del jugador en cada turno del Jefe

# -----------------
# libraries
# -----------------
import random

# -----------------
# input
# -----------------
hp= 50

# -----------------
# processing & storage
# -----------------
while True:
    dmg= random.randint(1,20)
    hp= hp-dmg

    print("El Jefe te ataco y te quito " +str(dmg) +" de vida")
    print("Ahora tienes " +str(hp) +" de vida restante")

# -----------------
# output
# -----------------

    if(hp<=0):
        print("G4M3_0V3R")
        break