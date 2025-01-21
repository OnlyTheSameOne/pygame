# Import der Pygame-Bibliothek
import pygame

# initialisieren von pygame
pygame.init()

# Variablen für die Bildschirmgröße
x_screen_width = 1200
y_screen_height = 750

# Titel für Fensterkopf
pygame.display.set_caption("Mein Spiel")

# Fenster öffnen
screen = pygame.display.set_mode((x_screen_width, y_screen_height))

# solane [ongoing] True ist läuft das Spiel
ongoing = True

# Bildschirm Aktualisierung einstellen
clock = pygame.time.Clock()

# Schleife - Game Loop
while ongoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False


    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeit pro Sekunde
    clock.tick(60)