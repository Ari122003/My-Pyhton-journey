import pygame

pygame.mixer.init()

pygame.mixer.music.load("rasiya.mp3")

pygame.mixer.music.set_volume(0.7)

pygame.mixer.music.play()


while True:
    x = input(
        "\nPRESS P TO PAUSE THE SONG,R TO RESUME THE SONG AND S TO STOP THE SONG\n")

    if (x == "p"):
        pygame.mixer.music.pause()

    elif(x == "r"):
        pygame.mixer.music.unpause()

    elif(x == "s"):
        pygame.mixer.music.stop()
        break
