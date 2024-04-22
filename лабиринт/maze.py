#u�Z
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y)
        self.speed = player_speed
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 200:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        keys = key.get_pressed()
        if keys[K_w] and self.speed <= 40:
            self.speed += 1
        if keys[K_s] and self.speed >= 3:
            self.speed -= 1
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height ):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
hero = Player("hero.png", 5, 425, 10)
cyborg = Enemy("cyborg.png", 200, 200, 2)
reward = GameSprite("treasure.png", 300, 300)
wall1 = Wall(0, 255, 0, 10, 10, 10, 400)
wall2 = Wall(0, 255, 0, 180, 180, 10, 350)
wall3 = Wall(0, 255, 0, 15, 260, 80, 10)
wall4 = Wall(0, 255, 0, 15, 10, 700, 10)
wall5 = Wall(0, 255, 0, 180, 180, 300, 10)
wall6 = Wall(0, 255, 0, 475, 300, 10, 400)


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (700, 500))
game = True
finish = False
FPS = 60
clock = time.Clock()
font.init()
font = font.SysFont("Arial", 70)
win = font.render("YOU WIN", True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        hero.reset()
        cyborg.reset()
        reward.reset()
        hero.update()
        cyborg.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        if sprite.collide_rect(hero, reward):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(hero, cyborg):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
        if sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
        if sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
    clock.tick(FPS)
    display.update()