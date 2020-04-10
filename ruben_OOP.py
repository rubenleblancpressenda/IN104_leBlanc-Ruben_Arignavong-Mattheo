class etres_vivants :
	
	"""Super classe contenant animal et humain"""

	def __init__(self,age,taille,poids):
		self.age = age
		self.taille=taille
		self.poids=poids

class humain(etres_vivants) :
	
	def __init__(self,age,taille,poids,sexe,nom):
		self.age = age
		self.taille=taille
		self.poids=poids
		self.sexe=sexe
		self.nom=nom
	def getName(self):
		print(self.nom)
	def __str__(self):
		print("Je pèse ",self.poids,"kg car j'aime beaucoup le paté")

class animal(etres_vivants) :
	
	def __init__(self,age,taille,poids,espece,lieu):
		self.age = age
		self.taille=taille
		self.poids=poids
		self.espece=espece
		self.lieu=lieu
	def getLocation(self):
		return self.lieu
	def move(self,nouveau_lieu):
		self.lieu = nouveau_lieu

Gege=humain(50,175,90,"masc","Gégé")
ours=animal(10,200,120,"ours","Russie")

Gege.getName()
Gege.__str__()
	

