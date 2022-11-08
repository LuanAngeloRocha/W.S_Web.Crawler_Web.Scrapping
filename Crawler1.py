import Scraping_ge
import Scrapping2



import csv
import pandas as pd

with open('Noticias.csv', 'w', newline='') as arquivo:
    final = csv.writer(arquivo, delimiter=';')
    final.writerow(['Titulo', 'Link'])

    for x in Scraping_ge.lista:

        final.writerow(x)
    
    for x in Scrapping2.lista_noticias:
        final.writerow(x)

print('=========================================================================')
print('Sites utiliados : Ge.globo e G1.globo')
print('Essas são as Vagas de Programação Disponives em São Paulo:')
print('=========================================================================')
ler = pd.read_csv("Noticias.csv", sep=';')
print(ler)


