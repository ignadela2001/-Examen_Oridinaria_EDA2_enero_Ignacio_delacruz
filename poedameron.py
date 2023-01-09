import heapq
frecuencias = {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05, 'M': 0.09, 'T': 0.15}
mont = []
for tab, frecuencia in frecuencias.items():
    heapq.heappush(mont, (frecuencia, tab))
while len(mont) > 1:
    frecuencia1, tab1 = heapq.heappop(mont)
    frecuencia2, tab2 = heapq.heappop(mont)
    heapq.heappush(mont, (frecuencia1 + frecuencia2, (tab1, tab2)))
print(heapq.heappop(mont))