# Drugi dzien

# ==============================================================================
# 3. POWROT DO FUNKCJI (ciag dalszy)
# ==============================================================================

# ------------------------------------------------------------------------------
# 3.3 Funkcja wewnatrz funkcji i funkcja zwracajaca funkcje
# ------------------------------------------------------------------------------

def funkcja():
    # ....
    # return ....
    # print('*'*20)
    pass

# funkcja() --> wywolanie funkcji
# funkcja --> przekazanie funkcji

def zewnetrzna(x):
    def wewnetrzna(y): # --> funkcja jest tylko i wylacznie widoczna w srodku
        return y * 2
    return wewnetrzna(x) + 1

# wewnetrzna(6) # --> zawartosc wewnetrzna funkcji zewnetrznej, nie mozna wywolac spoza

print(zewnetrzna(3))

# praktyczne wykorzystanie takiej funkcji

def raport(oceny):
    def srednia(lista):
        return sum(lista) / len(lista)
    return f'Srednia: {srednia(oceny):.2f}'

print(raport([5,7,3,4]))

# srednia()

# Domkniecie

# Funkcja zwracajaca funkcje
def potega(n):
    def poteguj(x):
        return x ** n # n pochodzi z zewnetrznej funkcji
    return poteguj    # zwracamy funkcje, a nie jej wywolanie

kwadrat = potega(2) # domkniecie
szescian = potega(3)

print(kwadrat,szescian)

print(kwadrat(8))   # 64
print(szescian(10)) # 1000

print(potega(2)(8))  # 64
print(potega(3)(10)) # 1000

#  Pulapka

"""
def licznik():
    stan = 0
    def zwieksz():
        stan += 1 # --> incrementacja  UnboundLocalError: cannot access local variable 'stan' where it is not associated with a value
        return stan
    return zwieksz

klik = licznik()
klik()
"""
print('*'*30)

def licznik():
    stan = 0
    def zwieksz():
        nonlocal stan
        stan += 1 
        return stan
    return zwieksz

klik = licznik()
print(klik(),klik(),klik())

drugi = licznik()
print(drugi())

# ##############################################################################
# ###  ZADANIA 3.3                                                           ###
# ##############################################################################

# 3.3.3: Napisz skarbonka(), która zwraca funkcję wplac(kwota). 
# Każda wpłata ma dodawać się do salda, a funkcja ma zwracać aktualne saldo.

def skarbonka():
    stan = 0
    def zwieksz(x):
        nonlocal stan
        stan = stan + x
        return stan
    return zwieksz

test = skarbonka()
print(test(5), test(10))

# dodatkowe
# 3.3.2: Napisz funkcję notatnik(), która zwraca funkcję dopisz(tekst). Każde wywołanie dopisuje notatkę 
# do wewnętrznej listy i zwraca wszystkie dotychczasowe notatki. Utwórz dwa niezależne notatniki. Dlaczego 
# tutaj nie trzeba używać nonlocal?

def notatnik():
    notatka = ''
    def dopisz(tekst):
        nonlocal notatka
        notatka = notatka + '\n' + tekst
        return notatka
    return dopisz
test = notatnik()
print(test('Ala ma kota'), test('Kot ma Ale'))

# ------------------------------------------------------------------------------
# 3.4 Funkcja jako argument funkcji
# ------------------------------------------------------------------------------

def zastosuj(funkcja, wartosc):
    return funkcja(wartosc)

def kwadracik(x):
    return x**2

print(zastosuj(kwadracik,5))
print(zastosuj(len,'Python'))

# Pulapka
# Przekazujemy zawsze funkcje, a nie jej wywolanie
# print(zastosuj(len(),'Python')) # TypeError: len() takes exactly one argument (0 given)

temperatury = [12, 18, 9, 21, 15]

def raport(dane, funkcja):
    return f"{funkcja.__name__}: {funkcja(dane)}"

print(raport(temperatury, max))    #21
print(raport(temperatury, min))    #9
print(raport(temperatury, sum))    #75
print(raport(temperatury, len))    # 5
print(raport(temperatury, sorted)) # [9, 12, 15, 18, 21]

operacje = {'najwyzsza':max,'najnizsza':min,'suma':sum}

for opis, f in operacje.items():
    print(opis, f(temperatury))

# ##############################################################################
# ###  ZADANIA 3.4                                                           ###
# ##############################################################################

# 3.4.3: Napisz funkcję przetworz(lista, funkcja), która zwraca nową listę z wynikami funkcji dla każdego elementu. 
# Sprawdź na ["ala", "bartek"] z str.upper i z len.

def przetworz(dane, funkcja):
    test = f'{funkcja.__name__}: '
    for i in dane:
        test = test + f'{funkcja(i)} '
    return [funkcja(x) for x in dane]  
    # return test 

print(przetworz(['ala','bartek'],str.upper))
print(przetworz(['ala','bartek'],len))

#dodatkowe
# 3.4.1: Napisz funkcję dwa_razy(funkcja, x), która wywołuje podaną funkcję dwa razy z rzędu 
# (funkcja(funkcja(x))). Sprawdź dla kwadrat i 3 oraz dla str.upper i "ala".

def dwa_razy(funkcja, x):
    return funkcja(funkcja(x))

print(dwa_razy(kwadrat, 3))
print(dwa_razy(str.upper, 'ala'))

# #dodatkowe
# 3.4.4: Napisz funkcję filtruj(lista, warunek), która zostawia tylko elementy, dla których warunek(x) 
# zwraca True. Sprawdź z własną funkcją czy_parzysta na [1, 2, 3, 4, 5] i porównaj z wbudowanym filter().

# 1 Sposob
# *******************************************************

def filtruj(lista, warunek):
    wynik = []
    for x in lista:
        if warunek(x):
            wynik.append(x)
    return wynik

print(filtruj([2,3,4,5,-1,-2,-3], lambda x: x>0))

# 2 Sposob
# *******************************************************

def czy_parzysta(x):
    return x % 2 == 0

def filtruj(lista, warunek):
    return [x for x in lista if warunek(x)]

liczby = [1,2,3,4,5,6]
print(filtruj(liczby,czy_parzysta))

#* bonus
print(list(filter(czy_parzysta,liczby)))

# ------------------------------------------------------------------------------
# 3.5 Rekurencja
# ------------------------------------------------------------------------------

# Funkcja, ktora wywoluje sama siebie

# cechy:
# warunek bazowy -> prosty przypadek, zeby zatrzymac dzialanie rekurencji
# krok rekurencyjny -> wywolanie samej siebie, tylko z arguementem blizszym warunku bazowego

# Silnia
# 5! = 5 x 4 x 3 x 2 x 1 = 120

def silnia(n):
    if n <= 1: # warunek bazowy
        return 1
    return n * silnia(n-1) # wywolanie samej siebie blizej warunku bazowego

print(silnia(5))

def w_nieskoczonosci(n):
    return w_nieskoczonosci(n+1)

# w_nieskoczonosci(6)  RecursionError: maximum recursion depth exceeded --> 1000

# Drugi przyklad fibonacci
# 0 ,1 ,1, 2, 3, 5 ,8, 13, 21, 34 ....
# 0 + 1 = , 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5 ........

# fib(n-1) + fib(n-2) __> zapis rekureyncji fibonaci

import time

# Fibonacci rekurencyjne
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# sposob petli while
def fib_while(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b # przesuwanie sie o jeden wyraz dalej
        i += 1
    return a

print(fib(6),fib_while(6))

# pomiar czasu, time.perf_counter()
n = 30 

start = time.perf_counter()
wynik = fib(n)
rekurencja = time.perf_counter() - start

start = time.perf_counter()
wynik_while = fib_while(n)
while_petla = time.perf_counter() - start

print(f"fib{n} = {wynik}")
print(f"Rekurencje: {rekurencja:.4f} s")
print(f"Petla while = {while_petla:.6f} s")
print(f"Petla jest ok: {rekurencja / while_petla:.0f} razy szybsza")

# Najlepsze zastosowanie --> zagniezdzone dane
def policz_elementy(dane):
    if isinstance(dane,list):
        return sum(policz_elementy(x) for x in dane)
    return 1

print(policz_elementy([1,[2,3,[4,5,[6]]]]))

# ------------------------------------------------------------------------------
# 3.6 Optymalizacja funkcji przez cache
# ------------------------------------------------------------------------------

# import biblioteki 

from  functools import lru_cache

""" Bardzo wolne dzialanie, uzyj cache
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(50))
"""

@lru_cache(maxsize=None) # --> bez limitu(None) 
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))

print(fib.cache_info()) 
# misses=51 --> ile razy wyniku nie bylo w pamieci
# hits=48 --> ile razy wynik juz byl w pamieci i wzielismy go gotowego
# maxsize --> limit pamieci
# currsize --> ile wynikow siedzi teraz w pamieci

def fib_zwykly(n):                    # ta sama funkcja, ale bez cache
    if n < 2:
        return n
    return fib_zwykly(n - 1) + fib_zwykly(n - 2)

start = time.perf_counter()
fib_zwykly(30)
bez_cache = time.perf_counter() - start
print(f"bez cache: {bez_cache:.6f} s") 

fib.cache_clear()  # czyscimy pamiec, zeby pomiar byl uczciwy
start = time.perf_counter()
wynik = fib(30)
z_cache = time.perf_counter() - start
print(f"z cache:   {z_cache:.6f} s")     # np. 0.000050 s
print(f"cache jest ok. {bez_cache / z_cache:,.0f} razy szybszy")

start = time.perf_counter()
fib(30)                               # drugi raz, wynik prosto z pamieci
print(f"drugi raz: {time.perf_counter() - start:.6f} s")   # np. 0.000001 s

# Pulapka 
# W przypadku cashowania argumenty musza byc hashowalne --> czyli jak jest mutowalne jak listy wywali nam blad

@lru_cache(maxsize=None)
def suma(liczba):
    return sum(liczba)

# suma([1,2,3])      # --> nie dziala na mutowalnego zmienialnych
print(suma((1,2,3))) # --> krotka dziala

# w randomizerach cacheowanie nie zadziala, nieoczekiwany wynik w postaci powtorzonych wartosci
import random

@lru_cache
def rzut_koscia():
    return random.randint(1, 6)

print(rzut_koscia(),rzut_koscia(),rzut_koscia())

def rzut_koscia():
    return random.randint(1, 6)

print(rzut_koscia(),rzut_koscia(),rzut_koscia())

# ##############################################################################
# ###  ZADANIA 3.6                                                           ###
# ##############################################################################

# 3.6.1: Dodaj cache do funkcji poniżej i wywołaj kwadrat(4), kwadrat(4), kwadrat(5). 
# Ile razy wypisze się Liczę...? Sprawdź cache_info(). def kwadrat(x): print("Liczę..."); return x * x

from functools import lru_cache as lru_cache

@lru_cache(maxsize=None)
def kwadrat(x):
    print("Liczę...")
    return x * x
print(kwadrat(4), kwadrat(4), kwadrat(5))
print(kwadrat.cache_info())

# ==============================================================================
# 4. GENERATORY
# ==============================================================================

# ------------------------------------------------------------------------------
# 4.1 yield
# ------------------------------------------------------------------------------

# Specjalna funkcja, ktora zwraca wartosci na zadanie --> yield

def prosty_generator():
    print("start")
    yield 1
    print("po pierwszym razie")
    yield 2
    print("po drugim razie")
    yield 3

# print(prosty_generator()) #--> <generator object prosty_generator at 0x709eb8147640>

gen = prosty_generator() # nic sie na ten moment nie dzieje 
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # Jak generator jest skonczony rzuca wyjatek StopIteration

gen_dwa = prosty_generator() # --> zaczyna od nowa 
print(next(gen_dwa))

# iteracja generatora przez petle
for wartosc in prosty_generator(): # Iteratorach 6
    print(wartosc)

# Generator vs lista:

# lista wszystko w pamieci naraz
lista = [x**2 for x in range(1000000)]

# generator, produkuje po jednym
gen = (x**2 for x in range(1000000))

import sys
print(sys.getsizeof(lista)) #8448728 bajty
print(sys.getsizeof(gen))   #208 bajty (zalezy od wersji pythona, na 3.12 wychodzi 200)

# generator wykonuje od razu sum/ max / min ....
print(sum(x**2 for x in range(1000000)))
print(max(len(s) for s in ['kot','hipopotam','pies']))

# Pulapka 
gen = (x * 2 for x in range(3))
print(list(gen)) # --> stworzenie listy z generatora !! tylko na skonczonych
print(list(gen)) # [] # --> generator sie wyczerpal 

# uzycie len() oraz indexowania jak na liscie w stosunku do generatora

# print(len(gen)) # TypeError: object of type 'generator' has no len()
# print(gen[0]) # TypeError: 'generator' object is not subscriptable

# ##############################################################################
# ###  ZADANIA 4.1                                                           ###
# ##############################################################################

# 4.1.1: Napisz generator z_wielkiej(imiona), który zwraca kolejne imiona zaczynające się wielką literą. Sprawdź na ["ala", "OLA", "eWa"].

# Funkcja do leniwego wyciagania wielolinikowa
# *****************************************************
# Stworzenie gotowej listy z gen 

def z_wielkiej(imiona):
    for x in imiona:
        yield x.capitalize()

gen_z1 = z_wielkiej(["ala", "OLA", "eWa"]) 
gen_z2 = z_wielkiej(["ala", "OLA", "eWa"]) 

print(next(gen_z1))
print(list(gen)) # gen zostal juz wykorzystany wyzej (wyczerpany), wiec wypisze []

# *****************************************************
gen = (x.capitalize() for x in ["ala", "OLA", "eWa"])
print(next(gen))
print(next(gen))
print(list(gen))
print(list(gen))

# 4.1.2: Napisz generator odliczanie(n), który zwraca liczby od n w dół do 1, a na końcu napis "Start!". Sprawdź dla n = 3.

def odliczanie(n):
    while n>0:
        print(n)
        yield n
        n=n-1
    if n == 0:
        print('Start!')
        yield 'Start!'

gen = odliczanie(3)
print(list(gen))

# ------------------------------------------------------------------------------
# 4.2 Generatory skonczone
# ------------------------------------------------------------------------------

def parzyste_do(limit):
    n = 0
    while n <= limit:
        yield n
        n +=2

for liczba in parzyste_do(10):
    print(liczba)

print(list(parzyste_do(10)))

# czytanie pliku
def czytaj_linie(sciezka):
    with open(sciezka, encoding='utf-8') as plik:
        for linia in plik:
            yield linia.strip() # --> usuwa biale spacje z lewej i prawej strony 

quo_vadis = czytaj_linie('dane.txt') 

# return w generatorze

def do_pustej_linii(linie):
    for l in linie:
        if not l:
            return # koniec generatora
        yield l

print(list(do_pustej_linii(['a','b','','d']))) # ['a', 'b']

# Bonus 
def wszystko(*kolekcje):
    for kolekcja in kolekcje:
        yield from kolekcja

print(list(wszystko([1,2],(3,),'ab'))) # --> [1, 2, 3, 'a', 'b']

# ##############################################################################
# ###  ZADANIA 4.2                                                           ###
# ##############################################################################

# 4.2.1: Masz zamówienia w formacie "produkt;cena": ["kawa;18.99", "herbata;9.50", "", "sok;6.20", "woda;2.50"]. Zbuduj łańcuch generatorów: pomiń puste linie, 
# wyciągnij ceny jako float, zostaw tylko droższe niż 5 zł i policz ich sumę.

zamowienia = ["kawa;18.99", "herbata;9.50", "", "sok;6.20", "woda;2.50"]

niepuste = (z for z in zamowienia if z)
ceny = (float(z.split(';')[1])   for z in niepuste)
drogie = (c for c in ceny if c > 5)
print(sum(drogie))

# 4.2.2: Napisz generator do_stopu(slowa), który zwraca słowa wielkimi literami, ale kończy działanie na słowie "STOP" (samego "STOP" nie zwraca). 
# Sprawdź na ["ala", "ma", "STOP", "kota"]. Podpowiedź: wielkie litery daje metoda upper(), np. "ala".upper() --> "ALA".

def do_stopu(slowa):
    for i in slowa:
        if i != 'STOP':
            yield i.upper()
        else:
            return
gen = do_stopu(["ala", "ma", "STOP", "kota"])
print(list(gen))

# 4.2.3: Napisz generator wszystkie_produkty(*koszyki), który za pomocą yield from zwraca po kolei produkty ze wszystkich przekazanych koszyków (list).

def wszystkie_produkty(*koszyki):
    for i in koszyki:
        yield from i
gen = wszystkie_produkty(['Bulka', 'Chleb', 'Ser', 'Maslo'], ['Chleb', 'Maslo'])
print(list(gen))

# ------------------------------------------------------------------------------
# 4.3 Generatory nieskonczone
# ------------------------------------------------------------------------------

def liczby_naturalne():
    n = 1 
    while True: # nieskonczona petla, to ok w generatorze
        # print('Typowe gaszenie pozaru',n)
        yield n
        n += 1

gen = liczby_naturalne()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Pulapka
# print(list(gen)) # Nigdy nie uzywamy listy na while 

# islice z biblioteki itertools jako wyciagnie slicingu z generatora jako liste
from itertools import islice

pierwsze_5 = list(islice(liczby_naturalne(),5))
print(pierwsze_5)

# petla z break jako iterowanie przez generaor nieskocznoy
for n in liczby_naturalne():
    if n * n > 50:
        break
    print(n)

from itertools import count, cycle

numery = count(100) # 100 101 102 103, .. w nieskonczonosc
print(next(numery), next(numery)) # 100 101 

duzyrni = cycle(['Ala','Ola','Ela'])
for dzien in ['pon','wt','sr','czw','pt','sob','ndz']:
    print(dzien, next(duzyrni))

# ##############################################################################
# ###  ZADANIA 4.3                                                           ###
# ##############################################################################

# 4.3.1: Napisz nieskończony generator potegi_dwojki(), który zwraca 1, 2, 4, 8, 16... Pobierz pierwsze 10 wartości.

from itertools import islice
def potega_dwojki():
    n=0
    while True:
        yield 2**n
        n=n+1 # --> mozna incrementowac n += 1 (ten sam wyniki)
gen = potega_dwojki()
pierwsze_10 = list(islice(potega_dwojki(),10))
print(pierwsze_10)

# Dodatkowe
# 4.3.2: Napisz nieskończony generator numery_zamowien(prefiks), który zwraca "ZAM-1", "ZAM-2", "ZAM-3", ... 
# Pobierz z niego pierwsze 3 numery, a potem w pętli z break znajdź pierwszy numer kończący się na 0.

def numery_zamowien(prefiks):
    n=0
    while True:
        n=n+1
        yield str(prefiks) + '-' + str(n)
        # yield f'{prefiks}-{n}'
gen = numery_zamowien('ZAM')
pierwsze_3 = list(islice(numery_zamowien('ZAM'),3))
print(pierwsze_3)

for nr in gen:
    if nr.endswith('0'):
        print(nr)
        break

# ==============================================================================
# 5. OBIEKTOWOSC
# ==============================================================================

# Programowanie obiektowe (OOP).łaczy dane(atrybuty) i zachowania(metody) w jedno  

# ------------------------------------------------------------------------------
# 5.1 Klasy a instancje
# ------------------------------------------------------------------------------

class Pies:
    pass   # pusta klasa na start

burek = Pies() #--> stworzenie instancji
azor = Pies() #--> druga niezalezna instajca

print(type(burek)) # <class '__main__.Pies'>
print(burek is azor) # False 
print(isinstance(burek,Pies)) # True --> instancja burek nalezy do klasy Pies

# ------------------------------------------------------------------------------
# 5.2 Atrybuty
# ------------------------------------------------------------------------------

burek.imie = 'Burek' # atrybut instancji
print(burek.imie) 
burek.ime = 'Burek' # atrybut instancji
print(burek.ime) # blad literowka wprowadzi nowy atrybt 
burek.wiek = 28 # atrybut instancji

# Atrybut przypisalismy do burka, nie do reksia, reksio nie ma takiego atrybut 
reksio = Pies()
# print(reksio.imie) # AttributeError: 'Pies' object has no attribute 'imie'

print(burek.__dict__) # {'imie': 'Burek', 'ime': 'Burek', 'wiek': 28}

# ------------------------------------------------------------------------------
# 5.3 Atrybuty domyslne
# ------------------------------------------------------------------------------

class Dog():
    gatunek = 'Piesowaty' # atrybut klasy, domyslny, wpolny dla wszystkich instancji 

zoja = Dog()
wafel = Dog()

print(wafel.gatunek)
print(zoja.gatunek)

zoja.gatunek = 'wilczur'

print(wafel.gatunek)
print(zoja.gatunek)

# zmiana przez klase atrybutu wspolnego

Dog.gatunek = 'pies domowy'

print(wafel.gatunek)
print(zoja.gatunek)

print(wafel.__dict__)
print(zoja.__dict__)

# ##############################################################################
# ###  ZADANIA 5.3                                                           ###
# ##############################################################################

# 5.3.1: Utwórz pustą klasę Ksiazka z atrybutami domyślnymi wypozyczalna = True i kara_za_dzien = 0.5. Utwórz dwie książki: lalka (tytuł "Lalka", autor "Prus") i encyklopedia 
#   (tytuł "Encyklopedia PWN"), której nie można wypożyczać. Wypisz przy każdej książce, czy można ją wypożyczyć. Potem jedną linijką podnieś karę do 1 zł dla wszystkich książek 
# naraz i sprawdź __dict__ encyklopedii: które atrybuty są jej własne, a które bierze z klasy?

class Ksiazka():
    wypozyczalnia = True
    kara_za_dzien = 0.5

lalka = Ksiazka()
lalka.tytul = 'Lalka'
lalka.autor = 'Prus'

encyklopedia = Ksiazka()
encyklopedia.tytul = 'Encyklopedia PWN'
encyklopedia.wypozyczalnia = False

print(encyklopedia.wypozyczalnia)
print(lalka.wypozyczalnia)
Ksiazka.kara_za_dzien = 1
print(encyklopedia.__dict__)

for k in [lalka, encyklopedia]:
    if k.wypozyczalnia:
        print(f'{k.tytul}: jest mozliwy do wypozyczenia')
    else:
        print(f'{k.tytul} tylko na miejscu')

wspolne = {k: v for k, v in vars(Ksiazka).items() if not k.startswith("__")} | encyklopedia.__dict__ # --> wspolne atrybuty klasowe i instancji razem
print(wspolne)

# print( Ksiazka.__dict__) caly slownik --> dict dla obiektu klasy

# ------------------------------------------------------------------------------
# 5.4 Obiekty jako atrybuty obiektu
# ------------------------------------------------------------------------------

class Silnik:
    pass

class Samochod:
    pass

auto = Samochod()
ford = Samochod()
auto.marka = "Toyota"
auto.silnik = Silnik() # obiekt jako atrybut obikeut
auto.silnik.moc = 132
ford.silnik = Silnik()
ford.silnik.moc = 400

print(auto.silnik.moc)
print(auto.silnik) # <__main__.Silnik object at 0x7c946f9406e0>

# Pulapka # wspolny obiekt jako przekazywany do atrybutow jako atrybut 

auto1 = Samochod()
auto2 = Samochod()
wspolny = Silnik()
wspolny.moc = 100
auto1.silnik = wspolny
auto2.silnik = wspolny

auto1.silnik.moc = 200
print(auto1.silnik.moc)
print(auto2.silnik.moc)

# ------------------------------------------------------------------------------
# 5.5 Metody
# ------------------------------------------------------------------------------

class Konto:
    saldo = 0

    def wplac(self, kwota):
        self.saldo += kwota # self = ten konkretny obiekt 

    def pokaz(self):
        print(f'Saldo: {self.saldo} zl')

    def wyplac(self, kwota):
        if kwota > self.saldo: 
            print("Brak srodkow")
            return 
        self.saldo -= kwota
        self.pokaz() # metoda wola inna metode przez self

moje = Konto()
# print(moje.pokaz) # <bound method Konto.pokaz of <__main__.Konto object at 0x70c62e648440>>
# moje.pokaz
moje.pokaz()
# moje.wplac() TypeError: Konto.wplac() missing 1 required positional argument: 'kwota'
moje.wplac(200)
moje.pokaz()
moje.wyplac(500)
moje.wyplac(150)

druga = Konto()
druga.pokaz()

# Pulapka w metodach zawsze dodawaj self
class Pies:
    def szczekaj(): 
        print('Hau!')

# Pies().szczekaj() TypeError: Pies.szczekaj() takes 0 positional arguments but 1 was given

# ##############################################################################
# ###  ZADANIA 5.5                                                           ###
# ##############################################################################

# 5.5.1: Napisz klasę Prostokat z metodami pole(), obwod() i opis(). Boki a i b ustaw obiektowi z zewnątrz. 
# Metoda opis() ma korzystać z dwóch pozostałych i zwracać Prostokąt 3x4: pole 12, obwód 14.

class Prostokat:
    def pole(self):
        return self.a * self.b
    def obwod(self):
        return (self.a) * 2 + (self.b) * 2
    def opis(self):
        return f'Prostokąt {self.a}x{self.b}: pole {self.pole()}, obwód {self.obwod()}'

p = Prostokat()
p.a = 4
p.b = 10

print(p.opis())

# Dlaczego lepsze niż zewnętrzne funkcje ?

# hermetyzacja - czyli logika i dane w jednym miejscu 
# Ponowne uzyc - ta sama klasa, metody przypisane do niej
# Bezpieczenstaw - kontrolwac dodawanie do danych 
# Czytelnosc konto.wyplac(100) mowi wiecej niz wyplac(konto, 100)

# ------------------------------------------------------------------------------
# 5.6 Widocznosc
# ------------------------------------------------------------------------------

#   metoda() --> publiczne 
#  _metoda() --> Chroniona , da sie wywolac, ale umownie sie tego nie robi
# __metoda() --> prywatna python zmienia nazwe (name mangling), wiec nie wywolamy jej z zewnatrz (jest sposob na to)

class Ekspres:
    def zrob_kawe(self):           # publiczna metoda
        self._podgrzej_wode()
        self._zaparz()
        self.__zapisz_w_liczniku()

    def _podgrzej_wode(self):       # chroniona metoda
        print('Podgrzewam wode')

    def _zaparz(self):             # chroniona metoda
        print('Parze kawe') 

    def __zapisz_w_liczniku(self):   # prywatna
        print("(Serwis) +1 kawa w liczniku")

e = Ekspres()
e.zrob_kawe()

# Podgrzewam wode
# Parze kawe
# (Serwis) +1 kawa w liczniku

# e.zaparz() AttributeError: 'Ekspres' object has no attribute 'zaparz'
# podkreslnik to czesc nazwy (_zaparz), chroniona da sie wywolac:
e._zaparz()

# e.__zapisz_w_liczniku() AttributeError: 'Ekspres' object has no attribute '__zapisz_w_liczniku'. Did you mean: '_Ekspres__zapisz_w_liczniku'? prywatna 
e._Ekspres__zapisz_w_liczniku() # dostanie sie do prywatnej 

# ------------------------------------------------------------------------------
# 5.7 Konstruktor __init__
# ------------------------------------------------------------------------------

# metoda wywływania automatycznie przy tworzeniu obiektu. Ustawia poczatkowy stan

class Osoba:
    def __init__(self):
        print("Tworzy nowa osobe!")
        self.energia = 100

o = Osoba()
print(o.energia)

# Pulapka atrybut wspolny lista i instacnja

class Cat:
    atrybut = []

    def __init__(self):
        self.atrybucik = []

o1 = Cat()
o1.atrybut.append(50)
o1.atrybucik.append(50)

o2 = Cat()
print(o2.atrybut)
print(o2.atrybucik)

# pulapka nazewnictwo __init__ ----> liteowka wywali blad 
# ale nie od razu: __int__ to zwykla metoda, blad wyjdzie dopiero przy Osoba('Ala') albo odczycie atrybutu

# ------------------------------------------------------------------------------
# 5.9 Parametryzacja konstruktora
# ------------------------------------------------------------------------------

class Osoba:
    def __init__(self,imie, wiek, miasto='nieznane'):
        self.imie = imie
        self.wiek = wiek
        self.miasto = miasto

ala = Osoba('Ala',28,'krakow') # jesli damy za duzo pozycji wywali nam blad za duzo argumentow. Tak samo w druga strone 
ola = Osoba('Ola',32)

print(ala.imie,ala.miasto)
print(ola.imie,ola.miasto)

# Osoba('Ala') # TypeError: Osoba.__init__() missing 1 required positional argument: 'wiek'

class Uczen:
    def __init__(self,imie,lista = []):
        self.imie = imie
        self.lista = lista

ala = Uczen("Ala")
ola = Uczen("Ola")
ala.lista.append(5)
print(ola.lista) 

class Uczen:
    def __init__(self, imie, oceny=None):  # dobrze
        self.imie = imie
        self.oceny = oceny if oceny is not None else []

# ##############################################################################
# ###  ZADANIA 5.9                                                           ###
# ##############################################################################

# Klasee z kontruktorem __init__ Samcohod() ktora bedzie zawierala pola do wpisania jako marka, kolor, pojemnosc domylnsa

# 5.9.1: Napisz klasę Samochod, której konstruktor przyjmuje marka, spalanie (litry na 100 km) i bak z wartością domyślną 50. Poza tym konstruktor ustawia dwa atrybuty, które nie są parametrami: paliwo (na start pełny bak) i przebieg = 0. Dodaj metody:

#     jedz(km): liczy potrzebne paliwo (km * spalanie / 100); jeśli wystarczy, zmniejsza paliwo i zwiększa przebieg, a jeśli nie, wypisuje Fiat: za mało paliwa na 500 km,
#     tankuj(litry): dolewa paliwo, ale nigdy ponad pojemność baku,
#     opis(): zwraca np. Toyota: przebieg 200 km, w baku 38.0 l.

# Utwórz Toyotę (spalanie 6, domyślny bak) i Fiata (spalanie 8, bak 35). Toyotą przejedź 200 km, Fiatem spróbuj 500 km, potem 300 km i zatankuj 100 l. Wypisz opisy obu aut.
"""
class Samochod:

    def __init__(self,marka,spalanie,bak=50):
        self.marka = marka
        self.spalanie = spalanie
        self.bak = bak
        self.paliwo = bak
        self.przebieg = 0

    def jedz(self,km):
        if ((km/100)*self.spalanie)>self.paliwo:
            return f'Za malo paliwa na {km} km'
        self.paliwo = self.paliwo - ((km/100)*self.spalanie)
        self.przebieg = self.przebieg + km

    def tankuj(self,litry):
        if self.paliwo + litry > 50:
            return 'Za mało pojemności w baku'
        self.paliwo = self.paliwo + litry

    def opis(self):
        return f'{self.marka}: przebieg {self.przebieg} km, w baku {self.paliwo}'

"""   

class Samochod:
    def __init__(self, marka, kolor, pojemnosc=180):
        self.marka = marka
        self.kolor = kolor
        self.pojemnosc = pojemnosc

auto1 = Samochod('Toyota', 'Czarny', 160)
auto2 = Samochod('Peugeot', 'Bialy', 180)

# ------------------------------------------------------------------------------
# 5.10 Dziedziczenie
# ------------------------------------------------------------------------------

# Dziedziczenie po jednej klasie

class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def jedz(self):
        print(f"{self.imie} je")

    def daj_glos(self):
        print(f"{self.imie}: ...")

class Pies(Zwierze):          # Pies dziedziczy po Zwierze
    def szczekaj(self):
        print(f"{self.imie}: Hau!")
    def daj_glos(self):
            print(f"{self.imie}: Hau!")

burek = Pies('burek')
burek.jedz()
burek.szczekaj()
burek.daj_glos() # Nadpisuje metode rodzica 

print(isinstance(burek, Pies))   # Prawda
print(isinstance(burek, Zwierze)) # Prawda
print(issubclass(Pies, Zwierze))   # Prawda

# super() --> wywolanie metody klasy rodzica do rozszerzenia

class Pracownik:
    def __init__(self, imie, pensja):
        self.imie = imie
        self.pensja = pensja
    def opis(self):
        return f"{self.imie}, pensja {self.pensja} zl"

class Kierownik(Pracownik):
    def __init__(self, imie, pensja, zespol):
        super().__init__(imie, pensja)   # rodzic ustawia imie i pensja
        self.zespol = zespol             # dziecko doklada wlasny atrybut

    def opis(self):
        tekst = super().opis()           # bierzemy gotowy opis od rodzica
        return f"{tekst}, zespol: {self.zespol} osob"   # i go rozszerzamy

jan = Pracownik("Jan", 6000)
ewa = Kierownik('Ewa', 900, 5)

print(jan.opis())
print(ewa.opis())
print(ewa.imie)

# Pulapka  brak super().__init__

class Pracownik:
    def __init__(self, imie, pensja):
        self.imie = imie
        self.pensja = pensja

# zle: wlasny __init__ w dziecku zastepuje konstruktor rodzica
class Kierownik(Pracownik):
    def __init__(self, imie, pensja, zespol):
        self.zespol = zespol             # zapomniane super().__init__(imie, pensja)

ewa = Kierownik("Ewa", 9000, 5)
print(ewa.zespol)
# print(ewa.imie) AttributeError: 'Kierownik' object has no attribute 'imie'

# Dzidziczenie po wielu klasach
# wielodziedziczeniem

class Plywak:
    def plyn(self):
        print("Plyne")

class Lotnik:
    def lec(self):
        print('Lece')

class Kaczka(Plywak, Lotnik): # dziedziecznie po obu klasach
    pass

donald = Kaczka()
donald.plyn()
donald.lec()

# Z kolejnoscia dziedziczenia (MRO)

class A:
    def kto(self):
        print('A')

class B:
    def kto(self):
        print('B')

class C(B,A): # Ta klasa rodzica, ktora jest pierwsze nadpisuje kolejnoscia 
    pass

C().kto() 

print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# ------------------------------------------------------------------------------
# 5.11 Metody i klasy abstrakcyjne
# ------------------------------------------------------------------------------

from abc import ABC, abstractmethod

"""
class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass 

    def opis(self):
        return f"{type(self).__name__} o polu {self.pole()}"

class Kolo(Figura):
    def __init__(self,r):
        self.r = r
 
K = Kolo(5)

# TypeError: Can't instantiate abstract class Kolo without an implementation for abstract method 'pole'
# Bez implementacji metody pola nie pzowoli stworzyc instancji

"""
class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass 

    def opis(self):
        return f"{type(self).__name__} o polu {self.pole()}"

class Kolo(Figura):
    def __init__(self,r):
        self.r = r
    def pole(self): # Pole tez nie pozwoli stworzyc instancji z literowka, bo nie ma takiej samej rodzic metody
        return 3.14 * self.r ** 2
 
k = Kolo(5)
print(k.pole())
print(k.opis())

# Pulapka

# zawsze musi byc polaczenie wybrana metoda z @abstracmethod oraz ABC w Figura(ABC)
class Figura:                   # zapomniane (ABC)
    @abstractmethod
    def pole(self):
        pass

Figura() 

# ------------------------------------------------------------------------------
# 5.12 Metody magiczne
# ------------------------------------------------------------------------------

# Metody magiczne --> __init__ --> metoda magiczna --> dunder 

# metoda str / repr
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

o = Osoba('Ala',30)
# Zwraca brzydki obiekt 
print(o) # <__main__.Osoba object at 0x7374bd2017f0>
print([0, Osoba('Ola',30)]) # [0, <__main__.Osoba object at 0x7e80cd4e8050>]

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    def __str__(self): # zwraca za pomoca print okreslone wartosci
        return f'Osoba: {self.imie, self.wiek}' # uwaga: {self.imie, self.wiek} to krotka --> Osoba: ('Ala', 30)
    def __repr__(self): # repr --> opis dla programisty, uzywany w konsoli i gdy obiekt siedzi w liscie lub slowniku
        return f'Osoba({self.imie}, {self.wiek})'

o = Osoba('Ala',30)
print([o, Osoba('Ola',30)])
print(o) #Przy pomocy __str__ print zamienia sie na to co chcemy przekazac z danej klasy przy pomocy print()

# w str zawsze w metodzie dunder musimy zwracac string 
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek
    def __str__(self):
        return self.wiek

# print(Osoba(30)) TypeError: __str__ returned non-string (type int)

# getitem, odczyt przez []

"""
class Zespol:
    def __init__(self, czlonkowie):
        self.czlonkowie = czlonkowie

z = Zespol(['Ala','Ola','Dominik'])
print(z[0])
print(len(z))

# Wywali bledy 

"""

class Zespol:
    def __init__(self, czlonkowie):
        self.czlonkowie = czlonkowie

    def __getitem__(self, indeks):
        return self.czlonkowie[indeks]
    
    def __len__(self):              # dla len()
        return len(self.czlonkowie)

z = Zespol(['Ala','Ola','Dominik'])
print(z[0])
print(len(z))

# setitem, zapis przez []

"""
class Dziennik:
    def __init__(self):
        self.oceny = {}

d = Dziennik()
d['matma'] = 5

TypeError: 'Dziennik' object does not support item assignment

Dziennik klasa nie obsluguje tej metody 
"""

class Dziennik:
    def __init__(self):
        self.oceny = {}

    def __setitem__(self, przedmiot, ocena):    # d[przedmiot] = ocena
        if not 1 <= ocena <= 6:
            raise ValueError("Ocena musi byc od 1 do 6")
        self.oceny[przedmiot] = ocena

    def __getitem__(self, przedmiot):           # d[przedmiot]
        return self.oceny[przedmiot]
        
d = Dziennik()
d['matma'] = 5

print(d['matma'])

# eq, porównanie przez ==

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Punkt(1, 2) == Punkt(1 ,2)) # False - niby dwa rozne obiekty 

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, inny):
        return self.x == inny.x and self.y == inny.y 

print(Punkt(1, 2) == Punkt(1 ,2)) # True
print(Punkt(1, 2) == Punkt(1 ,3)) # False 

# Istnieja jeszcze takie metody jak __add__ __lt__ __contains__ __iter__

# ------------------------------------------------------------------------------
# 5.13 Hermetyzacja
# ------------------------------------------------------------------------------

class Konto:
    def __init__(self,saldo,chroniona):
        self.__saldo = saldo
        self._chroniona = chroniona

konto = Konto(1000,50)

# print(konto.__saldo ) #ttributeError: 'Konto' object has no attribute '__saldo'
print(konto._Konto__saldo)
print(konto._chroniona)

konto._Konto__saldo = 2000
konto._chroniona = 500

# Nadpisywanie 
print(konto._Konto__saldo)
print(konto._chroniona)

# Kontrolowany dostęp

# property setter

print('*' * 20)

class Bank:
    def __init__(self,saldo):
        self.saldo = saldo

    @property 
    def saldo(self):        # getter, odczyt jak atrybut 
        return self.__saldo

    @saldo.setter
    def saldo(self, wartosc):
        if wartosc < 0:
            raise ValueError("Saldo nie moze byc ujemne!")
        self.__saldo = wartosc

bank = Bank(1000)
print(bank.saldo)
bank.saldo = 500
print(bank.saldo)

# bank.saldo = -100
# Bank(-100)

class Prostokat:
    def __init__(self,a,b):
        self.a = a 
        self.b = b

    @property
    def pole(self):
        return self.a * self.b 

p = Prostokat(3, 4)
print(p.pole)

# BLokada przez setter 
# p.pole = 100 # AttributeError: property 'pole' of 'Prostokat' object has no setter

# ------------------------------------------------------------------------------
# 5.14 Dokumentowanie klas
# ------------------------------------------------------------------------------

# przyklad tylko do pokazania docstringa, sama klasa nie jest prawdziwym kalkulatorem
class Kalkulor:
    """ Prosty kalkulator zbiera liczby za pomoca konstruktora init a nastepnie wykonuje metoda na nich dzialania
    
    """

    def dodaj(self ,a ,b):
        """ zwraca dodawanie dwoch cyfry przekazanych przez uzytkownika"""
        return 1

print(Kalkulor.__doc__)
# help(Kalkulor)

print(Kalkulor.dodaj.__doc__)

# ==============================================================================
# 6. ITERATORY
# ==============================================================================

# ------------------------------------------------------------------------------
# 6.1 __iter__ i __next__
# ------------------------------------------------------------------------------

# To sa obiekty po ktorych mozna iterowac petla for. Uzywa dwoch metod magicznych(dunder) __iter__ oraz __next__.Generator jest to sposob tworzenia iteratorow 

# __iter__ zwraca obiekt iteratora (zwykle self)
# __next__ zwraca kolejna wartosc, gdy nie ma juz wartosci rzuca wyjatek StopIteration

nums = [1,2,3]

nums_iterator = nums.__iter__()
print(nums_iterator.__next__()) # 1
print(nums_iterator.__next__()) # 2
print(nums_iterator.__next__()) # 3
# print(nums_iterator.__next__()) StopIteration

it = iter(nums)
print(next(it))

animals = ['papuga','pies','malpa']

# for animal in animals:
#     print(animal)

# robi pod spodem dokladnie iterator

animals_iterator = iter(animals)
while True:
    try:
        animal = next(animals_iterator)
        print(animal)
    except StopIteration:
        break

# iterator ma __iter__ oraz __next__, pamieta swoja pozycja 
# iterable (iterowalny) ma __iter__ np. lista,string,slownik

lista = [1,2,3] # --> iterable, ale nie iterator 
it = iter(lista) # --> jest to iterator 

# Bonus: wlasna klasa iterowalna (iterable), a nie iterator
# ma tylko __iter__ bez __next__, for dziala bo sam wola iter(), ale next(uzytkownicy) wywali TypeError

class Uzytkownicy:
    def __init__(self):
        self.uzytkownicy = {}

    def dodaj(self, login, haslo):
        self.uzytkownicy[login] = haslo

    def usun(self, login):
        self.uzytkownicy.pop(login)

    def __iter__(self):
        return iter(self.uzytkownicy.items())   # oddajemy gotowy iterator ze slownika

uzytkownicy = Uzytkownicy()
uzytkownicy.dodaj("tak", "haslo")
uzytkownicy.dodaj("nie", "haslo14")

for (login, haslo) in uzytkownicy:              # petla for dziala na naszej klasie
    print(f"Nazwa uzytkownika: {login}")
    print(f"Haslo: {haslo}")
# Nazwa uzytkownika: tak
# Haslo: haslo
# Nazwa uzytkownika: nie
# Haslo: haslo14

# class Powiadomienie:
#     def __init__(self, odbiorca, tresc):
#         self.odbiorca = odbiorca
#         self.tresc = tresc
#     def wyslij(self):
#         return f'Do {self.odbiorca}: {self.tresc}
# class Email(Powiadomienie):
#     def __init__(self, temat, odbiorca, tresc):
#         super().__init__(odbiorca, tresc)
#         self.temat = temat
#     def wyslij(self):
#         self.tresc = super().wyslij()
#         return f'[EMAIL] {self.temat}, {self.tresc}'
# class SMS