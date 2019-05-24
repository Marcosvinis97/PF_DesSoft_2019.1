# -*- coding: utf-8 -*-

# ----------------------------------------------BIBLIOTECAS -------------------------------------------------------
# Pyglet
import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
#Pymunk
import pymunk # pip install pymunk
from pymunk.pyglet_util import DrawOptions
#Math
from math import sqrt
import random
# --------------------------------------------CLASSE PRINCIPAL---------------------------------------------------
class Game:
    def __init__(self):
        #Creating a window
        self.width = 1280
        self.height = 720
        self.FPS = 60
        self.window = pyglet.window.Window(self.width,self.height,"Physics On Python", resizable = False)

        #Adding a icon
        icon = pyglet.image.load('icon.png')
        self.window.set_icon(icon)

        self.screen = IntroScreen(self)
        self.register_event_handlers()

    def register_event_handlers(self):
        self.window.on_mouse_press = self.screen.on_mouse_press
        self.window.on_key_press = self.screen.on_key_press
        self.window.on_draw = self.screen.on_draw

    def change_screen(self):
        self.screen = AnotherScreen(self)
        self.register_event_handlers()
        self.player = Ball(Ball,25,50,)

    def run(self):
        pyglet.app.run()

# -----------------------------------------------------SCREENS---------------------------------------------------
class Screen:
    def __init__(self, game):
        self.game = game
        self.window = self.game.window

    def on_mouse_press(self, x, y, button, modifier):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_draw(self):
        pass


class IntroScreen(Screen):
    def __init__(self, game):
        super(IntroScreen, self).__init__(game)

        #Adding image
        self.image = pyglet.resource.image("white.png")

        #Gif
        animation = pyglet.image.load_animation("jump.gif")
        self.animSprite = pyglet.sprite.Sprite(animation)

        #Labels (texts on screen)
        self.label = pyglet.text.Label("Physics On Python",
                                    font_name = "Cambria Math",
                                    font_size = 40,
                                    color = (0, 0, 0, 255),
                                    x = self.window.width *0.6,
                                    y = self.window.height / 2,
                                    anchor_x = "center",
                                    anchor_y = "center" )
        self.welcome = pyglet.text.Label("Bem vindo! Aperte ENTER para continuar",
                                    font_name = "Cambria Math",
                                    font_size = 20,
                                    color = (0, 0, 0, 255),
                                    x = self.window.width *0.6,
                                    y = self.window.height / 3,
                                    anchor_x = "center",
                                    anchor_y = "center" )

    def on_mouse_press(self, x, y, button, modifier):
        if button == mouse.LEFT:                                    
            print("The left mouse was pressed")
        elif button == mouse.RIGHT:
            print("Right Mouse was pressed")

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            print("Olá")
        if symbol == key.ENTER:
            print("Mudando de tela")
            self.game.change_screen()

    def on_draw(self):
        self.window.clear() # cleaning the window
        self.image.blit(0,0) #putting the image
        self.label.draw() # writing the label (title, for example)
        self.welcome.draw()
        self.animSprite.draw()

class AnotherScreen(Screen):
    def __init__(self, game):
        super(AnotherScreen, self).__init__(game)
        
        #Pymunk specifications
        self.options = DrawOptions()
        self.options.collision_point_color = (0,0,0,255)
        self.space = pymunk.Space()
        self.space.gravity = 0, -300
        self.space.idle_speed_threshold = 1000
        self.space.sleep_time_threshold = 50 
        # Pymunk Space
        self.player = Ball(25,100,(game.width/2,game.height/2))
        self.space.add(self.player.existence)
            # ELEMENTOS DINÂMICOS:
        # self.player2 = Ball(30,20,(35,height-30))
            #player2.body.velocity = (random.randint(-100,100),random.randint(-100,100))
        # self.space.add(player2.existence)
            # ELEMENTOS CINÉTICOS (SOLIDOS QUE NÃO SOFREM EFEITOS DE FORÇAS)
        self.triangle = Poly(100,((0,0),(100,0),(0,100)),(2,2))
        self.triangle.shape.friction = 0
        self.triangle.body.body_type = pymunk.Body.KINEMATIC
        self.triangle2 = Poly(100,((0,0),(100,0),(100,100)),(102,0))
        self.triangle2.shape.friction = 0
        self.triangle2.body.body_type = pymunk.Body.KINEMATIC
        self.space.add(self.triangle.existence,self.triangle2.existence)
            # ELEMENTOS ESTÁTICOS:
        self.segment1 = Segment((0,0),(game.width,0),2)
        self.segment2 = Segment((game.width,0),(game.width,game.height),2)
        self.segment3 = Segment((game.width,game.height),(0,game.height),2)
        self.segment4 = Segment((0,game.height),(0,80),2)
        self.space.add(self.segment1.shape, self.segment2.shape, self.segment3.shape, self.segment4.shape)
        

    def on_mouse_press(self, x, y, button, modifier):
        if button == mouse.LEFT:                                    
            print("The left mouse was pressed")
        elif button == mouse.RIGHT:
            print("Right Mouse was pressed")

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            print("Olá")
        if symbol == key.Q:
            print("Eba!")

    def on_draw(self):
        self.window.clear()
        self.space.debug_draw(self.options)


#-------------------------------------------------- OBJECTS ------------------------------------------------------------

class Ball():
    def __init__(self,radius,mass,position):
        self.radius = radius
        self.mass = mass
        self.moment = pymunk.moment_for_circle(self.mass,0,self.radius,(0,0))
        self.body = pymunk.Body(self.mass,self.moment, pymunk.Body.DYNAMIC)
        self.body.position = position
        self.shape = pymunk.Circle(self.body,self.radius,(0,0))
        self.shape.elasticity = 1
        self.body.velocity = 0,0
        self.shape.friction = 1.0
        self.existence = self.body,self.shape

class Segment():
    def __init__(self,start_point,end_point,thickness): # start e end_point = (x,y)
        self.start_point = start_point
        self.end_point = end_point
        self.thickness = thickness
        self.space = pymunk.Space()
        self.shape = pymunk.Segment(self.space.static_body,self.start_point,self.end_point,self.thickness)
        self.shape.elasticity = 0.9
        self.shape.friction = 1

class Dot():
    def __init__(self, point):
        self.point = point
        self.thickness = 3
        self.shape = pymunk.Segment(space.static_body,self.point,self.point,self.thickness)
        self.shape.elasticity = 1
        self.shape.friction = 1

class Box():
    def __init__(self, mass, size, position): # size = (largura, altura); position = (x_centro, y_centro)
        self.mass = mass
        self.size = size
        self.moment = pymunk.moment_for_box(self.mass,self.size)
        self.body = pymunk.Body(self.mass,self.moment, pymunk.Body.DYNAMIC)
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.body.position = position
        self.shape.elasticity = 0.6
        self.shape.friction = 1
        self.existence = self.shape,self.body

class Poly():
    def __init__(self,mass,vertices,position):
        self.mass = mass
        self.vertices = vertices
        self.shape = pymunk.Poly(None,self.vertices)
        self.moment = pymunk.moment_for_poly(self.mass, self.shape.get_vertices())
        self.body = pymunk.Body(self.mass,self.moment, pymunk.Body.DYNAMIC)
        self.shape.body = self.body
        self.body.position = position
        self.shape.elasticity = 1
        self.shape.friction = 1
        self.existence = self.body, self.shape

#-----------------------------------------------------start------------------------------------------------------------
if __name__ == '__main__': 
    game = Game()
    game.run()
