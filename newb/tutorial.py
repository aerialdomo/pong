#!/usr/bin/python
from base import *
from ball import Ball

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((250, 200))
    pygame.display.set_caption('I am a cow')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((210, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 44)
    text = font.render("Hello World", 1, (10, 10, 10))
    # need to make a rect to contain text, move rect to move text
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    # Blit everything to the screen, 
    # copy the pixels belonging to said object onto the destination object.
    # render game object
    screen.blit(background, (0, 0))
    pygame.display.flip()

    ball = Ball((20,5))
    ballsprite = pygame.sprite.RenderPlain(ball)

    # Event loop
    while True:
        pressed = pygame.key.get_pressed() 
        get_event = pygame.event.get()

        ballsprite.update()
        for event in get_event:
            if event.type == QUIT:
                return  
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    return              

        screen.blit(background, (0, 0))
        ballsprite.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()