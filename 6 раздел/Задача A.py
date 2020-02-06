text = input()

print(text[2])
print(text[len(text) - 2])

text2 = ""
for i in range(5):
    text2 += text[i]
print(text2)
print(text[0:len(text) - 2])

text3 = ""
for i in range(len(text)):
    if i % 2 == 0:
        text3 += text[i]
print(text3)

text4 = ""
for i in range(len(text)):
    if i % 2 == 1:
        text4 += text[i]
print(text4)

print(text[::-1])

text5 = text[::-1]
text6 = ""
for i in range(len(text5)):
    if i % 2 == 0:
        text6 += text5[i]
print(text6)

print(len(text))
