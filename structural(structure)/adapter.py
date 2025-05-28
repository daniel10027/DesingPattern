# Adapter Design Pattern
# Ce fichier contient une implémentation exemple du pattern.
"""
Adapter Design Pattern

Objectif :
Convertir l'interface d'une classe en une autre interface attendue par le client.

Utilisation :
- Intégration d’API tierces
- Compatibilité entre systèmes anciens et nouveaux

Avantages :
- Réutilisation de code existant
- Faible impact sur le code client
"""

"""
🎯 Cas d’usage : Adapter une API de lecteur audio
Imaginons une application qui s’attend à une méthode play_audio(file), mais on a une classe existante qui s'appelle MediaPlayer().start(file_path).
L’adapter va faire le lien entre les deux interfaces.
"""

# ------------------------------
# Interface attendue par le client
# ------------------------------
class AudioPlayer:
    def play_audio(self, file: str):
        pass

# ------------------------------
# Classe existante (incompatible avec AudioPlayer)
# ------------------------------
class MediaPlayer:
    def start(self, file_path: str):
        print(f"🎵 Lecture avec MediaPlayer: {file_path}")

# ------------------------------
# Adaptateur : rend MediaPlayer compatible
# ------------------------------
class MediaPlayerAdapter(AudioPlayer):
    def __init__(self, media_player: MediaPlayer):
        self.media_player = media_player

    def play_audio(self, file: str):
        self.media_player.start(file)

# ------------------------------
# Utilisation
# ------------------------------
if __name__ == "__main__":
    # Le client attend un AudioPlayer
    def play_song(player: AudioPlayer, song: str):
        player.play_audio(song)

    old_media_player = MediaPlayer()
    adapter = MediaPlayerAdapter(old_media_player)

    play_song(adapter, "musique.mp3")
