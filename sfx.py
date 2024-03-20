import pygame

# Sound Stuff
pygame.mixer.init()
def randomizeSound():
    pygame.mixer.music.load("assets/randomizeSound.mp3")
    pygame.mixer.music.play(loops=0)
def losingSound():
    pygame.mixer.music.load("assets/losingSound.mp3")
    pygame.mixer.music.play(loops=0)
def winningSound():
    pygame.mixer.music.load("assets/winningSound.mp3")
    pygame.mixer.music.play(loops=0)