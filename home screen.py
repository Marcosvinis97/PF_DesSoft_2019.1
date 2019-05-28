import pyglet
import pymunk

def assassin_space(space):
    mass = 91
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius) 
    body = pymunk.Body(mass, inertia) 
    body.position = 50, 80 
    shape = pymunk.Circle(body, radius) 
    space.add(body, shape) 
    return shape 

def add_static_line(space):
    body = pymunk.Body() 
    body.position = (0,0)
    floor = pymunk.Segment(body, (0, 20), (300, 20), 0)
    # space.add_static(floor) 
    return floor

class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch, img, space):
        self.space = space
        pyglet.sprite.Sprite.__init__(self, img, self.space.body.position.x, self.space.body.position.y)

    def update(self):
        self.x = self.space.body.position.x
        self.y = self.space.body.position.y

class Game(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 315, height = 220)
        self.batch_draw = pyglet.graphics.Batch()
        self.player1 = Assassin(batch = self.batch_draw, img = pyglet.image.load("icon.png"), space = assassin_space(space))
        pyglet.clock.schedule(self.update)
        add_static_line(space)

    def on_draw(self):
        self.clear()
        self.batch_draw.draw()
        self.player1.draw() 
        space.step(1/50.0) 

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            print ("The 'UP' key was pressed")

    def update(self, dt):
        self.player1.update()
        space.step(dt)

if __name__ == "__main__":
    space = pymunk.Space() #
    space.gravity = (0.0, -900.) #
    window = Game()
    pyglet.app.run()