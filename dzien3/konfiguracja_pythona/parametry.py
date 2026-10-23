# Parametry wiersza poleceń - moduł 
import click 

# instalowac biblioteke click


@click.command()

@click.option("--liczba", type=int, default = 1,help="ile razy powtorzyc")
@click.argument("tekst")
def powtorz(liczba, tekst):
    for _ in range(liczba):
        click.echo(tekst)

if __name__ == "__main__":
    powtorz()