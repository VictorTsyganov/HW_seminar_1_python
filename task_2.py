# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

input_list = []
for i in range(3):
    input_list.append(input('Введите значения Х, Y, Z (после ввода'
                            ' каждого значения нажимаем enter): '))

result = (not (input_list[0] or input_list[1] or input_list[2])
          == (not input_list[0] and not input_list[1] and not input_list[2]))

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
