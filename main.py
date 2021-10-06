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
    :return: toate numerele patrate perfecte din intervalul detrminat de n si m
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
def is_prime(n):
    '''

    :param n: un numar natural citit de la tastaura
    :return: True daca numarul este prim. In caz contrar (numarul nu este prim) returneaza False
    '''
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_superprime(n):
    '''

    :param n: un numar natural citit de la tastatura
    :return: True, daca numarul citit de la tastatura este superprim. False, in caz contrar.
    '''
    if n<2:
        return False
    while n!=0:
        if is_prime(n)==False:
            return False
        else:
            n=n//10
    return True
def test_is_superprime():
    assert is_superprime(15)==False
    assert is_superprime(101)==False
    assert is_superprime(233)==True
    assert is_superprime(237)==False
def main():
    while True:
        print('Optiuni: ')
        print('1.Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).')
        print('2.Afișează toate pătratele perfecte dintr-un interval închis dat')
        print('3. Determina daca un numar este superprim ')
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
        elif optiune=='3':
            n=int(input('Dati numarul de la tastatura: '))
            test_is_superprime()
            print(is_superprime(n))
        elif optiune=='x':
            break
        else:
            print("Optiune invalida citita de la tastatura")
if _name_=='_main_':
        test_get_leap_years()
        test_is_superprime()
        test_get_perfect_squares()

        main()
        exit(0)
