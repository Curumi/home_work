# Анимированные круги с использованием Tkinter

Этот проект реализует простую анимацию движущихся кругов с использованием библиотеки `tkinter` в Python. Круги отскакивают от стен и друг от друга, создавая динамичную и визуально привлекательную симуляцию.

---

## Возможности

- **Динамическая анимация**: Круги движутся в случайных направлениях с разными скоростями.
- **Обнаружение столкновений**: Круги отскакивают друг от друга и от стен холста.
- **Физическое взаимодейс твие**: При столкновении круги обмениваются скоростями и раздвигаются.
- **Настраиваемость**: Легко изменить количество кругов, их размеры и скорость.

---

## Как это работает

### Основные компоненты

1. **Класс `AnimatedObject`**:
   - Базовый класс, который определяет структуру для анимированных объектов.
   - Включает свойства для позиции, размера, цвета и метод для рисования объекта на холсте.

2. **Класс `AnimatedCircle`**:
   - Наследуется от `AnimatedObject`.
   - Реализует методы для рисования круга, его перемещения по холсту и обработки столкновений.

3. **Класс `AnimationApp`**:
   - Управляет основным циклом анимации.
   - Создает холст и инициализирует несколько кругов со случайными атрибутами.
   - Использует метод `after()` для обновления анимации через регулярные интервалы.

---

## Обзор кода

### Основные функции

- **Инициализация**: Класс `AnimationApp` настраивает окно Tkinter и холст, а также создает заданное количество анимированных кругов.
- **Цикл анимации**: Метод `animate()` обновляет положение каждого круга и обрабатывает их столкновения.
- **Обработка столкновений**: Круги определяют, когда они пересекаются, и корректируют свои позиции и скорости.

### Пример кода

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()
```
Этот код запускает анимацию, создавая главное окно Tkinter и вызывая класс `AnimationApp`.

---

## Как запустить

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Curumi/home_work.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd anim
   ```
3. Запустите скрипт:
   ```bash
   python Анимка.py
   ```

Убедитесь, что у вас установлен Python версии 3.6 или выше.

---

## Добавление проекта в GitHub Desktop

1. Откройте GitHub Desktop.
2. Выберите `File` > `Add Local Repository`.
3. Перейдите в директорию, где вы клонировали репозиторий.
4. Нажмите `Add Repository`.
5. Сделайте коммит и отправьте изменения в ваш репозиторий на GitHub.

---

## Настройка

- **Количество кругов**: Измените диапазон в цикле внутри метода `AnimationApp.__init__()`.
- **Свойства кругов**:
  - Размер: Настройте параметр `size` при инициализации `AnimatedCircle`.
  - Цвет: Измените параметр `color`, чтобы использовать конкретные RGB-значения.
- **Скорость**: Измените диапазон `dx` и `dy` в конструкторе `AnimatedCircle`.

---

## Пример результата

При запуске скрипта вы увидите белый холст размером 800x600 с 10 цветными кругами, которые движутся, отскакивая от стен и друг друга.

---

## Зависимости

- Python 3.6 или выше
- Стандартная библиотека (`tkinter`, `math`, `random`)

Дополнительные зависимости отсутствуют.

---

## Лицензия

Этот проект распространяется под лицензией MIT. Вы можете свободно использовать и изменять его.

---

## Вклад в проект

Мы приветствуем любые предложения и исправления! Если вы хотите:
- Сообщить об ошибке
- Предложить новую функцию
- Отправить pull request

Свяжитесь с нами или создайте issue.

---

### Автор

[Curumi](https://github.com/Curumi)

