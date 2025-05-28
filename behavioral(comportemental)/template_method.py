# Template Method Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Template Method Design Pattern

Objectif :
Définir le squelette d’un algorithme tout en laissant certaines étapes à des sous-classes.

Utilisation :
- Traitement de données
- Génération de rapports

Avantages :
- Réutilisation de code
- Flexibilité
"""

"""
🎯 Cas d’usage : Génération de rapport (PDF, HTML)
On définit un algorithme général pour générer un rapport :

Préparer les données

Formater le contenu

Générer la sortie

Les sous-classes personnalisent uniquement les étapes format_content() et generate_output().
"""

from abc import ABC, abstractmethod

# ------------------------------
# Classe abstraite : squelette de l'algorithme
# ------------------------------
class ReportGenerator(ABC):
    def generate_report(self):
        data = self.fetch_data()
        content = self.format_content(data)
        self.generate_output(content)

    def fetch_data(self):
        # Étape commune (peut être surchargée si besoin)
        return {
            "title": "Ventes mensuelles",
            "values": [1200, 2300, 1800, 2400]
        }

    @abstractmethod
    def format_content(self, data):
        pass

    @abstractmethod
    def generate_output(self, content):
        pass

# ------------------------------
# Implémentation HTML
# ------------------------------
class HtmlReport(ReportGenerator):
    def format_content(self, data):
        rows = "".join(f"<li>{v}€</li>" for v in data["values"])
        return f"<h1>{data['title']}</h1><ul>{rows}</ul>"

    def generate_output(self, content):
        print("📄 Rapport HTML généré :")
        print(content)

# ------------------------------
# Implémentation texte
# ------------------------------
class TextReport(ReportGenerator):
    def format_content(self, data):
        values = ", ".join(str(v) for v in data["values"])
        return f"{data['title']}\nValeurs: {values}"

    def generate_output(self, content):
        print("📄 Rapport texte généré :")
        print(content)

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    print("=== Rapport HTML ===")
    html_report = HtmlReport()
    html_report.generate_report()

    print("\n=== Rapport texte ===")
    text_report = TextReport()
    text_report.generate_report()
