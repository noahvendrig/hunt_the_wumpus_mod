# Imports
import pygame
import time

def main():
    pygame.init() # initialise!

    clock = pygame.time.Clock() #create a gameclock for setting FPS
    fps = 25 # set the fps here

    w = 1800 #width of window of game
    h = 900 #height of window of game
    running = True
    image1 = pygame.image.load("./img/bg.jpg") # whatever the path is for ur img. if ur stuck on how paths work dm
    image1 = pygame.transform.scale(image1, (w, h)) #scale down the image to the window size (in this case its my background img so i made it the full size)
    
    screen = pygame.display.set_mode((w, h)) #create the screen for the game
    fontColour = (0, 0, 0) #font colour is black here
    pygame.display.set_caption("GAME WINDOW TITLE") #title of the game window
    font = pygame.font.Font("freesansbold.ttf", 32) # whatever font  u wanna use

    wantToShowTextWithTimer = False

    while running: # only when running == True
        
        screen.blit(image1, (1, 1)) # blit the object to the screen, make it appear
        #screen.blit(image/text/whatever, (x,y coords))
        
        rect1 = pygame.draw.rect(screen,(0,0,255),(1200,100,100,50)) #create a rectange object (literally a rectangle on the screen) and draw it to the screen
        # rect1 = pygame.draw.rect(screen,(0,0,255),(100,150,300,90), 1, 10) # more advanced rectangle, everything after the pos can be deleted tho
        #rect = pygame.draw.rect(screen, (R,G,B), (left, top, width, height))
        #rect = pygame.draw.rect(screen, (R,G,B), (left, top, width, height), line_width, border_radius)
        text1 = font.render("noah is the best", True, fontColour)
        screen.blit(text1, (200, 200)) # 0,0 is at the top leftof the screen, so 200,200 should be somewhere in the top left quadrant 

        for event in pygame.event.get(): #for every event that occurs
                if event.type == pygame.QUIT:  # check if its a quit event, so we can close when x button hit
                    running = False # game will stop running and therefore quit
                    pygame.quit()
                

                if event.type == pygame.KEYDOWN: #event of a keyboard button hit. for specific key input refer to https://www.pygame.org/docs/ref/key.html
                    if event.key == pygame.K_ESCAPE: #close when escape hit
                        running = False # game will stop running and therefore quit
                        pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN: #this is for detecting mouse clicks idk if u need this   

                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        startTime = time.time() # the start time is whenever the rect is clicked on
                        wantToShowTextWithTimer = True #we want to show the timer text now!
                        print("Mouse clicked on the rect") #do whatever here
        
        if wantToShowTextWithTimer: # we put this in our while loop because itll happen every iteration, so time.time() is always updating
            text2 = font.render("TIMER TEXT!", True, fontColour) #set the text
            
            if time.time() - startTime < 3: # if it hasnt been 3 seconds yet
                screen.blit(text2, (600, 600))  # draw on screen
                # pygame.display.update()

        clock.tick(fps)
        pygame.display.update() #update the display # make sure that this is the LAST thing in the while loop cuz nothing after will show i think

if __name__ == "__main__": 
    main()