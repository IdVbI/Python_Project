import pygame
######################################################################################################

# 기본 초기화
pygame.init() 

# 화면 크기
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Game Name')

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트)

# 배경 이미지


# 케릭터 불러오기

# 이동할 좌표

# 이동속도

# 적

# 폰트 정의

# 촐 플레이 타임

# 시작 시간

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)
    # print('fps :'+str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)

    # 3. 게임 케릭터 위치 정의

    # 가로 경계

    # 세로 경계

    # 4. 출돌 처리

    # 충동 처리

    # 충돌 체크

    # 5. 화면에 그리기

    # 타이머

    # 시간, True, 글자 색상 

    pygame.display.update() # 게임화면 다시 그리기

# 잠시 대기
pygame.time.delay(1000) # 1초 대기후 종료

# pygame 종료
pygame.quit()
