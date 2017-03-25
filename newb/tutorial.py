#!/usr/bin/python
from base import *
from ball import Ball
from paddle import Paddle

def score_display(background, screen, font, player1):
    # how do i control where the score renders on to screen
    text = font.render(str(player1.score), True, (10, 10, 10))
    # text = font.render(str(player2.score), True, (10, 10, 10))

    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    screen.blit(text, textpos)

def main():
    SCREEN_WIDTH=350
    SCREEN_HEIGHT=200
    BALL_VECTOR=(20,5)

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

    # init player1 and player 2
    player1 = Paddle("right")
    player2 = Paddle("left")
    # init ball
    # how to restart?
    ball = Ball(BALL_VECTOR, SCREEN_WIDTH, SCREEN_HEIGHT)

    # init sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))
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

        ballsprite.update(player1, SCREEN_WIDTH, SCREEN_HEIGHT)
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
                if event.key == pygame.K_w:
                    player2.moveup()
                if event.key == pygame.K_s:
                    player2.movedown()    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player1.movepos = [0,0]
                    player1.state = "still"  
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player2.movepos = [0,0]
                    player2.state = "still"  
                                        
        screen.blit(background, (0, 0))
        screen.blit(background, player1.rect)
        ballsprite.draw(screen)
        playersprites.draw(screen)
        # probs a better place for some of the things in here
        score_display(background, screen, font, player1)

        pygame.display.flip()

if __name__ == '__main__': main()

