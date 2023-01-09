class Stormtrooper():
  def _init_(self, nombre, rango):
    self.nombre = nombre
    self.rango = rango
  def _str_(self):
    return "nombre {}, rango {}".format( self.nombre, self.rango )
class clasificacion(Stormtrooper):
  def _init_(self, nombre, rango, codigo_legion, identificador_cohorte, identificador_siglo, identificador_escuadra, numero_trooper):
    Stormtrooper._init_(self, nombre, rango)
    self.codigo_legion = codigo_legion
    self.identificador_cohorte = identificador_cohorte
    self.identificador_siglo= identificador_siglo
    self.identificador_escuadra = identificador_escuadra
    self.numero_trooper = numero_trooper
  def _str_(self):
    return Stormtrooper._str_(self) + f'codigo de legion {self.codigo_legion}, identificador de cohorte {self.identificador_cohorte}, identificador de siglo{self.identificador_siglo}, identificador de escuadra{self.identificador_escuadra}, numero de trooper{self.numero_trooper}'
stormtroopers = []    
for i in range(10):
    stormtroopers.append(Stormtrooper("Tk-"+str(i+1)+str(i+1)+str(i+1)+str(i+1)))

for trooper in stormtroopers:
    rating = Stormtrooper.clasificacion()
    print(rating)