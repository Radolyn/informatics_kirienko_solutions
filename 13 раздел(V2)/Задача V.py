# 
# 		В сети интернет каждому компьютеру присваивается четырехбайтовый код, который принято записывать в виде четырех чисел, каждое из которых может принимать значения от 0 до 255, разделенных точками. Вот примеры правильных IP-адресов:
# 

import ipaddress

a = input()


def valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return 'YES'
    except:
        return 'NO'


print(valid_ip(a))
