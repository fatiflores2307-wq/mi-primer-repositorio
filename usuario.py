#Datos personales del usuario
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
mail = input("Ingrese su correo: ")
nacimiento = input("Ingrese su año de nacimiento: ")
sexo = input("Ingrese su sexo: ")
nacimiento = int(nacimiento) 
phone= input("Ingrese su numero de telefono: ")
phone = str(phone)
#convertir año de nacimiemto a entero 
nacimiento = int(nacimiento)

#calcular edad
edad = 2026 - nacimiento

print(f"Tu edad es: {edad}")
print(f"Nombre: {name}")
print(f"Apellido: {lastname}")
print(f"Correo: {mail}")
print(f"Año de nacimiento: {nacimiento}")
print(f"Sexo: {sexo}")
print(f"Telefono: {phone}")
