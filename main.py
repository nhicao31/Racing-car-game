#Sally Pham = SP
#Minh-Anh Zaiser = MZ

#MZ
import pygame,sys
pygame.init() #initializes the Pygame
from pygame.locals import* #import all modules from Pygame
import random
import math
import time
screen = pygame.display.set_mode((798,600)) #intialize a window for display

#initializing pygame mixer (module for loading and playing sounds)
pygame.mixer.init()

#changing title of the game window
pygame.display.set_caption('Racing Beast')

#changing the logo
logo = pygame.image.load('car game/logo.jpeg') #load 'logo' image from car game folder
pygame.display.set_icon(logo)


############ MAKING INTRO SCREEEN ###########
IntroFont = pygame.font.Font("freesansbold.ttf", 38) #create a variable with new font, size 38

def introImg(x,y):
    intro = pygame.image.load("car game\intro.png") # load 'intro' image
    #draw 'intro' image onto the game window with width x and height y
    screen.blit(intro,(x,y))

def instructionIMG(x,y):
    instruct = pygame.image.load("car game\instruction.png") #load 'instruction' image as instruct
    run = True
    while run: # equivalent of while True -> forever loop
        screen.blit(instruct,(x,y)) #draw instructions onto game window
        pygame.display.update()
        
        #events = inputs (mainly from keyboard)
        for event in pygame.event.get(): #for an event in the queue of events
            if event.type == pygame.QUIT:
                run = False #stop running the loop if the event type is quit

#SP  
def aboutIMG(x,y):
    aboutimg = pygame.image.load("car game\About.png") #load new image from a file
    run = True
    while run: 
        screen.blit(aboutimg,(x,y)) #takes the background surface (aboutimg), draw the image onto the screen
        pygame.display.update() #update portions of the screen for software displays
        for event in pygame.event.get(): #get events from the queue
            if event.type == pygame.QUIT:
                run = False #if the type of the event is to uninitialize all pygame modules then return false and stop running

#MZ
def play(x,y):
    #write "PLAY" in the given font, antialias = True means the characters will have smoother edges, color red
    playtext = IntroFont.render("PLAY",True,(255,0,0))
    #draw playtext ("PLAY" written in red) onto the screen at x width and y height
    screen.blit (playtext,(x,y))
def ABOUT(x,y):
    #write "ABOUT" in red at the position (x,y)
    aboutText = IntroFont.render("ABOUT",True,(255,0,0))
    screen.blit (aboutText,(x,y))
def Instruction(x,y):
    #write 'INSTRUCTION' in red at position (x,y)
    instructionText = IntroFont.render("INSTRUCTION",True,(255,0,0))
    screen.blit(instructionText,(x,y))

#SP
def introscreen():
    run = True
    pygame.mixer.music.load('car game/startingMusic.mp3') #load a music file for playback
    pygame.mixer.music.play() #start playing music
    while run :
        screen.fill((0,0,0)) #fill the whole screen with a black colour (0,0,0)
        introImg(0,0) #displace the intro image on the whole screen
        play(100,450) #displacing the 'play' button at position (100,450)
        Instruction(280,450) #displacing the 'Instruction' button at position (280,450)
        ABOUT(615,450) #displacing the 'ABOUT' button at position (615,450)

        x,y = pygame.mouse.get_pos() #getting the mouse cursor position

        #storing rectangle coordinates (x, y, length, height) by making variables
        button1 = pygame.Rect(60,440,175,50) #creating a rectangle at coordinates (60,440,175,50)
        button2 = pygame.Rect(265,440,300,50) #creating a rectangle at coordinates (265,440,300,50)
        button3 = pygame.Rect(600,440,165,50) #creating a rectangle at coordinates (600,440,165,50)

        pygame.draw.rect(screen, (255,255,255), button1,6)
        pygame.draw.rect(screen, (255,255,255), button2,6)
        pygame.draw.rect(screen,(255,255,255),button3,6)
        #pygame.draw.rect takes these arguments (surface, color, coordinates, border)

        if button1.collidepoint(x,y): #if the cursor is on button1 (PLAY button)
            pygame.draw.rect(screen, (155,0,0), button1,6) #change from inactive to active by changing color from white to red
            if click: #if click on the PLAY button
                countdown() #move to the countdown function to start the game


        if button2.collidepoint(x,y): #if the cursor is on button2 (INSTRUCTION button) 
            pygame.draw.rect(screen, (155,0,0), button2,6) #change from inactive to active by changing color from white to red
            if click: #if click on the INSTRUCTION button
                instructionIMG(0,0) #display the instruction image

        
        if button3.collidepoint(x,y): #if the cursor is on button3 (ABOUT button) 
            pygame.draw.rect(screen,(155,0,0),button3,6) #change from inactive to active by changing color from white to red
            if click: #if click on the ABOUT button
                aboutIMG(0,0) #display the about image
                
        click = False #checking for mouse click event
        for event in pygame.event.get(): #handles the internal events and retrieves a list of external events
         if event.type == pygame.QUIT:
            run = False #if the type of the event is to uninitialize all pygame modules then return false and stop running
         if event.type == pygame.MOUSEBUTTONDOWN: #check if it is clicked
             if event.button == 1: #check if it is left click
                 click = True #enable whatever is clicked
        pygame.display.update() #make the display surface appear on the screen

  
#MZ
###### Countdown ######
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85) #font2 is the same font as before, but bigger size
    countdownBacground = pygame.image.load('car game/bg.png') #load the background image for countdown
    three = font2.render('3',True, (187,30,16)) #writes 3 in red
    two =   font2.render('2',True, (255,255,0)) #writes 2 in yellow
    one =   font2.render('1',True, (51,165,50)) #writes 1 in green
    go =    font2.render('GO!!!',True, (0,255,0)) #writes go!! in green

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0)) #draws the background onto the window at position (0,0)
    pygame.display.update() #update display => background image will appear

    ###### Displaying  three (3) ######
    screen.blit(three,(350,250)) #draws 3 onto the window
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ###### Displaying  two (2) ######
    screen.blit(two,(350,250)) #draws 2 onto the window
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ###### Displaying  one (1) ######
    screen.blit(one,(350,250)) #draws 1 onto the window
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1) #waits for 1 second

    ###### Displaying  Go!!! ######
    screen.blit(go,(300,250)) #draws go!! onto the window
    pygame.display.update() #update window display
    time.sleep(1) #waits for 1 second
    gameloop() #calling the gameloop so that our game can start after the countdown
    pygame.display.update()


#SP
def gameloop(): #defining our gameloop function

    pygame.mixer.music.load('car game\BackgroundMusic.mp3') #load a music file
    pygame.mixer.music.play() #start the music
    crash_sound = pygame.mixer.Sound('car game\car_crash.wav') #create a new Sound object from a file for collision

    #scoring part
    score_value = 0 #introduce score_value variable
    font1= pygame.font.Font("freesansbold.ttf",25)  #create a new Font object from a file with size 25

    def show_score(x,y):
        score = font1.render("SCORE: "+ str(score_value), True, (255,0,0)) #show score on new surface: render(text, antialias, color, background=None)
        screen.blit(score, (x,y)) #takes the "score" surface and display the score onto the screen

    #highscore part
    with open ("car game\highscore.txt","r") as f: #open the file using "with" so you do not have to close the file later, it'll close itself
            highscore = f.read() #read a single line from the file
    def show_highscore(x,y): 
        Hiscore_text = font1.render('HISCORE :' + str(highscore),True,(255,0,0)) #show high score on new surface: render(text, antialias, color, background=None)
        screen.blit (Hiscore_text,(x,y)) #takes the "Hiscore_text" surface and display the high score onto the screen
        pygame.display.update() #make the display surface appear on the screen
    
    #game over function
    def gameover():
        gameoverImg = pygame.image.load("car game\gameover.png") #setting the image when the game is over
        run = True 
        while run:

            screen.blit(gameoverImg,(0,0)) #takes the "gameoverImg" surface and display on the screen
            time.sleep(0.5) #add delay in time: 0.5 seconds
            show_score(330,400) #run the function show_score
            time.sleep(0.5) #add delay in time: 0.5 seconds
            show_highscore(330,450) #run the function show_highscore
            pygame.display.update() #make the display surface appear on the screen
            
            for event in pygame.event.get(): #handles the internal events and retrieves a list of external events
             if event.type == pygame.QUIT: 
                run = False
                pygame.quit()
                sys.exit() #if the type of the event is to uninitialize all pygame modules then return false, quit pygame and stop running
             if event.type == pygame.KEYDOWN: #detect if it is clicked
                if event.key == pygame.K_SPACE: #if space key is pressed
                    countdown() #enable countdown function
                if event.key == pygame.K_ESCAPE: #is escape key is pressed
                    pygame.quit()
                    sys.exit() #quit and exit game
        
   

    bg = pygame.image.load('car game/bg.png') #setting background image
    
    
    # setting player's main car
    maincar = pygame.image.load('car game\car.png') #setting image for main car
    maincarX = 350 #position of main car on x axis
    maincarY = 495 #position of main car on y axis
    maincarX_change = 0 #introduce position of maincarX_change variable
    maincarY_change = 0 #introduce position of maincarY_change variable

    #other cars
    car1 = pygame.image.load('car game\car1.jpeg') #setting the image to car1
    car1X = random.randint(178,490) #generate random numbers: randint(start, end)
    car1Y = 100 #setting position to car1Y
    car1Ychange = 10 #setting position to car1Ychange
    
    car2 = pygame.image.load('car game\car2.png') #setting the image to car2
    car2X = random.randint(178,490) #generate random numbers: randint(start, end)
    car2Y = 100 #setting position to car2Y
    car2Ychange = 10 #setting position to car2Ychange

    car3 = pygame.image.load('car game\car3.png') #setting the image to car3
    car3X = random.randint(178,490) #generate random numbers: randint(start, end)
    car3Y = 100 #setting position to car3Y
    car3Ychange = 10 #setting position to car3Ychange
       

    run = True
    while run:
        for event in pygame.event.get(): #handles the internal events and retrieves a list of external events
            if event.type == pygame.QUIT: 
                run = False
                pygame.quit()
                sys.exit() #if the type of the event is to uninitialize all pygame modules then return false, quit and stop running

            if event.type == pygame.KEYDOWN: #check if any key is pressed
                if event.key == pygame.K_RIGHT: #if right key is pressed
                    maincarX_change += 5 #move main car to the right 5
            
                if event.key == pygame.K_LEFT: #if left key is pressed
                    maincarX_change -= 5 #move main car to the left 5
                
                if event.key == pygame.K_UP: #if up key is pressed
                    maincarY_change -= 5 #move main car up 5
                    
                if event.key == pygame.K_DOWN: #if down key is pressed
                    maincarY_change += 5 #move main car down 5

            if event.type == pygame.KEYUP: #check if key is lifted up
                if event.key == pygame.K_RIGHT: #if right key is lifted up
                    maincarX_change = 0 #no change is made
            
                if event.key == pygame.K_LEFT: #if left key is lifted up
                    maincarX_change = 0 #no change is made
                
                if event.key == pygame.K_UP: #if up key is lifted up
                    maincarY_change = 0 #no change is made
                    
                if event.key == pygame.K_DOWN: #if down key is lifted up
                    maincarY_change = 0 #no change is made     

        #setting boundary for main car
        if maincarX < 178: #if position of car is less than 178
            maincarX = 178 #then position of car is 178
        if maincarX > 490: #if position of car is greater than 490
            maincarX = 490 #then position of car is 490
        
        if maincarY < 0: #if position of car is less than 0
            maincarY = 0 #then position of car is 0
        if maincarY > 495: #if position of car is greater than 495
            maincarY = 495 #then position of car is 495


        screen.fill((0,0,0)) #fill the display with black

        screen.blit(bg,(0,0)) #displaying the background image

        screen.blit(maincar,(maincarX,maincarY)) #displaying our main car

        screen.blit(car1,(car1X,car1Y)) #displace car1
        screen.blit(car2,(car2X,car2Y)) #displace car2
        screen.blit(car3,(car3X,car3Y)) #displace car3
        show_score(570,280) #enable show_score function
        show_highscore(0,0) #enable show_hiscore function

        
        #updating postion of main car
        maincarX += maincarX_change #main car position + the changed position of main car
        maincarY += maincarY_change #main car position + the changed position of main car

        #movement of other cars
        car1Y += car1Ychange #car position + the changed position of car
        car2Y += car2Ychange #car position + the changed position of car
        car3Y += car3Ychange #car position + the changed position of car
        #moving other cars infinitely
        if car1Y > 670: #if position of car1 is greater than 670
            car1Y = -100 #y value of car1 is set at -100
            car1X = random.randint(178,490) #generate random position for x value of car1
            score_value += 1 #add 1 to score
        if car2Y > 670: #if position of car2 is greater than 670
            car2Y = -150 #y value of car2 is set at -150
            car2X = random.randint(178,490) #generate random position for x value of car2
            score_value += 1 #add 1 to score
        if car3Y > 670: #if position of car3 is greater than 670
            car3Y = -200 #y value of car3 is set at -200
            car3X = random.randint(178,490) #generate random position for x value of car3
            score_value += 1 #add 1 to score

        #create highscore
        if score_value > int(highscore): #if score_value is greater than highscore
            highscore = score_value #show highscore as score_value

          
         

#MZ
        #DETECTING COLLISIONS BETWEEN THE CARS

        #getting distance between our main car and car1
        def iscollision(car1X,car1Y,maincarX,maincarY):
            
            #Using the formula to calculate distance from the coordinates
            #Distance between the main car (controlled by player) and car 1 (obstacle car)
            distance = math.sqrt(math.pow(car1X-maincarX,2) + math.pow(car1Y - maincarY,2)) 

            #checking if distance is smaller than 50, then collision will occur
            if distance < 50: 
                return True
            else:
                return False

        #getting distance between our main car and car2
        def iscollision(car2X,car2Y,maincarX,maincarY):
            distance = math.sqrt(math.pow(car2X-maincarX,2) + math.pow(car2Y - maincarY,2))

            #checking if distance is smaller than 50, then collision will occur
            if distance < 50:
                return True
            else:
                return False

        #getting distance between our main car and car3
        def iscollision(car3X,car3Y,maincarX,maincarY):
            distance = math.sqrt(math.pow(car3X-maincarX,2) + math.pow(car3Y - maincarY,2))

            #checking if distance is smaller then 50, then collision will occur
            if distance < 50:
                return True
            else:
                return False
        
        ##### giving collision a variable #####

        #collision between maincar and car1
        #coll1 = True if the distance between car1 and main car is smaller than 50
        coll1 = iscollision(car1X,car1Y,maincarX,maincarY) 

        #collision between maincar and car2
        #coll2 = True if the distance between car2 and main car is smaller than 50

        coll2 = iscollision(car2X,car2Y,maincarX,maincarY) 

        #collision between maincar and car3
        #coll3 = True if the distance between car3 and main car is smaller than 50
        coll3 = iscollision(car3X,car3Y,maincarX,maincarY) 

        #if coll1 = True => if the 2 cars are too close
        if coll1:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            #stop music
            pygame.mixer.music.stop()
            #play crash sound effect
            crash_sound.play()
        ###### calling our game over function #######
            time.sleep(1) #wait 1 second
            gameover()
          
        #if coll2 is True
        if coll2:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
        ###### calling our game over function #######
            time.sleep(1)
            gameover()
           

        #if coll3 is True    
        if coll3:       
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
        ###### calling our game over function #######
            time.sleep(1)
            gameover()
        
        #If any of the 3 cars collided with the main car 
        # => coll1, coll2 or coll3 True
        if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0 :
          pass
            

        # writing to our highscore.txt file
        with open ("car game\highscore.txt","w") as f: #opens the highscore file as f
            f.write(str(highscore)) #writes highscore value into the value
        

        pygame.display.update()
introscreen() #back to intro screen from the beginning
