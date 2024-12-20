# Clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada para manejar la lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Simulación del algoritmo de Grover para buscar un elemento
def simulacion_grover(lista, criterio):
    # Convertir la lista enlazada a una lista normal
    elementos = []
    actual = lista.cabeza
    while actual:
        elementos.append(actual.valor)
        actual = actual.siguiente

    print("Elementos en la lista:", elementos)

    # Verificar qué elementos cumplen el criterio
    cumple_criterio = [x for x in elementos if criterio(x)]
    if not cumple_criterio:
        return -1  # Si no hay elementos que cumplan el criterio

    # Seleccionar el primer elemento que cumple el criterio
    return cumple_criterio[0]

# Criterio: Buscar múltiplos de 5 mayores a 30
def criterio(valor):
    return valor % 5 == 0 and valor > 30

# Crear lista enlazada con algunos valores
lista = ListaEnlazada()
valores = [12, 35, 40, 25, 18, 50, 60]
for valor in valores:
    lista.agregar(valor)

print("Lista enlazada:")
lista.mostrar()

# Aplicar el algoritmo de Grover
resultado = simulacion_grover(lista, criterio)
if resultado != -1:
    print(f"El elemento encontrado que cumple el criterio es: {resultado}")
else:
    print("No se encontró ningún elemento que cumpla el criterio.")
