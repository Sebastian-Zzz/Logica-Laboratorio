inicio = int(input("introduce el inicio del rango: "))
hasta = int(input("introduce el final del rango: "))
print(f"Los números pares entre {inicio} y {hasta} son: ")
for i in range (inicio, hasta, 1):
    if i % 2 == 0 :
        print(i, end=" ")
print("\nHasta aquí!!")