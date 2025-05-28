# Prototype Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Prototype Design Pattern

Objectif :
Créer de nouveaux objets en copiant un prototype existant.

Utilisation :
- Jeux vidéos (cloner des personnages)
- Clonage d’objets lourds à instancier

Avantages :
- Réduction des coûts d'instanciation
- Évite la redondance
"""

"""
🎯 Cas d’usage : Clonage de personnages dans un jeu vidéo
On crée un prototype d'un personnage, puis on le clone pour créer plusieurs copies 
avec les mêmes propriétés de base (que l'on peut modifier si besoin).
"""

import copy

# ------------------------------
# Prototype : Personnage de jeu
# ------------------------------
class GameCharacter:
    def __init__(self, name, level, inventory):
        self.name = name
        self.level = level
        self.inventory = inventory  # liste mutable

    def clone(self):
        # Clone profond pour ne pas partager l'inventaire
        return copy.deepcopy(self)

    def __str__(self):
        return f"👤 {self.name} - Niveau {self.level} - Inventaire: {self.inventory}"

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    # Prototype original
    base_knight = GameCharacter("Chevalier", 10, ["Épée", "Bouclier"])
    print("🧬 Prototype :", base_knight)

    # Clone 1
    knight_clone = base_knight.clone()
    knight_clone.name = "Chevalier Fantôme"
    knight_clone.inventory.append("Cape invisible")
    print("📄 Clone 1 :", knight_clone)

    # Clone 2
    another_knight = base_knight.clone()
    another_knight.name = "Chevalier Noir"
    another_knight.level = 15
    print("📄 Clone 2 :", another_knight)

    # Vérification que l’inventaire est bien indépendant
    print("🔍 Prototype inchangé :", base_knight)
