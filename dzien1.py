# Pierwszy dzien

# ==============================================================================
# 1. LISTY
# ==============================================================================

# ------------------------------------------------------------------------------
# 1.1 Tworzenie list
# ------------------------------------------------------------------------------

pusta = []
print(pusta)
print(type(pusta))
pusta_dwa = list()

liczby = [1,2,3,4,5] #--> liczby
napisy = ['agrest','oliwka','jablko','porzeczka'] # --> napisy
zmiennoprzecinkowe = [5.6,2.5,7.8,2.4]
prawdziwosc = [True,False,True,False]
mieszana = [True,6.7,8,'agrest'] # unikac --> zacznie sypac bledy 

# Pulapka tworzenie zmiennoprzecinkowych
krotka = 5,6 #--> utworzenie krotki zamiast zmiennoprzecinkowej
print(type(krotka))

zagniezdzone = [[2,4],[6,7]]
zagniezdzona_glebokie = [[2,4],[6,[5,7],7],[6,7],[6,7]]

# z napisu utworzyc list
z_napisu = list('Programowanie')
print(z_napisu)
# z zakresu 
z_zakresu = list(range(5))

# range(start,stop,step)
# start --> poczatek z_zakresu
# stop --> koniec bez wlaczenia ostatniego
# step --> krok

print(z_zakresu)

# Mnozenie
zera = [0] * 5
print(zera)
puste = [None] * 5 
print(puste)
znaki_za = ['?'] * 5 
print(znaki_za)
elementy = [0,7,8] * 5
print(elementy)

# list comprehension

# for i in range(5)
lista_do_dzi = [i for i in range(1,11)] # najprostsze comprehension
print(lista_do_dzi)

wartosci = [-2,5,0,7,-1]

dodatnie = [x for x in wartosci if x >= 0]
print(dodatnie)
znaki = ['+' if x > 0 else '-' for x in wartosci]
print(znaki)
ujemne_bez = [x if x > 0 else 0 for x in wartosci]
print(ujemne_bez)
opis = ["duza" if x > 3 else 'mala' for x in wartosci if x % 2 == 0]
print(opis)
# modulo  --> sprawdzanie czy liczba jest podzielna
# x % 2 == 0

# Pulapka --> mnozenie

zla_macierz = [[0]*3] * 3 #--> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(zla_macierz)
zla_macierz[0][0] = 1
print(zla_macierz) #-> [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

dobra_macierz = [[0]*3 for _ in range(3)]
print(dobra_macierz)
dobra_macierz[0][0] = 1
print(dobra_macierz)

# Tworzenie list z slownika 
ceny = {'kawa':4.5,'herbata':3.5,'sok':2.5}

lista_produktow = list(ceny)
lista_produktow2 = list(ceny.keys())
print(lista_produktow)
print(lista_produktow2)
lista_cen = list(ceny.values())
print(lista_cen)

compr_slownik = [x for x in ceny.items()]
print(compr_slownik)

compr_slownik = [klucz for klucz,_ in ceny.items()]
print(compr_slownik)

lista_krotek = [('Ala', 45), ('Dominik', 35), ('Rafal', 27)]
lista_imion = [imie[0] for imie in lista_krotek]
# lista_imion = [imie[10] for imie in lista_krotek] # lista_imion = [imie[0] for imie in lista_krotek]
print(lista_imion)

# ##############################################################################
# ###  ZADANIA 1.1                                                           ###
# ##############################################################################

# 1.1.1: Bez pisania pętli stwórz: listę 10 zer, listę 4 elementów "?" 
# oraz listę liter słowa "programowanie".

list_1_1_1 = [0]*10
list_znaki_1_1_1 = ['?']*4
list_litery_1_1_1 = list('programowanie')
print(list_1_1_1)
print(list_znaki_1_1_1)
print(list_litery_1_1_1)

"""
# Pulapka
# list = [0]*10

#1000
print(list({'kawa':4.5,'herbata':3.5,'sok':2.5}))

import keyword 
print(keyword.kwlist)

""" 

# 1.1.2: Mając temperatury = [12, -3, 0, 25, -8, 17], utwórz nową listę, 
# w której temperatury ujemne zamienisz na 0, a pozostałe zostawisz bez zmian.

temperatury_1_1_2 = [12, -3, 0, 25, -8, 17]
temp_1_1_2 = [0 if x<0 else x for x in temperatury_1_1_2]
print(temp_1_1_2)

# 1.1.3: Z tej samej listy utwórz: listę samych temperatur dodatnich oraz 
# listę opisów "ciepło" (powyżej 15) / "zimno" (pozostałe) dla każdej temperatury.

temp_dodatnie_1_1_3 = [x for x in temperatury_1_1_2 if x > 0]
print(temp_dodatnie_1_1_3)
temp_1_1_2B = ['cieplo' if x>15 else 'zimno' for x in temperatury_1_1_2]
print(temp_1_1_2B)

# 1.1.4: Korzystając ze słownika ceny z bloku "Lista ze słownika" oraz listy zamówień 
# zamowienia = [("Ala", "kawa", 2), ("Ola", "herbata", 0), ("Ela", "kawa", 1), ("Jan", "sok", 3)] 
# (imię, produkt, ilość), utwórz za pomocą list comprehension: a) listę imion osób, które faktycznie 
# coś zamówiły (ilość większa od 0), b) listę kwot do zapłaty dla każdego zamówienia, 
# zaokrąglonych do 2 miejsc, c) listę opisów w formacie "Ala: duże" (kwota powyżej 20 zł) lub "Ela: małe" (pozostałe), 
# ale tylko dla osób, które coś zamówiły.

ceny = {'kawa':4.5, 'herbata':3.5, 'sok':2.5}
zamowienia = [("Ala", "kawa", 2), ("Ola", "herbata", 0), ("Ela", "kawa", 1), ("Jan", "sok", 3)]
#A
lista_imion = [imie for imie,produkt,ilosc in zamowienia if ilosc > 0]
print(lista_imion)
#B
lista_kwot = [f"{ceny.get(kwota[1])*kwota[2]:.2f}" for kwota in zamowienia] # round(do_zaokr,2)
print(lista_kwot)
lista_kwot2 = [ceny.get(kwota[1])*kwota[2] for kwota in zamowienia]
#c
wielkosc_zam = [f"{imie}: duze" if ceny[produkt]*ilosc > 20 else f"{imie}: male" for imie,produkt,ilosc in zamowienia if ilosc > 0]
print(wielkosc_zam)

# ------------------------------------------------------------------------------
# 1.2 Pobieranie wartosci z list
# ------------------------------------------------------------------------------

owoce = ['jablko','wisnia','agrest','porzeczka','mirabela']
# owoce =    0       1        2         3            4

print(owoce[0]) # --> wyciagniecie pierwszego z listy
# print(owoce[10]) #--> IndexError: list index out of range  poza zakresem indexu
print(owoce[4]) #--> zwraca 5 element listy (index 4)
print(owoce[-1]) #--> zwraca ostatni element listy
print(owoce[-3])
# print(owoce[-10]) #--> IndexError: list index out of range

# indexowanie zagniezdzone  - lista list
macierz = [[1,2,3],[4,5,6]]

print(macierz[0]) # --> zwraca pierwszy element listy -> liste
print(macierz[0][1])
print(macierz[0][-1])
print(macierz[-1][-1])
# print(macierz[-10][-1]) #--> IndexError: list index out of range
# print(macierz[-1][-10]) #--> IndexError: list index out of range 

gleboka_macierz = [1,[2,[3,[4,[5]]]]]
print(gleboka_macierz[1][1][1][0])

# Wyciaganie bezpieczne indexu 
index = 10
wartosc = owoce[index] if index < len(owoce) else None

# Slicingu (wycinki)

liczby = [0,1,2,3,4,5,6,7,8,9]

# liczby[start:stop:step]
print(liczby[0:3]) # [0,1,2] 
print(liczby[:3])  # [0,1,2] 
print(liczby[:])   # [0,1,2,3,4,5,6,7,8,9] 
print(liczby[:50]) # [0,1,2,3,4,5,6,7,8,9] nie ma list index out of range 
print(liczby[::2]) # [0,2,4,6,8]

# ujemne indexy w wycinkach
print(liczby[-3:]) # [7,8,9]
print(liczby[:-3]) # [0, 1, 2, 3, 4, 5, 6]
print(liczby[-3:-3])  # []

# odwrocenie slicingu 
print(liczby[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(liczby[2:8:-1])  # [] pusta lista - pulapka(odwrocone elementy )
print(liczby[8:2:-1]) # [8, 7, 6, 5, 4, 3]
print(liczby[-1:-3:-1]) # [9, 8]

# obiekt slice() Zapis [start:stop:step] --> slice(start,stop,step)

pesel = '96072910592'
ROK = slice(0,2)
MIESIAC = slice(2,4)
DZIEN = slice(4,6)

# print(f'Rok to: {ROK},Miesiac to: {MIESIAC}, DZIEN to {DZIEN}')
print(f'Rok to: {pesel[ROK]},Miesiac to: {pesel[MIESIAC]}, DZIEN to {pesel[DZIEN]}') 

# ##############################################################################
# ###  ZADANIA 1.2                                                           ###
# ##############################################################################

# 1.2.1: Mając tydzien = ["pon", "wt", "śr", "czw", "pt", "sob", "nd"], wyświetl pierwszy, ostatni i 
# przedostatni dzień tygodnia. Dla dwóch ostatnich użyj indeksów ujemnych.

tydzien = ["pon", "wt", "śr", "czw", "pt", "sob", "nd"]
# tydzien =  0     1     2      3     4      5      6

print(tydzien[0])
print(tydzien[-1])
print(tydzien[-2])

# 1.2.2: Z tej samej listy wytnij: dni robocze, weekend, co drugi dzień zaczynając od 
# poniedziałku oraz cały tydzień od tyłu.

print(tydzien[0:5])
print(tydzien[5:7])
print(tydzien[::2])
print(tydzien[::-1])

# 1.2.5*: Mając datę w formacie "2026-10-17", utwórz obiekty slice() o 
# nazwach ROK, MIESIAC, DZIEN i wypisz datę w polskim formacie 17.10.2026.

data = '2026-10-17'
ROK = slice(0,4)
MIESIAC = slice(5,7)
DZIEN = slice(8,10)
tekst = f"Rok to {data[ROK]} Miesiac to {data[MIESIAC]} Dzien to {data[DZIEN]}"
print(tekst)
print(f"{data[DZIEN]}.{data[MIESIAC]}.{data[ROK]}")

# ------------------------------------------------------------------------------
# 1.3 Iterowanie po listach
# ------------------------------------------------------------------------------

# for i in range(5)
# for x in obiekt

owoce = ['jablko','gruszka','wisnia']

for owoc in owoce:
    print(owoc)

# z indexem - enumerate()
for index,owoc in enumerate(owoce):
    print(f'{index}: {owoc}')

# enumerate z innym startem
for index,owoc in enumerate(owoce,start=1): # dowolny start nawet 20
    print(f'{index}: {owoc}')

ceny = [3.5,7,13]

for owoc,cena in zip(owoce,ceny):
    print(f'{owoc} - {cena} zl') 

# for index,owoc,cena in enumerate(zip(owoce,ceny)): --> wywali blad
#     print(f'{index}. {owoc} - {cena} zl') 

print(zip(owoce,ceny)) # --> <zip object at 0x74ace65d0780>
print(list(zip(owoce,ceny)))

for index,owoc in enumerate(zip(owoce,ceny),start=1):
    print(f'{index}. {owoc[0]} - {owoc[1]} zl') 

temperatury = [12, 15, 11, 18]
for dzis, jutro in zip(temperatury,temperatury[1:]):
    print(jutro-dzis)

# Pulapka iterowanie po listach

liczby  = [1, 2, 2, 3]            
#liczby = [0, 1, 2, 3] --> indexy
# liczby = [1,2,3] --> nie usunelo 2

"""
for x in liczby:
    if x == 2:
        liczby.remove(x)

print(liczby)
"""

liczby = [x for x in liczby if x != 2]
print(liczby)

# Pulapka zip() ucina nadmiarowe elementy w liscie
owoce = ['agrest','jablko']
ceny = [3.6, 6.8, 9.8, 5.6]

print(list(zip(owoce,ceny)))

owoce = ["jabłko", "banan", "wiśnia"]
for owoc in owoce:
    if owoc == 'agrest':
        print("Znaleziono")
        break 
else:
    print("Nie ma agrestu") # Wywoluje tylko jak skonczy sie lista

"""
owoce = ["jabłko", "agrest", "wiśnia"]
for owoc in owoce:
    if owoc == 'agrest':
        print("Znaleziono")
        break 
else:
    print("Nie ma agrestu") # Wywoluje tylko jak skonczy sie lista
"""

# ##############################################################################
# ###  ZADANIA 1.3                                                           ###
# ##############################################################################

# 1.3.1: Mając zakupy = ["mleko", "chleb", "masło", "jajka"], wypisz ponumerowaną listę zakupów zaczynając od 1 (1. mleko, 2. chleb, ...).

zakupy = ["mleko", "chleb", "masło", "jajka"]
for index,zakup in enumerate(zakupy,start=1):
    print(f'{index}. {zakup}')

# 1.3.4: Mając kurs euro z kolejnych dni kurs = [4.30, 4.28, 4.35, 4.31, 4.40], wypisz dla każdego dnia (od drugiego), 
# czy kurs wzrósł czy spadł i o ile. Użyj par sąsiednich elementów.

kurs = [4.30, 4.28, 4.35, 4.31, 4.40]
for index,i in enumerate(kurs):
    if index>0:
        roznica = kurs[index-1]-kurs[index]
        if roznica > 0:
            print(f'Kurs spadl o {abs(round(roznica,2))}')
        else:
            print(f'Kurs wzrosl o {abs(round(roznica,2))}')

# 1.3.6*: Z listy oceny = [5, 1, 2, 4, 2, 3] trzeba usunąć wszystkie oceny niższe niż 3. Kolega napisał pętlę z oceny.remove(o) 
# wewnątrz for o in oceny. Bez uruchamiania przewidź, co wyjdzie, wyjaśnij dlaczego, a potem napisz poprawną wersję.

oceny = [5, 1, 2, 4, 2, 3]
#Nie uda się ponieważ pętla będzie przeskakiwać przez elementy - jej długość będzie zmieniać się w trakcie działania.
oceny2 = [x for x in oceny if x >= 3]
print(oceny2)

# ------------------------------------------------------------------------------
# 1.4 Sprawdzanie, czy element znajduje sie na liscie
# ------------------------------------------------------------------------------

owoce = ["jabłko", "banan", "wiśnia"]

print('banan' in owoce)        # True
print('gruszka' in owoce)      # False
print('gruszka' not in owoce)  # True

# Bezpieczne pobranie indexu vs z bledem
print(owoce.index('banan'))

# print(owoce.index('bananaa')) # list.index(x): x not in list

if 'bananna' in owoce:
    print('bananna istnieje na liscie')
else:
    print('nie znajduje sie nia liscie')

# zliczanie 
litery = ['a','c','a','d','e']
print(litery.count('a')) # --> dwa wystapienia
print(litery.count('abc'))  # --> zero wystapien

owoce_dwa = ["JablKo", "bAnaN", "WisnIa"]

if 'BANAN' in owoce_dwa:
    print("Jest banan")
else:
    print("nie ma banana")

# Rozwiazanie problemu
if 'BANAN'.lower() in [x.lower() for x in owoce_dwa]:
    print('Banan znajduje sie na liscie')

# any()
print(any('jablko' in o.lower() for o in owoce_dwa))

if any('jablko' in o.lower() for o in owoce_dwa):
    pass

# ##############################################################################
# ###  ZADANIA 1.4                                                           ###
# ##############################################################################

# 1.4.1: Masz kolory = ["czerwony", "zielony", "niebieski"]. Jeśli na liście nie ma "żółty", wypisz Brak żółtego.

kolory = ["czerwony", "zielony", "niebieski"]
if "żółty" not in kolory:
    print("brak żółtego")
else:
    print("Jest żółty")

# 1.4.3: Masz imiona = ["Ala", "OLA", "ewa"]. Sprawdź, czy jest na niej "ola": bez względu na wielkość liter.

imiona = ["Ala", "OLA", "ewa"]
test = "OlA"
if test.lower() in [x.lower() for x in imiona]:
    print(f'Jest {test}')
else:
    print(f'Nie ma {test}')

# ------------------------------------------------------------------------------
# 1.5 Modyfikowanie zawartosci listy
# ------------------------------------------------------------------------------
# len() --> sa to funkcje
# obiekt.append() --> jest to metoda

liczby = [10, 20, 30]

liczby[1] = 99 #-> zamiana drugiego elementu (index 1) na 99
# liczby[10] = 99
liczby.append(40) #--> dodaje na koniec listy
# liczby.append(50,60) # TypeError: list.append() takes exactly one argument (2 given)
liczby.append([50,20]) #--> dodaje na koniec listy liste
# liczby.extend(50,20) TypeError: list.extend() takes exactly one argument (2 given)
liczby.extend([50,20]) #--> dodaje na koniec listy wiele elementow
liczby.insert(0,100)

print(liczby)

# Co sie dzieje jak inaczej dane podamy Pulapka
liczby_app = [10,20]
liczby_app.append([50,20])
# liczby_app.append(50,60)
# liczby_app.extend(50,20)
liczby_app.extend([50,20])

print(liczby_app)

# Modyfikowanie za pomoca slicingu
liczbyslice = [10, 20, 30]
print(liczbyslice)
liczbyslice[1:] = [50,60,70,90]
print(liczbyslice)

#Usuwanie elementow z listy 

liczbyu = [5, 10, 99, 30, 40, 99, 50, 60]

liczbyu.remove(99) # Usuwa pierwsze wystapienie elementu
# liczbyu.remove(1000)# ValueError: list.remove(x): x not in list
ostatni = liczbyu.pop() # zachowuje ostatni element w shcowku a zlisty usuwa
dzie = liczbyu.remove(99) # zwraca None usuwa pierwsze wystapienie elementu
pierwszy = liczbyu.pop(0) # zachowuje po indexie element z listy, usuwa go z listy
del liczbyu[3] # usuwa po indexie z listy

print(liczbyu)
print(ostatni)
print(dzie) # zwraca None --> to nie pop
print(pierwszy)

liczbyu.clear()
print(liczbyu)

# liczbyu.remove(100) #ValueError: list.remove(x): x not in list

if 100 in liczbyu:
    liczbyu.remove(100)

# ##############################################################################
# ###  ZADANIA 1.5                                                           ###
# ##############################################################################

# 1.5.1: Masz koszyk = ["chleb", "mleko"]. Zamień "mleko" na "kefir", dodaj "masło" na koniec i "jajka" na początek. Wypisz koszyk.

koszyk = ["chleb", "mleko"]
koszyk[1] = 'kefir'
koszyk.append('masło')
koszyk.insert(0,'jajka')
print(koszyk)

# 1.5.3: Masz kolejkę kolejka = ["Ala", "Ola", "Ewa"]. Obsłuż pierwszą osobę: usuń ją z listy i wypisz Obsługuję: Ala.

kolejka = ["Ala", "Ola", "Ewa"]
test = kolejka.pop(0)
print(f'Obsluguję {test}')
print(kolejka)

# 1.5.4: Masz zakupy = ["chleb", "masło", "cukier", "sól"]. Usuń z niej produkty "masło" i "mąka" tak, żeby program nie wywalił się błędem. 
# Dla brakującego produktu wypisz Nie ma na liście: ....

zakupy = ["chleb", "masło", "cukier", "sól"]
if 'masło' in zakupy:
    zakupy.remove('masło')
else:
    print('Nie ma na liscie: maslo')
if 'mąka' in zakupy:
    zakupy.remove('mąka')
else:
    print('Nie ma na liscie: maka')
print(zakupy)

# ------------------------------------------------------------------------------
# 1.6 Funkcje wbudowane w listy
# ------------------------------------------------------------------------------

liczbyf = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(liczbyf)) # --> dlugosc listy
print(sum(liczbyf)) # --> sumuje wszystkie elementy
print(min(liczbyf)) # --> daje minimalna wartosc
print(max(liczbyf)) # --> maxymalna wartosc 

zakupy = ["chleb", "masło", "cukier", "sól"]

print('*'*100)
print(len(zakupy)) # --> dlugosc listy
# print(sum(zakupy)) # --> TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(min(zakupy)) # --> daje minimalna  po znakach
print(max(zakupy)) # --> maxymalna wartosc po znakach

# any() all()
print(any(x > 8 for x in liczbyf)) #True
print(all(x > 3 for x in liczbyf)) #False
print(all(x > 0 for x in liczbyf)) #True

# sum z wyrazeniem
print(sum(x for x in liczbyf if x % 2 ==0))
print(sum(x > 3 for x in liczbyf))

# min / max --> key 
slowa = ['kot','hipopotam','pieso']
print(max(slowa,key=len)) # hipopotam -> najdluzsze
print(max(slowa))  # pies
print(min(slowa,key=len))

ludzie = [("Ala", 30), ("Ola", 25), ("Ela", 35)]
print(min(ludzie,key=lambda o: o[1]))
print(max(ludzie,key=lambda o: o[1]))

# Pulapka 

# Na pustych listach min() / max() zwraca bledy 
# print(max([])) ValueError: max() iterable argument is empty

pusta = []
# Rozwiazanie problemu max()
print(max(pusta,default=0))

# sum(pusta) / len(pusta) # ZeroDivision
srednia = sum(pusta) / len(pusta) if pusta else 0 
print(srednia)

# all() any()
print(any([])) # False 
print(all([])) # True

# ##############################################################################
# ###  ZADANIA 1.6                                                           ###
# ##############################################################################

# 1.6.1: Masz wyniki = [72, 95, 58, 88, 64]. Wypisz najwyższy wynik, najniższy i średnią: bez pętli.

wyniki = [72, 95, 58, 88, 64]
print(max(wyniki))
print(min(wyniki))
print(sum(wyniki)/len(wyniki))

# 1.6.3: Masz produkty = [("mleko", 3.49), ("ser", 12.99), ("chleb", 4.5)]. Znajdź najtańszy i najdroższy produkt za pomocą min / max z key=.

produkty = [("mleko", 3.49), ("ser", 12.99), ("chleb", 4.5)]
print(min(produkty,key=lambda o: o[1]))
print(max(produkty,key=lambda o: o[1]))

# 1.6.4: Napisz funkcję srednia(lista), która dla pustej listy zwraca 0 zamiast wywalać błąd. Dodatkowo wypisz największy element pustej 
# listy tak, żeby zamiast błędu pojawiło się brak.
""" 1 sposob
def srednia(x):
    print(x)
    if len(x) == 0:
        print("Lista jest pusta")
        return "Lista jest pusta"
    return sum(x)/len(x)

print(srednia([1,3,4,5,6]))
print(srednia([]))
"""

""" 2 sposob
def srednia_dwa(x):
    srednia = sum(x) / len(x) if x else 0 
    return srednia

print(srednia_dwa([1,3,4,5,6]))
print(max([],default='brak'))
"""

# ------------------------------------------------------------------------------
# 1.7 Sortowanie i odwracanie list sort(), sorted(), reversed()
# ------------------------------------------------------------------------------

liczby = [3, 1, 4, 1, 5]
print(liczby)
liczby.sort() #--> sortowanie od najm do naj
print(liczby)
liczby.sort(reverse=True) #--> od naj do najm
print(liczby)

liczby2 = [3, 1, 4, 1, 5]
print(sorted(liczby2)) 
print(sorted(liczby2, reverse=True)) 
print(liczby2)
print(reversed(liczby2)) # --> <list_reverseiterator object at 0x78498e1091e0>
print(list(reversed(liczby2)))

# key=len

slowa = ['banan','ala','anakonda']
slowa.sort(key=len)
print(slowa)

ludzie = [("Ala", 30), ("Ola", 25), ("Ela", 35)]
ludzie.sort(key=lambda osoba: osoba[1])
print(ludzie)

imiona = ["ola", "Ewa", "ala", "Bartek"]
print(sorted(imiona))
# print(sorted(imiona,key=str.lower())) # TypeError: unbound method str.lower() needs an argument
print(sorted(imiona,key=str.lower))

osoby = [("Ala", 30), ("Ola", 25), ("Ela", 35)]
print(sorted(osoby, key=lambda o: (-o[1],o[0])))

#Pulapka 

liczby = [3,1,4]
liczby = liczby.sort() # przypisanie metody zwraca None
print(liczby) # --> None 

liczby = [6,7,8]
liczby = sorted(liczby)
print(liczby)

# ##############################################################################
# ###  ZADANIA 1.7                                                           ###
# ##############################################################################

# 1.7.1: Masz oceny = [4, 2, 5, 3, 5]. Utwórz nową listę posortowaną rosnąco (oryginał ma zostać bez zmian), 
# a potem posortuj oryginał malejąco w miejscu.

oceny = [4, 2, 5, 3, 5]
oceny2 = sorted(oceny)
print(oceny2)
print(oceny)
oceny.sort(reverse=True)
print(oceny)

# 1.7.5: Masz produkty = [("ser", 12.99), ("mleko", 3.49), ("masło", 7.99), ("jogurt", 3.49)]. 
# Posortuj od najdroższego, a produkty w tej samej cenie: alfabetycznie.

produkty = [("ser", 12.99), ("mleko", 3.49), ("masło", 7.99), ("jogurt", 3.49)]
print(sorted(produkty, key=lambda o: (-o[1],o[0])))

# ------------------------------------------------------------------------------
# 1.8 Inne ciekawe funkcje i mozliwosci
# ------------------------------------------------------------------------------
kwadraty = [x**2 for x in range(10)]
parzyste = [x for x in range(10) if x % 2 ==0]
pary = [(x,y) for x in range(2) for y in range(2)] # zagniezdzone
print(pary)

# Kopiowanie list
oryginal = [1,2,3]
zla_kopia = oryginal # To nie jest kopia
zla_kopia.append(4)
print(oryginal)

dobra_kopia = oryginal.copy()
dobra_kopia.append(99)
print(oryginal)
print(dobra_kopia)

a = [1,2]
b = a
c = a.copy()

print(a == c,a is c)
print(a is b)

#Zagniezdzenia
import copy

oryg = [[1,2],[3,4]]
plytka = oryg.copy()
print(plytka[0])
plytka[0].append(99)
print(oryg)

gleboka = copy.deepcopy(oryg)
gleboka[0].append(6)
print(oryg)
print(gleboka)

# ==============================================================================
# 2. SLOWNIKI
# ==============================================================================

# ------------------------------------------------------------------------------
# 2.1 Tworzenie slownikow
# ------------------------------------------------------------------------------

pusty = {}
pusty2 = dict()

osoba = {'imie':'Damian','wiek':27,'miasto':'Krakow'} # json [{},{},{}]
osoba2 = dict(imie='Rafal',wiek=50)

# sparowane listy
klucze = ['a','b','c']
wartosci = [1,2,3]
slownik = zip(klucze,wartosci) # --> <zip object at 0x7b58d1dc1ec0>
slownik = dict(zip(klucze,wartosci))
print(slownik)

# dict comprehension
kwadraty = {x:x**2 for x in range(5)}
print(kwadraty)
# [0,1] jako klucz wywali blad Tylko niemutowalne na klucz

ceny = {"chleb": 4, "masło": 8, "ser": 12}
drogie = {k: v for k,v in ceny.items() if v > 5}
odwrocony = {v: k for k,v in ceny.items()}

print(ceny)
print(drogie)
print(odwrocony)

nowy_slownik = dict.fromkeys(['a','b','c'],0)
print(nowy_slownik)

# Laczenie dwoch slownikow w nowy
domyslne = {"kolor": "bialy", "rozmiar": 'M'}
wybrane = {"rozmiar":"L"}

print({**domyslne, **wybrane})
print(domyslne | wybrane)  

d = {'a':1,'b':2,'c':5,'a':99}
print(d)

# Pulapka 
pulapka_slownik = dict.fromkeys(['a','b','c'],[])
pulapka_slownik['a'].append(5)
print(pulapka_slownik)

# ##############################################################################
# ###  ZADANIA 2.1                                                           ###
# ##############################################################################

# 2.1.2: Masz imiona = ["Ala", "Ola", "Ela"] i wiek = [30, 25, 35]. Zrób z nich słownik imię --> wiek jedną linijką.

imiona = ["Ala", "Ola", "Ela"]
wiek = [30, 25, 35]
slownik = dict(zip(imiona,wiek))
print(slownik)

# 2.1.3: Z listy ["kot", "słoń", "hipopotam"] utwórz słownik słowo --> długość słowa.

lista = ["kot", "słoń", "hipopotam"]
slownik = {x:len(x) for x in lista}
print(slownik)

# 2.1.5: Masz kraje = {"pl": "Polska", "de": "Niemcy"}. Odwróć słownik tak, żeby po nazwie kraju dostać jego kod.

kraje = {"pl": "Polska", "de": "Niemcy"}
kody = {y:x for x,y in kraje.items()}
print(kody.get('Polska'))

# ------------------------------------------------------------------------------
# 2.2 Pobieranie wartosci ze slownikow
# ------------------------------------------------------------------------------

osoba = {"imie": "Ala", "wiek": 30}

print(osoba['imie'])
# print(osoba['banana']) # KeyError: 'banana'

# bezpieczne pobrac wartosc 

print(osoba.get("telefon")) # --> None
print(osoba.get("telefon",'brak')) 

# Sprawdzanie klucza
print('imie' in osoba)

#iterowanie
for klucz in osoba:
    print(klucz)

for klucz in osoba.keys():
    print(klucz)

for wartosc in osoba.values():
    print(wartosc)

for klucz,wartosc in osoba.items():
    print(klucz,wartosc)

# slowniki zagniezdzone
dane = {"imie": "Ala", "adres": {"miasto": "Kraków", "kod": "30-001"}}
print(dane['adres']['miasto'])

print(dane.get('praca', {}).get("firma"))

# Pulapki in
osoba = {"imie": "Ala", "wiek": 30}

print('Ala' in osoba) #--> przeszukuje po kluczach z defaulta
print('Ala' in osoba.values())

konto = {"saldo": 0}
"""
# Pulapka .get()
# 0, "", [] i None

if konto.get('saldo'):
    print('Jest saldo')
else:
    print('Brak salda')
"""

if "saldo" in konto:
    print('JEst taki klucz')

# ##############################################################################
# ###  ZADANIA 2.2                                                           ###
# ##############################################################################

# 2.2.2: Masz firma = {"nazwa": "ABC", "szef": {"imie": "Jan", "kontakt": {"email": "jan@abc.pl"}}}. Wypisz e-mail szefa. 
# Potem bezpiecznie pobierz imię księgowej (klucza "ksiegowa" nie ma): ma się wypisać brak.

firma = {"nazwa": "ABC", "szef": {"imie": "Jan", "kontakt": {"email": "jan@abc.pl"}}}
print(firma.get('szef').get('kontakt').get('email'))

if firma.get('ksiegowa') != None:
    print(firma.get('ksiegowa'))
else:
    print('Brak')

print(firma.get('ksiegowa', {}).get("imie",'brak'))

# 2.2.3: Masz magazyn {"jabłka": 12, "gruszki": 0, "śliwki": 5}. Dla produktów ["jabłka", "gruszki", "banany"] 
# wypisz stan (jabłka: 12 szt.), a dla produktu spoza oferty, np. banany: nie ma w ofercie. Uwaga: gruszki mają stan 0, ale są w ofercie.

# stany = {"jabłka": 12, "gruszki": 0, "śliwki": 5}
# produkty = ["jabłka", "gruszki", "banany"]
# for produkt in produkty:
#     ....

# del stany[produkt]

"""
stany = {"jabłka": 12, "gruszki": 0, "śliwki": 5, "banany": 0}
for produkt in list(stany):      # bez list() --> RuntimeError
    if stany[produkt] == 0:
        del stany[produkt]
print(stany)
"""

magazyn = {"jabłka": 12, "gruszki": 0, "śliwki": 5}
lista_do_sprawdzenia = ["jabłka", "gruszki", "banany"]
print('Stan:')
for i in lista_do_sprawdzenia:
    if i in magazyn.keys():
        print(f'{i}: {magazyn.get(i)} szt.')
    else:
        print(f'{i}: nie ma w ofercie')

# ------------------------------------------------------------------------------
# 2.3 Modyfikacja zawartosci slownikow
# ------------------------------------------------------------------------------

osoba = {"imie": "Ala", "wiek": 30}

osoba['wiek'] = 31
osoba['miasto'] = 'Krakow'

osoba.update({"wiek":32,"telefon":'998997995'})
osoba.update(email='ala@x.pl')

osoba['miejscowosc'] = osoba.pop('miasto')

print(osoba)

# setdefault
osoba.setdefault('waga',80)

osoba.setdefault('waga',100)
osoba.setdefault('waga',90)
osoba.setdefault('waga',10)

print(osoba)

# Usuwanie 

osoba = {"imie": "Ala", "wiek": 32, "telefon": "123", "email": "ala@x.pl"}

# wiek = osoba.pop() #TypeError: pop expected at least 1 argument, got 0
wiek = osoba.pop('wiek')
# miejscowosc = osoba.pop('miejscowosc') # KeyError: 'miejscowosc'
miejscowosc = osoba.pop('miejscowosc',None) 
del osoba['telefon']
ostatni = osoba.popitem()

print(osoba)

osoba.clear()

print(osoba)

if 'imie' in osoba:
    pass

# grupowanie elementow z listy
uczniowie = [("1A", "Ala"), ("1B", "Ola"), ("1A", "Ela")]
klasy = {}
for klasa, imie in uczniowie:
    klasy.setdefault(klasa, []).append(imie)
print(klasy)   # {'1A': ['Ala', 'Ela'], '1B': ['Ola']}

# to samo przez defaultdict --> brakujacy klucz sam dostaje pusta liste
from collections import defaultdict
klasy = defaultdict(list)
for klasa, imie in uczniowie:
    klasy[klasa].append(imie)
print(dict(klasy))   # {'1A': ['Ala', 'Ela'], '1B': ['Ola']}

# Counter z collections --> nie grupuje, tylko zlicza ile razy cos wystapilo
from collections import Counter
print(Counter("abracadabra"))  
print(Counter("abracadabra").most_common(2)) 

# ##############################################################################
# ###  ZADANIA 2.3                                                           ###
# ##############################################################################

# 2.3.1: Masz profil = {"login": "ala", "haslo": "1234"}. Zmień hasło na "qwerty", jednym update() 
# dodaj e-mail i miasto, a na koniec zmień nazwę klucza "login" na "uzytkownik".

profil = {"login": "ala", "haslo": "1234"}
profil.update({'haslo':'qwerty', 'email':'abc@efg.pl', 'miasto':'Rakow',})
profil['uzytkownik'] = profil.pop('login')
print(profil)

# 2.3.2: Masz koszyk = {"chleb": 4, "mleko": 3, "masło": 8}. Usuń mleko i wypisz jego cenę. Potem spróbuj usunąć 
# "ser" tak, żeby program nie wywalił się błędem. Na koniec wypisz sumę koszyka.

koszyk = {"chleb": 4, "mleko": 3, "masło": 8}
cena_mleka = koszyk.pop('mleko')
if koszyk.get('ser') != None:
    del(koszyk['ser'])
else:
    print('Nie mozna usunac sera')
print(f'Cena mleka wynosi {cena_mleka}')
print(f'Suma koszyka wynosi {sum(koszyk.values())}')

# ==============================================================================
# 3. POWROT DO FUNKCJI
# ==============================================================================

# funkcja() --> Blad nie ma takiej funkcji 

# Deklaraowanie funkcji
def funkcja():
    # print('Zwrot')
    return 'Zwrot'
#Wywolanie takiej funkcji 
funkcja()
zmienna = funkcja()
print(zmienna)

def mnozenie(a,b):
    return a * b

# print(mnozenie(4)) # TypeError: mnozenie() missing 1 required positional argument: 'b'
print(mnozenie(4,6))
# print(mnozenie(6,7,4,3)) # TypeError: mnozenie() takes 2 positional arguments but 4 were given

# ------------------------------------------------------------------------------
# 3.1 *args
# ------------------------------------------------------------------------------

def suma_fun(*args):
    return f'Suma wynosi {sum(args)}'

print(suma_fun())
print(suma_fun(5))
print(suma_fun(7,4))
print(suma_fun(5,7,4))
print(suma_fun(5,7,4,6,3,5,6,3,4,6,2))

print('*'* 40)

def suma_fun(*args): # z gory zalozone nazewnictwo, czyli nic sie nie stanie jak nazweimy inaczej wazna jest ta *
    print(args)
    print(*args)
    pierwszy, *reszta = args
    print(pierwszy)
    return f'Suma wynosi {sum(args)}'

print(suma_fun(5,7,4,6,3,5,6,3,4,6,2))

def maksimum(pierwszy,*reszta):
    wynik = pierwszy
    for x in reszta:
        if x > wynik:
            wynik = x
    return wynik

# print(maksimum()) # TypeError: maksimum() missing 1 required positional argument: 'pierwszy'
print(maksimum(9,3,5,10))

def zakupy(*produkty,sep=', '):
    return sep.join(produkty) # --> ''.join(lista)

print(zakupy('chleb','jajka','mleko'))
print(zakupy('chleb','jajka','mleko',sep='-'))

print('*'*20)
""" ypeError: zakupy() got multiple values for argument 'sep'
def zakupy(sep=', ',*produkty):
    return sep.join(produkty) # --> ''.join(lista)

print(zakupy('chleb','jajka','mleko')) # nie ma bledu, sep='chleb' --> jajkachlebmleko
print(zakupy('chleb','jajka','mleko',sep='-')) # tu dopiero TypeError
"""

# ##############################################################################
# ###  ZADANIA 3.1                                                           ###
# ##############################################################################

# 3.1.1: Napisz funkcję iloczyn(*liczby), która mnoży wszystkie przekazane liczby. Dla wywołania bez argumentów ma zwrócić 1.

def iloczyn(*args):
    wynik = 1
    for x in args:
        wynik = x * wynik
    return wynik

print(iloczyn(5,4,2,4))

# 3.1.3: Napisz funkcję srednia(pierwsza, *reszta), która liczy średnią z podanych liczb. Wywołanie bez żadnej liczby ma kończyć s
# ię błędem już przy wywołaniu, a nie dzieleniem przez zero.

def srednia(pierwsza, *reszta):
    return round((pierwsza + sum(reszta)/len(reszta)+1),2)

print(srednia(6,88,34,5,2,3,5))

"""
def srednia(pierwsza, *reszta):
    suma = pierwsza + sum(reszta)
    ilosc_rek = len(reszta)+1
    return suma/ilosc_rek
"""

# ------------------------------------------------------------------------------
# 3.2 **kwargs
# ------------------------------------------------------------------------------

def opisz(**kwargs):
    print(kwargs) #--> slownik
    # print(**kwargs)   # --> TypeError: print() got an unexpected keyword argument 'imie'

    if 'imie' in kwargs:
        print(kwargs['imie'])

    for klucz,wartosc in kwargs.items():
        print(f'{klucz}: {wartosc}')

opisz(imie='Pawel',wiek=80,miasto='Warszawa')

def funkcja(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)

funkcja(2,7,7,5,43,63,3,4,imie='Adam',wiek=28)

def pelna(a, *args, sep=' ', **kwargs):
    print(a,args,sep,kwargs)

pelna(1,5,3,sep='--',x=9)

def polacz_z_baza(**opcje):
    host = opcje.get("host",'localhost')
    port = opcje.get("port", 5432)
    print(f"{host}:{port}")
    return f"{host}:{port}"

polacz_z_baza()
polacz_z_baza(host='245.23.4.2.5',port=82)

def powitaj(imie,wiek):
    return f"Czesc {imie} masz {wiek} lat"

dane = {"imie":'Ala',"wiek":28}

print(powitaj(**dane))

# ##############################################################################
# ###  ZADANIA 3.2                                                           ###
# ##############################################################################

# 3.2.1: Napisz funkcję profil(**dane), która wypisuje wszystkie przekazane dane w formacie klucz -> wartość. 
# Wywołaj ją z login="ala" i miasto="Gdańsk".

def profil(**dane):
    for klucz,wartosc in dane.items():
        print(f'{klucz}: {wartosc}')
profil(login='ala', miasto='Gdańsk')

# 3.2.2: Napisz funkcję zamowienie(produkt, **opcje), która zwraca napis kawa x2, rabat 10%. 
# Jeśli nie podano ilosc, przyjmij 1, a jeśli nie podano rabat: 0.

def zamowienie(produkt, **opcje):
    ilosc = opcje.get('ilosc',1)
    rabat = opcje.get('rabat',0)
    return f'{produkt} x{ilosc}, rabat {rabat}%'

print(zamowienie('kawa', ilosc=2, rabat=10))
print(zamowienie('herbata'))