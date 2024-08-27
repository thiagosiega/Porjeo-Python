import pygame

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def update(self, target):
        target_rect = target.get_rect()
        self.x = -(target_rect.x + target_rect.width / 2 - self.width / 2)
        self.y = -(target_rect.y + target_rect.height / 2 - self.height / 2)