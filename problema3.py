#Hallar la suma de los primeros números naturales Formula: s = n(n+1)/2, donde n es la cantidad de números naturales


n: int
s: int
# entrada
n=int(input("Ingrese número de términos: "))
# proceso
s=n*(n+1)/2
# salida
print(f'La suma de los {n} primeros términos es: {s}')
