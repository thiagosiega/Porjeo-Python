import pygame

class Player:
    def __init__(self, x, y):
        self.altura = 50
        self.largura = 50
        self.max_pulos = 2  # Número máximo de pulos
        self.pulos_restantes = self.max_pulos  # Pulos disponíveis
        self.altura_pulo = 10
        self.velocidade_x = 5  # Velocidade de movimento horizontal
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.velocidade_y = 0
        self.gravidade = 0.5
        self.velocidade_maxima = 10
        self.pode_pular = True  # Controle para evitar múltiplos pulos com uma única pressão

    def colide(self, chao):
        return self.rect.colliderect(chao.rect)

    def jump(self):
        if self.pulos_restantes > 0 and self.pode_pular:
            print(self.pulos_restantes)
            self.velocidade_y = -self.altura_pulo  # Valor negativo para subir
            self.pulos_restantes -= 1
            self.pode_pular = False  # Desativa o pulo até que a tecla seja solta

    def resetar_pulos(self):
        self.pulos_restantes = self.max_pulos

    def mover(self):
        keys = pygame.key.get_pressed()

        """#setas para testar
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5"""


        # Movimento horizontal
        if keys[pygame.K_a]:
            self.rect.x -= self.velocidade_x
        if keys[pygame.K_d]:
            self.rect.x += self.velocidade_x

        # Movimento vertical (pulo)
        if keys[pygame.K_SPACE]:
            self.jump()
        else:
            self.pode_pular = True  # Permite pular novamente quando a tecla for solta"""

        # Aplicar gravidade
        
        self.velocidade_y += self.gravidade
        if self.velocidade_y > self.velocidade_maxima:
            self.velocidade_y = self.velocidade_maxima
        self.rect.y += self.velocidade_y
        

    def draw(self, screen,offset_x, offset_y):
        screen.blit(self.image, (self.rect.x + offset_x, self.rect.y + offset_y))
        
