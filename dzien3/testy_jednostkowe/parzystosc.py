# 11.1.1: Napisz w pliku parzystosc.py funkcję czy_parzysta(n), 
# która zwraca True dla liczb parzystych i False dla nieparzystych. 
# W pliku test_parzystosc.py napisz testy sprawdzające kilka przypadków: 
# liczby parzyste, nieparzyste i zero. Na koniec dopisz jeden test, 
# który celowo nie przejdzie, uruchom pytest 
# i odczytaj z wyniku, co porównał pytest i dlaczego test padł.

def parzystosc_sprawdz(a):
    if isinstance(a, int):
        if a % 2 == 0:
            return True
        else:
            return False
    else:
        raise ValueError('Podana zmienna nie jest liczba')