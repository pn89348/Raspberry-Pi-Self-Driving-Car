import pygame

running = True

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 70))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

def process_event(event=""):
    if event.type == pygame.QUIT:
        global running
        running = False

def pygame_setup():
    global WIDTH
    global HEIGHT
    global FPS
    global screen
    global clock
    global all_sprites
    global car

    WIDTH = 480
    HEIGHT = 300
    FPS = 30

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Raspberry Pi Car")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    car = Car()
    all_sprites.add(car)

pygame_setup()

# Loop
while running:
    # Timing
    clock.tick(FPS)
    # Input
    for event in pygame.event.get():
        process_event(event)
    # Update
    all_sprites.update()

    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
