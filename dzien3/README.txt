Dzien 3 - rozdzialy 7-11

7. Dekoratory
   decorators.py - zasada dzialania, dekorator z argumentem, kilka dekoratorow naraz,
   dekorator jako wzorzec projektowy, @staticmethod i @classmethod

8. Pakiety
   pakiety/aplikacja/main.py - wszystkie przyklady importow po kolei
   pakiety/aplikacja/modul1.py, modul2.py - wlasne moduly i cykliczny import
   pakiety/aplikacja/pakiet/ - pakiet, __init__.py i __all__
   pakiety/aplikacja/pakiet/pakiet_zagnie/ - pakiet zagniezdzony
   pakiety/modu_zew.py - modul spoza folderu aplikacji (sys.path)
   Uruchamianie: python pakiety/aplikacja/main.py

9. Wprowadzenie do asynchronicznosci
   py_threading.py - threading, start i join, Lock, ThreadPoolExecutor,
   zatrzymywanie watku przez Event, watki jako demony

10. Konfiguracja Pythona
   konfiguracja_pythona/podstawowy.py - pierwsza komenda click
   konfiguracja_pythona/parametry.py - opcja i argument
   konfiguracja_pythona/wybory.py - click.Choice
   konfiguracja_pythona/wiele_parametrow.py - prompt i flaga
   konfiguracja_pythona/bonus.py - parametry podane jako lista
   konfiguracja_pythona/brutto.py - zadanie 10.1.1 (wymaga click 8.5 lub nowszego)
   konfiguracja_pythona/pizzeria.py - zadanie 10.3.1
   srodowisko_wirt.py - reczne tworzenie venv i requirements.txt
   Pomoc do kazdego programu: python plik.py --help

11. Testy jednostkowe
   testy_jednostkowe/dodaj.py, test_dodaj.py - pytest, fixture, approx, parametryzacja, pokrycie
   testy_jednostkowe/pogoda.py, test_pogoda.py - makiety (unittest.mock)
   testy_jednostkowe/parzystosc.py, test_parzystosc.py - zadanie 11.1.1
   testy_jednostkowe/rabat.py, test_rabat.py - zadanie 11.1.2
   Uruchamianie: w folderze testy_jednostkowe wpisac pytest -v
   Dwa testy w test_dodaj.py (test_zly, test_float) padaja celowo.

Biblioteki: pip install click pytest pytest-cov requests
