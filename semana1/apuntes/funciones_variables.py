# Clase del 4 de junio de 2026
# Funciones y variables
# Autor: Jonathan
# Fecha: Junio 2026

# Calculator
x = float(input ("What's x? "))
y = float(input ("What's y? "))

z = round(x + y, 0)

print (z)

# Format number with commas
print (f"{z:,}")

# Vamos a crear una función
def main ():
    name = input ("What's your name? ")
    hello(name)    

def hello(to="world"):
    print (f"hello, {to}")

main()

# Ahora un ejemplo con números
def main ():
    x = int(input ("What's x? "))
    print ("x squared is ", square(x))

def square(n):
    return n * n

main()