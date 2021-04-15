import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_up_right = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляет атрибут х, а не rect.
        if self.moving_up_right and self.rect.right < self.screen_rect.right and self.rect.y > 0:
            self.x += self.settings.ship_speed
            self.y -= self.settings.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            # Движение корабля влево до границы экрана
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.y > 0:
            # Движение корабля ввкрх до границы экрана
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            # Обновление атрибута rect на основании rect.x и rect.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
