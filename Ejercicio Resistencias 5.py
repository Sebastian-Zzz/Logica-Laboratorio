resistencia1 = float(input("ingrese un valor de resistencia: "))
resistencia2 = float(input("ingrese un valor de resistencia: "))
resistencia3 = float(input("ingrese un valor de resistencia: "))
caso = int(input("ingrese un numero de caso del 1 al 5: "))

while caso<1 or caso>5:
    caso = int(input("ingrese un valor de caso valido del 1 al 5: "))

if caso == 1:
    variable = resistencia1+resistencia2+resistencia3
    aumento = variable*0.05 
    variable= variable + aumento
    limite_superior= int(input("ingrese limite mayor"))
    
elif caso==2:
    variable = 1/((1/resistencia1)+(1/resistencia2)+(1/resistencia3))
    aumento = variable*0.1
    variable= variable - aumento
    limite_inferior= int(input("limite menor"))
elif caso==3: 
    variable = 1/((1/resistencia1+resistencia2)+(1/resistencia3))

elif caso==4:
    variable = 1/((1/resistencia1+resistencia3)+(1/resistencia2))

elif caso==5:
    variable = 1/((1/resistencia2+resistencia3)+(1/resistencia1))
RT = variable

if RT and caso==1> limite_superior:
    print("Advertencia")
    RT= 0.05*RT
    RT= RT+20

if RT and caso==2 <limite_inferior:
    print("advertencia")
    RT=0.1*RT
    RT=RT-2

print (f"la resistencia total del circuito en caso: {caso} es {RT}")
