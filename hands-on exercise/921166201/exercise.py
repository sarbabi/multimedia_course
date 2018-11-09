#author: 921166201
#exercise: Time for action – bouncing ball animation (page 102)


import pyglet
import time
from pyglet.image.codecs.png import PNGImageDecoder

class SingleImageAnimation(pyglet.window.Window):
    def __init__(self, width = None, height = None):
        pyglet.window.Window.__init__(self,
                                      width = width,
                                      height = height,
                                      resizable = True)
        self.drawableObjects = []
        self.rising = False
        self.ballSprite = None
        self.paused = False
        self.createDrawableObjects()
        self.adjustWindowSize()

    def createDrawableObjects(self):
        """
        Create sprite objects that will be drawn within the
        window.
        """
        ball_img= pyglet.image.load('images/ball.png', decoder=PNGImageDecoder())
        ball_img.anchor_x = ball_img.width / 2
        ball_img.anchor_y = ball_img.height / 2

        self.ballSprite = pyglet.sprite.Sprite(ball_img)
        self.ballSprite.position = (self.ballSprite.width + 100,
                                     self.ballSprite.height*2 - 50)

        self.drawableObjects.append(self.ballSprite)

    def adjustWindowSize(self):
        """
        Resizes the pyglet window.
        """
        w = self.ballSprite.width*3
        h = self.ballSprite.height*3
        self.width = w
        self.height = h

    def on_draw(self):
        """
        Overrides pyglet.window.Window.on_draw to draw the sprite.
        """
        self.clear()
        for d in self.drawableObjects:
            d.draw()

    def on_key_press(self, key, modifiers):
        """
        Overrides pyglet.window.Window.on_key_press to handle
        key presee event
        """
        if key == pyglet.window.key.P and not self.paused:
            pyglet.clock.unschedule(self.moveObjects)
            self.paused = True
        elif key == pyglet.window.key.R and self.paused:
            pyglet.clock.schedule_interval(win.moveObjects, 1.0/20)
            self.paused = False

    def moveObjects(self, t):
        """
        Move the image sprites / play the sound .
        This method is scheduled to be called every 1/N seconds using
        pyglet.clock.schedule_interval.
        """
        if self.ballSprite.y - 100 < 0:
            self.rising = True
        elif self.ballSprite.y > self.ballSprite.height*2 - 50:
            self.rising = False

        if not self.rising:
            self.ballSprite.y -= 5
            self.ballSprite.rotation -= 6
        else:
            self.ballSprite.y += 5
            self.ballSprite.rotation += 5

win = SingleImageAnimation()

# Set window background color to white.
r, g, b, alpha = 1, 1, 1, 1
pyglet.gl.glClearColor(r, g, b, alpha)

# Schedule the method win.moveObjects to be called every
# 0.05 seconds.
pyglet.clock.schedule_interval(win.moveObjects, 1.0/20)


pyglet.app.run()


