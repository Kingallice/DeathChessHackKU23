import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,image,speed,p_x,p_y,p_gravity,df,sur,health,a_p,env=("grd","left","right")):
        super().__init__()
        if p_x > 0:
            p_x = env[2] - 100
        self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (100, 100))
        self.rect = self.image.get_rect(topleft = (p_x,p_y))
        self.speed = speed
        self.ground = env[0]
        self.left = env[1]
        self.right = env[2]
        self.gravity = p_gravity
        self.downforce = df
        self.dx = 0
        self.dy = 0
        self.sur = sur
        self.health = health
        self.a_p = a_p
        self.max_health = health

    def player_input(self,target):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.bottom >= self.ground:
            self.gravity = self.downforce

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_a]:
            self.rect.x += -self.speed

        if keys[pygame.K_f] and keys[pygame.K_d] and not keys[pygame.K_a]:
            self.attack_r(self.sur,target)

        if keys[pygame.K_f] and keys[pygame.K_a] and not keys[pygame.K_d]:
            self.attack_l(self.sur,target)

        if keys[pygame.K_f] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.attack_u(self.sur,target)

    def player_input2(self,target):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom >= self.ground:
            self.gravity = self.downforce

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x += -self.speed

        if keys[pygame.K_l] and keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.attack_r(self.sur,target)

        if keys[pygame.K_l] and keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.attack_l(self.sur,target)

        if keys[pygame.K_l] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.attack_u(self.sur,target)

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.ground: self.rect.bottom = self.ground


    def check_l_e(self):
        if self.rect.x < self.left:
            self.rect.x = self.left
        if self.rect.x > self.right - self.rect.width:
            self.rect.x = self.right - self.rect.width
            

    def attack_u(self, surface,target):
        sword = pygame.transform.smoothscale(pygame.image.load("Images/Pieces/sword_up.png").convert_alpha(), (100, 100))
        attacking_rect = sword.get_rect(topleft = (self.rect.centerx - 50, self.rect.y - 45))
        surface.blit(sword, attacking_rect)

        if attacking_rect.colliderect(target.rect):
            target.health -= self.a_p

    def attack_r(self, surface,target):
        sword = pygame.transform.smoothscale(pygame.image.load("Images/Pieces/sword.png").convert_alpha(), (100, 100))
        attacking_rect = sword.get_rect(topleft=(self.rect.centerx, self.rect.y))
        surface.blit(sword, attacking_rect)

        if attacking_rect.colliderect(target.rect):
            target.health -= self.a_p

    def attack_l(self,surface,target):
        sword = pygame.transform.smoothscale(pygame.image.load("Images/Pieces/sword_left.png").convert_alpha(), (100, 100))
        attacking_rect = sword.get_rect(topleft=(self.rect.centerx - 90, self.rect.y ))
        surface.blit(sword, attacking_rect)

        if attacking_rect.colliderect(target.rect):
            target.health -= self.a_p

    def win(self):
        file = open("./Config/battleOut.dat", "w+")
        file.write()
        return True
