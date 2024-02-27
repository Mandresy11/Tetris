import game
import pygame

def main_menu():
    BACKGROUND = game.Background('acceuil.jpg',[0,0])
    pygame.mixer.init()
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(1)
    run = True
    while run:
        win.blit(BACKGROUND.image, BACKGROUND.rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                pygame.display.quit()
                game.main()
                run = False

    pygame.quit()


win = pygame.display.set_mode((875,504))
pygame.display.set_caption('Tetris')
main_menu()
