# Command Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Command Design Pattern

Objectif :
Encapsuler une requête sous forme d'objet, permettant de paramétrer des actions.

Utilisation :
- Système undo/redo
- Planification de tâches

Avantages :
- Historique d’actions
- Flexibilité dans l'exécution
"""

"""
🎯 Cas d’usage : Télécommande programmable
On a une télécommande qui peut :

Allumer une lumière

Éteindre une lumière

Chaque action est encapsulée dans une commande (Command), et la télécommande peut exécuter ou annuler l’action (undo).
"""

from abc import ABC, abstractmethod

# ------------------------------
# Command Interface
# ------------------------------
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# ------------------------------
# Receiver (Lumière)
# ------------------------------
class Light:
    def turn_on(self):
        print("💡 Lumière allumée")

    def turn_off(self):
        print("💤 Lumière éteinte")

# ------------------------------
# Commandes concrètes
# ------------------------------
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# ------------------------------
# Invoker (Télécommande)
# ------------------------------
class RemoteControl:
    def __init__(self):
        self.command_history = []

    def submit(self, command: Command):
        command.execute()
        self.command_history.append(command)

    def undo_last(self):
        if self.command_history:
            command = self.command_history.pop()
            print("↩️ Annulation :")
            command.undo()
        else:
            print("❌ Rien à annuler.")

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    light = Light()
    turn_on = LightOnCommand(light)
    turn_off = LightOffCommand(light)

    remote = RemoteControl()

    # Allumer la lumière
    remote.submit(turn_on)
    # Éteindre la lumière
    remote.submit(turn_off)
    # Annuler la dernière action (éteindre → allumer)
    remote.undo_last()
