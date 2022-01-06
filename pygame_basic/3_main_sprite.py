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

# 케릭터 불러오기

character = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/RED_SLIME.gif')
character_size = character.get_rect().size  #   이미지 크기
character_wigth = character_size[0] # 가로 크기
character_height = character_size[1] # 세로 크기
character_x_pos = (screen_width / 2) - (character_wigth / 2)
character_y_pos = screan_height - character_height
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창 닫기 버튼이 눌림
            running = False

    screen.fill((180,180,200)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
