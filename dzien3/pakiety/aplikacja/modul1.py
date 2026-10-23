print("Laduje modul1")
from modul2 import funkcja_modulu2

def funkcja_modulu1():
    print("[modul1] funkcja_modulu1 dziala")
    funkcja_modulu2()


if __name__ == "__main__":
    print('Test')
    funkcja_modulu1()