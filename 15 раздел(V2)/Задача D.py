# ������ �111329. ���������� ���������
# �������� ��� ������ ������� ����� � �������� �������. ��� ����� �������� ������ ���� ����� ��� ������ ������ readlines().
# ��������� ������ �������� ����� ����������� ������������� �������� '\n'.

aa = open('input.txt', 'r')
aa1 = aa.readlines()
for i in range(len(aa1) - 1, -1, -1):
    print(aa1[i].replace('\n', '').replace('\\n', ''))
