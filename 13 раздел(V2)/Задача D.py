# # 		Выведите подряд, без пробелов, все символы, лежащие в таблице ASCII между двумя заданными символами.#     

a, b = ord(input()), ord(input())
for i in range(a , b + 1):
  print(chr(i), end='')
