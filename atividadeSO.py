import random

def fifo(lista):
    fila = []
    for i in range(10):
        fila.append(lista[i])
        print(f"Adicionou {fila[i]}")
    
    for i in range(10):
        removido = fila.pop(0)
        print(f"Removeu {removido}")

def shortestJob():
    

if __name__ == '__main__':
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 6))
    fifo(lista)
