import pygame
pygame.init()


class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill_func(self):
        return (self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        return (frame_color, self.rect, thickness)

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
card = Area(70, 170, 70, 100, (255, 255, 0))

x = 70
for _ in range(4):
    card = Area(x, 170, 70, 100, (255, 255, 0))
    x+= 100
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((155,155,155))
    pygame.draw.rect(window, *card.fill_func())
    pygame.draw.rect(window, *card.outline((255, 0, 0), 5))
    pygame.display.update()
    clock.tick(40)
