# Iterator Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Iterator Design Pattern

Objectif :
Fournir un moyen d’accéder aux éléments d’une collection sans exposer sa structure interne.

Utilisation :
- Boucles for personnalisées
- Structures de données complexes

Avantages :
- Encapsulation
- Séparation de la logique de parcours
"""

"""
🎯 Cas d’usage : Parcourir une collection personnalisée (Livre avec des chapitres)
Nous allons créer une classe Book contenant des chapitres, et un itérateur personnalisé BookIterator 
permettant de les parcourir proprement, sans exposer la structure interne.
"""

from typing import List, Iterator

# ------------------------------
# Itérable : Livre contenant des chapitres
# ------------------------------
class Book:
    def __init__(self, title: str, chapters: List[str]):
        self.title = title
        self._chapters = chapters

    def __iter__(self):
        return BookIterator(self._chapters)

# ------------------------------
# Itérateur : Permet de parcourir les chapitres
# ------------------------------
class BookIterator(Iterator):
    def __init__(self, chapters: List[str]):
        self._chapters = chapters
        self._index = 0

    def __next__(self):
        if self._index < len(self._chapters):
            chapter = self._chapters[self._index]
            self._index += 1
            return chapter
        else:
            raise StopIteration

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    my_book = Book("Design Patterns Explained", [
        "Introduction",
        "Creational Patterns",
        "Structural Patterns",
        "Behavioral Patterns",
        "Conclusion"
    ])

    print(f"📖 Parcours du livre : {my_book.title}")
    for chapter in my_book:
        print(f" - {chapter}")
