# Trzeci dzien

# ==============================================================================
# 7. DEKORATORY
# ==============================================================================

# ------------------------------------------------------------------------------
# 7.1 Zasada dzialania
# ------------------------------------------------------------------------------

# Dekorator przyjmuje funkcje, owija ja w funkcje wewnetrzna (zwraca wrapper)

def moj_dekorator(funkcja):
    def wrapper():
        print('Przed wywolaniem funkcji')
        funkcja()
        print("Po wywolaniu funkcji")
    return wrapper

def przywitaj():
    print('Czesc')

# reczne udekorowanie
przywitanie = moj_dekorator(przywitaj)
przywitanie()

@moj_dekorator
def przywitaj():
    print('Witaj')

przywitaj()

@moj_dekorator
def dodaj():
    print(2+7)

dodaj()

import functools

def loguj(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args,**kwargs):
        print(f"Wywoluje {funkcja.__name__} z {args}, {kwargs}")
        wynik = funkcja(*args,**kwargs)
        print(f"Wynik: {wynik}")
        return wynik
    return wrapper

@loguj
def dodaj(a,b):
    return a + b

dodaj(3,7)
print(dodaj.__name__)

# Pulapka wrapper bez returna

def loguj(funkcja):
    def wrapper(*args,**kwargs):
        print(f"Wywoluje ....")
        funkcja(*args,**kwargs) # brak return
    return wrapper

@loguj
def dodaj(a,b):
    return a + b

print(dodaj(3,7)) # --> None

# brak functools.wraps. Funkcja traci swoja tozszamosc
print(dodaj.__name__) # wrapper, nie dodaj

# dekorator z argumentem

def powtorz(n): # 1. przyjmuje argument dekoratora
    def dekorator(funkcja): # 2. przyjmuje funkcje
        @functools.wraps(funkcja)
        def wrapper(*args,**kwargs):# 3 zastepuje
            for _ in range(n):
                funkcja(*args,**kwargs)
        return wrapper
    return dekorator

@powtorz(4)   # rownowazne hej = powtorz(4)(hej)
def hej():
    print('hej')

hej()

# kilka dekoratorow naraz od dolu do gory, najblizszy funkcji owija ja pierwszy

def pogrub(funkcja):
    def wrapper():
        return "<b>" + funkcja() + "</b>"
    return wrapper

def kursywa(funkcja):
    def wrapper():
        return "<i>" + funkcja() + "</i>"
    return wrapper

@kursywa
@pogrub
def tekst():
    return 'raz-dwa-trzy'

print(tekst())

# ##############################################################################
# ###  ZADANIA 7.1                                                           ###
# ##############################################################################

# 7.1.1: Napisz dekorator ramka, który przed i po wywołaniu funkcji
# wypisuje linię =====. Użyj go na funkcji wypisującej Raport gotowy.

import functools

def ramka(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args,**kwargs):
        print('============')
        wynik = funkcja(*args,**kwargs)
        print('============')
        return wynik
    return wrapper

@ramka
def raport():
    print('Raport gotowy')

raport()

# Pulapka gdy w wrapperze jest print(wynik) zamiast return wynik i dwie ramki naraz
# def ramka(funkcja):
#     @functools.wraps(funkcja)
#     def wrapper(*args,**kwargs):
#         print('============')
#         wynik = funkcja(*args,**kwargs)
#         print(wynik) # zamiast return wynik
#         print('============')
#     return wrapper
#
# @ramka
# @ramka
# def printer(x):
#     return x
# printer('Ala ma kota')
# ============
# ============
# Ala ma kota
# ============
# None
# ============
# None bo wewnetrzny wrapper nic nie zwraca, a zewnetrzna ramka to wypisuje

# 7.1.2: Napisz dekorator @pomnoz_wynik(n) (z argumentem!),
# który mnoży wynik funkcji przez n. Sprawdź go na funkcji
# suma(a, b) z @pomnoz_wynik(3): suma(2, 4) ma zwrócić 18.

def pomnoz_wynik(n):
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args,**kwargs):
            wynik = funkcja(*args, **kwargs)
            return wynik * n
        return wrapper
    return dekorator

@pomnoz_wynik(3)
def suma(a,b):
    return a+b

print(suma(2,4))
print(suma(2,4)) # za drugim razem tez 18

# ------------------------------------------------------------------------------
# 7.2 Dekorator jako wzorzec projektowy
# ------------------------------------------------------------------------------

# dekorator jako wzorzec projektowy --> dodaje funkcjonalnosci dynamiczne bez zmieniania oryginalnego obiektu

import time

def zmierz_czas(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        wynik = funkcja(*args,**kwargs)
        czas = time.perf_counter() - start
        print(f'{funkcja.__name__} trwala {czas:.4f} s')
        return wynik
    return wrapper

@zmierz_czas
def wolna_funkcja():
    time.sleep(1)
    return 'gotowe'

wolna_funkcja()

# Dekoratory moga zapamietywac

import functools

def zapamietaj_ostatni(funkcja):
    # wrapper.ostatni_wynik = None #  UnboundLocalError: cannot access local variable 'wrapper' where it is not associated with a value
    @functools.wraps(funkcja)
    def wrapper(*args,**kwargs):
        wynik = funkcja(*args,**kwargs)
        wrapper.ostatni_wynik = wynik
        return wynik
    wrapper.ostatni_wynik = None
    return wrapper

@zapamietaj_ostatni
def kwadrat(x):
    return x * x

print(kwadrat.ostatni_wynik)
kwadrat(3)
kwadrat(5)
print(kwadrat.ostatni_wynik)

# ##############################################################################
# ###  ZADANIA 7.2                                                           ###
# ##############################################################################

# 7.2.1: Napisz dekorator licz_wywolania, który zlicza, ile razy wywołano funkcję.
# Licznik trzymaj jako atrybut wrappera
# (wrapper.licznik). Po trzech wywołaniach ma wynosić 3.

import functools
def licz_wywolania(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args,**kwargs):
        wrapper.licznik = wrapper.licznik + 1
        return funkcja(*args,**kwargs)
    wrapper.licznik = 0
    return wrapper

@licz_wywolania
def printer(x):
    return x

printer('Ala ma kota')
printer('Ala ma kota')
printer('Ala ma kota')
print(printer.licznik) # 3

# ------------------------------------------------------------------------------
# 7.3 Dekoratory funkcji
# ------------------------------------------------------------------------------

# Dekoratory funkcji (znane z wczesniejszych rozdzialow)

# @property, @saldo.setter sekcja 5.13 (hermetyzacja)
# @abstractmethod sekcja 5.11 klasy abstrakcyjne
# @lru_cache /  @functools.cache sekcja 3.6
# @staticmethod / @classmethod ponizej
# web @login_required

# @staticmethod, self --> metoda bez self
# @classmethod dostaje klase(cls) zamiast obiektu, taki alternatywny konstruktor

class Osoba:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    @staticmethod
    def czy_pelnoletni(wiek): # nie potrzebuje self ani cls
        return wiek >= 18

    @classmethod
    def z_napisu(cls, napis): # alternatywny konstruktor
        imie , wiek = napis.split('-')
        return cls(imie, int(wiek))

print(Osoba.czy_pelnoletni(17))
ala = Osoba.z_napisu("Ala-76")
print(ala.imie, ala.wiek)
