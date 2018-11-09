#author: 922122800
#exercise: Time for action – animation using a sequence of images (page 100)

import pyglet

#image ha ro adressdahe karde va dar yek moteghayer rekhte ba in sorat ke dar system man dar draives c ye poshe data sakhte shodae va dar poshe data poshe image gozashtam va image ha ro tosh gozashtam.shoma adrass on directore ke axha ro gozashtin badid.

image_frames = ("C:\\data\\Images\\clock1.png",
                "C:\\data\\Images\\clock2.png",
                "C:\\data\\Images\\clock3.png")

#axha mian lod mishan ya be abarate liste az tasavir ro mesaze
images = map(lambda img: pyglet.image.load(img), image_frames)

#in khat meyad animation ro mesaze be in sorart ke tasavir ke address dahe kardem dar faseleh 0.33 jabeja meshan va donbaley az tasaveyr be sorat animation sakhtee meshe.

animation = pyglet.image.Animation.from_image_sequence(images, 0.33)

#in khat yek nemoneh az animation ro sakhte
animSprite = pyglet.sprite.Sprite(animation)

#tanzimat tool & arze 
w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)

# tanzimat range paszamineh be range safid
pyglet.gl.glClearColor(1, 1, 1, 1)


#arsebare karde ke yak dayrektor ast va be tagher IPA komk mikonad
@win.event

#metode kashedan ro sada zadeh
def on_draw():
    win.clear()
#animation ro namaish mideh
    animSprite.draw()


