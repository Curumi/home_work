from tank import Tank
from tkinter import*

import world
import tank_collection
import texture


KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 60
def update():
    tank_collection.update()
    player = tank_collection.get_player()
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2 + player.get_size()//2)
    world.update_map()
    w.after(1000//FPS, update)



def key_press(event):
    player = tank_collection.get_player()
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)



def load_textures():
    # pass
    texture.load('tank_up',
                 '../img/up.png')
    texture.load('tank_down',
                 '../img/down.png')
    texture.load('tank_left',
                 '../img/left.png')
    texture.load('tank_right',
                 '../img/right.png')
    texture.load(world.BRICK,'../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE,'../img/wall.png' )


w = Tk()

load_textures()

w.title('Танки на минималках 2.0')
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg='light green')
canv.pack()


world.initialize(canv)

tank_collection.initialize(canv)

w.bind('<KeyPress>', key_press)

update()
w.mainloop()