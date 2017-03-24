from base import *

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        color = (66,134,244)
        width = 20
        height = 20
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kitten_50_50.jpeg')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

    def update(self, player1):
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
                self.offcourt(player=player1)
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
                # self.offcourt()
            # if tr and br or (tl and bl):
                # what else is going on there? 
                # print(111)
        else:
            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            # elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
            #     angle = math.pi - angle
            #     self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle,z)


    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

    def offcourt(self, player):
        player.score += 1
        print(player.score)
          