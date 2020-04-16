 
# Remarques sur le rendu du TD2

## Utilisation du constructeur de la super classe : 
On peut appeler directement le constructeur de la superclasse pour initialiser les attributs.
### Votre code : 
```python
class humain(etres_vivants) :
	
	def __init__(self,age,taille,poids,sexe,nom):
		self.age = age
		self.taille=taille
		self.poids=poids
		self.sexe=sexe
		self.nom=nom
```
### Appel au constructeur de la super classe :
```python
class humain(etres_vivants) :
	
	def __init__(self,age,taille,poids,sexe,nom):
		etres_vivants.__init__(self, age, taille, poids)
		self.sexe=sexe
		self.nom=nom
```
Même remarque pour la classe animal.

## La fonction \__str__
La fonction \__str__ est utilisée pour directement retourner une chaîne de caractères correspondant à l'objet qui l'appelle.

Cela devrait être
```python
def __str__(self):
		return "Je pèse " + str(self.poids) + " kg car j'aime beaucoup le paté"
```

Cette fonction est appelé de manière implicite lors de l'affichage d'un objet de classe humain.

Pour l'utiliser, il suffit à la dernière ligne de faire
```python
print(Gege)
```
Cela est équivalent à
```python
print(Gege.__str__())
```