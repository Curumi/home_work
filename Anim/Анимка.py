import tkinter as tk
from random import randint
from math import sqrt


# Базовый класс для объектов анимации
class AnimatedObject:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.id = None

    def draw(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


# Подкласс для анимированного круга
class AnimatedCircle(AnimatedObject):
    def __init__(self, canvas, x, y, size, color):
        super().__init__(canvas, x, y, size, color)
        self.dx = randint(-3, 3)
        self.dy = randint(-3, 3)
        self.draw()

    def draw(self):
        self.id = self.canvas.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color
        )

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        coords = self.canvas.coords(self.id)

        # Обработка столкновений со стенами
        if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width():
            self.dx = -self.dx
        if coords[1] <= 0 or coords[3] >= self.canvas.winfo_height():
            self.dy = -self.dy

    def check_collision(self, other):
        coords1 = self.canvas.coords(self.id)
        coords2 = self.canvas.coords(other.id)

        x1, y1 = (coords1[0] + coords1[2]) / 2, (coords1[1] + coords1[3]) / 2
        x2, y2 = (coords2[0] + coords2[2]) / 2, (coords2[1] + coords2[3]) / 2

        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        min_distance = (self.size + other.size) / 2

        if distance < min_distance:
            overlap = min_distance - distance

            # Вычисление направления отталкивания
            dx = (x2 - x1) / distance
            dy = (y2 - y1) / distance

            # Раздвижение объектов
            self.canvas.move(self.id, -dx * overlap / 2, -dy * overlap / 2)
            other.canvas.move(other.id, dx * overlap / 2, dy * overlap / 2)

            # Обмен скоростями (упрощенная модель)
            self.dx, other.dx = other.dx, self.dx
            self.dy, other.dy = other.dy, self.dy


# Основное окно программы
class AnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Animation with Collisions")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.objects = []
        for _ in range(10):
            x = randint(50, 750)
            y = randint(50, 550)
            size = randint(20, 50)
            color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
            circle = AnimatedCircle(self.canvas, x, y, size, color)
            self.objects.append(circle)

        self.animate()

    def animate(self):
        for obj in self.objects:
            obj.move()
        for i in range(len(self.objects)):
            for j in range(i + 1, len(self.objects)):
                self.objects[i].check_collision(self.objects[j])
        self.root.after(30, self.animate)


# Запуск программы
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()
