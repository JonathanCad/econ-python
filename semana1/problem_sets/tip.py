# Problem sets 0
# Funciones y variables: Tip
# Autor: Jonathan
# Fecha: Junio 2026

# Crear una función que calcule la propina de una comida.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):    
    return float(d.lstrip('$'))


def percent_to_float(p):
    return float(p.rstrip('%')) / 100


main()

