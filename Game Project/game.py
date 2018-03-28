import pygame
import gamebox

camera = gamebox.Camera(800,600)
background = gamebox.from_image(400,300, "background.jpg");
playGame = gamebox.from_text(camera.x, 370, "Play Game", "Arial", 50, "WHITE") 
Instructions = gamebox.from_text(camera.x, 450, "Instructions", "Arial", 50, "WHITE")
highlight = gamebox.from_color(camera.x, 400, "yellow", 300, 5) 
instructions = ["Controls", " ", "Use the a and d to move Mario left and right", "Use w to jump", "Use your cursor to aim your portal gun", "Use q for blue portals", "Use e for orange portals", "Go through one portal and come out the other!", " ", "Collect all 10 coins along the way as you try to get Mario out of this strange world", "Reach the red block at the end of the game", "Press b to get back to the start screen", "Use k to quit the game"]

def tick(keys):

	global background, playGame, Instructions, highlight, camera
	camera.draw(background)

	if pygame.K_w in keys:
		if background.y == 300:
			highlight = gamebox.from_color(camera.x, 400, "yellow", 300, 5) 
	if pygame.K_s in keys:
		if background.y == 300:
			highlight = gamebox.from_color(camera.x, 480, "yellow", 300, 5) 
	if pygame.K_b in keys:
				
		background = gamebox.from_image(400,300, "background.jpg");
		playGame = gamebox.from_text(camera.x, 370, "Play Game", "Arial", 50, "WHITE") 
		Instructions = gamebox.from_text(camera.x, 450, "Instructions", "Arial", 50, "WHITE")
		highlight = gamebox.from_color(camera.x, 400, "yellow", 300, 5) 
	if pygame.K_RETURN in keys:
		if highlight.y == 480:
			background = gamebox.from_color(0,0, "black", 0, 0)
			playGame = gamebox.from_color(0,0, "black", 0, 0)
			Instructions  = gamebox.from_color(0,0, "black", 0, 0)
			highlight  = gamebox.from_color(0,0, "black", 0, 0)
			camera.clear("blacK")
			y = 40
			for line in instructions:
				if y == 440 or y == 480:
					camera.draw(gamebox.from_text(camera.x,y,line, "Arial", 20, "green"))
				elif y == 400:
					camera.draw(gamebox.from_text(camera.x,y,line, "Arial", 20, "red"))
		
				else:
					camera.draw(gamebox.from_text(camera.x, y, line, "Arial", 20, "white"))
				y += 40	 
		elif highlight.y == 400:
			gamebox.Camera.is_initialized = False
			import switch
			switch.run_game()

	camera.draw(highlight)
	camera.draw(playGame)
	camera.draw(Instructions)
	camera.display()

ticks_per_second =  30 


#keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

































