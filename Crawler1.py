import Scrapping_ge
import Scrapping_g1



import csv
import pandas as pd

with open('Noticias.csv', 'w', newline='') as arquivo:
    final = csv.writer(arquivo, delimiter=';')
    final.writerow(['Titulo', 'Link'])

    for x1 in Scrapping_ge.lista_noticias:

        final.writerow(x1)
    
    for x2 in Scrapping_g1.lista_noticias:
        final.writerow(x2)

print('=========================================================================')
print('Sites utiliados : Ge.globo e G1.globo')
print('Essas são as Vagas de Programação Disponives em São Paulo:')
print('=========================================================================')
ler = pd.read_csv("Noticias.csv", sep=';')



