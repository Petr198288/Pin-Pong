from pygame import *
from random import randint
from time import time as timer
#подгружаем отдельно функции для работы со шрифт


#фоновая музыка

#нам нужны такие картинки:
img_back = "плоская-таблица-pong-pin-взгляд-сверху-поля-пингпонга-с-линией-вектором-118501901.webp" #фон игры
img_hero = "racket.png" #герой
img_enemy = "tenis_ball.png" #враг


#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
 
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
 
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

gun_clip = 5
#класс главного игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


#класс спрайта-врага
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
    #движение врага
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > 450:
            self.speed_y *= -1

        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y < 50:
            self.speed_y *= -1
        
 



#создаём окошко
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
rocket1 = Player(img_hero, 5, win_height - 495, 40, 120, 10)
rocket2 = Player(img_hero, 650, win_height - 495, 40, 120, 10)
ball = Enemy(img_enemy, 325, win_height - 275, 50, 50, 2)
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
game = True #флаг сбрасывается кнопкой закрытия окна
clock = time.Clock()
Reload = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
while game:
    
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
        ball.speed_x *= -1
        #событие нажатия на пробел - спрайт стреляет


    
    window.blit(background, (0,0))
    rocket1.reset()
    rocket2.reset()
    ball.reset()
    rocket1.update_l()
    rocket2.update_r()
    ball.update()

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200)) 
        game = False

    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200)) 
        game = False

    clock.tick(40)
    display.update()