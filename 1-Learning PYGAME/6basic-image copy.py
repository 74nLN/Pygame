import pygame
# ประกาศใช้งาน
pygame.init()
# หัวข้อเกม
pygame.display.set_caption("KAK Game")
# กำหนดสี RGB
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# ขนาดหน้าจอเกม
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

# แสดงหน้าจอเกม
screen.fill(WHITE)

# load image 
paddle = pygame.image.load("Image/paddle.png")


running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(paddle,(100,100))           #ADD
    pygame.display.update()
pygame.quit()