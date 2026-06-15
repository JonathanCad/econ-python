# Problem sets 1
# Funciones y variables: Bank
# Autor: Jonathan
# Fecha: Junio 2026

# Si el usuario responde Hello, el programa devuelve 0 usd. Si responde algo que empieza con H, el programa devuelve 20 usd. De lo contrario, el programa devuelve 100 usd.

def main():
    greeting = input("Greeting: ").lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()