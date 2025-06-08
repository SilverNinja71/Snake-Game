import pygame

pygame.init()
screen = pygame.display.set_mode((720,720))
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill("green")
  pygame.display.update()

pygame.quit()
exit(0)
