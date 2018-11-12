#author: 931112307
#exercise: Time for action – raindrops animation (page 114)
import pyglet
import time

# kelas RainDropsAnimation sazande kelas method pyglet.window.Window ra farakhani mikonad.
class RainDropsAnimation(pyglet.window.Window):
    def __init__(self, width = None, height = None):
        pyglet.window.Window.__init__(self,
                                      width = width,
                                      height = height)
        self.drawableObjects = []
        self.createDrawableObjects()

    # ashya ya spriteha ra braye rasm ghatarat baran dar darone panjere pyglet ejad mikonad.
    def createDrawableObjects(self):
        num_rows = 4
        num_columns = 1
        droplet = 'C:\\Users\\amir\\image\\droplet.png'
        # manategh daron file tasvir ra baraye ejad framehaye animition shakhsi estefade mikonad.
        animation = self.setup_animation(droplet,
                                         num_rows,
                                         num_columns)
        # sprite baraye sheye moteharek ghatarat baran ejad shode ast.
        self.dropletSprite = pyglet.sprite.Sprite(animation)
        self.dropletSprite.position = (0,0)

        # Add these sprites to the list of drawables
        self.drawableObjects.append(self.dropletSprite)

    # setup_animation sheye animition ra be vasileye manategh mokhtalef daron tasvir ejad mikonad.
    def setup_animation(self, img, num_rows, num_columns):
        # avalin nemone az tasvir dar khat zir ejad shode ast.
        base_image = pyglet.image.load(img)

        # yek nemone az ImageGrid ejad shode ast.
        animation_grid = pyglet.image.ImageGrid(base_image,
                                                num_rows,
                                                num_columns)
        image_frames = []

        for i in range(num_rows*num_columns, 0, -1):
            # mantaghe khas tasvir ra migirad va sepas anra ejad mikonad.
            frame = animation_grid[i-1]
            animation_frame = pyglet.image.AnimationFrame(frame, 0.8)
            # ghalebhaye animation mothark dar list image_frames zakhira shoda ast.
            image_frames.append(animation_frame)
        # nemoney pyglet.image.Animation ba astafad az in list ejad meshavad.
        animation = pyglet.image.Animation(image_frames)
        return animation
    # The overridden API method on_draw which is called when the Window. needs to be re-drawn.
    def on_draw(self):
        self.clear()
        for d in self.drawableObjects:
            d.draw()

# yek nemone panjere az panjere pyglet baraye namayesh animation ejad mikonad.
win = RainDropsAnimation()

# rang background panjere ra ba rang firozeye set mikonad.
r, g, b, alpha = 0, 1, 1, 1
pyglet.gl.glClearColor(r, g, b, alpha)

pyglet.app.run()





