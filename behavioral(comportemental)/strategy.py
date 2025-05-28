# Strategy Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Strategy Design Pattern

Objectif :
Permettre de définir une famille d’algorithmes, de les encapsuler et de les rendre interchangeables.

Utilisation :
- Algorithmes de tri
- Politique de paiement

Avantages :
- Comportement interchangeable
- Respect du principe ouvert/fermé
"""

"""
🎯 Cas d’usage : Stratégie de tri personnalisable
L’utilisateur peut choisir dynamiquement entre plusieurs algorithmes de tri : par ordre croissant, décroissant, 
ou par longueur (dans une liste de chaînes).
"""

from abc import ABC, abstractmethod
from typing import List

# ------------------------------
# Interface de stratégie
# ------------------------------
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[str]) -> List[str]:
        pass

# ------------------------------
# Stratégies concrètes
# ------------------------------
class AscendingSort(SortStrategy):
    def sort(self, data: List[str]) -> List[str]:
        return sorted(data)

class DescendingSort(SortStrategy):
    def sort(self, data: List[str]) -> List[str]:
        return sorted(data, reverse=True)

class LengthSort(SortStrategy):
    def sort(self, data: List[str]) -> List[str]:
        return sorted(data, key=len)

# ------------------------------
# Contexte : gestionnaire de tri
# ------------------------------
class SortManager:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data: List[str]):
        return self._strategy.sort(data)

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    data = ["banane", "kiwi", "pomme", "ananas"]

    manager = SortManager(AscendingSort())
    print("⬆️ Tri croissant :", manager.sort_data(data))

    manager.set_strategy(DescendingSort())
    print("⬇️ Tri décroissant :", manager.sort_data(data))

    manager.set_strategy(LengthSort())
    print("📏 Tri par longueur :", manager.sort_data(data))
