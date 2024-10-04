from random import randint

student = input('Представьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности 1 - 5; '))
except:
    level = 1
    print('Установлен первый уровень сложности.')


if level < 1 or level > 5:
    level = 1
    print('Установлен первый уровень сложности.')


print (f'Хорошо, {student}. Тебе задачка.')
min = 10 ** (level - 1)
max = 10 ** level - 1

a = randint (min, max)
b = randint (min, max)

print(f'{student}, сколько будет {a} + {b}? ', end='')
correct_answer = a + b
student_answer = input()

if student_answer == str(correct_answer):
    print(f'Ax, ну какой умница, {student}. Это пять!')
else:
    print(f'Два, {student}, можешь садиться! Правильный ответ (correct answer).')

