import sys, pygame
from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (35, 125, 240)

fish_image = pygame.image.load("fish.png")
fish_imgage = pygame.transform.smoothscale(fish_image(80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width//2, height//2)

def main():
	while True:
		clock.tick(60)
		screen.fill(color)
		screen.blit(fish_image, fish_rect)
		pygame.display.flip()



if __name__ == '__main__ ':
	main()