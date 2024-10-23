import time
import math

# Variables para el promedio
datos = 0
acum = 0
c = 1
prom = 0

# Variables para los datos máximos y mínimos
max_num = float(math.inf)
min_num = float(-(math.inf))

# Entradas de los intervalos de tiempo y número de datos a entrar
tiempo = int(input("Ingrese segundos para el intervalo de tiempo en la recoleccion de datos: "))
n = int(input("Ingrese el número de datos: "))

while (c <= n):
    datos = int(input(f"Ingrese dato #{c}: "))
    c += 1
    for i in range(tiempo):
            time.sleep(1)

    # Promedio de los datos
    acum += datos 
    prom = acum / n

    if datos < max_num:
        max_num = datos

    elif datos > min_num:
        min_num = datos

print("Su promedio es:",prom)
print("La humedad mínima registrada es:", max_num)
print("La humedad máxima registrada es:", min_num)
```
