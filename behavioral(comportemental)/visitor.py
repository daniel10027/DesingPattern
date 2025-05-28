# Visitor Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Visitor Design Pattern

Objectif :
Permettre d’ajouter des opérations sur une structure d’objets sans la modifier.

Utilisation :
- Analyse syntaxique
- Traitement de structure composite

Avantages :
- Ajout d'opérations facile
- Séparation des responsabilités
"""

"""
🎯 Cas d’usage : Calculer la somme et l'affichage d'une structure d'expressions mathématiques
On a une hiérarchie d’objets (nombres, additions, soustractions) et on souhaite y appliquer plusieurs 
opérations (affichage, évaluation, etc.) sans modifier leur structure.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Visitable (éléments de la structure)
# ------------------------------
class Expression(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_number(self)

class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_add(self)

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_subtract(self)

# ------------------------------
# Visitor de base
# ------------------------------
class ExpressionVisitor(ABC):
    @abstractmethod
    def visit_number(self, number):
        pass

    @abstractmethod
    def visit_add(self, add):
        pass

    @abstractmethod
    def visit_subtract(self, subtract):
        pass

# ------------------------------
# Visitor pour évaluation (calcul)
# ------------------------------
class EvaluatorVisitor(ExpressionVisitor):
    def visit_number(self, number):
        return number.value

    def visit_add(self, add):
        return add.left.accept(self) + add.right.accept(self)

    def visit_subtract(self, subtract):
        return subtract.left.accept(self) - subtract.right.accept(self)

# ------------------------------
# Visitor pour affichage en chaîne
# ------------------------------
class PrintVisitor(ExpressionVisitor):
    def visit_number(self, number):
        return str(number.value)

    def visit_add(self, add):
        return f"({add.left.accept(self)} + {add.right.accept(self)})"

    def visit_subtract(self, subtract):
        return f"({subtract.left.accept(self)} - {subtract.right.accept(self)})"

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    # Expression : (5 + 3) - 2
    expression = Subtract(Add(Number(5), Number(3)), Number(2))

    evaluator = EvaluatorVisitor()
    printer = PrintVisitor()

    print("🧮 Expression :", expression.accept(printer))  # (5 + 3) - 2
    print("✅ Résultat :", expression.accept(evaluator))  # 6
