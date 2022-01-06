import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기
screen_width = 480  # 가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('SB Game')

# FPS
clock = pygame.time.Clock()

# 배경 이미지

background = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/Golem.gif')

# 케릭터 불러오기

character = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/RED_SLIME.gif')
character_size = character.get_rect().size  #   이미지 크기
character_width = character_size[0] # 가로 크기
character_height = character_size[1] # 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

character_speed = 1

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)
    # print('fps :'+str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창 닫기 버튼이 눌림
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.fill((180,180,200)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
