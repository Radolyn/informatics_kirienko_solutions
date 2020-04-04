# Задача №111347. Отсортировать список участников по баллам
# Отсортируйте список участников олимпиады:
# 1) По убыванию набранного балла.
# 2) При равных значения балла - по фамилии в лексикографическом порядке.
# 3) При совпадающих баллах и фамилии - по имени в лексикографическом порядке.

fil = open('input.txt', 'r', encoding='utf8').readlines()
fil = [fil[i][:-1] if fil[i][-1] == '\n' else fil[i] for i in range(len(fil))]
fil.sort(key=lambda x: (-1 * int(x.split()[3]), x.split()[0], x.split()[1]))
print('\n'.join([
    fil[i].split()[0] + ' ' + fil[i].split()[1] + ' ' + fil[i].split()[3]
    for i in range(len(fil))
]))
