import pygame
import random
pygame.init()
import os


class startGame(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image=pygame.image.load(os.path.join(os.getcwd(),'static','screens','titleScreen.png'))
        self.color=[(255,0,0),(0,255,0),(0,0,255),(27,10,35),(32,32,32),(153,0,153),(51,0,51)]
        self.check=0
        self.nu=1
    def showStartMenu(self,screen):
        self.check+=1
        if self.check==10:
            self.nu=random.randint(0,6)
            self.check=0
        screen.fill(self.color[self.nu])
        screen.blit(self.image,(self.x,self.y))
    
    




class menuButtons(object):
    def __init__(self,x,y,overlay,screen):
        self.x=x
        self.y=y
        self.width=280
        self.height=120
        self.screen=screen
        self.font=pygame.font.SysFont('comicsans',60)
        self.overlay=overlay
        self.color=(255,255,255)
    

    def draw(self):
        pygame.draw.rect(self.screen,(0,0,0),(self.x-30,self.y-120,self.width+60,self.height),0)
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height),0)
        if self.overlay != '':
            font=pygame.font.SysFont('comicsans',60)
            text=font.render("INSTRUCTIONS",1,(255,255,255))
            self.screen.blit(text,(self.x+(self.width/2 - text.get_width()/2),self.y-120+(self.height/2 - text.get_height()/2)))
        if self.color ==(255,255,255):
            tex=font.render("INSTRUCTIONS",1,(255,255,255))
            self.screen.blit(tex,(self.x+(self.width/2 - text.get_width()/2),self.y-120+(self.height/2 - text.get_height()/2)))
            text=font.render(self.overlay,1,(0,0,0))
            self.screen.blit(text,(self.x+(self.width/2 - text.get_width()/2),self.y+(self.height/2 - text.get_height()/2)))
        else:
            tex=font.render("INSTRUCTIONS",1,(255,255,255))
            self.screen.blit(tex,(self.x+(self.width/2 - text.get_width()/2),self.y-120+(self.height/2 - text.get_height()/2)))
            text=font.render(self.overlay,1,(255,255,255))
            self.screen.blit(text,(self.x+(self.width/2 - text.get_width()/2),self.y+(self.height/2 - text.get_height()/2)))


    
    def mousePos(self,pos):
        x=pos[0]
        y=pos[1]
        if x>=self.x and x<=self.x+self.width:
            if y>=self.y and y<=self.y+self.height:
                self.color=(0,0,0)
                mouse=pygame.mouse.get_pressed()
                if mouse[0]==1:
                    return True
                
            else:
                self.color=(255,255,255)
        else:
            self.color=(255,255,255)
        if x>=self.x-30 and x<=self.x+self.width+60:
            if (y >= self.y - 120) and (y<=self.y+self.height):
                mouse=pygame.mouse.get_pressed()
                if mouse[0]==1:
                    return 2

        
        
class GameOver(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.show='YOU ARE DEAD!'
        self.screen = screen
        self.bg=(255,0,0)
        self.buttonbg=(255,0,0)
        self.textbg=(255,255,255)
        self.font=pygame.font.SysFont('comicsans',60)        
        self.fg=(255,255,255)

    def showFailed(self,pos,score):
        mx=pos[0]
        my=pos[1]

        if mx>=self.x+300 and mx<=self.x+300+280:
            if my>self.y+390 and mx<self.y+390+120:
                self.buttonbg=(255,255,255)
                self.textbg=(255,0,0)
                mouse=pygame.mouse.get_pressed()
                if mouse[0]==1:
                    return True
        else:
            self.buttonbg=(255,0,0)
            self.textbg=(255,255,255)



        self.screen.fill(self.bg)
        text=self.font.render(self.show,1,(self.fg))
        self.screen.blit(text,(self.x+300,self.y+280))
        pygame.draw.rect(self.screen,self.buttonbg,(self.x+300,self.y+390,280,120),0)
        text=self.font.render("PLAY AGAIN",1,self.textbg)
        t=self.font.render("You killed "+str(score),1,(255,255,255))
        self.screen.blit(t,((self.x+300)+(280/2 - text.get_width()/2),(self.y+320)+(120/2 - text.get_height()/2)))
        self.screen.blit(text,((self.x+300)+(280/2 - text.get_width()/2),(self.y+390)+(120/2 - text.get_height()/2)))



class HealthBar(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y
        self.screen=screen
        self.fg=(255,0,0)
        self.bg=(0,0,255)
        self.dead=0
        self.reducer=5
        self.healthAvail=25

    def showBar(self,x,y):
        self.x=x
        self.y=y
        bgRect=pygame.draw.rect(self.screen,self.bg,(self.x,self.y,100,10))
        bgRect=pygame.draw.rect(self.screen,self.fg,(self.x,self.y,self.healthAvail,10))

    def healthUpgrade(self,val):
        if self.healthAvail<=100:
            self.healthAvail+=val
    



    def hurt(self,val):
        self.healthAvail-=10
        if self.healthAvail<=0:
            self.dead=1
    
    
