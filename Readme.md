# 📐 Design Patterns en Python

Ce projet regroupe les **23 Design Patterns classiques** décrits par le livre *Design Patterns: Elements of Reusable Object-Oriented Software* des *Gang of Four (GoF)*.  
Ils sont organisés par catégorie, chacun dans son propre fichier Python, avec des explications et une structure de base.

---

## 🧠 Qu’est-ce qu’un Design Pattern ?

Un **Design Pattern** est une solution réutilisable à un problème de conception courant en génie logiciel.  
Il ne s'agit pas de code prêt à l'emploi, mais d'un **modèle** ou d’un **modèle architectural**.

---

## 📂 Catégories de Design Patterns

### 🏗️ 1. Creational Patterns
Ils gèrent la **création des objets** de manière flexible.

| Pattern | Description |
|--------|-------------|
| Singleton | Garantit qu'une classe n'a qu'une seule instance. |
| Factory Method | Laisse les sous-classes décider quel objet instancier. |
| Abstract Factory | Crée des familles d'objets liés sans spécifier leur classe concrète. |
| Builder | Construit des objets complexes étape par étape. |
| Prototype | Crée des objets par clonage. |

---

### 🧱 2. Structural Patterns
Ils concernent la **composition des classes et objets**.

| Pattern | Description |
|--------|-------------|
| Adapter | Convertit une interface en une autre attendue. |
| Bridge | Sépare abstraction et implémentation. |
| Composite | Structure hiérarchique (arbres). |
| Decorator | Ajoute dynamiquement des fonctionnalités. |
| Facade | Fournit une interface simplifiée à un sous-système complexe. |
| Flyweight | Réduit l'utilisation mémoire via des objets partagés. |
| Proxy | Fournit un représentant ou un substitut à un autre objet. |

---

### 🤖 3. Behavioral Patterns
Ils traitent de la **communication entre objets**.

| Pattern | Description |
|--------|-------------|
| Chain of Responsibility | Passe une requête à travers une chaîne de gestionnaires. |
| Command | Encapsule une action dans un objet. |
| Interpreter | Implémente un interpréteur pour un langage. |
| Iterator | Parcourt une collection sans exposer sa structure. |
| Mediator | Centralise les communications entre objets. |
| Memento | Capture et restaure un état interne. |
| Observer | Notifie automatiquement les changements d’un objet. |
| State | Modifie le comportement selon l’état de l’objet. |
| Strategy | Définit des comportements interchangeables. |
| Template Method | Définit le squelette d’un algorithme. |
| Visitor | Ajoute des opérations à une structure d’objet sans la modifier. |

---

## 🔧 Utilisation typique

- **Creational** : initialisation, configuration flexible
- **Structural** : adapter du code existant, organisation modulaire
- **Behavioral** : flux logique, communication, traitement d’événements

---

Chaque fichier contient :
- 📝 Une explication en haut en commentaire
- 🧱 Une classe ou structure de base pour démarrer

---

## 🧪 Bonus

Tu peux étendre chaque pattern avec :
- ✅ Un exemple d’utilisation
- ✅ Un test unitaire
- ✅ Un schéma UML ou d’exécution

---

## 🎓 Références

- *Design Patterns - GoF (1994)*
- *Refactoring Guru* – https://refactoring.guru/design-patterns
- *SourceMaking* – https://sourcemaking.com/design_patterns
