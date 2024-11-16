import texture
from tkinter import *
import world
import tanks_collection
KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

FPS = 60

def update():
    tanks_collection.update()

    player = tanks_collection.get_player()

    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH//2 + player.get_size()//2, player.get_y() - world.SCREEN_HEIGHT//2 + player.get_size()//2)

    w.after(1000 // FPS, update)

def key_press(event):
    player = tanks_collection.get_player()

    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0,5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5,0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5,0)
    elif event.keycode == 32:
        tanks_collection.spawn_enemy()

def load_textures():
    texture.load('up', '../img/up.png')
    texture.load('down','../img/down.png')
    texture.load('right', '../img/right.png')
    texture.load('left', '../img/left.png')
    print(texture._frames)



w = Tk()

load_textures()

w.title('')
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='alice blue')
#canv = Canvas(w, width=world.WIDTH, height=world.HEIGHT, bg='alice blue')
canv.pack()



tanks_collection.initialize(canv)
w.bind('<KeyPress>', key_press)


update()
w.mainloop()