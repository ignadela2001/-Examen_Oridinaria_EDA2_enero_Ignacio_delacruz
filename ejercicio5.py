def fuerza(bolsa, indice):
    if indice == len(bolsa):
        return False
    if bolsa[indice] == "SableDeLuz":
        return True, indice+1
    else:
        return fuerza(bolsa, indice+1)