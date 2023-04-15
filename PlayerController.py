import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,image,speed,p_x,p_y,p_gravity,df,sur):
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (100, 100))
        self.rect = self.image.get_rect(topleft = (p_x,p_y))
        self.speed = speed
        self.ground = 595
        self.gravity = p_gravity
        self.downforce = df
        self.dx = 0
        self.dy = 0
        self.sur = sur
        self.health = 10
        self.a_p = 20
        self.attacking = False


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom >= self.ground:
            self.gravity = self.downforce

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_a]:
            self.rect.x += -self.speed

        if keys[pygame.K_f] and keys[pygame.K_d] and not keys[pygame.K_a]:
            self.attack_r(self.sur)

        if keys[pygame.K_f] and keys[pygame.K_a] and not keys[pygame.K_d]:
            self.attack_l(self.sur)

        if keys[pygame.K_f] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.attack_u(self.sur)

    def player_input2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom >= self.ground:
            self.gravity = self.downforce

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x += -self.speed

        if keys[pygame.K_l] and keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.attack_r(self.sur)

        if keys[pygame.K_l] and keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.attack_l(self.sur)

        if keys[pygame.K_l] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.attack_u(self.sur)

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.ground: self.rect.bottom = self.ground


    def check_l_e(self):
        if self.rect.left + self.rect.x < 0:
            self.rect.x = -self.rect.left
        if self.rect.right + self.rect.x > 2500:
            self.rect.x = 2500 - self.rect.right

    def attack_u(self, surface):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y - 50, 5, self.rect.height)
        pygame.draw.rect(surface, (255,255,255), attacking_rect)

    def attack_r(self, surface):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (255,255,255), attacking_rect)

    def attack_l(self,surface):
        attacking_rect = pygame.Rect(self.rect.left - 80, self.rect.y, self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (255, 255, 255), attacking_rect)


