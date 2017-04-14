#!/usr/bin/python
from base import *
from ball import Ball
from paddle import Paddle

def score_display(background, screen, font, player1, player2):
    font_color = (10, 10, 10)
    text_p1 = font.render(str(player1.score), True, font_color)
    text_p2 = font.render(str(player2.score), True, font_color)

    textpos_p1 = text_p1.get_rect()
    textpos_p1.right = background.get_rect().right
    textpos_p1.topright = background.get_rect().topright
    screen.blit(text_p1, textpos_p1)

    textpos_p2 = text_p2.get_rect()
    textpos_p2.left = background.get_rect().left
    textpos_p2.topleft = background.get_rect().topleft
    screen.blit(text_p2, textpos_p2)

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

        ballsprite.update(player1, player2, SCREEN_WIDTH, SCREEN_HEIGHT)
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
        ballsprite.draw(screen)
        playersprites.draw(screen)
        # probs a better place for some of the things in here
        score_display(background, screen, font, player1, player2)

        pygame.display.flip()

if __name__ == '__main__': main()

