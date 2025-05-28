# Mediator Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Mediator Design Pattern

Objectif :
Définir un objet central pour encapsuler la communication entre plusieurs objets.

Utilisation :
- Système de chat
- UI complexes

Avantages :
- Réduction du couplage
- Communication centralisée
"""

"""
🎯 Cas d’usage : Système de chat simplifié
Chaque utilisateur communique via un ChatRoom central (le médiateur) au lieu de s’envoyer
 des messages directement. Cela évite que les objets soient couplés entre eux.
"""

# ------------------------------
# Le Médiateur : ChatRoom
# ------------------------------
class ChatRoom:
    def __init__(self):
        self.participants = []

    def register(self, user):
        self.participants.append(user)
        user.chatroom = self

    def send(self, message, sender):
        for user in self.participants:
            if user != sender:
                user.receive(message, sender)

# ------------------------------
# Les collègues qui utilisent le médiateur
# ------------------------------
class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = None

    def send(self, message):
        print(f"📤 {self.name} envoie : {message}")
        if self.chatroom:
            self.chatroom.send(message, self)

    def receive(self, message, sender):
        print(f"📥 {self.name} reçoit de {sender.name} : {message}")

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    # Création du médiateur
    chatroom = ChatRoom()

    # Création des utilisateurs
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Enregistrement auprès du médiateur
    chatroom.register(alice)
    chatroom.register(bob)
    chatroom.register(charlie)

    # Envoi de messages
    alice.send("Salut tout le monde !")
    bob.send("Salut Alice !")
    charlie.send("Bonjour à tous !")
