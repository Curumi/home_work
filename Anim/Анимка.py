import tkinter as tk
from random import randint

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
        if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width():
            self.dx = -self.dx
        if coords[1] <= 0 or coords[3] >= self.canvas.winfo_height():
            self.dy = -self.dy

# Основное окно программы
class AnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Animation")
        
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
        self.root.after(30, self.animate)

# Запуск программы
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()
