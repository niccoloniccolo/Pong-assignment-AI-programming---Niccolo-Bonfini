# Import the pygame module
import pygame

# Define the Paddle class, which inherits from pygame.sprite.Sprite
class Paddle(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()  # Call the constructor of the parent class (pygame.sprite.Sprite)

        # Create a surface for the paddle image
        self.image = pygame.Surface((10, 100))
        self.image.fill((255, 255, 255))  # Fill the surface with white color

        # Get the rectangular area of the image
        self.rect = self.image.get_rect()

        # Set the initial position of the paddle
        self.rect.center = (x, y)

        # Initialize the speed of the paddle
        self.speed = 0

    # Method to move the paddle
    def move(self):
        self.rect.y += self.speed  # Move the paddle vertically based on its speed

        # Ensure the paddle stays within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600