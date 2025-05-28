# Proxy Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Proxy Design Pattern

Objectif :
Fournir un substitut ou un représentant pour un autre objet.

Utilisation :
- Lazy loading
- Contrôle d’accès
- Cache

Avantages :
- Contrôle des accès
- Chargement différé
"""

"""
🎯 Cas d’usage : Contrôle d’accès à une base de données protégée
Nous allons créer :

une classe réelle Database,

un proxy DatabaseProxy qui protège l'accès par mot de passe.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Interface commune
# ------------------------------
class DatabaseInterface(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

# ------------------------------
# Objet réel (Real Subject)
# ------------------------------
class RealDatabase(DatabaseInterface):
    def query(self, sql: str):
        print(f"🧠 Exécution de la requête SQL : {sql}")

# ------------------------------
# Proxy
# ------------------------------
class DatabaseProxy(DatabaseInterface):
    def __init__(self, password: str):
        self._password = password
        self._real_db = None

    def query(self, sql: str):
        if self._authenticate():
            if not self._real_db:
                self._real_db = RealDatabase()
            self._real_db.query(sql)
        else:
            print("🚫 Accès refusé : mot de passe incorrect.")

    def _authenticate(self) -> bool:
        user_input = input("🔐 Entrez le mot de passe pour accéder à la base : ")
        return user_input == self._password

# ------------------------------
# Utilisation client
# ------------------------------
if __name__ == "__main__":
    db_proxy = DatabaseProxy(password="secret123")
    db_proxy.query("SELECT * FROM users;")
