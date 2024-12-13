import math

def find_min_angle(x1, x2, y1, y2, z1, z2):

    angle_X = math.atan2(x2, x1)
    angle_Y = math.atan2(y2, y1)
    angle_Z = math.atan2(z2, z1)

    min_angle = min(angle_X, angle_Y, angle_Z)

    if min_angle == angle_X:
        return (x1, x2)
    elif min_angle == angle_Y:
        return (y1, y2)
    else:
        return (z1, z2)

x1, x2 = int(input('Координата точки x1 равны : ')), int(input('Координата точки x2 равны : '))
y1, y2 = int(input('Координата точки y1 равны : ')), int(input('Координата точки y2 равны : '))
z1, z2 = int(input('Координата точки z1 равны : ')), int(input('Координата точки z2 равны : '))

point = find_min_angle(x1, x2, y1, y2, z1, z2)
print(f"Координаты точки с минимальным углом: {point}")