import pygame

class Bullet:

    def __init__(self, user_x, user_y, user_right, user_down):
       
        self.bullet = bullet.get_rect()
        self.user_x = user_x
        self.user_y = user_y
        self.user_right = user_right
        self.user_left = user_down
        self.bullet = pygame.image.load("bullet2.jpg")
        

    def bulletFire(self):

        bulletrect = self.bullet.get_rect()
        bulletrect.x = self.user_x
        bulletrect.y = self.user_y
        
        bulletrect.move([self.user_right, self.user_left])


        



