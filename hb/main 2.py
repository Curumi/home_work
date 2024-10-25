from hitbox import Hitbox



#hb1= Hitbox(10, 10, 100, 100)

#print(hb1.x)
#print(hb1.y)
#print(hb1.width)
#print(hb1.height)

hb1= Hitbox(0,0,100,100)
hb2= Hitbox(150, 100, 100,100)
hb3= Hitbox(350, 300, 100,100)

print(f'верхняя граница hb1: {hb1.top}',
      f'верхняя граница hb2: {hb2.top}',
      f'верхняя граница hb3: {hb3.top}')
print(f'нижняя граница hb1: {hb1.bottom}',
      f'нижняя граница hb2: {hb2.bottom}',
      f'нижняя граница hb2: {hb3.bottom}')
print(f'левая граница hb1: {hb1.left}',
      f'левая граница hb2: {hb2.left}',
      f'левая граница hb2: {hb3.left}')
print(f'правая граница hb1: {hb1.right}',
      f'правая граница hb2: {hb2.right}',
      f'правая граница hb2: {hb3.right}')



intersection = hb1.intersects(hb2)

print(intersection)