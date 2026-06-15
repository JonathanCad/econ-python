# Clase del 12 de junio de 2026
# Condicionales
# Autor: Jonathan
# Fecha: Junio 2026

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# Ejemplo de condicional 2

if x != y:
    print("x is not equal to y")
else:    
    print("x is equal to y")

# Ejemplo de condicional 3

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")   
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Ejemplo de condicional 4

x = int(input("What's x? "))

if x % 2 == 0:
    print("x is even")  
else:    print("x is odd")  

# Ahora vamos a crear una función que determine si un número es par o impar

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")  
    else:    
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False    
    
main()

# Ejemplo de condicional 5: utilizando 'case'

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print(f"Hello, {name}!")
