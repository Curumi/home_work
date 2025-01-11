import texture as skin
import world
import tanks_collection
from hitbox import Hitbox
from tkinter import *
from random import randint

class Unit:
    def __init__(self, canvas, x, y, speed, padding, bot, default_image):
        self._speed = speed
        self._x = x
        self._y = y
        self._vx = 0
        self._vy = 0
        self._canvas = canvas
        self._hp = 100
        self._dx = 0
        self._dy = 0
        self._bot = bot
        self._hitbox = Hitbox(x, y, world.BLOCK_SIZE, world.BLOCK_SIZE, padding = padding)
        self._default_image = default_image
        self._left_image = default_image
        self._right_image = default_image
        self._forward_image = default_image
        self._backward_image = default_image
        self._create()

def create(self):
    self._id = self._canvas.create_image(self._x, self._y, image = skin.get(self._default_image), anchor =NW)

def __del__(self):
    try:
        self._canvas.delete(self._id)
    except Exception:
        pass

    def forward(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.__id, image = skin.get(self._forward_image))

    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.__id, image = skin.get(self._backward_image))

    def left(self):
        self.__vx = -1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image = skin.get(self._left_image))

    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.__id, image = skin.get(self._right_image))

    def stop(self):
        self.__vx = 0
        self.__vy = 0

    def update(self):
        if self._bot:
            self._AI()
        self.dx = self.vx * self._speed
        self.dy = self.vy * self._speed
        self._x += self._dx
        self._y += self._dy
        self._update.hitbox()

    def AI(self):
        pass

    def update_hitbox(self):
        self._hitbox.moveto(self._x, self._y)