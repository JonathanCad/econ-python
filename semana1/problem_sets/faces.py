# Problem sets 0
# Funciones y variables: Faces
# Autor: Jonathan
# Fecha: Junio 2026

# Crear una función que devuelva lo que el usuario escriba con una cara feliz o triste

def faces():
    first = input()
    first = first.replace(":)", "🙂")
    first = first.replace(":(", "🙁")
    print(first)

faces()
