import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("가위바위보")

# 색상 설정
WHITE = (255, 255, 255)

# 공 설정
class Ball:
    def __init__(self, x, y, dx, dy, radius, image):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.image = image

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        SCREEN.blit(self.image, (self.x - self.radius, self.y - self.radius))

# 이미지 경로
scissor_image_path = "scissors.png"
rock_image_path = "rock.png"
paper_image_path = "paper.png"

# 이미지 생성
scissor_image = pygame.image.load(scissor_image_path)
scissor_image = pygame.transform.scale(scissor_image, (30, 30))
rock_image = pygame.image.load(rock_image_path)
rock_image = pygame.transform.scale(rock_image, (30, 30))
paper_image = pygame.image.load(paper_image_path)
paper_image = pygame.transform.scale(paper_image, (30, 30))

images = [scissor_image, rock_image, paper_image]
balls = []

# 10개씩의 공 생성
for image in images:
    for _ in range(10):
        balls.append(Ball(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.randint(-3, 3), random.randint(-3, 3), 30, image))


# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면 지우기
    SCREEN.fill(WHITE)

    # 공 그리기 및 이동
    for ball in balls:
        ball.move()
        ball.draw()

        # 벽 충돌 체크
        if ball.x - ball.radius < 0 or ball.x + ball.radius > WIDTH:
            ball.dx *= -1
        if ball.y - ball.radius < 0 or ball.y + ball.radius > HEIGHT:
            ball.dy *= -1

    # 공끼리 부딪혔을 때 이미지 변경
    for ball1 in balls:
        for ball2 in balls:
            if ball1 != ball2:
                distance = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
                if distance < ball1.radius * 2:
                    if ball1.image == scissor_image and ball2.image == paper_image:
                        ball2.image = scissor_image
                    elif ball1.image == rock_image and ball2.image == scissor_image:
                        ball2.image = rock_image
                    elif ball1.image == paper_image and ball2.image == rock_image:
                        ball2.image = paper_image
                    
    # 화면 업데이트
    pygame.display.update()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
