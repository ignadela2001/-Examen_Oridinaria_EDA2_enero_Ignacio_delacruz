import numpy as np

val = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100


def problema_Mochila(valores, pesos, peso_maximo): 

    n = len(valores) 
    matriz = np.array([[0]*(peso_maximo+ 1)]*(len(pesos) + 1))
    for i in range(n + 1):
        for w in range(peso_maximo + 1): 
            if i == 0 or w == 0: 
                matriz[i, w] = 0 
            elif pesos[i-1] <= w: 
                matriz[i, w] = max(valores[i-1] + matriz[i-1, w-pesos[i-1]],   
                              matriz[i-1, w])
            else: 
                matriz[i, w] = matriz[i-1, w] 
    
    print("La solución optima es Z = {}".format(matriz[n, w]))

    return matriz[n, w] 