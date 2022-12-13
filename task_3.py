# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

input_list = []
for i in range(2):
    input_list.append(int(input('Введите значения Х, Y (после ввода'
                            ' каждого значения нажимаем enter): ')))

if input_list[0] > 0 and input_list[1] > 0:
    print(f'Точка с координатами {input_list[0]} и'
          f' {input_list[1]} в первой четверти')
elif input_list[0] < 0 and input_list[1] > 0:
    print(f'Точка с координатами {input_list[0]} и'
          f' {input_list[1]} во второй четверти')
elif input_list[0] < 0 and input_list[1] < 0:
    print(f'Точка с координатами {input_list[0]} и'
          f' {input_list[1]} в третьей четверти')
else:
    print(f'Точка с координатами {input_list[0]} и'
          f' {input_list[1]} в четвертой четверти')