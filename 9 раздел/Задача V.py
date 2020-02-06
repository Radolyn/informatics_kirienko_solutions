# Дан список. Не изменяя его и не используя дополнительные списки,
# определите, какое число в этом списке встречается чаще всего.


l = list(map(int, input().split()))

m = 0
m_count = 0

for item in l:
    i_count = l.count(item)
    if i_count > m_count:
        m = item
        m_count = i_count

print(m)
