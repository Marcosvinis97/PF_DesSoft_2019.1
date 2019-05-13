# -*- coding: utf-8 -*-
"""Created on Thu May  9 19:41:42 2019
Testando pymunk no pyglet
"""

import pyglet  # pip install pyglet
from pyglet.window import key, mouse
import pymunk # pip install pymunk
from pymunk.pyglet_util import DrawOptions
from math import sqrt
import random

width = 720
height = 480
FPS = 60
window = pyglet.window.Window(width, height, "Pymunk Testing", resizable = False)
options = DrawOptions()
options.collision_point_color = (0,0,0,255)
space = pymunk.Space()
space.gravity = 0, -300
space.idle_speed_threshold = 1000
space.sleep_time_threshold = 50 

class Ball():
    def __init__(self,radius,mass,position):
        self.radius = radius
        self.mass = mass
        self.moment = pymunk.moment_for_circle(self.mass,0,self.radius,(0,0))
        self.body = pymunk.Body(self.mass,self.moment, pymunk.Body.DYNAMIC )
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
        self.shape = pymunk.Segment(space.static_body,self.start_point,self.end_point,self.thickness)
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


# CRIAÇÃO DO PLAYER (CONTROLÁVEL)
player = Ball(25,100,(width/2,height/2))
player.shape.elasticity = 1
player.shape.friction = 0
space.add(player.existence)

# ELEMENTOS DINÂMICOS:
player2 = Ball(30,20,(35,height-30))
#player2.body.velocity = (random.randint(-100,100),random.randint(-100,100))
space.add(player2.existence)

# ELEMENTOS CINÉTICOS (SOLIDOS QUE NÃO SOFREM EFEITOS DE FORÇAS)
triangle = Poly(100,((0,0),(100,0),(0,100)),(2,2))
triangle.shape.friction = 0
triangle.body.body_type = pymunk.Body.KINEMATIC
triangle2 = Poly(100,((0,0),(100,0),(100,100)),(102,0))
triangle2.shape.friction = 0
triangle2.body.body_type = pymunk.Body.KINEMATIC
space.add(triangle.existence,triangle2.existence)

# ELEMENTOS ESTÁTICOS:
segment1 = Segment((0,0),(width,0),2)
segment2 = Segment((width,0),(width,height),2)
segment3 = Segment((width,height),(0,height),2)
segment4 = Segment((0,height),(0,80),2)
space.add(segment1.shape, segment2.shape, segment3.shape, segment4.shape)



running = True
@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    if running:
        space.step(dt)

@window.event
def on_key_press(symbol,modifiers):
    # AUMENTA A VELOCIDADE NOS RESPECTIVOS SENTIDOS
    if symbol == key.RIGHT:
        player.body.velocity += 300,0
    if symbol == key.LEFT:
        player.body.velocity -= 300,0
    if symbol == key.UP:
        player.body.velocity += 0,300
    if symbol == key.DOWN:
        player.body.velocity -= 0,300
    # GRAVIDADE ZERO
    if symbol == key.SPACE:
        if space.gravity == (0, -300):
            space.gravity = 0,0
        else:
            space.gravity = 0,-300
    # PARA O TEMPO (USO NÃO RECOMENDADO CASO HAJA MUITOS ELEMENTOS NO ESPAÇO)
    if symbol == key.T:
        for bodies in space.bodies:
            if bodies.body_type == pymunk.Body.DYNAMIC:
                if not bodies.is_sleeping:
                    bodies.sleep()
                else:
                    bodies.activate()
    # FECHA O JOGO
    if symbol == key.ESCAPE:
        running = False
                
@window.event
def on_mouse_press(x,y,button,modifiers):
    # LADO DIREITO ADICIONA 1 QUADRADO CINÉTICOS NA POSIÇÃO DO MOUSE
    if button & mouse.RIGHT:
        box = Box(50,(25,25),(x,y))
        box.body.body_type = pymunk.Body.KINEMATIC
        space.add(box.existence)
    # LADO ESQUERDO ADICIONA 1 QUADRADO DINÂMICO NA POSIÇÃO DO MOUSE
    if button & mouse.LEFT:
        box = Box(50,(25,25),(x,y))
        space.add(box.existence)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update,1/60)
    pyglet.app.run()





