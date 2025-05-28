# Facade Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Facade Design Pattern

Objectif :
Fournir une interface simplifiée à un ensemble complexe de classes.

Utilisation :
- Librairies complexes
- API simplifiées

Avantages :
- Réduction de la complexité
- Meilleure lisibilité pour le client
"""

"""
🎯 Cas d’usage : Système de démarrage de PC
Derrière un simple bouton power_on(), plusieurs composants (BIOS, CPU, disque dur) doivent être initialisés.
Le Façade va masquer cette complexité pour l’utilisateur.
"""

# ------------------------------
# Sous-systèmes complexes
# ------------------------------

class BIOS:
    def execute(self):
        print("🧬 BIOS initialisé")

class CPU:
    def freeze(self):
        print("🧠 CPU gelé")

    def jump(self, position):
        print(f"🧠 CPU saute à l'adresse {position}")

    def execute(self):
        print("🧠 CPU exécute les instructions")

class HardDrive:
    def read(self, lba, size):
        print(f"💾 Lecture de {size} blocs à l'adresse {lba}")
        return "boot_code"

# ------------------------------
# Façade
# ------------------------------

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.bios = BIOS()
        self.hard_drive = HardDrive()

    def power_on(self):
        print("🔌 Démarrage du PC...")
        self.cpu.freeze()
        self.bios.execute()
        boot_code = self.hard_drive.read(0, 10)
        self.cpu.jump(boot_code)
        self.cpu.execute()
        print("✅ PC prêt à l'utilisation")

# ------------------------------
# Utilisation client
# ------------------------------

if __name__ == "__main__":
    pc = ComputerFacade()
    pc.power_on()
