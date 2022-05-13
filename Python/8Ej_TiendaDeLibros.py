nombre = str(input("Introduce el nombre del libro: "))
id = int(input("Introduce el id del libro: "))
precio = float(input("Introduce el precio del libro: "))
envioGratis = str(input("Indicar ¿El envio es gratuito? (S/N): "))

def esGratis(envioGratis):
    envioGratis = envioGratis.upper()

    if envioGratis == "S":
        return "Si"
    elif envioGratis == "N":
        return "No"

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print(f"\nEl nombre del libro es: {nombre}"
      f"\nEl id del libro es: {id}"
      f"\nEl precio del libro es: {precio}"
      f"\nEl envio es gratis?", esGratis(envioGratis))
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")