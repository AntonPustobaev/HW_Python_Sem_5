# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.

def get_up_num(list):
    ups = [list[0]]
    for i in list:
        if i > max(ups):
            ups.append(i)
    return ups    

list = [1, 5, 2, 3, 6, 8, 3, 4, 1, 7, 9]
print(list)
print(get_up_num(list))