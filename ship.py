import pygame

class Ship():
	"""Инициализирует корабль и задает его начальную позицию"""
	def __init__(self, screen):
		self.screen = screen

		#Загрузка изображения корабля и получение прямоугольника
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Каждый новый корабль появляется у нижнкго края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect)