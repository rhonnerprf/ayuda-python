i = 0
sum = 0
xi = int(input("Ingrese un número entero o 0 para terminar: "))
while xi != 0:
    sum = sum + xi
    i = i + 1
    xi = int(input("Ingrese un número entero o 0 para terminar: "))
media = sum/i
print("media =", media)
