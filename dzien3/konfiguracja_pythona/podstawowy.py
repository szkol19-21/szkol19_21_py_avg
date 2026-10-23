# Parametry wiersza poleceń - moduł 
import click 

# instalowac biblioteke click


@click.command()
@click.option("--imie",default='swiecie',help='Kogo przywitac')
def przywitaj(imie):
    click.echo(f'Czesc, {imie}')

if __name__ == "__main__":
    przywitaj()

from click.testing import CliRunner

wynik = CliRunner().invoke(przywitaj, ["--imie", "Ala"])
print(wynik.output)    