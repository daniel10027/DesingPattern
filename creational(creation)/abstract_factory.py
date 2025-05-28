# Abstract Factory Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Abstract Factory Design Pattern

Objectif :
Fournir une interface pour créer des familles d'objets liés ou dépendants sans spécifier leur classe concrète.

Utilisation :
- Interface utilisateur multi-thèmes
- Systèmes multiplateformes (Windows/Mac/Linux)

Avantages :
- Cohérence entre les objets créés
- Encapsulation des détails de création
"""

"""
🎯 Cas d’usage : Interface graphique multi-thème (Light / Dark)
On veut créer une interface composée de boutons et de checkboxes.
Selon le thème (Light ou Dark), on instancie la famille d’objets correspondante.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Interfaces des produits
# ------------------------------
class Button(ABC):
    @abstractmethod
    def render(self): pass

class Checkbox(ABC):
    @abstractmethod
    def render(self): pass

# ------------------------------
# Produits Concrets – Thème Light
# ------------------------------
class LightButton(Button):
    def render(self):
        print("🟦 Bouton Light")

class LightCheckbox(Checkbox):
    def render(self):
        print("⬜️ Checkbox Light")

# ------------------------------
# Produits Concrets – Thème Dark
# ------------------------------
class DarkButton(Button):
    def render(self):
        print("⬛ Bouton Dark")

class DarkCheckbox(Checkbox):
    def render(self):
        print("🟥 Checkbox Dark")

# ------------------------------
# Interface de la Factory Abstraite
# ------------------------------
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass

# ------------------------------
# Factories concrètes
# ------------------------------
class LightThemeFactory(GUIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()

class DarkThemeFactory(GUIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()

# ------------------------------
# Application qui utilise la factory
# ------------------------------
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        self.button.render()
        self.checkbox.render()

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    theme = input("Choisissez un thème (light/dark) : ").strip().lower()

    if theme == "dark":
        factory = DarkThemeFactory()
    else:
        factory = LightThemeFactory()

    app = Application(factory)
    app.render()
