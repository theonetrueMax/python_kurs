import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 1000, 1000
TILE = 50
GRID_W = WIDTH // TILE
GRID_H = HEIGHT // TILE

FPS = 10
GAME_TIME = 200
FRUIT_LIFETIME = 35


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 20)

def load_image(path):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (TILE, TILE))

IMG_HEAD = load_image("Zestaw 9/assets/head.png")
IMG_BODY = load_image("Zestaw 9/assets/body.png")
IMG_FRUIT_GOOD = load_image("Zestaw 9/assets/fruit_good.png")
IMG_FRUIT_BAD = load_image("Zestaw 9/assets/fruit_bad.png")

snake = [(GRID_W//2, GRID_H//2)]
direction = (1, 0)
score = 0

fruit_pos = None
fruit_type = None
fruit_age = 0
running=True
def spawn_fruit():
    global fruit_pos, fruit_type, fruit_age
    fruit_pos = (random.randint(0, GRID_W-1), random.randint(0, GRID_H-1))
    fruit_type = random.choice(["good", "bad"])
    fruit_age = 0

def rotate_image_for_direction(image, direction):
    dx, dy = direction
    if dx == 1 and dy == 0: 
        angle = 90
    elif dx == -1 and dy == 0: 
        angle = -90
    elif dx == 0 and dy == -1:  
        angle = 180
    elif dx == 0 and dy == 1:   
        angle = 0
    else:
        angle = 0

    return pygame.transform.rotate(image, angle)

def segment_direction(prev, current):
    px, py = prev
    cx, cy = current
    return (cx - px, cy - py)

UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

turn_right = {
    UP:    RIGHT,
    RIGHT: DOWN,
    DOWN:  LEFT,
    LEFT:  UP,
}

def turn_90_right(direction):
    return turn_right[direction]

def move_snake():
    x, y = snake[0]
    dx, dy = direction

    new_head = ((x + dx) % GRID_W, (y + dy) % GRID_H)

    # ruch wstecz → koniec
    if len(snake) > 1 and new_head == snake[1]:
        return False

    snake.insert(0, new_head)

    global score, fruit_pos, fruit_type,running

    if new_head == fruit_pos:
        if fruit_type == "good":
            score += 1
      
        else:
            score -= 1
            if len(snake) > 2:
                snake.pop()
                snake.pop()
            else:
                snake.pop()
                running = False
        fruit_pos = None
    else:
        snake.pop()

    return True


start_ticks = pygame.time.get_ticks()


while running:
    clock.tick(FPS)

    elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
    if elapsed >= GAME_TIME:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            dx, dy = direction
            if event.key == pygame.K_UP and dy != 1:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and dy != -1:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and dx != 1:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and dx != -1:
                direction = (1, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            direction = turn_90_right(direction)

    if fruit_pos is None:
        spawn_fruit()
    else:
        fruit_age += 1
        if fruit_age > FRUIT_LIFETIME:
            fruit_pos = None

    alive = move_snake()
    if not alive:
        running = False

    screen.fill((0, 0, 70))

    if fruit_pos:
        x, y = fruit_pos
        img = IMG_FRUIT_GOOD if fruit_type == "good" else IMG_FRUIT_BAD
        screen.blit(img, (x*TILE, y*TILE))

    for i, (x, y) in enumerate(snake):
        if i == 0:
            img = rotate_image_for_direction(IMG_HEAD, direction)
        else:
            prev = snake[i-1]
            dir_seg = segment_direction(prev, (x, y))
            img = rotate_image_for_direction(IMG_BODY, dir_seg)

        screen.blit(img, (x*TILE, y*TILE))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
print("GAME OVER. SCORE =", score)