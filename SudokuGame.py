import pygame

#Initialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Logo
pygame.display.set_caption("Sudoku Solver")

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False