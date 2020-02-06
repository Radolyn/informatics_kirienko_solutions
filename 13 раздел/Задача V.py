# 		В сети интернет каждому компьютеру присваивается четырехбайтовый код, который принято записывать в виде четырех чисел, каждое из которых может принимать значения от 0 до 255, разделенных точками. Вот примеры правильных IP-адресов:
# 


import ipaddress

ip = input()


def validateIp(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False


if validateIp(ip):
    print('YES')
else:
    print('NO')
