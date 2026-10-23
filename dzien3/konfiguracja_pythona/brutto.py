# 10.1.1: Napisz program brutto.py, który przyjmuje cenę netto jako argument 
# (click.argument, liczba zmiennoprzecinkowa) oraz opcję --vat (liczba całkowita, domyślnie 23) 
# i wypisuje cenę brutto. python brutto.py 100 → Brutto: 123.0 zł, 
# python brutto.py 100 --vat 8 → Brutto: 108.0 zł.

import click
# instalowac biblioteke click

@click.command()
@click.option('--vat', type=int,default=23,help='stawka vat')
@click.argument("kwota", type=float, help='kwota do obliczenia')
def oblicz_kwote(vat,kwota):
    click.echo(f'{kwota + kwota*vat/100} zł')

if __name__=="__main__":
    oblicz_kwote()