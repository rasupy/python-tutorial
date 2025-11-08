import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("初めてのPygame 画像表示")

    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()

    img_bg = pygame.image.load("../py_samples/Chapter10/pg_bg.png")
    img_chara = [
        pygame.image.load("../py_samples/Chapter10/pg_chara0.png"),
        pygame.image.load("../py_samples/Chapter10/pg_chara1.png"),
    ]
    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))

        x = tmr % 160
        for i in range(5):
            screen.blit(img_bg, [i * 160 - x, 0])
            screen.blit(img_chara[tmr % 2], [224, 160])
            pygame.display.update()
            clock.tick(5)


if __name__ == "__main__":
    main()
