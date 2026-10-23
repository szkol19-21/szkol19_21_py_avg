# aplikacja/
# └── main.py

# Importowanie bibliotek
# Biblioteki wbudowane w pythona(nie trzeba ich pobierac), oraz takie zewnetrzne( trzeba pobrac)

# Import calej biblioteki
import math 
print(math.pi)

# Import z aliasem
import math as m
print(m.pi)

# Import tylko niektorych nazw z biblioteki
from math import pi, sqrt
print(sqrt(20),pi)

# Import niektorych z aliasem 
from math import pi as liczba_pi, sqrt as pierwiastek
print(liczba_pi,pierwiastek(20))

from math import *

# Wlasne moduly

# aplikacja/
# ├── main.py
# ├── modul1.py
# └── modul2.py

# Import calej z modulu wlasnego
import modul1
modul1.funkcja_modulu1()

# Import z modulu wlasnego z aliasem
import modul2 as m2
m2.funkcja_modulu2()

# Import konkretnej funkcji z modulu wlasnego
from modul1 import funkcja_modulu1
funkcja_modulu1()


# Aby nie importowac wszystkich wywolan z modulu wlasnego, gdzie moga byc testy dobrze sobie opakowac to
""" aplikacja/modul1.py
if __name__ == "__main__":
    print('Test')
    funkcja_modulu1()
"""
# Pakietem jest folder w tej samej lokalizacji zawierajacy inne moduly do zaimportowania

# aplikacja/
# ├── main.py
# ├── modul1.py
# ├── modul2.py
# └── pakiet/
#     ├── __init__.py                ← na razie pusty
#     ├── modul_pakietu1.py
#     └── modul_pakietu2.py


# aplikacja/pakiet/modul_pakietu1.py
"""
def funkcja_pakietu1():
    print("[pakiet/modul_pakietu1] funkcja_pakietu1 dziala")
"""

# aplikacja/pakiet/modul_pakietu2.py
"""
def funkcja_pakietu2():
    print("[pakiet/modul_pakietu2] funkcja_pakietu2 dziala")
"""

# import modulu z pakietu
import pakiet.modul_pakietu1
pakiet.modul_pakietu1.funkcja_pakietu1() # dlugie wywolanie 

# Import z aliasem
import pakiet.modul_pakietu1 as pmp
pmp.funkcja_pakietu1()

# Import jednej funkcji z pakietu
from pakiet.modul_pakietu2 import funkcja_pakietu2
funkcja_pakietu2()

# Nowa mozliwosc dzieki importom w __init__
# from pakiet import funkcja dziala dzieki liniom from .modul import ..., a nie dzieki __all__
# __all__ decyduje tylko o tym, co wejdzie przy from pakiet import *
# aplikacja/pakiet/__init__.py
"""
from .modul_pakietu1 import funkcja_pakietu1
from .modul_pakietu2 import funkcja_pakietu2

__all__ = ['funkcja_pakietu1',"funkcja_pakietu2"]
"""
print('*'*20)
from pakiet import funkcja_pakietu1, funkcja_pakietu2

funkcja_pakietu1()
funkcja_pakietu2()

# import * bierze tylko nazwy z __all__
from pakiet import *

funkcja_pakietu1()
funkcja_pakietu2()

# Pakiet zagniezdzony 
# aplikacja/
# ├── main.py
# ├── modul1.py
# ├── modul2.py
# └── pakiet/
#     ├── __init__.py
#     ├── modul_pakietu1.py
#     ├── modul_pakietu2.py
#     └── pakiet_zagnie/     ← pakiet w pakiecie
#         ├── __init__.py            ← na razie pusty
#         └── modul_pakietu_zagn.py

# Import zagn pakietu

# aplikacja/pakiet/pakiet_zagnie/modul_pakietu_zagn.py
"""
def funkcja_pakietu_zagn():
    print("[pakiet/pakiet_zagnie/modul_pakietu_zagn] funkcja_pakietu_zagn dziala")
"""

from pakiet.pakiet_zagnie.modul_pakietu_zagn import funkcja_pakietu_zagn
funkcja_pakietu_zagn()

# Skracanie przez dwa __init__.py i __all__
# Najpierw pakiet zagniezdzony wystawia swoja funkcje 
# pakiet/pakiet_zagnie/__init__.py
"""
from .modul_pakietu_zagn import funkcja_pakietu_zagn

__all__ = ['funkcja_pakietu_zagn']
"""


# jak mamy juz wystawiony pakiet zagnie na swiat to przekazujemy go dalej kolejnym __init__.py
# pakiet/__init__.py
"""
from .pakiet_zagnie import funkcja_pakietu_zagn

__all__ = [.....,'funkcja_pakietu_zagn']
"""
print('*'*10)
from pakiet import funkcja_pakietu_zagn as fpz
fpz()


# Modul poza aplikacja
# pakiety/
# ├── modu_zew.py                    ← POZA folderem aplikacji
# └── aplikacja/
#     ├── main.py
#     ├── modul1.py
#     ├── modul2.py
#     └── pakiet/ ...

# pakiety/modu_zew.py
"""
def funkcja_zew():
    print("[modu_zew] funkcja_zew dziala")
"""

# import ..modu_zew  SyntaxError: invalid syntax

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent)) # // doda folder pakiety


import modu_zew
modu_zew.funkcja_zew()

# Pulapka
# Cykliczne importy: modul A importuje modul B, modul B importuje modul A --> w tym samym momencie
# Nadpisywanie importem * wszystkich funkcji (takze tych ktore mogles napisac wczesniej)
# Import wzgledny (from . import ...) w pliku uruchamianym bezposrednio, a nie jako czesc pakietu
# --> ImportError: attempted relative import with no known parent package

# -->  modul1.py importuje modul2.py i odwrotnie wywala blad 
# ImportError: cannot import name 'funkcja_modulu1' from 'modul1' (consider renaming 


from modul2 import wywolaj_pakiet1

wywolaj_pakiet1()