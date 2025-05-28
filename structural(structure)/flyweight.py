# Flyweight Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Flyweight Design Pattern

Objectif :
Réduire l’utilisation mémoire en partageant autant que possible les objets similaires.

Utilisation :
- Systèmes graphiques
- Éditeurs de texte (caractères)

Avantages :
- Optimisation mémoire
- Meilleures performances
"""

"""
🎯 Cas d’usage : Système d'affichage de caractères dans un éditeur de texte
Au lieu de créer un objet Character pour chaque lettre dans un document (potentiellement des millions), 
on partage les instances identiques (même style, police...).
"""

# ------------------------------
# Objet partagé (Flyweight)
# ------------------------------
class Character:
    def __init__(self, symbol: str, font: str, size: int):
        self.symbol = symbol
        self.font = font
        self.size = size

    def display(self, position_x: int, position_y: int):
        print(f"Affichage '{self.symbol}' ({self.font}, {self.size}) à ({position_x},{position_y})")

# ------------------------------
# Fabrique de Flyweight
# ------------------------------
class CharacterFactory:
    def __init__(self):
        self._characters = {}

    def get_character(self, symbol: str, font: str, size: int) -> Character:
        key = (symbol, font, size)
        if key not in self._characters:
            self._characters[key] = Character(symbol, font, size)
            print(f"🆕 Création d’un nouveau caractère pour {key}")
        else:
            print(f"✅ Réutilisation de {key}")
        return self._characters[key]

# ------------------------------
# Utilisation client
# ------------------------------
if __name__ == "__main__":
    factory = CharacterFactory()

    text = "HELLO"
    for i, letter in enumerate(text):
        char = factory.get_character(letter, "Arial", 12)
        char.display(i, 0)

    # Réutilisation du même texte avec le même style
    for i, letter in enumerate(text):
        char = factory.get_character(letter, "Arial", 12)
        char.display(i, 1)

    print(f"\nNombre total d'objets Character créés : {len(factory._characters)}")
