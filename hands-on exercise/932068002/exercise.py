#author: 932068002
#exercise: Time for action – raindrops animation (page 114)

import pyglet
import time

class RainDropsAnimation(pyglet.window.Window):
    def __init__(self, width = None, height = None):
        pyglet.window.Window.__init__(self, width = width, height = height)
        self.drawableObjects = []
        self.createDrawableObjects()

    def createDrawableObjects(self):
        """
        Create the objects (sprites) for drawing within the
        pyglet Window.
        """
        num_rows = 4
        num_columns = 1
        droplet = 'C:\\Users\\amir\\image\\droplet.png'
        animation = self.setup_animation(droplet, num_rows, num_columns)

        self.dropletSprite = pyglet.sprite.Sprite(animation)
        self.dropletSprite.position = (0,0)

        # Add these sprites to the list of drawables
        self.drawableObjects.append(self.dropletSprite)

    def setup_animation(self, img, num_rows, num_columns):
        """
        Create animation object using different regions of
        a single image.
        @param img: The image file path
        @type img: string
        @param num_rows: Number of rows in the image grid
        @type num_rows: int
        @param num_columns: Number of columns in the image grid
        @type num_columns: int
        """
        base_image = pyglet.image.load(img)
        animation_grid = pyglet.image.ImageGrid(base_image, num_rows, num_columns)
        image_frames = []

        for i in range(num_rows*num_columns, 0, -1):
            frame = animation_grid[i-1]
            animation_frame = pyglet.image.AnimationFrame(frame, 0.2)
            image_frames.append(animation_frame)

        animation = pyglet.image.Animation(image_frames)
        return animation

    def on_draw(self):
        """
        The overridden API method on_draw which is called when the Window
        needs to be re-drawn.
        """
        self.clear()
        for d in self.drawableObjects:
            d.draw()


# Create a Pyglet Window instance to show the animation.
win = RainDropsAnimation()

# Set window background color to white.
r, g, b, alpha = 1, 1, 1, 1
pyglet.gl.glClearColor(r, g, b, alpha)

pyglet.app.run()


