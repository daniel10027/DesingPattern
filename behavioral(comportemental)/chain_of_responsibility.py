# Chain Of Responsibility Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Chain of Responsibility Design Pattern

Objectif :
Permettre à plusieurs objets de traiter une requête sans que l’expéditeur connaisse le gestionnaire exact.

Utilisation :
- Middleware
- Moteur de validation
- Traitement d'événements

Avantages :
- Faible couplage
- Traitement flexible
"""

from abc import ABC, abstractmethod

# Classe de base pour tous les handlers
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def next(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return True  # Fin de chaîne

    @abstractmethod
    def handle(self, request):
        pass

# Handler 1 : Vérifie que l'utilisateur est connecté
class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("is_authenticated", False):
            print("⛔ Utilisateur non authentifié.")
            return False
        print("✅ Authentification OK.")
        return self.next(request)

# Handler 2 : Vérifie que le produit est en stock
class StockHandler(Handler):
    def handle(self, request):
        if request.get("stock", 0) < request.get("quantity", 1):
            print("⛔ Stock insuffisant.")
            return False
        print("✅ Stock disponible.")
        return self.next(request)

# Handler 3 : Vérifie que le paiement est valide
class PaymentHandler(Handler):
    def handle(self, request):
        if not request.get("payment_valid", False):
            print("⛔ Paiement refusé.")
            return False
        print("✅ Paiement accepté.")
        return self.next(request)

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de la chaîne de responsabilité
    auth = AuthHandler()
    stock = StockHandler()
    payment = PaymentHandler()

    auth.set_next(stock).set_next(payment)

    # Requête exemple
    request = {
        "is_authenticated": True,
        "stock": 50,
        "quantity": 30,
        "payment_valid": True
    }

    print("🔁 Traitement de la commande :")
    if auth.handle(request):
        print("🎉 Commande validée avec succès.")
    else:
        print("❌ La commande a échoué.")
