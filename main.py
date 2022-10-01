from math import pi
import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 700, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
BLUE = 0, 0, 255
FONT = pygame.font.SysFont("JetBrains Mono", 25)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PI Approximation")
center = 350, 300
radius = 200
square = pygame.Rect(
    center[0] - radius,
    center[1] - radius,
    radius * 2,
    radius * 2
)
start = False
points = 0
circle_points = 0

def draw():
    global points, circle_points

    approximation = 4 * (circle_points/points) if points else 0
    pi_text = FONT.render(f"~π: {approximation}", True, WHITE)
    off_by = abs((approximation - pi)/pi) * 100
    off_by_text = FONT.render(f"Off By %: {off_by}", True, WHITE)

    update_rect = pygame.Rect(
        0,
        0,
        700,
        pi_text.get_height() + off_by_text.get_height()
    )
    window.fill(BLACK, update_rect)
    window.blit(pi_text, (700 - pi_text.get_width(), 0))
    window.blit(off_by_text, (700 - off_by_text.get_width(), pi_text.get_height()))

    if start:
        for _ in range(100):
            x = randint(center[0] - radius, center[0] + radius)
            y = randint(center[1] - radius, center[1] + radius)
            points += 1

            dist = (x - center[0]) ** 2 + (y - center[1]) ** 2
            in_circle = dist <= radius ** 2
            if in_circle:
                circle_points += 1
            
            pygame.draw.circle(
                window, GREEN if in_circle else BLUE, (x, y), 1)

    pygame.draw.circle(window, WHITE, center, radius, 2)
    pygame.draw.rect(window, WHITE, square, 2)


def main():
    global start

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start

        draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
