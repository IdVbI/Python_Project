import random
import pygame
######################################################################################################

# 기본 초기화
pygame.init() 

# 화면 크기
screen_width = 900  # 가로
screen_height = 800 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Falling Monster')

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트)

# 배경 이미지

sky = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/SKY.png')
ground = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/Ground.png')


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

# 이동속도
character_speed = 1

# 박쥐
enemy = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/Mini_Devil.gif')
enemy_size = enemy.get_rect().size  #   이미지 크기
enemy_width = enemy_size[0] # 가로 크기
enemy_height = enemy_size[1] # 세로 크기
enemy_x_pos = random.randint(0, screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 5

# 골렘
enemy2 = pygame.image.load('/Users/limseongbin/Downloads/pyhton/pygame_basic/PISXEL/Golem.gif')
enemy2_size = enemy2.get_rect().size  #   이미지 크기
enemy2_width = enemy2_size[0] # 가로 크기
enemy2_height = enemy2_size[1] # 세로 크기
enemy2_x_pos = random.randint(0, screen_width-enemy2_width)
enemy2_y_pos = 0
enemy2_speed = 8


# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 촐 플레이 타임
total_time = 20

# 시작 시간
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)
    # print('fps :'+str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)
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

    # 3. 게임 케릭터 위치 정의
    character_x_pos += to_x * dt


    # 가로 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 박쥐 낙하
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = -100
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
    
    enemy2_y_pos += enemy2_speed

    if enemy2_y_pos > screen_height:
        enemy2_y_pos = -100
        enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
    


    # 4. 출돌 처리

    # 충동 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos


    # 충돌 체크
    if character_rect.colliderect(enemy_rect) or character_rect.colliderect(enemy2_rect):
        game_result = 'You die'
        running = False

    # 5. 화면에 그리기

    screen.blit(sky,(0,0)) # 배경 그리기
    screen.blit(ground,(0,0)) # 배경 그리기


    screen.blit(character, (character_x_pos, character_y_pos)) # 케릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos)) # 적 그리기


    # 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 초 단위로 표시

    # 시간, True, 글자 색상 
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0,0,0))
    if total_time - elapsed_time <= 0:
        game_result = 'Victory'
        running = False   

    screen.blit(timer, (10,10))

    pygame.display.update() # 게임화면 다시 그리기

msg = game_font.render(game_result,True, (250, 80, 80))
msg_rect = msg.get_rect(center=(int(screen_width / 2),int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 잠시 대기
pygame.time.delay(1000) # 1초 대기후 종료

# pygame 종료
pygame.quit()
