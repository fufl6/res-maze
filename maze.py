from pygame import *
window = display.set_mode((700,500))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
back = transform.scale(image.load('background.jpg'), (700,500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 370:
            self.direction = 'right'
        if self.rect.x >= 671:
            self.direction = 'left'
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
sp1 = Player('or.png', 200, 100, 10)
sp2 = Enemy('jk.png', 150, 150,10)
sp3 = GameSprite('1488.png',550,300, 0)



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back,(0,0))
    sp1.update()
    sp2.update()
    sp1.reset()
    sp2.reset()
    sp3.reset()
    display.update()
    clock.tick(60)

    