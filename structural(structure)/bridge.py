# Bridge Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Bridge Design Pattern

Objectif :
Séparer l'abstraction d'une classe de son implémentation pour qu'elles puissent évoluer indépendamment.

Utilisation :
- UI avec plusieurs moteurs de rendu
- Systèmes multi-plateformes

Avantages :
- Flexibilité
- Extension indépendante

"""

"""
🎯 Cas d’usage : UI multi-moteur de rendu (console / HTML)
On a une abstraction UIComponent (bouton, alerte, etc.) qui peut être rendue différemment selon le moteur (ConsoleRenderer, HtmlRenderer).
Le Bridge permet de séparer le "quoi" (abstraction) du "comment" (implémentation).
"""

from abc import ABC, abstractmethod

# ------------------------------
# Implémentation : interface de rendu
# ------------------------------
class Renderer(ABC):
    @abstractmethod
    def render_button(self, label: str):
        pass

# ------------------------------
# Implémentations concrètes
# ------------------------------
class ConsoleRenderer(Renderer):
    def render_button(self, label: str):
        print(f"[Console] >>> [ {label} ]")

class HtmlRenderer(Renderer):
    def render_button(self, label: str):
        print(f"[HTML] <button>{label}</button>")

# ------------------------------
# Abstraction : UIComponent
# ------------------------------
class UIComponent(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self):
        pass

# ------------------------------
# Abstraction étendue : bouton
# ------------------------------
class Button(UIComponent):
    def __init__(self, label: str, renderer: Renderer):
        super().__init__(renderer)
        self.label = label

    def render(self):
        self.renderer.render_button(self.label)

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    print("=== Rendu console ===")
    console_button = Button("Valider", ConsoleRenderer())
    console_button.render()

    print("\n=== Rendu HTML ===")
    html_button = Button("Envoyer", HtmlRenderer())
    html_button.render()
