# Problem sets 0
# Funciones y variables: Einstein
# Autor: Jonathan
# Fecha: Junio 2026

# Crear una función que devuelva la masa de un objeto en joulios, dado su masa en kilogramos


def einstein():
    mass = float(input("m: "))
    energy = mass * (3 * 10**8)**2
    print(f"E: {energy:.0f}")

einstein()

