# Определите, есть ли во входном файле символ '@'. Выведите слово YES или NO.
f = open('input.txt')
s = f.read()
if s.count("@"):
    print("YES")
else:
    print("NO")
f.close()
