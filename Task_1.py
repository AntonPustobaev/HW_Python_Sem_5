# 34. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл, содержащий сумму многочленов

def Read_pol(file_name):
    file = open(file_name)
    pol = file.read().split(' ')
    file.close()
    return pol


def Sum_poynomials(first_file, second_file):
    polynomial = Read_pol(first_file)
    pol_sum = Pol_in_dict(polynomial)
    polynomial = Read_pol(second_file)
    return Pol_in_dict(polynomial)


def Pol_in_dict(polynomial, polynomial_sum = {}):
    for i in polynomial:
        c = i.split('^')
        if c[0].isnumeric():
            if not polynomial_sum.get(0):
                polynomial_sum[0] = int(c[0])
            else:
                polynomial_sum[0] += int(c[0])
        if len(c) != 1:
            if not polynomial_sum.get(c[1]):
                polynomial_sum[c[1]] = int(c[0].replace('x', ''))
            else:
                polynomial_sum[c[1]] += int(c[0].replace('x', ''))
    return Convert_to_string(polynomial_sum)


def Convert_to_string(prynomial_sum):
    str_polynomial = ""
    key = prynomial_sum.keys()
    for i in key:
        if i != '1' and i != 0:
            str_polynomial += f'{prynomial_sum[i]}x^{i} + '
        elif i == '1':
            str_polynomial += f'{prynomial_sum[i]}x + '
        else:
            str_polynomial += f'{prynomial_sum[i]} '
    str_polynomial += '= 0'
    return str_polynomial

file_name1 = 'Polynomial1.txt'
file_name2 = 'Polynomial2.txt'
f = open('Sum_polynomials.txt', 'w')
f.write(Sum_poynomials(file_name1, file_name2))
f.close()