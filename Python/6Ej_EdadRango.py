edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30

print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print("Estas dentro del rango de los 20 años")
    elif treinta:
        print("Estas dentro del rango de los 30 años")
else:
    print("No estas dentro del rango de los 20 y 30 años")