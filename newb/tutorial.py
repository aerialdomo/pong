#!/usr/bin/python
from base import *
from ball import Ball
from bat import Bat

def score_display(background, screen, font, player1):
    text = font.render(str(player1.score), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    screen.blit(text, textpos)

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((350, 200))
    pygame.display.set_caption('I am a cow')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((210, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 44)

    # Blit everything to the screen, 
    # copy the pixels belonging to said object onto the destination object.
    # render game object
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # init player1
    global player1 
    player1 = Bat("right")
    # init ball
    ball = Ball((20,5))

    # init sprites
    playersprites = pygame.sprite.RenderPlain((player1))
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

        ballsprite.update(player1)
        playersprites.update()
        for event in get_event:
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1.moveup()
                if event.key == pygame.K_DOWN:
                    player1.movedown()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player1.movepos = [0,0]
                    player1.state = "still"                                         

        screen.blit(background, (0, 0))
        screen.blit(background, player1.rect)
        ballsprite.draw(screen)
        playersprites.draw(screen)
        # probs a better place for some of the things in here
        score_display(background, screen, font, player1)

        pygame.display.flip()

if __name__ == '__main__': main()

