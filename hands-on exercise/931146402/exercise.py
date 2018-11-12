#author: 931146402
#exercise: Time for action – bouncing ball animation (page 102)

import pyglet
import time

class SingleImageAnimation(pyglet.window.Window):
  def __init__(self, width=600, height=600):
    pyglet.window.Window.__init__(self,
    width=width,
    height=height,
    resizable = True)
    self.drawableObjects = []
    self.rising = False
    self.ballSprite = None
    self.createDrawableObjects()
    self.adjustWindowSize()
  def createDrawableObjects(self):
    """
    Create sprite objects that will be drawn within the
    window.
    """
    ball_img= pyglet.image.load('images/ball.png')
    ball_img.anchor_x = ball_img.width / 2
    ball_img.anchor_y = ball_img.height / 2
    self.ballSprite = pyglet.sprite.Sprite(ball_img)
    self.ballSprite.position = (
      self.ballSprite.width + 100, 
      self.ballSprite.height*2 - 50)
    self.drawableObjects.append(self.ballSprite)
  def adjustWindowSize(self):
     w = self.ballSprite.width * 3
     h = self.ballSprite.height * 3
     self.width = w
     self.height = h
  def moveObjects(self, t):
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
  def on_draw(self):
    self.clear()
    for d in self.drawableObjects:
      d.draw()
win = SingleImageAnimation()
# Set window background color to gray.
pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)  

pyglet.clock.schedule_interval(win.moveObjects, 1.0/20)

pyglet.app.run()

