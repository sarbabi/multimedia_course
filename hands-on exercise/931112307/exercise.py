#author: 931112307
#exercise: Time for action – raindrops animation (page 114)
import pyglet
import time

class RainDropsAnimation(pyglet.window.Window):
    def __init__(self, width = None, height = None):
        pyglet.window.Window.__init__(self,
                                      width = width,
                                      height = height)
        self.drawableObjects = []
        self.createDrawableObjects()

    def createDrawableObjects(self):
        num_rows = 4
        num_columns = 1
        droplet = "C:\\Images\\droplet.png"
        animation = self.setup_animation(droplet,
                                         num_rows,
                                         num_columns)
        self.dropletSprite = pyglet.sprite.Sprite(animation)
        self.dropletSprite.position = (0,0)

        self.drawableObjects.append(self.dropletSprite)

    def setup_animation(self, img, num_rows, num_columns):

        base_image = pyglet.image.load(img)
        animation_grid = pyglet.image.ImageGrid(base_image,
                                                num_rows,
                                                num_columns)
        image_frames = []

        for i in range(num_rows*num_columns, 0, -1):
            frame = animation_grid[i-1]
            animation_frame = pyglet.image.AnimationFrame(frame, 0.2)
            image_frames.append(animation_frame)

        animation = pyglet.image.Animation(image_frames)
        return animation

    def on_draw(self):

        self.clear()
        for d in self.drawableObjects:
            d.draw()


win = RainDropsAnimation()
r, g, b, alpha = 1, 1, 1, 1
pyglet.gl.glClearColor(r, g, b, alpha)
pyglet.app.run()
