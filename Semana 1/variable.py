nombre = "David"
precio = 25
print(nombre)

numeros = [1,2,3,4]

for items in numeros:
    print(items)

for i in range(10):
    print("I:", i )

    contador = 1

    while contador < 20:
        print("valor", contador)
        contador += 1

password = ""

while password != "123":
    print("Ingrese en el while")
    pasword = input("ingrese su password: ")


if password == "123":
    print("Sistema de inicio")