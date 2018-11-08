#author: 931104510
#exercise: Time for action – viewing an existing animation (page 98)

import pyglet
animation = pyglet.image.load_animation("C:\\Images\\SimpleAnimation.gif")
animSprite = pyglet.sprite.Sprite(animation)
w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)
r, g, b, alpha = 0.5, 0.5, 0.8, 1.
pyglet.gl.glClearColor(r, g, b, alpha)


@win.event
def on_draw():
    win.clear()
    animSprite.draw()


pyglet.app.run()

