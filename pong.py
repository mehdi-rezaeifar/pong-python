import random
from turtle import color, onkeypress, speed
import arcade
from time import sleep

class player1(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.color=arcade.color.GREEN_YELLOW
        self.width = 30
        self.height=80
        self.speed=6
        self.score=0
        self.center_x=(game.width/2)-450
        self.center_y=game.height/2
        self.score=0
        self.screen_height=game.height
        
    def harkat(self):
        self.center_y += self.change_y*self.speed
    def draw (self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

class player2(arcade.Sprite):

    def __init__(self,game):
        super().__init__()
        self.color=arcade.color.PURPLE_HEART
        self.width = 30
        self.height=80
        self.speed=5
        self.score=0
        self.center_x=(game.width/2)+450
        self.center_y=game.height/2
        self.h=game.height
        self.score=0
    def harkat(self):      
        self.center_y += self.change_y*self.speed    
    def draw (self):
         arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)       
        
class Ball(arcade.Sprite):
    def __init__(self,game) :
        super().__init__()
        self.color=arcade.color.WHITE_SMOKE
        self.r=15
        self.center_x=game.width/2
        self.center_y=game.height/2
        self.width=22
        self.height=22
        self.speed=5
        self.screen_height=game.height/2
        self.change_x=-0.5
        self.change_y=1
        self.hitter=0
        self.first_time=True
    def harkat (self):
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

class game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280,height=600,title="Amin Pong Game")
        self.background_color=arcade.color.BLACK
        self.ball=Ball(self)#important
        self.player1=player1(self)
        self.player2 = player2(self)
        self.hit_upper_wall=False
        self.hit_lower_wall=False
        self.down_press=True
        self.up_press=True
    def on_key_press(self, symbol,modifier):
        if symbol == arcade.key.UP :
                self.player1.change_y=1
                self.player1.change_x=0
        elif symbol == arcade.key.DOWN :
            self.player1.change_y=-1
            self.player1.change_x=0
    def on_key_release(self, symbol,modifier): 
        if symbol == arcade.key.UP:
                self.player1.change_y=0
                self.player1.change_x=0
        elif symbol == arcade.key.DOWN:
            self.player1.change_y=0
            self.player1.change_x=0
    def on_update(self,delta_time):
        self.player2.harkat()
        self.player1.harkat()
        if(int(self.ball.center_y)>self.ball.screen_height*2-20):
            self.hit_upper_wall=True
            self.hit_lower_wall=False
            if(self.ball.first_time):
                
                self.ball.change_x =  -0.5
                self.ball.change_y = -1
                self.ball.first_time=False
        if(int(self.ball.center_y)<self.ball.r):
            self.hit_upper_wall=False
            self.hit_lower_wall=True
        if(arcade.check_for_collision(self.player1,self.ball)):
            self.ball.hitter=1
            if(self.ball.center_y<=self.player1.center_y+self.player1.height/2 and
            self.ball.center_y>self.player1.center_y+self.player1.height/3 ):
                self.ball.change_x = random.uniform(1, 2)
                self.ball.change_y = random.uniform(1, 2)
            elif(self.ball.center_y<=self.player1.center_y+self.player1.height/3 and
            self.ball.center_y>self.player1.center_y-self.player1.height/3 and self.hit_upper_wall ):
                self.ball.change_x = random.uniform(1, 2)
                self.ball.change_y = random.uniform(-.6, -0.4)
            elif(self.ball.center_y<=self.player1.center_y+self.player1.height/3 and
            self.ball.center_y>self.player1.center_y-self.player1.height/3 and self.hit_lower_wall ):
                self.ball.change_x = random.uniform(1, 2)
                self.ball.change_y = random.uniform(0.4, 0.6)
            elif(self.ball.center_y<=self.player1.center_y-self.player1.height/3 and
            self.ball.center_y>=self.player1.center_y-self.player1.height/2 ):
                self.ball.change_x = random.uniform(1, 2)
                self.ball.change_y = random.uniform(-2, -1)
        elif(arcade.check_for_collision(self.player2,self.ball)):
            self.ball.hitter=2
            if(self.ball.center_y<=self.player2.center_y+self.player2.height/2 and
            self.ball.center_y>self.player2.center_y+self.player2.height/3 ):
                self.ball.change_x = random.uniform(-1, -2)
                self.ball.change_y = random.uniform(1, 2)
            elif(self.ball.center_y<=self.player2.center_y+self.player2.height/3 and
            self.ball.center_y>self.player2.center_y-self.player2.height/3 and self.hit_upper_wall ):
                self.ball.change_x = random.uniform(-1, -2)
                self.ball.change_y = random.uniform(-.6, -0.4)
            elif(self.ball.center_y<=self.player2.center_y+self.player2.height/3 and
            self.ball.center_y>self.player2.center_y-self.player2.height/3 and self.hit_lower_wall ):
                self.ball.change_x = random.uniform(-1, -2)
                self.ball.change_y = random.uniform(0.4, 0.6)
            elif(self.ball.center_y<=self.player2.center_y-self.player2.height/3 and
            self.ball.center_y>=self.player2.center_y-self.player2.height/2 ):
                self.ball.change_x = random.uniform(-1, -2)
                self.ball.change_y = random.uniform(-2, -1)
        if(int(self.ball.center_y)>self.ball.screen_height*2-20):
            self.hit_upper_wall=True
            self.hit_lower_wall=False
            if(self.ball.hitter==1):
                self.ball.change_x =  1
                self.ball.change_y = -1
            elif(self.ball.hitter==2):
                self.ball.change_x =  -1
                self.ball.change_y = -1
        if(int(self.ball.center_y)<self.ball.r):
            self.hit_upper_wall=False
            self.hit_lower_wall=True
            if(self.ball.hitter==1):
                self.ball.change_x =  1
                self.ball.change_y = 1
            elif(self.ball.hitter==2):
                self.ball.change_x =  -1
                self.ball.change_y = 1        
        if (self.ball.center_x+150<self.player1.center_x ):
                self.player2.score += 1
                self.ball=Ball(self)
        if( self.ball.center_x-150>self.player2.center_x):
                self.player1.score += 1
                self.ball=Ball(self)
        self.ball.harkat()
        if(self.ball.center_y<self.player2.center_y):
            self.player2.change_y=-1
        elif(self.ball.center_y>self.player2.center_y):
            self.player2.change_y=+1
        elif(self.ball.center_y==self.player2.center_y):
            self.player2.center_y=self.ball.center_y
        if(self.player1.center_y+self.player1.height/2>=self.player1.screen_height-self.player1.height/4):  
                self.player1.change_y=0
        if(self.player1.center_y-self.player1.height/2<=self.player1.height/4):    
                 self.player1.change_y=0
    def on_draw(self):
        arcade.start_render()
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        text = f"Score: {self.player1.score}"
        arcade.draw_text(text,self.width/50,self.height-100,arcade.color.WHITE,25,font_name=("Times New Roman","Times","Liberation Serif"  ))

        text = f"Score: {self.player2.score}"
        arcade.draw_text(text,18*self.width/20,self.height-100,arcade.color.WHITE,25,font_name=("Times New Roman","Times","Liberation Serif" ))   
pong=game()
arcade.run()