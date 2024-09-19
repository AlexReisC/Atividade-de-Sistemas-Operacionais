import random

numeroDeProcessos = 10

def fifo(lista):
    print("FIFO:")
    fila = []
    for i in range(numeroDeProcessos):
        fila.append(lista[i])
        print(f"Executando {fila[i]}")
    
    for i in range(numeroDeProcessos):
        fila.pop(0)


def shortestJob(lista):
    print("Shortest Job First:")
    fila = lista[:]
    fila.sort()

    for i in range(numeroDeProcessos):
        print(f"Executando {fila[i]}")
    
    for i in range(numeroDeProcessos):
        fila.pop(0)

def roundRoubin(lista):
    print("Round Roubin:")
    fila = []
    for i in range(numeroDeProcessos):
        fila.append(lista[i])
        timeSlice = random.randint(1,3)
        if(timeSlice > 2):
            print(f"Execucao de {fila[i]} interrompida. Tempo esgotado!")
        else:
            print(f"Executando {fila[i]}")

        for i in range(numeroDeProcessos):
            fila.pop(0)        

""" A implementacao do escalonador com prioridades ocorre com multiplas filas 
e cada uma pode ter sua politica de escalonamento """
def prioridades(lista):
    print("Prioridades")
    fila1 = []
    fila2 = lista[:5]
    fila2.sort()

    print("Fila 1")
    for i in range(numeroDeProcessos//2):
        fila1.append(lista[i])
        print(f"Executando {fila1[i]} numa prioridade de FIFO")
    
    print("Fila 2")
    for i in range(numeroDeProcessos//2):
        print(f"Executando {fila2[i]} numa prioridade de SJF")

    for i in range(numeroDeProcessos//2):
        fila1.pop(0)
        fila2.pop(0)


if __name__ == '__main__':
    lista = []
    for i in range(numeroDeProcessos):
        lista.append(random.randint(1, 7))
    
    #fifo(lista)
    #shortestJob(lista)
    #roundRoubin(lista)
    prioridades(lista)