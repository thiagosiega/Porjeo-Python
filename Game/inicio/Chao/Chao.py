import pygame
import random
class Chao:
    def __init__(self, x, y,altura,largura):
        self.altura = altura
        self.largura = largura
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.largura, self.altura))
        self.cor = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def colide(self, player):
        return self.rect.colliderect(player.rect)
    
    def draw(self, screen, offset_x, offset_y):
        self.image.fill(self.cor)
        screen.blit(self.image, (self.rect.x + offset_x, self.rect.y + offset_y))