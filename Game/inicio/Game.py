import pygame

from Player.Player import Player
from Chao.Chao import Chao

player = Player(50, 50)
Poss_chao = [
    Chao(0, 500, 50, 8000),
    Chao(0, 300, 50, 200),
    Chao(500, 300, 50, 200),
]
fps = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game")
    fpsClock = pygame.time.Clock()

    # Dimensões da tela
    screen_width, screen_height = screen.get_size()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Mover o jogador
        player.mover()

        # Cálculo do deslocamento (offset) para centralizar a câmera no jogador
        offset_x = screen_width // 2 - player.rect.centerx
        offset_y = screen_height // 2 - player.rect.centery

        # Limpar a tela
        screen.fill((0, 0, 0))

        # Desenhar o cenário com o deslocamento da câmera
        for chao in Poss_chao:
            chao.draw(screen, offset_x, offset_y)

        # Desenhar o jogador com o deslocamento da câmera
        player.draw(screen, offset_x, offset_y)

        for chao in Poss_chao:
            if player.colide(chao):
                # Verifica colisão pela parte inferior do jogador
                if player.rect.bottom > chao.rect.top and player.velocidade_y > 0:
                    player.rect.bottom = chao.rect.top
                    player.velocidade_y = 0
                    player.resetar_pulos()  # Chama o método para resetar os pulos
                # Verifica colisão pela parte superior do jogador
                elif player.rect.top < chao.rect.bottom and player.velocidade_y < 0:
                    player.rect.top = chao.rect.bottom
                    player.velocidade_y = 0
                # Verifica colisão pela lateral direita do jogador
                elif player.rect.right > chao.rect.left and player.rect.left < chao.rect.right:
                    if player.velocidade_x > 0:  # Movimento para a direita
                        player.rect.right = chao.rect.left
                        player.velocidade_x = 0
                # Verifica colisão pela lateral esquerda do jogador
                elif player.rect.left < chao.rect.right and player.rect.right > chao.rect.left:
                    if player.velocidade_x < 0:  # Movimento para a esquerda
                        player.rect.left = chao.rect.right
                        player.velocidade_x = 0

        # Controlar o FPS
        fpsClock.tick(fps)
        
        pygame.display.update()


if __name__ == "__main__":
    main()
