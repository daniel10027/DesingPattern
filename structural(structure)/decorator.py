# Decorator Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Decorator Design Pattern

Objectif :
Ajouter dynamiquement des responsabilités à un objet sans modifier son code source.

Utilisation :
- Middlewares
- Systèmes d'extensions

Avantages :
- Plus flexible que l’héritage
- Combinaison dynamique des comportements
"""

"""
🎯 Cas d’usage : Ajout dynamique de fonctionnalités à un café
On a un objet Coffee de base, auquel on peut ajouter dynamiquement des décorateurs : lait, sucre, crème, etc.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Composant de base
# ------------------------------
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# ------------------------------
# Composant concret
# ------------------------------
class BasicCoffee(Coffee):
    def cost(self):
        return 2.0

    def description(self):
        return "Café simple"

# ------------------------------
# Décorateur de base
# ------------------------------
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

# ------------------------------
# Décorateurs concrets
# ------------------------------
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", lait"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2

    def description(self):
        return self._coffee.description() + ", sucre"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.7

    def description(self):
        return self._coffee.description() + ", chantilly"

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    coffee = BasicCoffee()
    print(f"➡️ {coffee.description()} : {coffee.cost():.2f}€")

    # Ajouter lait
    coffee = MilkDecorator(coffee)
    # Ajouter sucre
    coffee = SugarDecorator(coffee)
    # Ajouter chantilly
    coffee = WhippedCreamDecorator(coffee)

    print(f"➡️ {coffee.description()} : {coffee.cost():.2f}€")
