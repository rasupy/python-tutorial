import pygame
import sys

WHITE = (255, 255, 255)  # 色の定義: 白
BLACK = (0, 0, 0)  # 色の定義: 黒


def main():
    pygame.init()  # pygameモジュールの初期化
    pygame.display.set_caption("初めてのpygame")  # ウィンドウに表示されるタイトル
    screen = pygame.display.set_mode((800, 600))  # 描画面を初期化
    clock = pygame.time.Clock()  # clockオブジェクトを作成
    font = pygame.font.Font(None, 80)  # フォントオブジェクトを作成
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        txt = font.render(str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt, [300, 200])
        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
