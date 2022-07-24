
def Get_growing_row(list):
    growing = [list[0]]
    for i in list:
        if growing[-1] < i:
            growing.append(i)
    return growing


list = [1, 5, 2, 3, 6, 8, 3, 4, 1, 7, 9]
print(list)
print(Get_growing_row(list))