import pygame
import gamebox
import math
import switch

WIDTH_WIN = 800
HEIGHT_WIN = 600
camera = gamebox.Camera(WIDTH_WIN, HEIGHT_WIN)

char = gamebox.from_image(400, HEIGHT_WIN - 50, 'mario.png')
char.size = 40,50
#I found a low res sprite sheet, I upscaled it properly and made mirror images of the sprites to use
sprite = gamebox.load_sprite_sheet('sprite_sheet.png',2,5)

#a bunch of default states to save time typing the same thing over and over
rest_right = sprite[0]
jump_right = sprite[4]
rest_left = sprite[5]
jump_left = sprite[9]
char.image = rest_right

aim = gamebox.from_color(char.left, char.center[1]-20, 'pink', 10,10)

highlight = gamebox.from_color(camera.center[0] + 125, camera.center[1] - 20, "yellow", 250, 5)

#initialize portals at origin
blue_portal = gamebox.from_color(0,0,'blue', 0,0)
orange_portal = gamebox.from_color(0,0,'orange',0,0)

#X is a portal wall
#O is a non-portal wall
#E is a portal wall with a coin above it
level ='''
X----------XXXXXXXXXX--X-------------------------------------------------------------------------------------
------------------------------------------------------------------------XXXXXX-------------------------------
-O------E---------------------------XXXXXX-----------------------------------XE--X---------------------------
-O------X--------------OOE-OOO------X----X---------------------------------------X---------------------------
-O------X---------------------------X----X------------------------------OOOOOOOOOO-----------------X----X----
-O------X---------------------------XEX--X---------------OOOO------------------------------------------------
-O------X------------------------------------------OOOOOOO----------X----------------------------------------
-O--------------------X---------------------------------------------X----------------------------X--------X--
-O--------------------X-------------------------------------E------XX--------------------E--------X------X---
-O--------------------X----------------------------OOOOOOOOOO--------------------------------------XXFFXX----
-O-O------------------X-----------------------OO---------X---------------------------------------------------
-O-O------------------X----------------------------------X---------------------------------------------------
-O-O------------------XEX--------------------------------XEXX------------------------------------------------
-O-O------------------X--------------------------------------------------------------------------------------
XXEXXXXXXXXXXXXXXXXXXXX--------XXXXEXXXXXXXXX-------------------XXXXX----------------------------------------
'''


yspeed = 0
xspeed = 20

#counters prevent constant stream of bullets when q or e are pressed
q_counter = 0
e_counter = 0

coin_count = 0
#this timer is for the count up timer
time = 0
clock = 0
#this timer is for sprite animations
sprite_timer = 0

blue_wall_side = 'top'
orange_wall_side = 'top'
#variable to keep track of what the last direction of movement was
movement = 'right'

bullets = []
wallsPortal = []
wallsNonPortal = []
wallFinal = []
coins = []

coin_counter = gamebox.from_text(WIDTH_WIN - 100, 50, str(coin_count) + ' coins', "Arial", 24, 'white')
timer = gamebox.from_text(WIDTH_WIN - 100, 100, str(time) + ' s', "Arial", 24, "white")


def levelBuild(level):
    level = level.splitlines()
    level = level[1:] #first line is technically '\n' but I left it there to make the string visualization look better 

    for line in range(len(level)):
        for elem in range(len(level[line])):
            #loop through every line and every elem in that line
            #add entities to appropriate lists depending on value in string
            if level[line][elem] == "X":
                #I got these colors from colorpicker.com- it has a really cool feature where it'll give you a matching set of colors!
                wallsPortal.append(gamebox.from_color((elem * 40) + 20,(line * 40) + 20, '#1a2c3d', 40, 40))
            if level[line][elem] == "O":
                wallsNonPortal.append(gamebox.from_color((elem * 40) + 20, (line * 40) + 20, 'white', 40, 40))
            if level[line][elem] == 'E':
                wallsPortal.append(gamebox.from_color((elem * 40) + 20, (line * 40) + 20, '#1a2c3d', 40, 40))
                coins.append(gamebox.from_color((elem * 40) + 20, (line * 40) - 20, 'yellow', 5, 5))
            if level[line][elem] == 'F':
                wallFinal.append(gamebox.from_color((elem * 40) + 20, (line * 40) + 20, 'red', 40, 40))
    #since the walls are actually made of smaller squares, sometimes the bullet will pass through the block and 'hit' an inside wall
    #so the portal gets oriented wrong and is inside the wall
    #it's super annoying and I tried fixing it for weeks but could never figure it out

levelBuild(level)

def angle(sprite,mousex, mousey):
    #finds angle between aim sprite and cursor
    #finds adjacent leg and opposite leg  of the right triangle made with hypotenuse vector between aim sprite and mouse cursor
    legAdj = sprite.center[0] - mousex
    legOpp = sprite.center[1] - mousey
    
    #prevents error when atan = 0
    try: 
        ang = math.atan(math.fabs(legOpp/legAdj))
    except ZeroDivisionError:
        ang = math.pi/2

    #adjusts the angle since game coords are in QIV of Cartesian and regular unit circle is reflected horizontally
    if sprite.center[0] > mousex and sprite.center[1] < mousey:
        ang = -1*ang - math.pi
    elif sprite.center[0] > mousex and sprite.center[1] > mousey:
        ang += math.pi
    elif sprite.center[0] < mousex and sprite.center[1] > mousey:
        ang = -1*ang
        
    return [ang, legAdj, legOpp]

def rotPoint(point, axis, ang):
    #code from http://archives.seul.org/pygame/users/Apr-2007/msg00151.html
    #I would have just used the idea and not taken the code directly, but this is a pretty elegant solution
    x, y = point[0] - axis[0], point[1] - axis[1]
    radius = math.sqrt(x*x + y*y)
    
    #this statement fixes a bug that makes the aim sprite become separated from the char sprite
    if radius >= 21 or radius <= 18:
        radius = 20
    #h and v are new coords for the sprite's center
    h = axis[0] + (radius * math.cos(ang))
    v = axis[1] + (radius * math.sin(ang))
    
    return h,v

def tick(keys):
    #bunch of variables
    global xspeed
    global yspeed
    global q_counter
    global e_counter
    global coin_count
    global clock
    global time
    global blue_wall_side
    global orange_wall_side
    global movement
    global sprite_timer
    
    #constant variables 
    BULLET_SPEED = 20
    PORTAL_HEIGHT = 60
    PORTAL_WIDTH = 10

    #ASCII codes for the 3 keys that move the character
    #119 w
    #100 d
    #97 a
    
    #points the character in the right direction when not moving
    if movement == 'right' and pygame.key.get_pressed()[100] == 0 and pygame.key.get_pressed()[119] == 0:
        char.image = rest_right
    elif movement == 'left' and pygame.key.get_pressed()[97] == 0 and pygame.key.get_pressed()[119] == 0:
        char.image = rest_left  

    #gravity 
    yspeed += 1.5
    char.y += yspeed

    #basically, the game coords are dependent on origin (top left) and are independent of where the camera is
    #but the mouse coords are dependent on top left of camera
    #so, when the camera moves to the right 50 units, the game pixel will be a different coord, but the mouse coord will be the same
    #so these two lines fix this problem and make the mouse coords dependent on the origin of the game and not the camera
    diffx = camera.center[0] - WIDTH_WIN/2
    diffy = camera.center[1] - HEIGHT_WIN/2

    mousex = pygame.mouse.get_pos()[0] + diffx #implements fix
    mousey = pygame.mouse.get_pos()[1] + diffy

    #left and right movement with appropriate sprite animation
    #lots of repetitive garbage cause there are two directions AND two types of walls to iterate through
    if pygame.K_d in keys and pygame.K_a not in keys:
        movement = 'right'
        char.x += xspeed
        for wall in wallsPortal:
            if char.bottom_touches(wall):
                sprite_timer += 1
                if sprite_timer % 9 == 0:
                    char.image = sprite[1]
                elif sprite_timer % 9 == 3:
                    char.image = sprite[2]
                elif sprite_timer % 9 == 6:
                    char.image = sprite[3]
        for wall in wallsNonPortal:
            if char.bottom_touches(wall):
                sprite_timer += 1
                if sprite_timer % 9 == 0:
                    char.image = sprite[1]
                elif sprite_timer % 9 == 3:
                    char.image = sprite[2]
                elif sprite_timer % 9 == 6:
                    char.image = sprite[3]
    if pygame.K_a in keys and pygame.K_d not in keys:
        movement = 'left'
        char.x -= xspeed
        for wall in wallsPortal:
            if char.bottom_touches(wall):
                sprite_timer += 1
                if sprite_timer % 9 == 0:
                    char.image = sprite[6]
                elif sprite_timer % 9 == 3:
                    char.image = sprite[7]
                elif sprite_timer % 9 == 6:
                    char.image = sprite[8]
        for wall in wallsNonPortal:
            if char.bottom_touches(wall):
                sprite_timer += 1
                if sprite_timer % 9 == 0:
                    char.image = sprite[6]
                elif sprite_timer % 9 == 3:
                    char.image = sprite[7]
                elif sprite_timer % 9 == 6:
                    char.image = sprite[8]
    
    #camera moves right when char moves past center of the screen
    if char.x >= camera.center[0]:
        camera.x += xspeed
    #camera moves left when char moves back past leftmost quarter of the screen
    if char.x <= camera.center[0] - WIDTH_WIN/4:
        camera.x -= xspeed
    #so, char is only in the second quarter of the screen- gives nice scrolling effect

    #allows char to collect coins
    if len(coins) > 0:
        for coin in coins:
            if char.touches(coin):
                #had bug where it would say 'coin not in coins' which was weird, but this fixes it
                if coin in coins:
                    #removes coin so char can only collect coin once
                    coins.remove(coin)
                coin_count += 1

    #both of these for loops allow the char to stand on both types of walls and not fall through them
    for wall in wallsPortal:
        if char.bottom_touches(wall):
            yspeed = 0
            if pygame.K_w in keys:
                yspeed -= 20
                if movement == 'right':
                    char.image = jump_right
                else:
                    char.image = jump_left
        if char.touches(wall):
            char.move_to_stop_overlapping(wall)

    for wall in wallsNonPortal:
        if char.bottom_touches(wall):
            yspeed = 0
            if pygame.K_w in keys:
                yspeed -= 20
                if movement == 'right':
                    char.image = jump_right
                else:
                    char.image = jump_left
        if char.touches(wall):
            char.move_to_stop_overlapping(wall)

    #reorients aim sprite based on position of mouse cursor
    aim_angle = angle(aim, mousex, mousey)
    #had visual bug when cursor was inside char- aim sprite spun wildly out of control
    #this statement prevents aim sprite from moving when cursor is inside the char
    if math.hypot(mousex - char.center[0], mousey - char.center[1]) > 20:
        aim.center = rotPoint(aim.center, char.center, aim_angle[0])

    #these statements are awful, I know
    #but it was the best way I could think of to make the char come out of the correct side of the portal
    #I really hate this, but it works so it's not that bad I suppose
    if char.touches(blue_portal):
        yspeed = 0
        #this statement prevents warping to origin when the other portal hasn't been placed
        #(remember that both portals are initialized at the origin)
        if orange_portal.x != 0 and orange_portal.y != 0:
            if orange_wall_side =='left':
                char.center = [orange_portal.right + 25, orange_portal.y]
            elif orange_wall_side == 'right':
                char.center = [orange_portal.left - 25, orange_portal.y]
            elif orange_wall_side == 'top':
                char.center = [orange_portal.x, orange_portal.bottom + 25]
            elif orange_wall_side == 'bottom':
                char.center = [orange_portal.x, orange_portal.top - 25]
                #adds a little yspeed boost so if both portals are on the ground, there's a nice yo-yo-ing effect
                if blue_wall_side == 'bottom':
                    yspeed -= 15
                    
    elif char.touches(orange_portal):
        yspeed = 0
        if blue_portal.x != 0 and blue_portal.y != 0:
            if blue_wall_side =='left':
                char.center = [blue_portal.right + 25, blue_portal.y]
            elif blue_wall_side == 'right':
                char.center = [blue_portal.left - 25, blue_portal.y]
            elif blue_wall_side == 'top':
                char.center = [blue_portal.x, blue_portal.bottom + 25]
            elif blue_wall_side == 'bottom':
                char.center = [blue_portal.x, blue_portal.top - 25]
                if orange_wall_side == 'bottom':
                    yspeed -= 15
    
    #only shoots once per key press, prevents stream of bullets whenever the key is tapped
    if pygame.K_q in keys:
        q_counter = 1
    if pygame.K_q not in keys and q_counter == 1:
        q_counter = 0
        bullets.append([gamebox.from_color(aim.center[0], aim.center[1], 'blue', 3, 3), aim_angle[1], aim_angle[2], 'blue'])
    if pygame.K_e in keys:
        e_counter = 1
    if pygame.K_e not in keys and e_counter == 1:
        e_counter = 0
        bullets.append([gamebox.from_color(aim.center[0], aim.center[1], 'orange', 3, 3), aim_angle[1], aim_angle[2], 'orange'])
    
    camera.clear('black')

    #draw everything
    for wall in wallsPortal:
        camera.draw(wall)
    for wall in wallsNonPortal:
        camera.draw(wall)
    for wall in wallFinal:
        camera.draw(wall)
    for coin in coins:
        camera.draw(coin)
    
    camera.draw(char)
    camera.draw(aim)
    
    for bullet in bullets:
        rad_sq = math.sqrt(bullet[1]*bullet[1] + bullet[2]*bullet[2])

        #commemorates the one time Jack was right 
        #his fix made bullets fly accurately towards mouse cursor by normalizing bullet radius vectors so speeds are constant
        
        #Jack_is_right_counter = 0
        x_speed = (BULLET_SPEED*bullet[1])/rad_sq
        y_speed = (BULLET_SPEED*bullet[2])/rad_sq
        #Jack's f* right
        #Jack_is_right_counter += 1
        
        bullet[0].x -= x_speed
        bullet[0].y -= y_speed
        
        #when a bullet touches a white wall, nothing happens
        for wall in wallsNonPortal:
            if bullet[0].touches(wall):
                if bullet in bullets:
                    bullets.remove(bullet)
        
        for wall in wallsPortal:
            if bullet[0].touches(wall):
                #all of this is just to orient the portals properly based on how a bullet hits the wall
                if bullet[3] == 'blue':
                    if bullet[0].left_touches(wall) or bullet[0].right_touches(wall):
                        blue_portal.size = PORTAL_WIDTH, PORTAL_HEIGHT
                        if bullet[0].left_touches(wall):
                            blue_wall_side = 'left'
                        else:
                            blue_wall_side = 'right'
                    else:
                        blue_portal.size = PORTAL_HEIGHT, PORTAL_WIDTH
                        if bullet[0].top_touches(wall):
                            blue_wall_side = 'top'
                        else:
                            blue_wall_side = 'bottom'
                    blue_portal.center = bullet[0].center
                elif bullet[3] == 'orange':
                    if bullet[0].left_touches(wall) or bullet[0].right_touches(wall):
                        orange_portal.size = PORTAL_WIDTH, PORTAL_HEIGHT
                        if bullet[0].left_touches(wall):
                            orange_wall_side = 'left'
                        else:
                            orange_wall_side = 'right'
                    else:
                        orange_portal.size = PORTAL_HEIGHT, PORTAL_WIDTH
                        if bullet[0].top_touches(wall):
                            orange_wall_side = 'top'
                        else:
                            orange_wall_side = 'bottom'
                    orange_portal.center = bullet[0].center
                
                if bullet in bullets:
                    bullets.remove(bullet)
                
                if blue_portal.touches(wall):
                    blue_portal.move_to_stop_overlapping(wall)
                if orange_portal.touches(wall):
                    orange_portal.move_to_stop_overlapping(wall)
                
        #makes a bullet go off screen a little bit in case it hits a wall, but deletes it once it gets past a certain distance 
        if bullet[0].x > camera.center[0] + WIDTH_WIN or bullet[0].x < camera.center[0] - WIDTH_WIN:
            if bullet in bullets:
                bullets.remove(bullet)
        if bullet[0].y > camera.center[1] + HEIGHT_WIN or bullet[0].y < camera.center[1] - HEIGHT_WIN:
            if bullet in bullets:
                bullets.remove(bullet)
        
        
        camera.draw(bullet[0])
    
    #makes timer tick up once a second instead of once a tick
    clock += 1
    if clock % 30 == 0:
        time += 1
    #redeclares timer and coin_counter every tick to update the numbers
    timer = gamebox.from_text(WIDTH_WIN - 100, 100, str(time) + " s", 'Arial', 24, 'white')
    coin_counter = gamebox.from_text(WIDTH_WIN - 100, 50, str(coin_count) + ' coins', 'Arial', 24, 'white')

    #moves the timer and coin counter when the camera moves
    timer.left = camera.right - 100
    coin_counter.left = camera.right - 100
    #draws a bit more 
    camera.draw(timer)
    camera.draw(coin_counter)

    camera.draw(blue_portal)
    camera.draw(orange_portal)
    
    #------End conditions------
    
    #Reaching the end of the level
    #This whole for loop is a mess and awful
    #Basically a copy of the selection in the main menu 
    for wall in wallFinal:
        if char.touches(wall):
            char.move_to_stop_overlapping(wall)
            yspeed = 0
            black = gamebox.from_color(camera.center[0],camera.center[1],'black', WIDTH_WIN,HEIGHT_WIN)
            camera.draw(black)
            congrats = gamebox.from_text(camera.center[0], camera.center[1] - 200, 'Congratulations!', 'Arial',48,'white')
            coin_amount = gamebox.from_text(camera.center[0],camera.center[1] - 150, 'You found ' + str(coin_count) + ' out of 10 coins', 'Arial', 36, 'white')
            
            choice1 = gamebox.from_text(camera.center[0], camera.center[1] - 40, 'Quit Game','Arial', 24, 'white')
            choice2 = gamebox.from_text(camera.center[0], camera.center[1] + 40, 'Go back to Title Screen','Arial',24,'white')
            
            highlight.x = camera.center[0]
            if pygame.K_s in keys:
                if highlight.y == camera.center[1] - 20:
                    highlight.y = camera.center[1] + 60
            elif pygame.K_w in keys:
                if highlight.y == camera.center[1] + 60:
                    highlight.y = camera.center[1] - 20
            
            camera.draw(highlight)
            camera.draw(congrats)
            camera.draw(coin_amount)
            camera.draw(choice1)
            camera.draw(choice2)
                
            if pygame.K_RETURN in keys:
                if highlight.y == camera.center[1] - 20:
                    quit()
                elif highlight.y == camera.center[1] + 60:
                    gamebox.Camera.is_initialized = False
                    switch.run_title()
                
            xspeed = 0
    if char.y >= HEIGHT_WIN + 50:
        char.center = [400, HEIGHT_WIN - 80]
    #b goes back to the title screen
    if pygame.K_b in keys:
        gamebox.Camera.is_initialized = False
        switch.run_title()
        #quit()
    #k quits the game
    if pygame.K_k in keys:
        quit()
    
    camera.display()

gamebox.timer_loop(30, tick)
































