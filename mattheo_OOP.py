class Ecole():
	def __init__(self,nom,type_ecole,adresse):
		self.nom = nom
		self.type_ecole = type_ecole
		self.adresse = adresse

class Ecole_Inge(Ecole):
	def __init__(self,nom,type_ecole,adresse,nbre_cours_physique,nbre_cours_info):
		
		Ecole.__init__(self,nom,type_ecole,adresse)
		self.__nbre_cours_physique = nbre_cours_physique
		self._nbre_cours_info = nbre_cours_info

	def Get_nbre_cours_physique(self):
		print("Le nbre de cours de physique est de {}".format(self.__nbre_cours_physique))


	def Set_nbre_cours_physique(self,nbre_cours_physique):
		self.__nbre_cours_physique = nbre_cours_physique
		print("Le nbre de cours de physique a ete mis a jour a {}".format(self.__nbre_cours_physique))

class Ecole_Com(Ecole):
	def __init__(self,nom,type_ecole,adresse,nbre_cours_design,nbre_cours_gestion):
		
		Ecole.__init__(self,nom,type_ecole,adresse)		
		self.__nbre_cours_design = nbre_cours_design
		self._nbre_cours_gestion = nbre_cours_gestion

	def Get_nbre_cours_design(self):
		print("Le nbre de cours de design est de {}".format(self.__nbre_cours_design))
		


	def Set_nbre_cours_design(self,nbre_cours_design):
		self.__nbre_cours_design = nbre_cours_design
		print("Le nbre de cours de design a ete mis a jour a {}".format(self.__nbre_cours_design))




ENSTA = Ecole_Inge('ENSTA','Inge','Palaiseau',80,70)
Ecole_Inge.Get_nbre_cours_physique(ENSTA)
Ecole_Inge.Set_nbre_cours_physique(ENSTA,40)

ISCOM = Ecole_Com('ISCOM','Com','Paris',60,90)
Ecole_Com.Get_nbre_cours_design(ISCOM)
Ecole_Com.Set_nbre_cours_design(ISCOM,80)

print(ISCOM._nbre_cours_gestion)
ISCOM._nbre_cours_gestion = 120
print(ISCOM._nbre_cours_gestion)


