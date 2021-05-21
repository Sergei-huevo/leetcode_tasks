# Функция, которая получает на вход лист с целыми числами и нулями.
# Нужно реализовать сдвиг всех нулей вправо, порядок чисел сохранить

def null_to_right(array_list):
    if 0 not in array_list:
        return array_list
    counter = 0
    array_of_nulls = []
    while counter < len(array_list):
        if array_list[counter] != 0:
            counter += 1
        else:
            array_of_nulls.append(array_list.pop(counter))
    array_list.extend(array_of_nulls)
    return array_list


new_array = [0,0,0,0,0,0,1, 2, 0, 4, 6, 0, 0, 0, 0, 87, 9]
print(null_to_right(new_array))
