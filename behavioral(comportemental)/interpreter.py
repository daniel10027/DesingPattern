# Interpreter Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Interpreter Design Pattern

Objectif :
Donner un interpréteur pour un langage.

Utilisation :
- Expressions mathématiques
- Requêtes DSL

Avantages :
- Extensible
- Adapté aux petits langages
"""
"""
🎯 Cas d’usage : Interpréter des expressions arithmétiques simples
Par exemple, l'expression "5 + 2" ou "5 + 2 - 3" est interprétée et évaluée.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Expression abstraite
# ------------------------------
class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

# ------------------------------
# Expressions terminales
# ------------------------------
class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value

# ------------------------------
# Expressions non terminales
# ------------------------------
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()
    
class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() * self.right.interpret()
    
class Division(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() / self.right.interpret()
    
class Exponand(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() ** self.right.interpret()
    


# ------------------------------
# Parser simple
# ------------------------------
def parse_expression(expression_str: str) -> Expression:
    tokens = expression_str.split()
    stack = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit():
            stack.append(Number(int(token)))
        elif token == '+':
            left = stack.pop()
            i += 1
            right = Number(int(tokens[i]))
            stack.append(Add(left, right))
        elif token == '-':
            left = stack.pop()
            i += 1
            right = Number(int(tokens[i]))
            stack.append(Subtract(left, right))
        i += 1

    return stack.pop()

# ------------------------------
# Exemple d'utilisation
# ------------------------------
if __name__ == "__main__":
    expression = "5 + 3 - 2 ** 2"
    parsed = parse_expression(expression)
    result = parsed.interpret()
    print(f"🧮 Expression: {expression} = {result}")
