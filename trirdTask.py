# noinspection PyTypeChecker
def coordinates_input(x):
    coordinate_point = [0] * x
    for i in range(x):
        verity = False
        while not verity:
            try:
                number = float(input(f"Введите {i + 1} координату: "))
                coordinate_point[i] = number
                verity = True
                if coordinate_point[i] == 0:
                    verity = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Введите пожалуйста числа!")
    return coordinate_point


def test_coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 < xy[1]:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = coordinates_input(2)
test_coordinates(koordinate)
