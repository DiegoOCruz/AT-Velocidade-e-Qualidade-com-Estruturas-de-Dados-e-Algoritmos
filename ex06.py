import random
import time

lista = []
for i in range(1, 10_001):
    lista.append(round(random.uniform(0.1, 999.9), 2))

 
def ordenar(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

begin_time = time.time()
ordenar(lista[:1000].copy())
print(f"Tempo de execução: {time.time() - begin_time:.2f} segundos")


print("\n")
print("----------------------------------------------------------------")
print("\n")

begin_time = time.time()
ordenar(lista.copy())
print(f"Tempo de execução: {time.time() - begin_time:.2f} segundos")
