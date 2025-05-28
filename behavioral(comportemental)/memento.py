# Memento Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Memento Design Pattern

Objectif :
Capturer et restaurer l’état interne d’un objet sans exposer ses détails.

Utilisation :
- Undo / redo
- Sauvegarde d’états

Avantages :
- Encapsulation préservée
- Historique des états
"""

"""
🎯 Cas d’usage : Éditeur de texte avec fonctionnalité "Undo"
L’objectif est de permettre à l’utilisateur d’écrire du texte, de sauvegarder 
l’état actuel, puis de revenir en arrière (undo) si besoin — sans exposer l’état interne du texte.
"""

# ------------------------------
# Memento : capture l'état
# ------------------------------
class TextMemento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        return self._content

# ------------------------------
# Originator : l'objet dont on capture l'état
# ------------------------------
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return TextMemento(self._content)

    def restore(self, memento: TextMemento):
        self._content = memento.get_saved_content()

# ------------------------------
# Caretaker : gère l’historique des états
# ------------------------------
class History:
    def __init__(self):
        self._history = []

    def backup(self, memento: TextMemento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()
        return None

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Bonjour ")
    history.backup(editor.save())

    editor.write("le monde !")
    history.backup(editor.save())

    editor.write(" Ceci sera supprimé.")
    print(f"📄 Avant undo : {editor.get_content()}")

    # Undo une fois
    editor.restore(history.undo())
    print(f"↩️ Après 1er undo : {editor.get_content()}")

    # Undo une deuxième fois
    editor.restore(history.undo())
    print(f"↩️ Après 2e undo : {editor.get_content()}")
