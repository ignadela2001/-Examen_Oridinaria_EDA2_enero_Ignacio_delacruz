class Valiosos:
    def _init_(self, name, w, price, fechacaducidad):
        self.name = name
        self.w = w
        self.price = price
        self.fechacaducidad = fechacaducidad
        print ("Artefacto creado con éxito")

    def _str_(self):
        return 'Artefacto {}, w {}, Precio {}, Fecha de Caducidad {}'.format(self.name, self.w, self.price, self.fechacaducidad)

artefactos = []

artefacto_1 = Valiosos("Blaster",6, 1500, "2055-12-23")
artefacto_2 = Valiosos("Cristal kyber", 0.3, 500000, "2053-02-24")
artefacto_3= Valiosos("At-St",100000, 1000000, "2076-04-13")

artefactos.append(artefacto_1)
artefactos.append(artefacto_2)
artefactos.append(artefacto_3)

artefactos.sort(key=lambda x: x.fechacaducidad)


for artefacto in artefactos:
    if artefacto.name == "Blaster":
        artefacto.price = 6000
