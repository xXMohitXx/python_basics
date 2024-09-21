import pygame
import sys
import random

pygame.init()

# Screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Constants
gravity = 0.5
bird_flap_velocity = -10
pipe_velocity = 5
pipe_gap = 150

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Font
font = pygame.font.SysFont(None, 48)

# Bird class
class Bird:
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.width = 50
        self.height = 50
        self.velocity = 0

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))

    def update(self):
        self.velocity += gravity
        self.y += self.velocity

        # Prevent the bird from going off-screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height
            self.velocity = 0

    def flap(self):
        self.velocity = bird_flap_velocity

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 50
        self.height = random.randint(100, 300)
        self.gap = pipe_gap

    def draw(self):
        pygame.draw.rect(screen, green, (self.x, 0, self.width, self.height))
        pygame.draw.rect(screen, green, (self.x, self.height + self.gap, self.width, screen_height - self.height - self.gap))

    def update(self):
        self.x -= pipe_velocity

    def is_off_screen(self):
        return self.x + self.width < 0

    def collides_with(self, bird):
        if bird.x < self.x + self.width and bird.x + bird.width > self.x:
            if bird.y < self.height or bird.y + bird.height > self.height + self.gap:
                return True
        return False

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.callback = callback

    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.width, self.height))
        text_surf = font.render(self.text, True, white)
        screen.blit(text_surf, (self.x + (self.width - text_surf.get_width()) // 2, self.y + (self.height - text_surf.get_height()) // 2))

    def is_clicked(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

# Main game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe(700), Pipe(1000)]
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()

            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if retry_button.is_clicked(pygame.mouse.get_pos()):
                    game_loop()

        if not game_over:
            bird.update()

            for pipe in pipes:
                pipe.update()
                if pipe.collides_with(bird):
                    game_over = True

            # Check if bird passed through the pipe
            for pipe in pipes:
                if pipe.x + pipe.width < bird.x and not hasattr(pipe, 'scored'):
                    score += 1
                    pipe.scored = True

            # Remove off-screen pipes and add new ones
            if pipes[0].is_off_screen():
                pipes.pop(0)
                pipes.append(Pipe(screen_width))

        # Drawing everything
        screen.fill(black)
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        # Draw score
        score_text = font.render(str(score), True, white)
        screen.blit(score_text, (screen_width // 2, 20))

        # Draw game over and retry button
        if game_over:
            game_over_text = font.render("Game Over", True, white)
            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
            retry_button.draw()

        pygame.display.update()
        clock.tick(60)

def main_menu():
    start_button = Button("Start", screen_width // 2 - 100, screen_height // 2 - 25, 200, 50, game_loop)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(pygame.mouse.get_pos()):
                    start_button.callback()

        # Draw menu
        screen.fill(black)
        start_button.draw()
        pygame.display.update()

retry_button = Button("Retry", screen_width // 2 - 100, screen_height // 2 + 50, 200, 50, game_loop)
main_menu()
