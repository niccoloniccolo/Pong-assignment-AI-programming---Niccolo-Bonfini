# Import the pygame module
import pygame

# Define the Ball class, which inherits from pygame.sprite.Sprite
class Ball(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()  # Call the constructor of the parent class (pygame.sprite.Sprite)

        # Create a surface for the ball image
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))  # Fill the surface with white color

        # Get the rectangular area of the image
        self.rect = self.image.get_rect()

        # Set the initial position of the ball
        self.rect.center = (400, 300)

        # Set the initial speeds of the ball in the x and y directions
        self.speed_x = 5
        self.speed_y = 5

    # Method to move the ball
    def move(self):
        # Move the ball horizontally and vertically based on its speeds
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # If the ball reaches the top or bottom of the screen, reverse its vertical speed to bounce it
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

    # Method to reset the ball to its initial position and speed
    def reset(self):
        self.rect.center = (400, 300)  # Reset the position of the ball
        self.speed_x = 5  # Reset the horizontal speed of the ball
        self.speed_y = 5  # Reset the vertical speed of the ball