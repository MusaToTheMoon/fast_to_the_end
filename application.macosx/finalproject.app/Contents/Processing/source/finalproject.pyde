add_library('minim')
import os

PATH = os.getcwd()
player = Minim(this)

ERROR_FOR_COLLISION = 10 

# -------SKIP OVER THIS--------------------------------------------------------------
# class MultiStop(Platform):
#     def __init__(self,p1,p2,p3,speed,img):
#         Platform.__init__(self,p1,p2,speed,img)
#         self.p3 = p3
#         self.part = 1  
#         print(self.dir)
#         self.vx1 = self.vx
#         self.vy1 = self.vy
#         self.i = 1
#         self.gradient1 = self.gradient
        
#         if self.p2[0]-self.p3[0] != 0:
#             self.gradient2 = float(self.p2[1]-self.p3[1])/(self.p2[0]-self.p3[0])
#             self.vx2 = (sqrt(1/(1+sq(self.gradient2))))*speed
#             self.vy2 = (self.gradient2*self.vx2)
#         else:
#             self.vx2 = 0
#             self.vy2 = 1*speed
#             self.gradient2 = None
        
#         # print(self.vx1,self.vy1,self.vx2,self.vy2)
        
#     def update(self):
#         if self.dir == 1:
#             print(self.dir)
#         if self.part == 1:
#             print(0)
#             if self.p1[0] < self.p2[0]:
#                 print(2)
#                 if self.x < self.p1[0]:
#                     print(3)
#                     self.dir = self.dir*-1
#             # elif self.p1[0] > self.p2[0]:
#             #     print(4, self.dir)
#             #     if self.x > self.p1[0]:
#             #         print(5, self.x, self.p1[0])
#             #         self.dir = self.dir*-1
#             elif self.p1[0] == self.p2[0]:
#                 print(6)
#                 if self.p1[1] < self.p2[1]:
#                     print(7)
#                     if self.y < self.p1[1]:
#                         print(8)
#                         self.dir = self.dir*-1
#                 elif self.p1[1] > self.p2[1]:
#                     print(9, self.y)
#                     if self.y > self.p1[1]:
#                         print(10)
#                         self.dir = self.dir*-1
                        
#             self.vx = self.vx1
#             self.vy = self.vy1
            
#         elif self.part == 2:
#             print(11)
#             if self.p2[0] < self.p3[0]:
#                 print(12)
#                 if self.x > self.p3[0]:
#                     print(13)
#                     self.dir = self.dir*-1
#             # elif self.p2[0] > self.p3[0]:
#             #     print(14)
#             #     if self.x < self.p3[0]:
#             #         print(15)
#             #         self.dir = self.dir*-1         
#             elif self.p2[0] == self.p3[0]:
#                 print(16)
#                 if self.p2[1] < self.p3[1]:
#                     print(17)
#                     if self.y > self.p3[1]:
#                         print(18)
#                         self.dir = self.dir*-1
#                 elif self.p2[1] > self.p3[1]:
#                     print(19)
#                     if self.y < self.p3[1]:
#                         print(20)
#                         self.dir = self.dir*-1

#             self.vx = self.vx2
#             self.vy = self.vy2
        
#         print('first platform', self.dir, self.gradient, self.vx, self.vy)
#         self.y += self.vy*self.dir
#         self.x += self.vx*self.dir
#         # print(self.vx)
        
#         if self.part == 1:
#             print(21)
#             if self.p1[0] < self.p2[0]:
#                 print(22)
#                 if self.x >= self.p2[0]:
#                     print(23)
#                     self.part = 2
#             elif self.p1[0] == self.p2[0]:
#                 print(24)
#                 if self.p1[1] < self.p2[1]:
#                     print(25)
#                     if self.y >= self.p2[1]:
#                         print(26)
#                         self.part = 2
#                 elif self.p1[1] > self.p2[1]:
#                     print(27)
#                     if self.y <= self.p2[1]:
#                         print(28)
#                         self.part = 2
            
#             self.vx = self.vx1
#             self.vy = self.vy1
#             # elif self.p1[0] > self.p2[0]:
#             #     print(24)
#             #     if self.x <= self.p2[0]:
#             #         print(25)
#             #         self.part = 2
#             # elif self.p1[0] == self.p2[0]:
                
#         elif self.part == 2:
#             print(29)
#             if self.p2[0] < self.p3[0]:
#                 print(30)
#                 if self.x <= self.p2[0]:
#                     print(31)
#                     self.part = 1
#             elif self.p2[0] == self.p3[0]:
#                 print(32)
#                 if self.p2[1] < self.p3[1]:
#                     print(33)
#                     if self.y <= self.p2[1]:
#                         print(34)
#                         self.part = 1
#                 elif self.p2[1] > self.p3[1]:
#                     print(35)
#                     if self.y >= self.p2[1]:
#                         print(36)
#                         self.part = 1
#             # elif self.p2[0] > self.p3[0]:
#             #     print(29)
#             #     if self.x >= self.p2[0]:
#             #         print(30)
#             #         self.part = 1
#         # print(self.x)
#         # if self.dir == 1 and self.x == self.p2[0]:
#         #     self.part = 2
#         # elif self.dir == 2 and self.x == self.p2[0]:
#         #     self.part = 1
            
#         # if self.p1[0]-self.p2[0] == 0:
#         #     if self.part == 1 and self.y = self.p2[0]:
#         #         self.part = 2
#         #     elif self.part == 2 and self.x = self.p2[0]:
#         #         self.part = 1
#         # else:
#         # if self.
#         # if self.part == 1 and self.x >= self.p2[0]:
#         #     self.part = 2
#         # elif self.part == 2 and self.x <= self.p2[0]:
#         #     self.part = 1

# class CircularPlatform:
#     def __init__(self,p1,p2,increasing,speed,img):
#         self.p1 = p1
#         self.p2 = p2
#         self.increasing = increasing # can take either True -> increasing or False -> decreasing
#         self.x = p1[0]
#         self.y = p1[1]
#         # print(self.x, self.y)
#         self.img = loadImage(PATH+"/images/{0}.png".format(img))
#         self.radius = self.p1[0] - self.p2[0]
        
#         self.vx = 1

#         if self.increasing == True:
#             self.center = [self.p1[0], self.p2[1]]
#         else:
#             self.center = [self.p2[0], self.p1[1]]
            
                
#         if p1[1] > p2[1]:
#             self.upward = True
#         elif p1[1] < self.p1[1]:
#             self.upward = False
        
#     def display(self):
#         self.update()
#         # print('working')
#         image(self.img,self.x, self.y)
        
#     def update(self):
#         if self.upward == True:
#             # print('working')
            
#             self.x += self.vx
#             self.vy = sqrt(sq(self.radius) - sq(self.x))
#             self.y = self.center[1]+self.vy
#             # print(self.x, self.y)
#             # print(self.center[1], sqrt(sq(self.radius) - sq(self.x-self.center[0])))
#             # self.y = self.center[1]-sqrt(sq(self.radius) - sq(self.x-self.center[0]))
#-------------------------------------------------------------------------------------------

class Individual: # class for creatures
    def __init__ (self, x,y,r,g,img,w,h,F):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.g = g
        self.w=w
        self.h=h
        self.slice=0
        self.F=F
        self.dir = 1
        self.img = loadImage(PATH+"/images/{0}.png".format(img))

    def gravity(self): # gravity
         
        if self.y+self.r < self.g:
            self.vy += 0.8
            
            if self.y+self.r+self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
        else:
            self.vy = 0
                           
    def update(self):
        self.gravity()
        
        self.x += self.vx
        self.y += self.vy
        
class Man(Individual): # man class inherits from Individual class
    def __init__(self, x,y,r,g,img,w,h,f):
        Individual.__init__(self, x,y,r,g,img,w,h,f)
        self.keyHandlers = {LEFT:False, RIGHT:False, UP:False}
        self.standing = True # man is stationary or running
        self.on_platform = -1 # to store the index of the platform the man is currently standing on
        self.health = 5
        self.death = False # set to True every time man loses a health point
        
        # sounds for man
        self.jump_sound = player.loadFile(PATH+"/sounds/jump.wav")
        self.death_sound = player.loadFile(PATH+"/sounds/death.wav")
        self.pickup_sound = player.loadFile(PATH+"/sounds/pickup.wav")
        
    def enemyCollision(self): # collisions with enemies of all sorts
        for e in game.enemies:
            if sqrt(sq((self.x+10)-(e.x)) + sq((self.y)-(e.y))) <= e.r + self.r:
                self.death = True
                self.death_sound.rewind()
                self.death_sound.play()
                    
    def platformCollision(self): 
        for ind,p in enumerate(game.platforms): # determine which platform man is standing on

            if self.x+self.r >= p.x and self.x-self.r <= p.x + p.w and self.y+self.r <= p.y+10:
                if isinstance(p, VanishPlatform): # further condition for vanishing platforms
                    if p.show == True: # vanishing platform must be showing
                        self.on_platform = ind
                        break
                    else:
                        self.on_platform = -1
                else:
                    self.on_platform = ind
                    break
            else:
                self.on_platform = -1 # -1 means man on ground

        if self.on_platform != -1: # reset ground
            if p.p2 != None and self.y+self.r >= p.y and self.g == game.g: # stationary platforms have p2 set to None 
                self.y -= 10
            self.g = p.y
        else:
            self.g = game.g
                
    def hasanaatPickup(self): # hasanaat are good deeds
        if len(game.hasanaat) != 0: # game.hasanaat is a list containing all hasanaat
            for h in game.hasanaat:
                if sqrt(sq((self.x)-(h.x)) + sq((self.y)-(h.y))) <= h.r + self.r:
                    game.hasanaat.remove(h) # hasanaat removed if collected
                    self.pickup_sound.rewind()
                    self.pickup_sound.play()
                    
    def update(self):
        self.platformCollision()
        self.hasanaatPickup()
        self.enemyCollision()
        self.gravity()
        
        if self.keyHandlers[LEFT] and self.x-self.r >= 0:
            self.vx = -9
        elif self.keyHandlers[RIGHT]:
            self.vx = 9
        else:
            self.vx = 0
        
        if self.keyHandlers[UP] and self.vy == 0:
            self.vy = -17
            self.jump_sound.rewind()
            self.jump_sound.play()
        
        # --- for moving platform and man combined movement ---
        platform_vx = 0
        platform_vy = 0
        
        if self.on_platform != -1 and game.platforms[self.on_platform].p2 != None: # narrow down to just moving platforms

            # if game.platforms[self.on_platform].vy < 0:
            #     ERROR = game.platforms[self.on_platform].vy*-1
            # elif game.platforms[self.on_platform].vy > 0:
            #     ERROR = game.platforms[self.on_platform].vy

            ERROR = 15
            
            if game.platforms[self.on_platform].y -ERROR <= self.y+self.r <= game.platforms[self.on_platform].y+ERROR:
                platform_vx = game.platforms[self.on_platform].vx*game.platforms[self.on_platform].dir                
            if self.y+self.r >= game.platforms[self.on_platform].y-10:
                platform_vy = game.platforms[self.on_platform].vy*game.platforms[self.on_platform].dir
        # ---------------------------------------------

        # update y and x value of man
        self.y += self.vy + platform_vy
        self.x += self.vx + platform_vx        
        
        # to ensure man stays in the center
        if self.x >= game.w//2:
            game.x += self.vx    
        
    def display(self):
        self.update()
        # slicing because two different images being used for standing and running
        if self.vx != 0:
            self.slice = (self.slice+0.2)%self.F
            self.dir = self.vx
            self.standing = False            
        else:
            self.slice = 0
            self.standing = True

        # displaying man
        if self.dir > 0:
            if self.standing == True: # displaying standing
                self.img = loadImage(PATH+"/images/{0}.png".format('stand'))
                image(self.img, self.x-self.r-game.x,self.y-self.r,115,self.h)
            else: # displaying running
                self.img = loadImage(PATH+"/images/{0}.png".format('run4'))
                image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.slice)*self.w,0,(int(self.slice)+1)*self.w,self.h)
        elif self.dir < 0:
            if self.standing == True: # displaying standing
                self.img = loadImage(PATH+"/images/{0}.png".format('stand'))
                image(self.img, self.x-self.r-game.x,self.y-self.r,115,self.h,115,0,0,self.h)
            else: # displaying running
                self.img = loadImage(PATH+"/images/{0}.png".format('run4'))
                image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.slice+1)*self.w,0,int(self.slice)*self.w,self.h)
                
        
        # stroke(255,0,0)
        # strokeWeight(3)
        # line(self.x-game.x,self.g,self.x+2*self.r-game.x,self.g)

class Pickup:
    def __init__(self,p,r,w,h,img): # class for Hasanaat
        self.x = p[0]
        self.y = p[1]
        self.r = r
        self.w = w
        self.h = h
        self.img = loadImage(PATH+"/images/{0}.png".format(img))
        self.collected = False
    
    def display(self):
        image(self.img,self.x-self.r-game.x,self.y-self.r)

class Infopoint(): # class for displaying info within the level
    def __init__(self,x,y,info):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 200
        self.img = loadImage(PATH+"/images/infopoint.png") # image of the 'i' - same for all infopoints
        self.info = loadImage(PATH+"/images/{0}.png".format(info)) # image to be displayed - different for different infopoints - contains only the text
    
    def display(self):
        image(self.img, self.x-game.x, self.y)

    def displayInfo(self):
        tint(255, 180)
        image(black, 0, 0)
        tint(255,255)
        image(self.info,0,0)
        
class Checkpoint(): # class for checkpoints
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 160
        self.h = 200
        self.active = False # to check whether the checkpoint has been activated
        self.saved_x_value = 0 # stores the x value to return the man to it
        self.img = loadImage(PATH+"/images/checkpoint.png")
        
    def display(self):
        image(self.img, self.x-game.x, self.y-self.h)
        
    def setActive(self): 
        # condition ensures if char goes back, already active checkpoints do not take priority over the activated checkpoint that is furthest from the start
        if self.active == False and game.man.x>=self.x:#game.w//2 - ERROR_FOR_COLLISION <= self.x-game.x <= game.w//2 + ERROR_FOR_COLLISION:
            self.active = True
            self.saved_x_value = game.man.x # saves man's x value
            game.active_checkpoints.append(self) # appends the checkpoint to the list of active checkpoints    
        
class Chaser: # chasing enemy - moves horizontally 
    def __init__(self,p,min_x, max_x, r,w,h,img,speed = 1):
        self.x = p[0]
        self.y = p[1]
        self.min_x = min_x # min x value for the movement
        self.max_x = max_x # max x value for the movement
        self.r = r
        self.w = w
        self.h = h
        self.speed = speed
        self.img = loadImage(PATH+"/images/{0}.png".format(img))

    def display(self):
        self.update()
        image(self.img,self.x-game.x,self.y)
    
    def update(self): # chasing the man
        if game.man.x -10 <= self.x <= game.man.x +10 or game.man.x <= self.min_x or game.man.x >= self.max_x:
            pass
        elif self.x < game.man.x:
            self.x += self.speed
        elif self.x > game.man.x:
            self.x -= self.speed
        
class Platform: # stationary platform class
    def __init__(self,p,w,h,img):
        self.x = p[0]
        self.y = p[1]
        self.w = w
        self.h = h
        self.img = loadImage(PATH+"/images/{0}.png".format(img))
        self.p2 = None

    def display(self):
            image(self.img, self.x-game.x, self.y)
        
class VanishPlatform(Platform):
    def __init__(self,p,w,h,img,wait):
        Platform.__init__(self,p,w,h,img)
        self.wait = wait # decides the time to show and vanish - in seconds
        self.show = True
        self.last_switch = millis() # stores the time for the last switch    
    
    def display(self):
        if millis() < self.last_switch + (1000*self.wait): # keep showing or vanishing for the length of the wait time
            if self.show == True:
                image(self.img, self.x-game.x, self.y)
        else: # run once every time wait time has passes
            self.last_switch = millis() 
            self.show = not self.show # switches show to vanish and vice versa     

class MovingPlatform: # class for moving platform
    # moves in all directions: horizontal, vertical, and at any other gradient as well - between any two points
    def __init__(self,p1,p2,w,h,img,speed = 1):
        self.img = loadImage(PATH+"/images/{0}.png".format(img))
        self.w = w
        self.h = h
        
        self.x = p1[0]
        self.y = p1[1]
        self.p1 = p1 # point 1
        self.p2 = p2 # point 2

        # assign a direction depending on point 1's x and point 2's x
        if self.p1[0] < self.p2[0]:
            self.dir = 1
        elif self.p1[0] > self.p2[0]:
            self.dir = -1
        else: # if equal, meaning no horizontal movement, only vertical movement, use y values to compare instead
            if self.p1[1] < self.p2[1]:
                self.dir = 1
            elif self.p1[1] > self.p2[1]:
                self.dir = -1
        
        if self.p1[0] != self.p2[0]: # do not run for vertical movements that have no horizontal movement
            self.gradient = float(self.p1[1]-self.p2[1])/(self.p1[0]-self.p2[0])
            # to ensure inclined movements with higher gradients do not move quicker
            # ensures overall movement is of 1(*speed) --- d = sqrt(x^2 + y^2) = 1 
            self.vx = (sqrt(1/(1+sq(self.gradient))))*speed # speed to control the speed
            self.vy = (self.gradient*self.vx)
        else: # for vertical movements with no horizontal movement
            self.vx = 0
            self.vy = 1*speed
            self.gradient = None
            
    def display(self):
        self.update()
        image(self.img,self.x-game.x, self.y)
    
    def update(self): 
        if self.p1[0] < self.p2[0]: # update direction at end points of movement
            if self.x > self.p2[0] or self.x < self.p1[0]:
                self.dir = self.dir*-1
        elif self.p1[0] > self.p2[0]:
            if self.x > self.p1[0] or self.x < self.p2[0]:
                print(1)
                self.dir = self.dir*-1
        else: # for purely veritcal movements with no horizontal movements, do it using y values
            if self.p1[1] < self.p2[1]:
                if self.y > self.p2[1] or self.y < self.p1[1]:
                    self.dir = self.dir*-1
            elif self.p1[1] > self.p2[1]:
                if self.y > self.p1[1] or self.y < self.p2[1]:
                    self.dir = self.dir*-1
        # increment or decremenet
        self.y += self.vy*self.dir
        self.x += self.vx*self.dir                
        
class VibEnemy(MovingPlatform): # inherits from moving platform class
    def __init__(self,p1,p2,r,w,h,img,speed = 1):
        MovingPlatform.__init__(self,p1,p2,w,h,img,speed)
        self.r = r

    def display(self):
        self.update()
        image(self.img,self.x-self.r-game.x,self.y-self.r)
        
class Game:
    def __init__(self,w,h,g):
        # self.pause = False
        self.state = 'menu' # for state of game: takes values: 'menu' 'how to play' 'play' 'game over' 'high scores' 
        self.x=0
        self.w=w
        self.h=h
        self.g=g
        self.man = Man(100,100,50,self.g,"run4",137,100,7)

        self.begin_time = 0 # stores begin time for score keeping - score is the time taken to finish the level
        self.scores_file = 'highscores.txt' # file name that stores all scores
        self.name = '' # stores name of the player
        
        self.bg_imgs = []  # background     
        for i in range(1,6):
            self.bg_imgs.append(loadImage(PATH+"/images/layer_0{0}.png".format(i)))

        self.healthbars = [] # contains all healthbar images
        for i in range(1,6):
            self.healthbars.append(loadImage(PATH+"/images/hbar{0}.png".format(i)))

        self.platforms = [] # contains al platforms
        
        # stationary platforms
        self.platforms.append(Platform([1000,500],165,50,"platform1"))
        self.platforms.append(Platform([self.w,350],165,50,"platform1"))
        self.platforms.append(Platform([self.w+1100,100],165,50,"platform1"))
        self.platforms.append(Platform([2*self.w+100,500],165,50,"platform1"))
        self.platforms.append(Platform([2*self.w+700,300],165,50,"platform1"))
        self.platforms.append(Platform([3*self.w+700,450],165,50,"platform1"))
        self.platforms.append(Platform([4*self.w+400,200],165,50,"platform1"))
        
        # moving platforms
        self.platforms.append(MovingPlatform([self.w+200,100],[self.w+200,400],320,50,"platform2",2))
        self.platforms.append(MovingPlatform([self.w+600,100],[self.w+800,400],165,50,"platform1",5))
        self.platforms.append(MovingPlatform([2*self.w+150,350],[self.w*2+600,400],165,50,"platform1",5))
        self.platforms.append(MovingPlatform([2*self.w+850,225],[self.w*2+1200,450],165,50,"platform1",1))
        self.platforms.append(MovingPlatform([3*self.w+150,250],[self.w*3+150,500],165,50,"platform1",1))
        self.platforms.append(MovingPlatform([3*self.w+900,450],[self.w*3+1050,200],165,50,"platform1",1))
        
        # vanishing platforms
        self.platforms.append(VanishPlatform([3*self.w+350,200],165,50,"platform1",2))
        self.platforms.append(VanishPlatform([4*self.w+100,225],165,50,"platform1",1))
        self.platforms.sort(key = self.sortPlatform)

        # self.platform3 = CircularPlatform([100,100],[500,500],True,1,"platform1")
        # self.platform2 = MultiStop([100,600],[100,200],[600,100],5,"platform1")
        
        self.enemies = [] # contains both types of enemies
        self.enemies.append(Chaser([self.w,475],1000,self.w+500,35,70,70,"peach",5))
        self.enemies.append(VibEnemy([self.w+700,400],[self.w+700,100],35,70,70,"donut",5))
        self.enemies.append(VibEnemy([self.w+600,525],[self.w+1000,525],35,70,70,"donut",5))
        self.enemies.append(VibEnemy([2*self.w+425,350],[2*self.w+450,175],35,70,70,"donut",4))
        self.enemies.append(Chaser([self.w*2+850,475],self.w*2+250,self.w*2+1000,35,70,70,"donut",5))
        self.enemies.append(VibEnemy([3*self.w+300,250],[3*self.w+350,450],35,70,70,"donut",4))
        self.enemies.append(VibEnemy([3*self.w+900,400],[3*self.w+1200,400],35,70,70,"donut",4))
        
        self.checkpoints = [] # contains ALL checkpoints
        self.checkpoints.append(Checkpoint(800, self.h-150))
        self.checkpoints.append(Checkpoint(2*self.w, self.h-150))
        self.checkpoints.append(Checkpoint(3*self.w, self.h-150))
        
        self.active_checkpoints = [] # contains ONLY activated checkpoints
        
        self.infopoints = [] # contains all infopoints
        self.infopoints.append(Infopoint(400, 400, "info1"))

        self.hasanaat = [] # contains all pickups
        self.hasanaat.append(Pickup([self.w+400,50],50,100,100,"hasanaat"))
        self.hasanaat.append(Pickup([self.w+1200,200],50,100,100,"hasanaat"))
        self.hasanaat.append(Pickup([2*self.w+750,250],50,100,100,"hasanaat"))
        self.hasanaat.append(Pickup([3*self.w+600,50],50,100,100,"hasanaat"))
        self.hasanaat.append(Pickup([4*self.w+475,150],50,100,100,"hasanaat"))
        
        self.bg_sound = player.loadFile(PATH+"/sounds/bgnasheed.mp3")
        self.bg_sound.rewind()
        self.bg_sound.play()
        
    def sortPlatform(self,x): # sorting platforms
        return x.y
    
    def display(self):
        if self.state == 'menu':
            image(mosque,0,0,self.w,self.h)

            fill(255)
            textSize(100)
            textAlign(CENTER,CENTER)
            text('FAST TO THE END',self.w//2,self.h//4)
            
            if  500 <= mouseX <= 800 and 325 <= mouseY <= 375: # turn yellow
                fill(255,255,0)
            else:
                fill(255)
                
            textSize(50)
            text("Play Game",self.w//2,350) # clicking on this sets menu -> 'play'
            
            if 475 <= mouseX <= 825 and 425 <= mouseY <= 475: # turn yellow
                fill(255, 255, 0)
            else:
                fill(255)
                
            # textSize(50)
            # textAlign(CENTER,CENTER) # clicking on this sets menu -> 'how to play'
            text('How to Play',self.w//2, 450)
            
            if 475 <= mouseX <= 825 and 525 <= mouseY <= 575: # turn yellow
                fill(255, 255, 0)
            else:
                fill(255)
                
            # textSize(50)
            # textAlign(CENTER,CENTER)
            text('High Scores',self.w//2, 550) # clicking on this sets menu -> 'high scores'
        
        elif self.state == 'how to play': # how to play section
            image(mosque,0,0,game.w,game.h)
            tint(255, 128)
            image(black, 0, 0)
            tint(255,255)
            image(howtoinfo,0,0)
            
            textSize(20)
            text("Press ENTER to go back", self.w//2, 50)
            
        elif self.state == 'play':
            if self.begin_time == 0: # run only once
                self.begin_time = millis() # note begin time after play has been clicked
    
            cnt = 5
            for img in self.bg_imgs: # display bgs
                    
                x = self.x//cnt
                
                # portion 1
                image(img, 0, 0, self.w-x%self.w, self.h, int(x)%self.w, 0, self.w, self.h)
                
                # portion 2            
                image(img, self.w-x%self.w, 0, x%self.w, self.h, 0, 0, int(x)%self.w, self.h)
                
                # if self.bg_imgs.index(img) == 4:
                #     self.water.display(cnt)
                
                if self.bg_imgs.index(img) not in [1,2]: # display both cloud images at the same rate as the moon and the lantern image
                    cnt -= 1
                    
            for c in self.checkpoints: # display checkpoints
                c.display()
                c.setActive() # set checkpoint active
            
            for i in self.infopoints: # display infopoints
                i.display()
                
            for p in self.platforms: # display platforms
                p.display()    
            
            if len(self.hasanaat) != 0: # display hasanaat pickups if all have not been collected already
                for h in self.hasanaat:
                    h.display()
                        
            self.man.display() # display playable character: man
            
            if len(self.hasanaat) == 0: # game over condition - winning conclusion
                self.state = 'game over'
                self.win = True 
                
            for e in self.enemies: # display enemies
                e.display()    
            
            if self.man.death == True: # in case of collision with food
                if self.man.health == 1: # game over condition - losing conclusion
                    self.state = 'game over'
                    self.win = False
                else:
                    if len(self.active_checkpoints) == 0: # if no checkpoints, return to beginning
                        game.x = 0
                    else: # return to last checkpoint
                        game.x = self.active_checkpoints[-1].saved_x_value-self.w//2
                        self.man.x = self.active_checkpoints[-1].saved_x_value
                        
                    self.man.health -= 1
                    self.man.death = False
            
            image(self.healthbars[self.man.health-1],0,0) # display healthbars
    
            stroke(255)
            textSize(20)
            textAlign(LEFT)
            text("HASANAAT: " + str(len(self.hasanaat))+ " LEFT",1280-245,30) # display how many hasanaat still need to be collected before game can end
            self.score = millis()-self.begin_time # updates score
            text("TIME ELAPSED: " + str(self.score//1000) + "." + str((self.score%1000)//100), 1280-245,60) # store score in readable format
            
            for i in self.infopoints: # display the info when man close to the infopoint
                if i.x - 50 <= self.man.x <= i.x + i.w:
                    i.displayInfo()
                    
        elif self.state == 'game over': # game over
            image(mosque,0,0,game.w,game.h)
            tint(255, 128)
            image(black, 0, 0)
            tint(255, 255)
                        
            fill(255)
            textSize(32)
            textAlign(CENTER)
            if self.win == False: # in case of win, return to meny, no score
                text("You were not able to collect all 5 Hasanaat, better luck next time...", self.w//2,self.h//2)
                textSize(20)
                text("Press ENTER to go back to the menu", self.w//2, self.h//2+200)
            elif self.win == True: # in case of loss, input score
            # elif len(self.collected_hasanaat) == 5:
                self.readScores() # read previous scores from text file
                # new high score condition, uses 2nd item for each item (item is list itself of format [name,score]) in self.highscores
                if len(self.highscores) == 0 or self.score >= max(self.highscores, key = lambda x:int(x[1])): 
                    text("CONGRATS! You collected all 5 hasanaat AND did it in record time.", game.w//2, game.h//2-200)
                else:
                    text('CONGRATS! You collected all 5 hasanaat.',self.w//2,self.h//2-200)
                text("Your score: {0}.{1} seconds only".format(self.score//1000,(self.score%1000)//100), self.w//2, self.h//2-100)
                text('Enter your name and press ENTER:', self.w//2, self.h//2)
                text(self.name,self.w//2,self.h//2+100) # display name as it is being typed

        elif self.state == 'high scores': # high scores
            image(mosque,0,0,game.w,game.h)
            tint(255, 128)
            image(black, 0, 0)
            tint(255,255)
            
            self.readScores() # read scores and sort them
            
            fill(255)
            textAlign(CENTER)
            textSize(50)
            text("High Scores (seconds)", game.w//2, 230)
            
            textAlign(LEFT)
            textSize(24)
            i = 1
            for score in self.highscores:
                if i <= 7: # dislay 7 top scores in readable format
                    text("{0}. {1}: {2}.{3}".format(i,score[0],int(score[1])//1000,(int(score[1])%1000)//100), self.w//2-100, 300 + 35*i)
                i += 1

            textAlign(CENTER)
            textSize(20)
            text("Press ENTER to exit.", self.w//2, self.h - 100)
            
    def writeScore(self): # write a score to the file
        f = open(self.scores_file, 'a')
        f.write(self.name + ',' + str(self.score) + '\n')
        f.close()
    
    def readScores(self): # reads scores and sorts them as well
        self.highscores = [] # to store scores
        newfile = open(self.scores_file,'r')
        for line in newfile:
            fileline = line.strip().split(',') # fileline = [name,score]
            self.highscores.append(fileline)
        self.highscores.sort(key = lambda x:int(x[1])) # sort using score
        newfile.close()

black = loadImage(PATH+"/images/black.png")
mosque = loadImage(PATH+"/images/mosque.png")
# enemies = ["donut","blue-fruit","orange","peach","pizza","burger","apple","hotdog","meat"]
howtoinfo = loadImage(PATH+"/images/info1.png")
                
game = Game(1280,720,570)

myFont = PFont() 
def setup():
    background(255,255,255)
    size(game.w,game.h)
    
    myFont = loadFont("CooperBlack-48.vlw") # font
    textFont(myFont, 28)
    
def draw():
    game.display()
    
def keyPressed():
    if game.state == 'play': # move character
        if keyCode == LEFT:
            game.man.keyHandlers[LEFT] = True
        elif keyCode == RIGHT:
            game.man.keyHandlers[RIGHT] = True
        elif keyCode == UP:
            game.man.keyHandlers[UP] = True
            
    elif game.state == 'how to play': # take back to menu upon press of enter
        if key == ENTER:
            game.state = 'menu'
                    
    elif game.state == 'game over':
        if game.win == False: # take back to menu upon press of enter in case of loss
            if key == ENTER:
                game.__init__(1280,720,570)
        elif game.win == True: # input name in case of win
            if key == ENTER: # save score and show highscores
                game.writeScore() 
                game.state = 'high scores'
            elif key == BACKSPACE: # remove last entered character
                game.name = game.name[:-1]
            elif key == ',': # skip over all of these
                pass
            elif keyCode == LEFT:
                pass
            elif keyCode == RIGHT:
                pass
            elif keyCode == UP:
                pass
            else:
                game.name += str(key) # add to the name
            
    elif game.state == 'high scores':
        if key == ENTER: # create a new game, returns to menu by default
            game.__init__(1280,720,570)
    
def keyReleased(): # movement
    if keyCode == LEFT:
        game.man.keyHandlers[LEFT] = False
    elif keyCode == RIGHT:
        game.man.keyHandlers[RIGHT] = False
    elif keyCode == UP:
        game.man.keyHandlers[UP] = False
   
def mouseClicked(): # used on menu
    if game.state == "menu":
        if  500 <= mouseX <= 800 and 325 <= mouseY <= 375:
        # if  500 <= mouseX <= 650 and 275 <= mouseY <= 300:
            game.state = "play"
        elif 475 <= mouseX <= 825 and 425 <= mouseY <= 475:
            game.state = "how to play"
        elif 475 <= mouseX <= 825 and 525 <= mouseY <= 575:
            game.state = 'high scores' 
    
