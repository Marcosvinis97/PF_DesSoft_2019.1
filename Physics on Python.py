# -*- coding: utf-8 -*-

# ----------------------------------------------BIBLIOTECAS -------------------------------------------------------
# Pyglet
import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
#Pymunk
import pymunk # pip install pymunk
from pymunk.pyglet_util import DrawOptions
from pymunk.vec2d import Vec2d
#Math
from math import sqrt, degrees
import random

class Player():
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
        self.vida = 1000
        
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
        self.combustivel = 3000
        self.existence = self.body,self.shape

class Segment():
    def __init__(self,start_point,end_point,thickness): # start e end_point = (x,y)
        self.start_point = start_point
        self.end_point = end_point
        self.thickness = thickness
        self.space = pymunk.Space()
        self.shape = pymunk.Segment(self.space.static_body,self.start_point,self.end_point,self.thickness)
        self.shape.elasticity = 0.0001
        self.shape.friction = 1

class Dot():
    def __init__(self, point):
        self.point = point
        self.thickness = 3
        self.space = pymunk.Space()
        self.shape = pymunk.Segment(self.space.static_body,self.point,self.point,self.thickness)
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
        self.vida = 1000


# --------------------------------------------CLASSE PRINCIPAL---------------------------------------------------
class Game:
    def __init__(self):
        self.width = 1350
        self.height = 595
        self.FPS = 60
        self.window = pyglet.window.Window(self.width,self.height,"Physics On Python", resizable = False)
        icon = pyglet.image.load('icon.png')
        self.window.set_icon(icon)
        #Music
        #music = pyglet.media.load('winter.wav', streaming = False)
        #music.play()
        self.screen = IntroScreen(self)
        self.register_event_handlers()

    def register_event_handlers(self):
        self.window.on_mouse_press = self.screen.on_mouse_press
        self.window.on_key_press = self.screen.on_key_press
        self.window.on_draw = self.screen.on_draw

    def change_screen(self,symbol):
        if symbol == key._1:
            self.screen = AnotherScreen(self)
            self.register_event_handlers()
        if symbol == key._2:
            self.screen = CarScreen(self)
            self.register_event_handlers()
        if symbol == key.ESCAPE:
            self.screen = IntroScreen(self)
            self.register_event_handlers()            

    def run(self):
        pyglet.app.run()
        
    
#-------------------------------------------------- OBJECTS ------------------------------------------------------------


collision_types = {
        "player":1}

class Player():
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
        
        self.shape.collision_type = collision_types["player"]
      #  joint = pymunk.GrooveJoint(AnotherScreen.space.static_body,self,(100,100),(1180,100),(0,0))
        
        self.existence = self.body, self.shape
        self.vida = 1000
        
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
        self.combustivel = 3000
        self.existence = self.body,self.shape

class Segment():
    def __init__(self,start_point,end_point,thickness): # start e end_point = (x,y)
        self.start_point = start_point
        self.end_point = end_point
        self.thickness = thickness
        self.space = pymunk.Space()
        self.shape = pymunk.Segment(self.space.static_body,self.start_point,self.end_point,self.thickness)
        self.shape.elasticity = 0.0001
        self.shape.friction = 1

class Dot():
    def __init__(self, point):
        self.point = point
        self.thickness = 3
        self.space = pymunk.Space()
        self.shape = pymunk.Segment(self.space.static_body,self.point,self.point,self.thickness)
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
        self.vida = 1000


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
        self.animation = pyglet.image.load_animation("jump.gif")

        self.animSprite = pyglet.sprite.Sprite(self.animation,x=0, y=game.height-300)

        #Labels (texts on screen)
        self.label = pyglet.text.Label("Simulador Físico Lunar",
                                    font_name = "Cambria Math",
                                    font_size = 40,
                                    color = (0, 0, 0, 255),
                                    x = self.window.width *0.6,
                                    y = self.window.height / 2,
                                    anchor_x = "center",
                                    anchor_y = "center" )
        self.welcome = pyglet.text.Label("Aperte 1 para Aeronave, Aperte 2 para carro",
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
        if symbol == key._1 or symbol == key._2:
            print("Mudando de tela")
            self.game.change_screen(symbol)

    def on_draw(self):
        self.window.clear() # cleaning the window
        self.image.blit(0,0) #putting the image
        self.label.draw() # writing the label (title, for example)
        self.welcome.draw()
        self.animSprite.draw()

class AnotherScreen(Screen):
    def __init__(self, game):
        super(AnotherScreen, self).__init__(game)

        pyglet.clock.schedule_interval(self.update,1/60)
        #Pymunk specifications
        self.options = DrawOptions()
        self.options.collision_point_color = (0,0,0,255)
        self.space = pymunk.Space()
        self.space.gravity = 0, -100
        self.space.idle_speed_threshold = 10
        self.space.sleep_time_threshold = 500
        # Pymunk Space

        self.player = Player(10,( (0,0),(171/5, 0),(171/10,300/5) ),(game.width/2,game.height/2))
        self.player.body.center_of_gravity = ( (0 + 171/5 + 171/10)/3, 300/15)
        self.player.body.elasticity = 0.0001
        self.player.body.friction = 1
        self.player_image = pyglet.image.load("nave.png")
       # self.player_image.anchor_x, self.player_image.anchor_y = self.player_image.width//2, self.player_image.height//2
        self.player_sprite = pyglet.sprite.Sprite(self.player_image, x = self.player.body.position[0], y = self.player.body.position[1])
        self.player.combustivel = 3000
        self.space.add(self.player.existence)

        self.bussola = pyglet.image.load("bussola.png")
        self.bussola.anchor_x, self.bussola.anchor_y = self.bussola.width//2, self.bussola.height//2
        self.bussola_sprite = pyglet.sprite.Sprite(self.bussola, x = game.width-50, y = game.height-50)
        
            # ELEMENTOS ESTÁTICOS:
        self.segment1 = Segment((0,13),(game.width,13),2)
        self.segment2 = Segment((game.width,0),(game.width,game.height),2)
        self.segment3 = Segment((game.width,game.height),(0,game.height),2)
        self.segment4 = Segment((0,game.height),(0,80),2)
        self.space.add(self.segment1.shape, self.segment2.shape, self.segment3.shape, self.segment4.shape)
        
        
        self.background = pyglet.resource.image("Plano_Game1.png")
        self.solo = pyglet.resource.image("Solo.png")
        

        self.texts = [self.player.body.velocity, 
                      self.player.body.position,
                      self.player.body.angle,
                      self.player.body.angular_velocity,
                      self.player.combustivel,
                      self.player.vida]
        self.status = [0]*len(self.texts)
        for i in range(len(self.texts)):
            self.status[i] = pyglet.text.Label("{}".format(self.texts[i]),
                                    font_name = "Arial",
                                    font_size = 10,
                                    color = (100, 255, 0, 255),
                                    x = game.width -200,
                                    y = game.height -50 - (21*i),
                                    anchor_x = "left",
                                    anchor_y = "center",
                                    align = "left")
        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = self.coll_begin
        self.handler.pre_solve = self.coll_pre
        self.handler.post_solve = self.coll_post
        self.handler.separate = self.coll_separate
        self.player.vida = 1000

    def on_mouse_press(self, x, y, button, modifier):
        # LADO DIREITO ADICIONA 1 QUADRADO CINÉTICOS NA POSIÇÃO DO MOUSE
        if button & mouse.RIGHT:
            box = Box(50,(25,25),(x,y))
            box.body.body_type = pymunk.Body.KINEMATIC
            self.space.add(box.existence)
        # LADO ESQUERDO ADICIONA 1 QUADRADO DINÂMICO NA POSIÇÃO DO MOUSE
        if button & mouse.LEFT:
            box = Box(50,(25,25),(x,y))
            self.space.add(box.existence)

    def on_key_press(self, symbol, modifiers):
        
        if self.player.combustivel > 0 :
            # AUMENTA A VELOCIDADE NOS RESPECTIVOS SENTIDOS
            if symbol == key.RIGHT:
                self.player.body.angular_velocity -= 1
                self.player.combustivel -= 10
            if symbol == key.LEFT:
                self.player.body.angular_velocity += 1
                self.player.combustivel -= 10
            if symbol == key.UP:
                self.player.body.apply_impulse_at_local_point((0,1000),self.player.body.center_of_gravity)
                self.player.combustivel -= 10
            if symbol == key.DOWN:
                self.player.body.apply_impulse_at_local_point((0,-1000),self.player.body.center_of_gravity)
                self.player.combustivel -= 10
            if symbol == key.ESCAPE:
                game.change_screen(symbol)

               
            # GRAVIDADE ZERO
            if symbol == key.SPACE:
                if self.space.gravity == (0, -300):
                    self.space.gravity = 0,0
                else:
                    self.space.gravity = 0,-300
                    # PARA O TEMPO (USO NÃO RECOMENDADO CASO HAJA MUITOS ELEMENTOS NO ESPAÇO)
            if symbol == key.T:
                for bodies in self.space.bodies:
                    if bodies.body_type == pymunk.Body.DYNAMIC:
                        if not bodies.is_sleeping:
                            bodies.sleep()
                        else:
                            bodies.activate()

    def on_key_release(self,symbol,modifiers):
       if symbol in (key.RIGHT,key.LEFT):
           self.player.body.angular_velocity = 0
     

    def update(self,dt): #dt é "data time"
#        for meteoro in self.meteoros:
#            self.meteoros[meteoro]["meteoro_image"].position,self.meteoros[meteoro]["meteoro_image"].rotation = self.meteoros[meteoro]["meteoro"].body.position, -degrees(self.meteoros[meteoro]["meteoro"].body.angle)

        self.player_sprite.position,self.player_sprite.rotation, self.bussola_sprite.rotation = self.player.body.position, -degrees(self.player.body.angle), -degrees(self.player.body.angle)

        self.space.step(dt)
        self.texts = ["player's velocity: {:.2f}".format(Vec2d(self.player.body.velocity)[0]), 
                      "player's position: {0:.2f},{1:.2f}".format(self.player.body.position[0],self.player.body.position[1]),
                      "player's angle: {:.2f}".format(self.player.body.angle),
                      "player's angular velocity: {:.2f}".format(self.player.body.angular_velocity),
                      "player's combustivel: {:.2f} L".format(self.player.combustivel),
                      "player's vida: {:.2f}".format(self.player.vida)]
        for i in range(len(self.status)):
            self.status[i] = pyglet.text.Label("{}".format(self.texts[i]),
                                    font_name = "Arial",
                                    font_size = 10,
                                    color = (100, 255, 0, 255),
                                    x = game.width -200,
                                    y = game.height -100 - (21*i),
                                    anchor_x = "left",
                                    anchor_y = "center",
                                    align = "center")
        
    def on_draw(self):
        self.space.debug_draw(self.options)
        self.window.clear()
#        for meteoro in self.meteoros:
#            self.meteoros[meteoro][sprite].draw()
        self.background.blit(0,0)
        self.bussola_sprite.draw(), self.player_sprite.draw()
        self.solo.blit(0,0)
        
        for i in range(len(self.texts)):
            self.status[i].draw()

    def coll_begin(self,arbiter,space,data):
        self.player.vida -= 10
        return True

    def coll_pre(self,arbiter,space,data):
        return True

    def coll_post(self,arbiter,space,data):
        print("post solve")
        return True
 
    def coll_separate(self,arbiter,space,data):
        print("separate")
        return True

class CarScreen(Screen):
    def __init__(self, game):
        super(CarScreen, self).__init__(game)

        pyglet.clock.schedule_interval(self.update,1/60)
        #Pymunk specifications
        self.options = DrawOptions()
        self.options.collision_point_color = (0,0,0,255)
        self.space = pymunk.Space()
        self.space.gravity = 0, 0
        self.space.idle_speed_threshold = 10
        self.space.sleep_time_threshold = 50
        # Pymunk Space
        self.distance_car_x = 300
        self.distance_car_y = 300
        self.car = Poly(50,( (0,0),(80,0),(80,30),(30,60),(0,60) ),(self.distance_car_x, self.distance_car_y))   
        self.car.body.center_of_gravity = (40,30)
        self.car.body.elasticity = 0.1
        self.car.body.friction = 1
        self.space.add(self.car.existence)
        
        self.roda_dianteira = Ball(20,20,(self.distance_car_x + 40, self.distance_car_y-30))
        self.roda_dianteira.shape.elasticity = 0.1
        self.roda_traseira = Ball(20,20,(self.distance_car_x- 50, self.distance_car_y-30))
        self.roda_traseira.shape.elasticity = 0.1
        self.c = pymunk.PinJoint(self.car.body, self.roda_traseira.body, (0, 0), (0, 0))
        self.e = pymunk.SlideJoint(self.car.body, self.roda_traseira.body, (0, 60), (0, 0), 81,  100)
        self.g = pymunk.DampedSpring(self.car.body, self.roda_traseira.body, (0, 60), (0, 0), 100, 1000,70)
        self.d = pymunk.PinJoint(self.car.body, self.roda_dianteira.body,(80,0), (0,0))
        self.f = pymunk.SlideJoint(self.car.body, self.roda_dianteira.body, (80,30), (0, 0), 60, 70)
        self.h = pymunk.DampedSpring(self.car.body, self.roda_dianteira.body, (80,30), (0,0), 100, 1000,65)
        self.space.add(self.c, self.d, self.roda_dianteira.existence, self.roda_traseira.existence, self.e, self.f, self.g, self.h)
  
        
            # ELEMENTOS ESTÁTICOS:
        self.segment1 = Segment((0,0),(game.width,0),2)
        self.segment2 = Segment((game.width,0),(game.width,game.height),2)
        self.segment3 = Segment((game.width,game.height),(0,game.height),2)
        self.segment4 = Segment((0,game.height),(0,0),2)
        self.space.add(self.segment1.shape, self.segment2.shape, self.segment3.shape, self.segment4.shape)

    def on_mouse_press(self, x, y, button, modifier):
        pass


    def on_key_press(self, symbol, modifiers):
        # AUMENTA A VELOCIDADE NOS RESPECTIVOS SENTIDOS
        if symbol == key.RIGHT:
            self.car.body.apply_impulse_at_local_point((10000,0),self.car.body.center_of_gravity)
        if symbol == key.LEFT:
            self.car.body.apply_impulse_at_local_point((-10000,0),self.car.body.center_of_gravity)
#        if symbol == key.UP:
#            self.player.body.velocity += (0,100)
#        if symbol == key.DOWN:
#            self.player.body.velocity -= (0,100)
        # GRAVIDADE ZERO
        if symbol == key.SPACE:
            if self.space.gravity == (0, -300):
                self.space.gravity = 0,0
            else:
                self.space.gravity = 0,-300
        # PARA O TEMPO (USO NÃO RECOMENDADO CASO HAJA MUITOS ELEMENTOS NO ESPAÇO)
        if symbol == key.T:
            for bodies in self.space.bodies:
                if bodies.body_type == pymunk.Body.DYNAMIC:
                    if not bodies.is_sleeping:
                        bodies.sleep()
                    else:
                        bodies.activate()
        if symbol == key.ESCAPE:
            game.change_screen(symbol)
    def update(self,dt): #dt é "data time
        self.space.step(dt)
        
    def on_draw(self):
        self.window.clear()
        self.space.debug_draw(self.options)
#-----------------------------------------------------start------------------------------------------------------------
if __name__ == '__main__': 
    game = Game()
    game.run()
