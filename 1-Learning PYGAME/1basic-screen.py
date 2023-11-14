import pygame
# ประกาศใช้งาน
pygame.init()
# หัวข้อเกม
pygame.display.set_caption("KAK Game")
# ขนาดหน้าจอเกม
SCREEN_W = 800
SCREEN_H = 600
pygame.display.set_mode((SCREEN_W,SCREEN_H))
# แสดงหน้าจอเกม
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()