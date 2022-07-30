import sys, pygame
from turtle import forward
pygame.init()



clock = pygame.time.Clock()

right = 0
down = 0

size = width, height = 1000, 1000
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("cow_background.jpg")

ball = pygame.image.load("intro_ball.gif")

user_location = 0

ballrect = ball.get_rect()

players = []


while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

#-----------------------Listen for movement to start-------------------------------

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                right = -2
            if event.key == pygame.K_RIGHT:
                print("right")
                right = 2
            if event.key == pygame.K_UP:
                print("up")
                down = -2
            if event.key == pygame.K_DOWN:
                print("down")
                down = 2
            if event.key == pygame.K_SPACE:
                print("Space Pressed")
                bulletrect = bullet.get_rect()
                bulletrect.x = user_location[0]
                bulletrect.y = user_location[1]
                bulletrect.move([right*2, down*2])
                screen.blit(bullet, bulletrect)
#-------------------------Listen for movement to stop--------------------------------

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("left up")
                right = 0
            if event.key == pygame.K_RIGHT:
                print("right up")
                right = 0
            if event.key == pygame.K_UP:
                print("up up")
                down = 0
            if event.key == pygame.K_DOWN:
                print("down up")
                down = 0
        


        
#----------------------------Move the ball in the current direction-=--------------------------------

    ballrect = ballrect.move([right, down])
    print(right)

    user_location = ballrect.topleft

#----------------------------




#----------------------------Rendering other players postions----------------------------------------
    # screen.fill("black")

    screen.blit(background, (0,0))

    for player in players:
        player_ballrect = ball.get_rect()
        player_ballrect.x = player["right"]
        player_ballrect.y = player["down"]

        print(player)
        screen.blit(ball, player_ballrect)

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    
    screen.blit(ball, ballrect)
    pygame.display.flip()