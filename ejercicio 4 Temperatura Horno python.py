import random

TemperaturaElegida = int(input("Ingrese la temperatura deseada para el horno: "))
Tmax = TemperaturaElegida + (TemperaturaElegida*(10/100))
Tmin = TemperaturaElegida - (TemperaturaElegida*(10/100))
TemperaturaActual = random.randint(1,300)
print(f"La temperatura actual del horno es {TemperaturaActual}")

for i in range(1,TemperaturaElegida,1): #usar un bucle while
    Potencia = 0.1*(TemperaturaElegida-TemperaturaActual)
    print(f"La potencia de calentamiento es {Potencia}")
    TemperaturaActual += Potencia
    print(f"La temperatura actual es: {TemperaturaActual}")
