import pygame

def play_sound(sound_path:str, play_once:bool):

    sound = pygame.mixer.Sound(sound_path)

    if play_once:

        if not pygame.mixer.get_busy():  # Check if no sound is currently playing
            
            sound.play()
        
            return

    else:

        sound.play()