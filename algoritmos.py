import random

def fifo(lista):
    print("FIFO:")
    fila = []
    for i in range(10):
        fila.append(lista[i])
        print(f"Executando {fila[i]}")
    
    for i in range(10):
        removido = fila.pop(0)
        print(f"Removendo {removido}")


def shortestJob(lista):
    print("Shortest Job First:")
    fila = lista[:]
    fila.sort()

    for i in range(10):
        print(f"Executando {fila[i]}")
    
    for i in range(10):
        removido = fila.pop(0)
        print(f"Removendo {removido}")

#def roundRoubin(lista):
    

if __name__ == '__main__':
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 6))
    
    #fifo(lista)
    shortestJob(lista)