# Problem sets 1
# Funciones y variables: Deep
# Autor: Jonathan
# Fecha: Junio 2026

# Si el usuario responde 42, la respuesta a la pregunta fundamental de la vida, el universo y todo lo demás, entonces el programa debe imprimir "Yes". De lo contrario, debe imprimir "No".

def main():
    answer = input("What's the answer to the Ultimate Question of Life, The Universe, and Everything? ")
    if answer in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()
