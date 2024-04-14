from pygame import *


#створи вікно гри
window = display.set_mode((700,500))
FPS = 60
clock = time.Clock()
#задай фон сцени
bg = image.load("background.png")
bg = transform.scale(bg, (700,500))
pl1 = image.load("sprite1.png")
pl1 = transform.scale(pl1, (100,70))
pl2 = image.load("sprite2.png")
pl2 = transform.scale(pl2, (100,70))
#створи 2 спрайти та розмісти їх на сцені
class Player(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        self.image = transform.scale(sprite_img, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player_1 = Player(pl1, 70,70,150,260)
player_2 = Player(pl2, 70,70,400,260)

#оброби подію «клік за кнопкою "Закрити вікно"»
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(bg, (0,0))
    window.blit(player_1.image, player_1.rect)
    window.blit(player_2.image, player_2.rect)

    window.blit(pl2, (400,260))
    display.update()
    clock.tick(FPS)
