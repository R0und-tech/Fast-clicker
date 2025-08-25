from random import randint

import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill_func(self):
        return self.fill_color, self.rect

    def outline(self, frame_color, thickness):
        return frame_color, self.rect, thickness


class Label(Area):
    def set_text(self, text, font_size, font_color):
        self.image = pygame.font.SysFont("GothicG", font_size).render(text, True, font_color)

    def draw_all(self, window, rect_func, frame_color, thickness, shift_x, shift_y):
        rect_func(window, *self.fill_func())
        rect_func(window, *self.outline(frame_color, thickness))
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_without_text(self, window, rect_func, frame_color, thickness):
        rect_func(window, *self.fill_func())
        rect_func(window, *self.outline(frame_color, thickness))


window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
cards = []
x = 36
for _ in range(4):
    card = Label(x, 170, 90, 150, (255, 255, 0))
    x+= 110
    card.set_text("Click", 26, BLACK)
    cards.append(card)
run = True
wait = 0
while run:
    if wait == 0:
        wait = 20
        num = randint(0, 3)
    wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for num_card, card in enumerate(cards):
                if card.rect.collidepoint(x, y):
                    if num_card == num:
                        card.fill_color = GREEN
                    else:
                        card.fill_color = RED
                else:
                    card.fill_color = YELLOW

    window.fill((155,155,155))
    for index, card in enumerate(cards):
        if index == num:
            card.draw_all(window, pygame.draw.rect, (0, 0, 100), 10, 13, 62)
        else:
            card.draw_without_text(window, pygame.draw.rect, (0, 0, 100), 10)
    pygame.display.update()
    clock.tick(40)
