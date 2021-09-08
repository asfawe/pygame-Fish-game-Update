import pygame as pg

pg.init()

화면가로길이 = 600
화면세로길이 = 800

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.display.set_caption('생선잡기_게임')

배경이미지 = pg.image.load('img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0, 0))

물고기1 = pg.image.load('img/물고기1.png')
물고기1 = pg.transform.scale(물고기1, (64, 64))
화면.blit(물고기1, (100, 400))

물고기2 = pg.image.load('img/물고기2.png')
물고기2 = pg.transform.scale(물고기2, (64, 64))
화면.blit(물고기2, (200, 300))

스코어바 = pg.image.load('img/스코어바.png')
스코어바 = pg.transform.scale(스코어바, (250, 74))


시간바 = pg.image.load('img/시간바.png')
시간바 = pg.transform.scale(시간바, (200, 55))
#             1          2            3        4       5
pg.draw.line(화면, (255,255,255), (200,200),(300,200), 3) # 1. 어디에 그릴지 2. 색깔 3. 스타트포지션 4. 엔드표지션 x 자표는 300, y 자표는 200, 5. 윗스는 3

pg.display.update()

폰트 = pg.font.SysFont('hy얕은샘물m', 30, True)
시작시간 = pg.time.get_ticks()
잡은물고기 = 0

while True:
    경과시간 = round((pg.time.get_ticks() - 시작시간) / 1000, 1) # round를 이용해서 소수점 1첫번째 자리까지  소수점을 나타내야하기 때문에 나눈기 1000을 한다. 
    화면.blit(시간바, (0, 10))
    화면.blit(스코어바, (350, 2))

    시간 = 폰트.render(f'{경과시간} 초', True, (0,0,0)) # render은 텍스트를 출력할수 있게 하는것이다.
    화면.blit(시간, (60, 28))

    물고기점수 = 폰트.render(f'{잡은물고기} 마리', True, (0,0,0))
    화면.blit(물고기점수, (450, 28))

    pg.display.update() # 화면을 건들면 무조건 pg.display.update()를 해줘야 한다.

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()