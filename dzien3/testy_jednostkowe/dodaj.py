# Testy jednostkowe

def dodawanie(a,b):
    return a + b

def podziel(a, b):
    if b == 0:
        raise ValueError("Nie dzielimy przez zero!")
    return a / b 

class Konto:
    def __init__(self,saldo):
        self.saldo = saldo
        
    def wplac(self, kwota):
        self.saldo += kwota


def odejmowanie(a,b):
    return a -b 



