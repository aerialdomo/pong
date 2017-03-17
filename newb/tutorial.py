#!/usr/bin/python
from base import *
from ball import Ball
from bat import Bat

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
    # text = font.render("Hello World", 1, (10, 10, 10))
    # need to make a rect to contain text, move rect to move text
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos.centery = background.get_rect().centery
    # background.blit(text, textpos)

    # Blit everything to the screen, 
    # copy the pixels belonging to said object onto the destination object.
    # render game object
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # init player
    global player 
    player = Bat("right")
    # init ball
    ball = Ball((20,5))

    # init sprites
    playersprites = pygame.sprite.RenderPlain((player))
    ballsprite = pygame.sprite.RenderPlain(ball)

    # Initialise clock
    # whyyyyyyy
    clock = pygame.time.Clock()

    # Event loop
    running = True
    while running:
        clock.tick(60)

        pressed = pygame.key.get_pressed() 
        get_event = pygame.event.get()

        ballsprite.update()
        playersprites.update()
        for event in get_event:
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("K_up")
                    player.moveup()
                if event.key == pygame.K_DOWN:
                    print("K_down")
                    player.movedown()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.movepos = [0,0]
                    player.state = "still"                                         

        screen.blit(background, (0, 0))
        screen.blit(background, player.rect)
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()