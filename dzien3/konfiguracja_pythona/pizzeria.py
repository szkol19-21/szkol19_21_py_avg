# 10.3.1: Napisz program pizza.py z opcją 
# --rozmiar (tylko big, bigXL lub Small, wymagana) i flagą 
# --na-wynos. Ma wypisać np. 
# Pizza L, na wynos albo Pizza M, na miejscu.

import click
# instalowac biblioteke click

@click.command()
@click.option('--rozmiar',required=True, type=click.Choice(['big','bigXL', 'small']), help='Wypisz rozmiar')
@click.option('--na_wynos',is_flag=True)
def zam(rozmiar,na_wynos):
    if na_wynos:
        wiadomosc = f'Pizza {rozmiar}, na wynos'
    else:
        wiadomosc = f'Pizza {rozmiar}, na miejscu'
    click.echo(wiadomosc)



if __name__=="__main__":
    zam()