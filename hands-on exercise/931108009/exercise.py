import pyglet
import time

class RainyDayAnimation(pyglet.window.Window):
    def __init__(self, width = None, height = None):
        pyglet.window.Window.__init__(self,
                                      width = width,
                                      height = height,
                                      resizable = True)
        self.drawableObjects = []
        self.paused = False

        self.createDrawableObjects()
        self.adjustWindowSize()
        # Make sure to replace the following media path to
        # with an appropriate path on your computer.
        self.horn_sound =pyglet.media.load('data/horn.wav', streaming=False)

    def createDrawableObjects(self):
        """
        Create the objects (sprites) for drawing within the
        pyglet Window.
        """
        num_rows = 4
        num_columns = 1
        droplet = 'data/droplet.png'
        animation = self.setup_animation(droplet,
                                         num_rows,
                                         num_columns)

        self.dropletSprite = pyglet.sprite.Sprite(animation)
        self.dropletSprite.position = (0,200)

        cloud = pyglet.image.load('data/cloud.png')
        self.cloudSprite = pyglet.sprite.Sprite(cloud)
        self.cloudSprite.y = 100

        lightening = pyglet.image.load('data/lightening.png')
        self.lSprite = pyglet.sprite.Sprite(lightening)
        self.lSprite.y = 200

        car = pyglet.image.load('data/car.png')
        self.carSprite = pyglet.sprite.Sprite(car, -500, 0)


        # Add these sprites to the list of drawables
        self.drawableObjects.append(self.cloudSprite)
        self.drawableObjects.append(self.lSprite)
        self.drawableObjects.append(self.dropletSprite)
        self.drawableObjects.append(self.carSprite)

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

    def adjustWindowSize(self):
        """
        Adjust the width and height of the Pyglet Window.
        """
        w = 600
        h = 900
        self.width = w
        self.height = h

    def on_draw(self):
        """
        The overridden API method on_draw which is called when the Window
        needs to be re-drawn.
        """
        self.clear()
        for d in self.drawableObjects:
            d.draw()

    def on_key_press(self, key, modifiers):
        """
        Captures key press events.
        Overrides pyglet.window.Window.on_key_press()
        """
        if key == pyglet.window.key.P and not self.paused:
            pyglet.clock.unschedule(self.moveObjects)
            pyglet.clock.unschedule(self.show_lightening)
            self.paused = True
        elif key == pyglet.window.key.R and self.paused:
            pyglet.clock.schedule_interval(self.moveObjects, 1.0/20)
            pyglet.clock.schedule_interval(self.show_lightening, 1.0)
            self.paused = False

    def moveObjects(self, t):
        """
        Move the image sprites / play the sound .
        This method is scheduled to be called every 1/N seconds using
        pyglet.clock.schedule_interval.

        """
        if self.carSprite.x <= self.cloudSprite.width:
            self.carSprite.x += 10
        else:
            self.carSprite.x = -500
            self.horn_sound.play()

    def show_lightening(self, t):
        """
        toggle the property value Sprite.visible , also move
        the sprite representing the lightening image
        This method is scheduled to be called every second using
        pyglet.clock.schedule_interval.
        """
        if self.lSprite.visible:
           self.lSprite.visible = False
        else:
            if(self.lSprite.x == 100):
                self.lSprite.x += 200
            else:
                self.lSprite.x = 100

            self.lSprite.visible = True

# Create a Pyglet Window instance to show the animation.
win = RainyDayAnimation()

# Set window background color to white.
r, g, b, alpha = 0, 1, 1, 1
pyglet.gl.glClearColor(r, g, b, alpha)

# Schedule the method RainyDayAnimation.moveObjects to be called every
# 0.05 seconds.
pyglet.clock.schedule_interval(win.moveObjects, 1.0/20)

# Show the lightening every 1 second
pyglet.clock.schedule_interval(win.show_lightening, 1.0)

pyglet.app.run()#author: 931108009
#exercise: Project: drive on a rainy day!(page 117)

