# Дан файл, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.
f = open('input.txt')
s = f.readlines()
b = 0
for i in range(len(s)):
    a = "".join(s[i])
    a = a.split()
    for i in range(len(a)):
        b += int(a[i])
    print(b)
    b = 0
f.close()
