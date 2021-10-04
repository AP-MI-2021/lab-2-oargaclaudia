import math
def get_leap_years(a,b):
    '''
    :param a: un an citit de la tastatura
    :param b: un alt an citit de la tastatura
    Afiseaza toti anii bisecti intre doi ani dati
    '''
    anbisect = ''
    for i in range(a,b+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            anbisect=anbisect+str(i)+ " "
    return anbisect

def test_get_leap_years():
    assert get_leap_years(12,25)=="12 16 20 24 "
    assert get_leap_years(1582,1600)=="1584 1588 1592 1596 1600 "
    assert get_leap_years(1601,1630)=="1604 1608 1612 1616 1620 1624 1628 "
def get_perfect_squares(n, m):
    '''

    :param n:  un numar citit de la tastatura
    :param m: un numar citit de la tastatura
    :return:
    '''
    numereperfecte = ''
    if math.sqrt(n) == math.isqrt(n) and n!=0:
        numereperfecte+=str(n) + " "
    for i in range(math.isqrt(n) + 1, math.isqrt(m) + 1):
        if i!=0:
            numereperfecte += str(i * i) + " "
    return numereperfecte


def test_get_perfect_squares():
    assert get_perfect_squares(10, 16) == "16 "
    assert get_perfect_squares(9, 16) == "9 16 "
    assert get_perfect_squares(5, 10) == "9 "
    assert get_perfect_squares(4, 10) == "4 9 "
    assert get_perfect_squares(100, 121) == "100 121 "
    assert get_perfect_squares(0, 10) == "1 4 9 "
while True:
        print('1.Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).')
        print('2.Afișează toate pătratele perfecte dintr-un interval închis dat')
        print('x.Iesire din program-Exit')
        optiune=input('Alege optiunea: ')
        if optiune=='1':
            a=int(input("Dati primul numar: "))
            b=int(input("Dati al doilea numar: "))
            test_get_leap_years()
            print(get_leap_years(a,b))
        elif optiune=='2':
            a = int(input("Dati primul numar: "))
            b = int(input("Dati al doilea numar: "))
            test_get_perfect_squares()
            print(get_perfect_squares(a,b))
        elif optiune=='x':
            break
        else:
            print("Optiune invalida")