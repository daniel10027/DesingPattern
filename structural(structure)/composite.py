# Composite Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Composite Design Pattern

Objectif :
Composer des objets en structures arborescentes pour représenter des hiérarchies tout-partie.

Utilisation :
- Arborescence de fichiers
- Menus, arbres DOM

Avantages :
- Traitement uniforme des objets simples et composés
"""

"""
🎯 Cas d’usage : Structure de répertoires et fichiers
On veut modéliser une hiérarchie où un dossier peut contenir :

des fichiers (éléments simples)

d'autres dossiers (éléments composites)

Le Composite Pattern permet de traiter les deux de la même façon.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Composant de base
# ------------------------------
class FileSystemItem(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# ------------------------------
# Élément simple : fichier
# ------------------------------
class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print("  " * indent + f"📄 {self.name}")

# ------------------------------
# Élément composite : dossier
# ------------------------------
class Directory(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def display(self, indent=0):
        print("  " * indent + f"📁 {self.name}")
        for child in self.children:
            child.display(indent + 1)

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    # Créer la structure
    root = Directory("Projet")
    root.add(File("README.md"))
    root.add(File("requirements.txt"))

    src = Directory("src")
    src.add(File("main.py"))
    src.add(File("utils.py"))

    tests = Directory("tests")
    tests.add(File("test_main.py"))

    root.add(src)
    root.add(tests)

    # Affichage de la hiérarchie
    root.display()
