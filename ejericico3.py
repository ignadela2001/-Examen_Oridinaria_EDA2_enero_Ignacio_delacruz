class Stormtrooper():
  def _init_(self,name, rank):
    self.name = name
    self.rank = rank
  def _str_(self):
    return "name {}, rank {}".format( self.name, self.rank )
class clasificacion(Stormtrooper):
  def _init_(self, name, rank, legioncode, indentcorte, indentsiglo, indentescuadra, clonenumber):
    Stormtrooper._init_(self, name, rank)
    self.legioncode = legioncode
    self.indentcorte = indentcorte
    self.indentsiglo= indentsiglo
    self.indentescuadra = indentescuadra
    self.clonenumber = clonenumber
  def _str_(self):
    return Stormtrooper._str_(self) + f'codigo de la legion {self.legioncode}, identificador cohorte {self.indentcorte}, identificador del siglo{self.indentsiglo}, identificador de su escuadra{self.indentescuadra}, numero de cloon{self.clonenumber}'
stormtroopers = []    
for i in range(10):
    stormtroopers.append(Stormtrooper("Tk-"+str(i+1)+str(i+1)+str(i+1)+str(i+1)))

for stormtrooper in stormtroopers:
    rating = Stormtrooper.clasificacion(i)
    print(rating)