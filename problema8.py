#Calcule el volumen de un cilindro recto conociendo su radio y su altura.


from math import pi
r: float
h: float
VolCilindro: float

# entrada
r=float(input("Ingrese el radio del cilindro: "))
h=float(input("Ingrese altura del cilibdro: "))

# proceso
VolCilindro = 3.14**r**r**h

# salida
print(f'El volumen es: {VolCilindro}')
