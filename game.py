# Import necessary modules
import pygame
import sys
from paddle import Paddle
from ball import Ball


# Define the Game class
class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up the game window
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pong")

        # Set up the game clock
        self.clock = pygame.time.Clock()

        # Create sprites (paddles and ball)
        self.player_paddle = Paddle(20, 300)
        self.opponent_paddle = Paddle(780, 300)
        self.ball = Ball()

        # Create a sprite group to hold all sprites
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player_paddle, self.opponent_paddle, self.ball)

    # Method to handle events such as key presses
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player_paddle.speed = -5
                elif event.key == pygame.K_s:
                    self.player_paddle.speed = 5
                elif event.key == pygame.K_UP:
                    self.opponent_paddle.speed = -5
                elif event.key == pygame.K_DOWN:
                    self.opponent_paddle.speed = 5
                elif event.key == pygame.K_SPACE:
                    self.ball.reset()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.player_paddle.speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.opponent_paddle.speed = 0
        return True

    # Method to update the game state
    def update(self):
        # Move paddles and ball
        self.player_paddle.move()
        self.opponent_paddle.move()
        self.ball.move()

        # Handle collisions between ball and paddles
        if pygame.sprite.collide_rect(self.ball, self.player_paddle) or pygame.sprite.collide_rect(self.ball,
                                                                                                   self.opponent_paddle):
            self.ball.speed_x *= -1

        # Reset ball if it goes out of bounds
        if self.ball.rect.left <= 0 or self.ball.rect.right >= 800:
            self.ball.reset()

    # Method to draw the game elements on the screen
    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        self.all_sprites.draw(self.screen)  # Draw all sprites on the screen
        pygame.display.flip()  # Update the display

    # Method to run the game loop
    def run(self):
        running = True
        while running:
            running = self.handle_events()  # Handle events
            self.update()  # Update game state
            self.draw()  # Draw game elements
            self.clock.tick(60)  # Cap the frame rate to 60 FPS

        pygame.quit()  # Quit pygame
        sys.exit()  # Exit the program