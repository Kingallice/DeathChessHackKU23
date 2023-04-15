import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,image,speed,p_x,p_y,p_gravity,df):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft = (p_x,p_y))
        self.speed = speed
        self.ground = 595
        self.gravity = p_gravity
        self.downforce = df

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom >= self.ground:
            self.gravity = self.downforce

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_s]:
            pass

        if keys[pygame.K_a]:
            self.rect.x += -self.speed

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.ground: self.rect.bottom = self.ground

