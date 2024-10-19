inicio= int(input("introduce el inicio del rango:"))
hasta = int(input("introduce el finaldel rango:"))
print(f"los numeros impares entre {inicio} y {hasta} son:")
for i in range (inicio,hasta,2):
    if i % 2!=0: 
        print(i, end=" ")
print("\nhasta aqui!!")