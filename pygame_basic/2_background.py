import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기
screen_width = 480  # 가로
screan_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screan_height))

# 화면 타이틀
pygame.display.set_caption('SB Game')

# 배경 이미지

background = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/Golem.gif')

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창 닫기 버튼이 눌림
            running = False

    screen.fill((180,180,200)) # 배경 그리기

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
