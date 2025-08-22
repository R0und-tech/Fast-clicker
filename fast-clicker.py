import pygame
pygame.init()

BLACK = (0, 0, 0)

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
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
cards = []
x = 36
for _ in range(4):
    card = Label(x, 170, 90, 150, (255, 255, 0))
    x+= 100
    card.set_text("Click", 26, BLACK)
    cards.append(card)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((155,155,155))
    for card in cards:
        card.draw_all(window, pygame.draw.rect, (0, 0, 100), 10, 13, 62)
    pygame.display.update()
    clock.tick(40)
