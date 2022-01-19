from ssl import OPENSSL_VERSION_NUMBER


while 5<6:
    print('Введите число ')
    x = int(input())
    y = x
    system = 2
    newnum1 = []
    index = 0
    while y > 0:
        newnum = ( y % system)
        newnum1.insert(0,newnum)
        y = y //2
    print(newnum1)
    