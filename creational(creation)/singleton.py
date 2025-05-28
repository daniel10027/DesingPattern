# Singleton Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Singleton Design Pattern

Objectif :
Garantir qu'une classe n'ait qu'une seule instance et fournir un point d'accès global à cette instance.

Utilisation :
- Gestionnaire de configuration
- Connexion à une base de données
- Logger global

Avantages :
- Contrôle de l'accès à une ressource unique
"""

"""
🎯 Cas d’usage : Logger global
Le Singleton est idéal lorsqu’on souhaite garantir une seule instance partagée dans toute l’application : logger, configuration, cache, etc.
"""

class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("🆕 Création de l'instance du Logger.")
            cls._instance = super().__new__(cls)
            cls._instance._logs = []
        return cls._instance

    def log(self, message):
        self._logs.append(message)
        print(f"📝 LOG: {message}")

    def show_logs(self):
        print("📜 Historique des logs :")
        for entry in self._logs:
            print(f" - {entry}")

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    logger1 = LoggerSingleton()
    logger1.log("Démarrage de l'application.")

    logger2 = LoggerSingleton()
    logger2.log("Connexion à la base de données établie.")

    print(f"logger1 est logger2 ? {logger1 is logger2}")  # ✅ True
    logger2.show_logs()
