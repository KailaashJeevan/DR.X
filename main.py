import pygame
import random
import math
import menu
import os


pygame.init()

#Game Defaults
screen=pygame.display.set_mode((840,640))
bgList=[pygame.image.load(os.path.join(os.getcwd(),'static','bgMain.png')),pygame.image.load(os.path.join(os.getcwd(),'static','bgAsse.png'))]
run_state=True
villanControlSystem=[]
killCount=0
order=[1,1,1,0,1,0,1,0,0,1]
enemyWeaponList=[]
enemyShootTime=0
pygame.display.set_caption("DR.X")
x2=bgList[1].get_width()
preScreen=0
villanHeroCollCheck=0
postScreen=840
imgCon=0


######################## SOCORE VARIABLE###########
score=0

#Flow##############################################################
###########################GAME
####FLOW
###################################
menu_Loader=True
plause_menu=False
player_died=False
game_on=False
click_state=False
######################################
####################################
#############################
#BackgroundLoader
run_bg=True
bgs=[pygame.image.load(os.path.join(os.getcwd(),'static','bgMain.png')),pygame.image.load(os.path.join(os.getcwd(),'static','bgAsse.png'))]

#MenuItems
menu_screen=menu.startGame(0,0)
startGameBtn=menu.menuButtons(280,480,"START GAME",screen)
##### AUDIO LOADS###############
try:
    bgm=pygame.mixer.music.load(os.path.join(os.getcwd(),'static','auSources','bgm.mp3'))
    pygame.mixer.music.play()
    wScream=pygame.mixer.Sound(os.path.join(os.getcwd(),'static','auSources','cri-d-effroi-scream.wav'))
    evilLaugh=pygame.mixer.Sound(os.path.join(os.getcwd(),'static','auSources','EvilLaugh.wav'))
    fireBall=pygame.mixer.Sound(os.path.join(os.getcwd(),'static','auSources','Fireball+1.wav'))
    monster=pygame.mixer.Sound(os.path.join(os.getcwd(),'static','auSources','monst.wav'))

except:
    print("FROM THE AUTHOR OF THE GAME: KAILAASH JEEVAN J")
    print("SEEMS THERE IS SOME ERROR!")
    print("PLEASE RE-RUN THE SCRIPT IT WILL WORK.Try deleting the __pycache__ folder and re-run")
    print("The GAME was BUILT on A LINUX MACHINE")


#########HERO CLASS################
class hero(object):
    def __init__(self,x,screen):
        self.x=x
        self.jump=15
        self.hero_stand=pygame.image.load(os.path.join(os.getcwd(),'static','hero','standing.png'))
        self.hero_run=[pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk2.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','walk1.png'))]
        self.y=480
        self.hero_jump=[pygame.image.load(os.path.join(os.getcwd(),'static','hero','jump1.png')),pygame.image.load(os.path.join(os.getcwd(),'static','hero','jump2.png'))]
        self.screen=screen
        self.health=100
        self.jump_mode=False
        self.look=1
    
    def screenPlayerStand(self,x,y):
        screen.blit(self.hero_stand,(x,y))

    def run(self,c):
        image=self.hero_run[c]
        show=image
        if self.look ==-1:
            show=pygame.transform.flip(image,True,False)
        if not self.jump_mode:
            screen.blit(show,(self.x,self.y))
    
    def jumping(self):
        #JUMPING
        if self.y<440:
            image=self.hero_jump[1]
            show=image
            if self.look==-1:
                show=pygame.transform.flip(image,True,False)
            screen.blit(show,(self.x,self.y))
        else:
            image=self.hero_jump[0]
            show=image
            if self.look==-1:
                show=pygame.transform.flip(image,True,False)
            screen.blit(show,(self.x,self.y))
        if self.jump_mode:
            if hero.jump>=-15:
                self.y-=(hero.jump * 2)
                self.jump-=1

            else:
                self.jump=15
                self.jump_mode=False




##########################TARGET CLASS#########################

class target(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen
        self.img=pygame.image.load(os.path.join(os.getcwd(),'static','screens','target.png'))
    
    def showOff(self):
        self.screen.blit(self.img,(self.x,self.y))





##################   ENEMY#  #################


class enemy(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen
        self.img=[pygame.image.load(os.path.join(os.getcwd(),'static','ENEMY','enemy stand.png')),pygame.image.load(os.path.join(os.getcwd(),'static','ENEMY','enemy stand2.png'))]
        self.swifter=0
        self.unit=1
        self.health=30
        self.show=self.img[0]
        self.adder=0

        
    def move(self):
        self.adder+=30

        if self.adder ==300:
            self.adder=0
            if self.swifter==1:
                self.swifter=0
            else:
                self.swifter=1
        # print(str(self.adder)+':'+str(self.swifter))
        if self.x < 40 and self.unit == -1:
            self.unit=1
            
            
        elif self.x > 710 and self.unit == +1:
            self.unit=-1
            
        
        if self.unit==1:
            image=self.img[self.swifter]
            self.show=pygame.transform.flip(image,True,False)
        else:
            image=self.img[self.swifter]
            self.show=image
        lover=random.randint(1,10)
        trancer=random.randint(1,lover)
        
        self.screen.blit(self.show,(self.x,self.y))
        
        self.x+=8*self.unit
###################### ENEMY WEAPON SHOOT#############
# ####################################################
# #####################################################

class enemyProjectile(object):
    def __init__(self,x,y,screen,aimx,aimy):
        self.x=x
        self.y=y
        self.aimx=aimx
        self.speed=8
        self.aimy=aimy
        self.screen=screen
        self.color=(255,0,0)

    def shoot(self):
        if self.aimx<self.x:
            self.x-=self.speed
        else:
            self.x+=self.speed
            
        if self.aimy<self.y:
            self.y-=self.speed
        else:
            self.y+=self.speed

        pygame.draw.circle(self.screen,self.color,(self.x,self.y),7)
        


########################################
###########      BULLET ##########

class bullet(object):
    def __init__(self,x,y,aimx,aimy,screen):
        self.x=x
        self.y=y
        self.aimx=aimx
        self.aimy=aimy
        self.speed=8
        self.screen=screen
        self.img=pygame.image.load(os.path.join(os.getcwd(),'static','ENEMY','ememy weapon.png'))

    def shoot(self):
        if self.aimx<self.x:
            self.x-=self.speed
        else:
            self.x+=self.speed
            
        if self.aimy<self.y:
            self.y-=self.speed
        else:
            self.y+=self.speed
            
            

            
        self.screen.blit(self.img,(self.x,self.y))

############################   M-FUNCTIONS ##################

def showScore(score):
    t="Kills:  "+str(score)
    font=pygame.font.SysFont('comicsans',60)
    text=font.render(t,1,(255,25,55))
    screen.blit(text,(10,10))

def checkDistance(x1,y1,x2,y2):
    dist=math.sqrt((math.pow((x2-x1),2)-(math.pow((y2-y1),2))))
    return dist





def moveScr():
    global postScreen
    global preScreen
    global run_bg
    global imgCon
    if hero.x> 415 and run_bg:
        preScreen-=5
        if preScreen < 0:
            postScreen-=5
            if (postScreen <= 0 or preScreen==0) and run_bg:
                if imgCon <len(order):

                    imgCon+=1
                    if imgCon+1==len(order):
                        imgCon=0
                    wScream.play()
                    if healthbar.healthAvail+10<=100:
                        healthbar.healthAvail+=10
                    for i in range(imgCon+1):
                        vx=random.randint(590,700)
                        vy=random.randint(100,480)
                        xy=random.randint(10,40)
                        villanControlSystem.append(enemy(vx+xy,vy,screen))
                preScreen=3
                postScreen=837
                
    if imgCon <len(order)-1:
        screen.blit(bgs[order[imgCon]],(preScreen,0))
    else:
        screen.blit(bgs[order[imgCon]],(preScreen,0))
        screen.blit(bgs[order[imgCon]],(postScreen,0))
        run_bg=False
    if imgCon+1 < len(order):
        screen.blit(bgs[order[imgCon+1]],(postScreen,0))

##################################################################
        
total=0
inst=pygame.image.load(os.path.join(os.getcwd(),'static','instructions.png'))
istDo=False
hero_x=0

############CLASS ASSIGNS##############################
hero=hero(0,screen)
aim=target(500,400,screen)
healthCheck=0
villan=enemy(712,480,screen)
bgCountCheck=0
look=1
gameOverEvent=menu.GameOver(0,0,screen)
#Bullet
# enemyWeapon=enemyProjectile(0,0,screen,840,640)
ListAllBullets=[]
bulletTaker=100
count_Run=0
istDo=True
menu_Loader=False
clock=pygame.time.Clock()
healthbar=menu.HealthBar(hero.x,hero.y-50,screen)


###############################################
############################GAME STARTES#######
###############################################


while run_state:

    keys=pygame.key.get_pressed()

    for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run_state=False




    if menu_Loader:
        healthbar.healthAvail=25
        healthbar.dead=0
        villanControlSystem=[]
        hero.x=0
        imgCon=0
        score=0
        enemyWeaponList=[]
        menu_screen.showStartMenu(screen)
        startGameBtn.draw()
        click_state=startGameBtn.mousePos(pygame.mouse.get_pos())
        if click_state==True or keys[pygame.K_RETURN]:
            menu_Loader=False
            player_died=False
            game_on=True
            plause_menu=False
        if click_state ==2:
            istDo=True
            menu_Loader=False
            player_died=False
            game_on=False
            plause_menu=False


    elif istDo:
        screen.blit(inst,(0,0))
        if keys[pygame.K_ESCAPE]:
            istDo=False
            menu_Loader=True
            player_died=False
            game_on=False
            plause_menu=False





    elif game_on:
        clock.tick(30)
        # screen.blit(bgs[0],(0,0))
        moveScr()

        

        #KeyPressessc
        
        if hero.x==416:
            if not keys[pygame.K_d]:
                hero.x=415
        
        if keys[pygame.K_a]:
            if count_Run < 30:
                if hero.x>-30:
                    hero.x-=8
                    hero.look=-1
                    count_Run+=round(15/3)
            else:
                count_Run=0
        elif keys[pygame.K_d]:
                if count_Run < 30 and hero.x<413:
                    hero.x+=8
                    hero.look=1
                    total+=5

                    count_Run+=round(15/3)
                elif hero.x>414 and run_bg:
                    total+=8
                    count_Run+=round(15/3)
                    hero.x=416
                elif not run_bg:
                    hero.x+=5
                    hero.look=1
                    total+=5
                    count_Run+=round(15/3)
                    if hero.x>839:
                        hero.x=838
                else:
                    count_Run=0
    






        if keys[pygame.K_SPACE] and not hero.jump_mode:
            hero.jump_mode=True
            
        ##############TERGET MOVEMENT################
        if keys[pygame.K_RIGHT]:
            if aim.x>718:
                aim.x=715
            aim.x+=30
        if keys[pygame.K_LEFT]:
            if aim.x<10:
                aim.x=15
            aim.x-=30
        if keys[pygame.K_DOWN]:
            if aim.y>540:
                aim.y=539
            aim.y+=30
        if keys[pygame.K_UP]:
            if aim.y<10:
                aim.y=15
            aim.y-=30


            
    
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and len(ListAllBullets)<=10:
            if bulletTaker>=100 :
                bulletTaker=0
                ListAllBullets.append(bullet(hero.x,hero.y,aim.x,aim.y,screen))
            bulletTaker+=18
            


        # hero.screenPlayerStand(hero_x,0)
        if count_Run>=30:
            count_Run=0


        

        if hero.jump_mode:
            hero.jumping()
        hero.run(count_Run)

        #Villan Stuff
        for villan in villanControlSystem:
            villan.move()
            monster.play()
            try:
                villanHeroCollCheck=checkDistance(villan.x,villan.y,hero.x,hero.y)
                if villanHeroCollCheck<=100:
                    if healthCheck>100:
                        healthCheck=0
                        healthbar.hurt(8)
                    else:
                        healthCheck+=10
            except:
                pass

            if enemyShootTime==200:
                enemyShootTime=0
                enemyWeaponList.append(enemyProjectile(villan.x,villan.y,screen,hero.x,hero.y+30))
            else:
                enemyShootTime+=10
        for e in enemyWeaponList:
            e.shoot()
            try:
                dist=checkDistance(e.x,e.y,hero.x,hero.y)
                if dist <8:
                    healthbar.healthAvail-=5
            except:
                pass
            if abs((e.aimx-e.x)/e.speed)<=1:
                if abs((e.aimy-e.y)/e.speed)<=1:
                    enemyWeaponList.pop(enemyWeaponList.index(e))




        aim.showOff()
        for b in ListAllBullets:
            b.shoot()
            fireBall.play()
            for e in villanControlSystem:
                try:
                    dist=checkDistance(e.x,e.y,b.x,b.y)
                    if dist<150:
                        if killCount>50:
                            e.health-=8
                            ListAllBullets.pop(ListAllBullets.index(b))
                        else:
                            killCount+=1
                    if e.health<=0:
                        if healthbar.healthAvail+5<=100:
                            healthbar.healthAvail+=5
                        villanControlSystem.pop(villanControlSystem.index(e))
                        score+=1
                except:
                    pass        
            # print(str(b.aimy)+"::"+str(b.y))
            # print(str(b.aimx)+"::"+str(b.x))
            try:
                if (b.aimy == b.y or abs(b.aimy-b.y)<=b.speed):
                    if ( b.aimx==b.x or (abs(b.aimx-b.x)<=b.speed)):
                        ListAllBullets.pop(ListAllBullets.index(b))
            except:
                pass

        healthbar.showBar(hero.x+20,hero.y-20)
        showScore(score)
        if healthbar.dead==1:
            menu_Loader=False
            player_died=True
            game_on=False
            plause_menu=False
    elif player_died:
        playAgain=False
        evilLaugh.play()
        playAgain=gameOverEvent.showFailed(pygame.mouse.get_pos(),score)       
        if playAgain:
            menu_Loader=True
            player_died=False
            game_on=False
            plause_menu=False
    pygame.display.update()
