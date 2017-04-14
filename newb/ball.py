from base import *

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector, screen_width, screen_height):
        color = (66,134,244)
        ball_size = (50, 50)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pokeball.png')
        self.image = pygame.transform.scale(self.image, ball_size)
        # rect is ball
        self.rect = self.image.get_rect(center=(screen_width/2,screen_height/2))
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

    def update(self, player1, player2, screen_width, screen_height):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
        (angle,z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                self.offcourt(player1, screen_width, screen_height)
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
                self.offcourt(player2, screen_width, screen_height)
                # what else is going on there? 
        else:
            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle,z)


    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

    def offcourt(self, player, screen_width, screen_height):
        player.score += 1
        # ball position reset
        self.rect = self.image.get_rect(center=(screen_width/2,screen_height/2))


          