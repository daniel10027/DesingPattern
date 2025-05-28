# Factory Method Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Factory Method Design Pattern

Objectif :
Définir une interface pour créer un objet, mais laisser les sous-classes décider quelle classe instancier.

Utilisation :
- Systèmes de plugins
- Création dynamique d'objets selon un type

Avantages :
- Faible couplage entre la création et l’utilisation
"""

"""
🎯 Cas d’usage : Création d’un transport selon le type (voiture, vélo, moto)
L'application ne connaît pas à l'avance la classe concrète à instancier. 
On délègue la décision à une méthode create_transport() dans des sous-classes.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Produit : interface Transport
# ------------------------------
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# ------------------------------
# Produits concrets
# ------------------------------
class Car(Transport):
    def deliver(self):
        print("🚗 Livraison par voiture.")

class Bike(Transport):
    def deliver(self):
        print("🚲 Livraison par vélo.")

class Scooter(Transport):
    def deliver(self):
        print("🛵 Livraison par scooter.")

# ------------------------------
# Creator : classe de base
# ------------------------------
class Logistics(ABC):
    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

# ------------------------------
# Créateurs concrets
# ------------------------------
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Car()

class BikeLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Bike()

class UrbanLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Scooter()

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    choice = input("Choisir un mode de transport (car, bike, scooter): ").strip().lower()

    if choice == "bike":
        logistics = BikeLogistics()
    elif choice == "scooter":
        logistics = UrbanLogistics()
    else:
        logistics = RoadLogistics()

    logistics.plan_delivery()
