# Builder Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Builder Design Pattern

Objectif :
Séparer la construction d'un objet complexe de sa représentation, afin que le même processus puisse créer différentes représentations.

Utilisation :
- Génération de documents complexes (PDF, HTML)
- Construction d’objets avec de nombreuses options

Avantages :
- Construction étape par étape
- Plus de lisibilité et de flexibilité
"""

"""
🎯 Cas d’usage : Construction d’un burger personnalisé
Un burger peut avoir différentes options : pain, viande, fromage, sauces, accompagnements…
Le builder permet de construire l’objet étape par étape sans avoir un constructeur énorme.
"""
# ------------------------------
# Produit final : Burger
# ------------------------------
class Burger:
    def __init__(self):
        self.ingredients = []

    def add(self, item):
        self.ingredients.append(item)

    def __str__(self):
        return "🍔 Burger avec : " + ", ".join(self.ingredients)

# ------------------------------
# Builder abstrait
# ------------------------------
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self): pass
    def add_patty(self): pass
    def add_cheese(self): pass
    def add_veggies(self): pass
    def add_sauce(self): pass

    def get_burger(self):
        return self.burger

# ------------------------------
# Builder concret pour burger classique
# ------------------------------
class ClassicBurgerBuilder(BurgerBuilder):
    def add_bun(self):
        self.burger.add("pain sésame")

    def add_patty(self):
        self.burger.add("steak boeuf")

    def add_cheese(self):
        self.burger.add("cheddar")

    def add_veggies(self):
        self.burger.add("salade, tomate")

    def add_sauce(self):
        self.burger.add("ketchup")

# ------------------------------
# Builder concret pour burger végétarien
# ------------------------------
class VeggieBurgerBuilder(BurgerBuilder):
    def add_bun(self):
        self.burger.add("pain complet")

    def add_patty(self):
        self.burger.add("galette de légumes")

    def add_cheese(self):
        self.burger.add("fromage vegan")

    def add_veggies(self):
        self.burger.add("salade, avocat, oignons")

    def add_sauce(self):
        self.burger.add("sauce soja")

# ------------------------------
# Director : utilise un builder
# ------------------------------
class BurgerDirector:
    def __init__(self, builder: BurgerBuilder):
        self.builder = builder

    def construct_burger(self):
        self.builder.add_bun()
        self.builder.add_patty()
        self.builder.add_cheese()
        self.builder.add_veggies()
        self.builder.add_sauce()
        return self.builder.get_burger()

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    print("=== Burger Classique ===")
    classic_builder = ClassicBurgerBuilder()
    director = BurgerDirector(classic_builder)
    print(director.construct_burger())

    print("\n=== Burger Végétarien ===")
    veggie_builder = VeggieBurgerBuilder()
    director = BurgerDirector(veggie_builder)
    print(director.construct_burger())
