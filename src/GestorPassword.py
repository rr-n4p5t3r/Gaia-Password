import random
import string
import json

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

def guardar_password(sitio, usuario, password, archivo):
    with open(archivo, 'r') as file:
        passwords = json.load(file)
    
    passwords[sitio] = {'usuario': usuario, 'password': password}
    
    with open(archivo, 'w') as file:
        json.dump(passwords, file, indent=4)

def obtener_password(sitio, archivo):
    with open(archivo, 'r') as file:
        passwords = json.load(file)
    
    if sitio in passwords:
        return passwords[sitio]
    else:
        return None

def mostrar_sitios(archivo):
    with open(archivo, 'r') as file:
        passwords = json.load(file)
    
    print("Sitios almacenados:")
    for sitio in passwords:
        print(sitio)

def main():
    archivo_passwords = 'passwords.json'

    while True:
        print("\nGestor de passwords")
        print("1. Generar una nueva password")
        print("2. Guardar una password")
        print("3. Obtener una password")
        print("4. Mostrar todos los sitios almacenados")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            longitud = int(input("Longitud de la password a generar: "))
            password = generar_password(longitud)
            print("password generada:", password)

        elif opcion == '2':
            sitio = input("Sitio web o servicio: ")
            usuario = input("Nombre de usuario: ")
            password = input("password: ")
            guardar_password(sitio, usuario, password, archivo_passwords)
            print("password guardada correctamente.")

        elif opcion == '3':
            sitio = input("Sitio web o servicio: ")
            datos_password = obtener_password(sitio, archivo_passwords)

            if datos_password:
                print("Usuario:", datos_password['usuario'])
                print("password:", datos_password['password'])
            else:
                print("No se encontró la password para el sitio especificado.")

        elif opcion == '4':
            mostrar_sitios(archivo_passwords)

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
