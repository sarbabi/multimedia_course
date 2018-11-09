#author: 941149002
#exercise: Project: a simple bowling animation (page 108)

from pyglet.gl import *
import time


class SingleImageAnimation(pyglet.window.Window):

    def __init__(self, width=None, height=None):
        """the init method
        define the variables and objects
        """
        super().__init__(width=width, height=height, resizable=True)
        self.drawableObjects = []
        self.rising = False
        self.ballSprite = None
        self.pinSprite = None
        self.createDrawableObjects()
        self.adjustWindowSize()
        self.paused = False
        self.pinHorizontal = False

    def createDrawableObjects(self):
        """
        method for create the objects
        """
        ball_img = pyglet.image.load('images/ball.png')
        ball_img.anchor_x = ball_img.width // 2
        ball_img.anchor_y = ball_img.height // 2
        pin_img = pyglet.image.load('images/pin.png')
        pin_img.anchor_x = (pin_img.width // 4) * 3
        pin_img.anchor_y = 0
        self.ballSprite = pyglet.sprite.Sprite(ball_img)
        self.ballSprite.position = (0 + 100, self.ballSprite.height)
        self.pinSprite = pyglet.sprite.Sprite(pin_img)
        self.pinSprite.position = (self.ballSprite.width * 2 + 200, self.ballSprite.height // 2)
        # Add these sprites to the list of drawables
        self.drawableObjects.append(self.pinSprite)
        self.drawableObjects.append(self.ballSprite)

    def adjustWindowSize(self):
        """
        method for define the size of window
        """
        w = self.ballSprite.width * 100
        h = self.ballSprite.height * 10
        self.width = w
        self.height = h

    def moveObjects(self, t):
        """
        method for moving objects
        """

        if self.pinHorizontal:
            self.ballSprite.x = 100

        if self.ballSprite.x + self.ballSprite.width / 2 < self.pinSprite.x - self.pinSprite.width / 2:
            if self.ballSprite.x == 100:
                time.sleep(1)
                self.pinSprite.rotation = 0
                self.pinHorizontal = False

            self.ballSprite.x += 5
            self.ballSprite.rotation += 5

        if self.ballSprite.x + self.ballSprite.width / 2 >= self.pinSprite.x - self.pinSprite.width / 2:
            self.pinSprite.rotation += 5
            if self.pinSprite.rotation == 90:
                self.pinHorizontal = True

    def on_key_press(self, key, modifiers):
        """
        method for setting the keys
        """
        if key == pyglet.window.key.P and not self.paused:
            pyglet.clock.unschedule(self.moveObjects)
            self.paused = True
        elif key == pyglet.window.key.R and self.paused:
            pyglet.clock.schedule_interval(self.moveObjects, 1.0 / 30)
            self.paused = False

    def on_draw(self):
        self.clear()
        for d in self.drawableObjects:
            d.draw()


win = SingleImageAnimation()
# Set window background color.
pyglet.gl.glClearColor(0.5, 0.5, 0.9, 1)

pyglet.clock.schedule_interval(win.moveObjects, 1.0 / 30)

pyglet.app.run()
