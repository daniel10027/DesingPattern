# State Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
State Design Pattern

Objectif :
Permettre à un objet de changer son comportement en fonction de son état interne.

Utilisation :
- Machines à états
- Systèmes de navigation

Avantages :
- Organisation claire
- Ajout d'états sans modifier l'objet principal
"""

"""
🎯 Cas d’usage : Machine à boisson
Une machine passe par plusieurs états :

- Attente d’une pièce

- Prête à délivrer une boisson

- En train de servir

Le comportement change selon l’état.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Contexte : Machine à boisson
# ------------------------------
class VendingMachine:
    def __init__(self):
        self.state = WaitingForCoinState()

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_product(self):
        self.state.select_product(self)

# ------------------------------
# Interface d’état
# ------------------------------
class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def select_product(self, context):
        pass

# ------------------------------
# États concrets
# ------------------------------
class WaitingForCoinState(State):
    def insert_coin(self, context):
        print("🪙 Pièce insérée.")
        context.set_state(ProductSelectionState())

    def select_product(self, context):
        print("❌ Veuillez d'abord insérer une pièce.")

class ProductSelectionState(State):
    def insert_coin(self, context):
        print("❌ Pièce déjà insérée.")

    def select_product(self, context):
        print("🥤 Produit sélectionné. Distribution en cours...")
        context.set_state(WaitingForCoinState())

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    machine = VendingMachine()

    machine.select_product()    # ❌ Pas encore de pièce
    machine.insert_coin()       # ✅ Pièce insérée
    machine.insert_coin()       # ❌ Déjà inséré
    machine.select_product()    # ✅ Produit distribué
    machine.select_product()    # ❌ Revenir à état initial
