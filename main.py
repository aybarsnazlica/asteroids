import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for player in updatable:
            player.update(dt)

        for player in drawable:
            player.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60)  # limits FPS to 60
        dt /= 1000
        player.update(dt)

    pygame.quit()


if __name__ == "__main__":
    main()
