# Observer Design Pattern
# Ce fichier contient une implémentation exemple du pattern.

"""
Observer Design Pattern

Objectif :
Permettre à des objets d’être notifiés automatiquement des changements d’un autre objet.

Utilisation :
- Interfaces graphiques
- Systèmes de notification

Avantages :
- Découplage entre sujet et observateurs
- Réactivité
"""

"""
🎯 Cas d’usage : Système de notifications météo
Quand la station météo met à jour la température, tous les abonnés (affichages ou alertes) sont notifiés automatiquement.
"""

from abc import ABC, abstractmethod

# ------------------------------
# Sujet (observable) : Station météo
# ------------------------------
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temp):
        print(f"🌡️ Mise à jour de la température : {temp}°C")
        self._temperature = temp
        self.notify()

# ------------------------------
# Observateur abstrait
# ------------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# ------------------------------
# Observateurs concrets
# ------------------------------
class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"📺 Affichage de la température : {temperature}°C")

class TemperatureAlert(Observer):
    def update(self, temperature):
        if temperature > 30:
            print("🚨 Alerte : Canicule détectée !")
        elif temperature < 5:
            print("❄️ Alerte : Froid extrême détecté.")

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    station = WeatherStation()
    display = TemperatureDisplay()
    alert = TemperatureAlert()

    station.attach(display)
    station.attach(alert)

    station.set_temperature(22)
    station.set_temperature(35)
    station.set_temperature(2)
