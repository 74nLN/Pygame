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
# Show ALL FONT IN TERMINAL
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)

#Custom font
custom_font = pygame.font.Font("Font/Coiny.ttf",20)
title_text = custom_font.render("Hello Pygame",True,RED)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(title_text,(80,100))            #ADD   
    pygame.display.update()
pygame.quit()