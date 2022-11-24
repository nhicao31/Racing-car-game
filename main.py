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
        gameoverImg = pygame.image.load("car game\gameover.png")
        run = True
        while run:

            screen.blit(gameoverImg,(0,0))
            time.sleep(0.5)
            show_score(330,400)
            time.sleep(0.5)
            show_highscore(330,450)
            pygame.display.update()
            
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    countdown()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
    
    #setting background image
    bg = pygame.image.load('car game/bg.png')
    
    
    # setting our player
    maincar = pygame.image.load('car game\car.png')
    maincarX = 350
    maincarY = 495
    maincarX_change = 0
    maincarY_change = 0

    #other cars
    car1 = pygame.image.load('car game\car1.jpeg')
    car1X = random.randint(178,490)
    car1Y = 100
    car1Ychange = 10    
    car2 = pygame.image.load('car game\car2.png')
    car2X = random.randint(178,490)
    car2Y = 100
    car2Ychange = 10

    car3 = pygame.image.load('car game\car3.png')
    car3X = random.randint(178,490)
    car3Y = 100
    car3Ychange = 10
       

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

                #checking if any key has been pressed
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 5
            
                if event.key == pygame.K_LEFT:
                    maincarX_change -= 5
                
                if event.key == pygame.K_UP:
                    maincarY_change -= 5
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change += 5

                #checking if key has been lifted up
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0
            
                if event.key == pygame.K_LEFT:
                    maincarX_change = 0
                
                if event.key == pygame.K_UP:
                    maincarY_change = 0
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change = 0            

        #setting boundary for our main car
        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490
        
        if maincarY < 0:
            maincarY = 0
        if maincarY > 495:
            maincarY = 495


        #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
        screen.fill((0,0,0))

        #displaying the background image
        screen.blit(bg,(0,0))

        #displaying our main car
        screen.blit(maincar,(maincarX,maincarY))

        #displaing other cars
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
          #calling our show_score function
        show_score(570,280)
        #calling show_hiscore function
        show_highscore(0,0)

        
        
        #updating the values
        maincarX += maincarX_change
        maincarY += maincarY_change

        #movement of the enemies
        car1Y += car1Ychange
        car2Y += car2Ychange
        car3Y += car3Ychange
        #moving enemies infinitely
        if car1Y > 670:
            car1Y = -100
            car1X = random.randint(178,490)
            score_value += 1
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178,490)
            score_value += 1
        if car3Y > 670:
            car3Y = -200
            car3X = random.randint(178,490)
            score_value += 1

        #checking if highscore has been created
        if score_value > int(highscore):
            highscore = score_value

          
         

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
