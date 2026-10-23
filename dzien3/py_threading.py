# ------------------------------------------------------------------------------
# map() i filter() na listach
# ------------------------------------------------------------------------------

liczby = [1,2,3,4,5,6]
# map() filter()
# map() --> odpowiedzalna zmienianie danych w liscie
parzyste = filter(lambda x: x % 2 == 0, liczby)
print(parzyste)# <filter object at 0x74c2072974f0>
print(list(parzyste))
kwadraty = map(lambda x: x ** 2,liczby)
print(kwadraty) # <map object at 0x74c2072974f0>
print(list(kwadraty))

# ==============================================================================
# 9. ASYNCHRONICZNOSC
# ==============================================================================

# ------------------------------------------------------------------------------
# 9.1 Biblioteka threading
# ------------------------------------------------------------------------------

# (THREAD) watek -> niezalezny ciag wykonywania dzialajacy wspolbieznie z glownym programem
import threading
import time

"""
def zadania(nazwa, ile):
    for i in range(ile):
        print(f"[{nazwa}] krok {i}")
        time.sleep(0.5)

# utworzyc watki
w1 = threading.Thread(target=zadania, args=("A", 3))
w2 = threading.Thread(target=zadania, args=("B", 3))

w1.start() # uruchamianie
w2.start()
w1.join() # czeka az watek A skonczy
w2.join() # czeka az watek B skonczy
print('Wszystkie watki zakonczone')
"""

"""
def pobierz(nr):
    print(f"Start pboierania {nr}")
    time.sleep(2)
    print(f"Koniec pobierania {nr}")

start = time.perf_counter()
watki = [threading.Thread(target=pobierz, args=(i,)) for i in range(3)]

for w in watki:
    w.start()
for w in watki:
    w.join()
print(f"Czas: {time.perf_counter() - start:.1f}s")
"""

# Pulapka --> ('ala') to str nie jest to krotka
# TypeError: pobierz() takes 1 positional argument but 3 were given
"""
def pobierz(imie):
    print('czesc', imie)

w1 = threading.Thread(target=pobierz, args=('ala'))

w1.start()
"""

# Pulapka --> target=praca() wywoluje funkcje od razu w glownym watku, a watek dostaje None i nic nie robi
# do target podajemy sama nazwe funkcji bez nawiasow: target=praca
"""
def praca():
    time.sleep(0.5)
    print('watek skonczyl')

w = threading.Thread(target=praca())
w.start()
print('Koniec programu')
"""

# wyscig (race condition) kilka watkow zmienia ta sama zmiennna jednoczesnie i nadpisuja sobie wyniku
"""
licznik = 0

def dodaj():
    global licznik
    for _ in range(100):
        tmp = licznik
        time.sleep(0.0001)
        licznik = tmp + 1

watki = [threading.Thread(target=dodaj) for _ in range(5)]

for w in watki: w.start()
for w in watki: w.join()
print(licznik) # np. 114 zamiast 500 mimo 5 watkow, za kazdym razem wychodzi inna liczba
"""

# Rozwiazanie problemu licznika z watkami
"""
licznik = 0
lock = threading.Lock()

def dodaj_bezpiecznie():
    global licznik
    for _ in range(100):
        with lock:
            tmp = licznik
            time.sleep(0.0001)
            licznik = tmp + 1

watki = [threading.Thread(target=dodaj_bezpiecznie) for _ in range(5)]

for w in watki: w.start()
for w in watki: w.join()
print(licznik)
"""

# Wyniki z watkow --> gdy potrzebujemy wynikow z watkow, uzywamy ThreadPoolExecutor z concurrent.futures
"""
from concurrent.futures import ThreadPoolExecutor

def pobierz(nr):
    time.sleep(1)
    return f"dane {nr}"

with ThreadPoolExecutor() as pula:
    wyniki = list(pula.map(pobierz, [1,2,3]))

print(wyniki)
"""

# ##############################################################################
# ###  ZADANIA 9.1                                                           ###
# ##############################################################################

# 9.1.1: Napisz funkcję sprawdz(adres), która „sprawdza” stronę przez time.sleep(1) i zapisuje do słownika wyniki[adres] = "OK".
# Uruchom ją w osobnych wątkach dla ["a.pl", "b.pl", "c.pl"], poczekaj na wszystkie i wypisz słownik oraz czas (ok. 1s).
"""
import time
import threading

wyniki = {}
list_to_check=["a.pl", "b.pl", "c.pl"]

def sprawdz(adres):
    time.sleep(1)
    wyniki[adres] = 'OK'

start = time.perf_counter()
watki = [threading.Thread(target=sprawdz, args=(a, )) for a in list_to_check]
for w in watki: w.start()
for w in watki: w.join()
print(wyniki)
print(f"Czas: {time.perf_counter() - start:.1f}s")
"""

# 9.1.2: Napisz funkcję licz(kto), która trzy razy wypisuje imię i numer (Ala 1, Ala 2, Ala 3),
# z przerwą pół sekundy między kolejnymi liczbami. Uruchom ją dla "Ala" i "Ola" na dwa sposoby:
#     normalnie, czyli po kolei: najpierw licz("Ala"), potem licz("Ola"),
#     w dwóch wątkach naraz.
# Przy obu sposobach zmierz czas przez time.perf_counter() i porównaj kolejność wypisywania oraz czas.
# Na końcu wypisz Koniec.
"""
import threading
import time
def licz(kto):
    for i in range(1, 4):
        print(f"{kto} {i}")
        time.sleep(0.5)

start = time.perf_counter()
licz("Ala")
licz("Ola")
koniec = time.perf_counter()
print(f"\nCzas sekwencyjnie: {koniec - start:.2f} s")

w1 = threading.Thread(target=licz, args=("Ala",))
w2 = threading.Thread(target=licz, args=("Ola",))
start = time.perf_counter()
w1.start()
w2.start()
w1.join()
w2.join()
koniec = time.perf_counter()
print(f"\nCzas wielowątkowo: {koniec - start:.2f} s")
print("Koniec")
"""

# ------------------------------------------------------------------------------
# 9.2 Zatrzymywanie watkow i demony
# ------------------------------------------------------------------------------

# Threading nie ma czegos kill stop()
# Zatrzymywanie watku warunkiem

# stop = threading.Event()

# def pracownik():
#     licznik = 0
#     while not stop.is_set():
#         licznik += 1
#         print(f"pracuje.... {licznik}")
#         time.sleep(0.5)
#     print('watek: dostalem sygnal, koncze porzadnie ')

# w = threading.Thread(target=pracownik)
# w.start()

# time.sleep(1.6)
# stop.set()
# w.join()
# print('main: watek zakonczony')

# Wątki jako demony
# watek deamon dziala w tle i jest automatycznie zabijany, gdy glowny program, sie konczy

def w_tle():
    while True:
        print('...pracuje w tle...')
        time.sleep(1)

d = threading.Thread(target=w_tle, daemon=True) # daemon jako argument z True
d.start()
# zamknelo program mimo braku d.join()
time.sleep(3)
print('Glowny program konczy, demon zostanie zabity ')
# watek demon nie blokuje zamkniecia programu

# Pulapka bez daemona program nigdy sie nie zakonczy, bo czeka na watek z petla nieskonczona
