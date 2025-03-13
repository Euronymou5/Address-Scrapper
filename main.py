# Simple random address scrapper.
# By: Euronymou5

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
from io import StringIO
import random
from rich import print as print_rich
from colorama import Fore
import time
import argparse
import json
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.highlighter import Highlighter
import os

parser = argparse.ArgumentParser()
parser.add_argument("-code", "-c", type=str, help="Añadir codigo ISO personalizado.")
parser.add_argument("-quantity", "-q", type=int, default=1, help="Añadir cantidad de resultados.")
parser.add_argument("-save", type=str, help="Guardar datos en un archivo json.")
args = parser.parse_args()

class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({random.randint(16, 255)})", index, index + 1)

rainbow = RainbowHighlighter()

logo = f"""
     _       _     _                                                              
    / \   __| | __| |_ __ ___  ___ ___   ___  ___ _ __ __ _ _ __  _ __   ___ _ __ 
   / _ \ / _` |/ _` | '__/ _ \/ __/ __| / __|/ __| '__/ _` | '_ \| '_ \ / _ \ '__|
  / ___ \ (_| | (_| | | |  __/\__ \__ \ \__ \ (__| | | (_| | |_) | |_) |  __/ |   
 /_/   \_\__,_|\__,_|_|  \___||___/___/ |___/\___|_|  \__,_| .__/| .__/ \___|_|   
                                                           |_|   |_|          
                                | By: Euronymou5 |    
"""

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# En caso de utilizar codigo aleatorio.
def search_principal(bestrandom_url, headers, random_entry):
    try:
        web = requests.get(bestrandom_url, headers=headers)
        soup = BeautifulSoup(web.content, 'html.parser')

        campos = ['Street', 'City', 'State/province/area', 'Phone number', 'Country calling code']
        li = soup.find('li', class_='col-sm-6')

        if li:
            p_tags = li.find_all('p')
            textos = [p.get_text(strip=True) for p in p_tags]
    
            if textos:
                datos = {}
                for i, texto in enumerate(textos):
                    try:
                        clave, valor = texto.split(':', 1)
                        datos[clave.strip()] = valor.strip()
                    except ValueError:
                        datos[campos[i]] = texto.strip()

        print_rich(f'\n[bold] {datos}')
        if args.save == 'json':
            numeros_aleatorios = [random.randint(1, 9000) for _ in range(1)]
            with open(f'output/datos_{numeros_aleatorios}.json', 'w') as archivo:
                json.dump(datos, archivo, indent=4)

        if args.save == 'txt':
            numeros_aleatorios = [random.randint(1, 9000) for _ in range(1)]
            with open(f'output/datos_{numeros_aleatorios}.txt', 'w') as archivo:
                for clave, valor in datos.items():
                    archivo.write(f'{clave}: {valor}\n')
    except:
        print(f'\n{Fore.RED}[ERROR]: No se han podido obtener resultados con el país: {Fore.BLUE}{random_entry[1]} - {random_entry[0]}')
        time.sleep(2)
        exit()

# En caso de utilizar un codigo iso personalizado.
def search_alternativo(bestrandom_url, headers, codigo):
    try:
        web = requests.get(bestrandom_url, headers=headers)
        soup = BeautifulSoup(web.content, 'html.parser')

        campos = ['Street', 'City', 'State/province/area', 'Phone number', 'Country calling code']
        li = soup.find('li', class_='col-sm-6')

        if li:
            p_tags = li.find_all('p')
            textos = [p.get_text(strip=True) for p in p_tags]
    
            if textos:
                datos = {}
                for i, texto in enumerate(textos):
                    try:
                        clave, valor = texto.split(':', 1)
                        datos[clave.strip()] = valor.strip()
                    except ValueError:
                        datos[campos[i]] = texto.strip()
                        
        print_rich(f'\n[bold] {datos}')
        if args.save == 'json':
            numeros_aleatorios = [random.randint(1, 9000) for _ in range(1)]
            with open(f'output/datos_{numeros_aleatorios}.json', 'w') as archivo:
                json.dump(datos, archivo, indent=4)

        if args.save == 'txt':
            numeros_aleatorios = [random.randint(1, 9000) for _ in range(1)]
            with open(f'output/datos_{numeros_aleatorios}.txt', 'w') as archivo:
                for clave, valor in datos.items():
                    archivo.write(f'{clave}: {valor}\n')
    except:
        print(f'\n{Fore.RED}[ERROR]: No se han podido obtener resultados con el codigo: {Fore.BLUE}{codigo}')
        time.sleep(2)
        exit()

def main():
    clear()
    print_rich(rainbow(logo))

    if args.code != 'random':
        codigo = args.code
        bestrandom_url = f'https://www.bestrandoms.com/random-address-in-{codigo}?quantity=1'

        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        with Progress(
            SpinnerColumn(spinner_name="line"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task(f"[bold yellow] Buscando informacion... Codigo: {codigo}, Cantidad: {args.quantity}.", total=100)

            while not progress.finished:
                time.sleep(0.02)
                progress.update(task, advance=1)

        for _ in range(args.quantity):
            search_alternativo(bestrandom_url, headers, codigo)

    if args.code == 'random':
        csv_url = "https://gist.githubusercontent.com/tadast/8827699/raw/61b2107766d6fd51e2bd02d9f78f6be081340efc/countries_codes_and_coordinates.csv"

        resp = requests.get(csv_url)
        csv_data = StringIO(resp.text)
        df = pd.read_csv(csv_data)

        simple = []
        for _, row in df.iterrows():
            code = row['Alpha-2 code'].replace('"', '').strip().lower()
            country = row['Country'].replace('"', '').strip()
            simple.append((code, country))

        random_entry = random.choice(simple)
        bestrandom_url = f'https://www.bestrandoms.com/random-address-in-{random_entry[0]}?quantity=1'

        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        with Progress(
            SpinnerColumn(spinner_name="line"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task(f"[bold yellow] Buscando informacion... Pais: {random_entry[1]}, Codigo: {random_entry[0]}, Cantidad: {args.quantity}.", total=100)

            while not progress.finished:
                time.sleep(0.02)
                progress.update(task, advance=1)
        
        for _ in range(args.quantity):
            search_principal(bestrandom_url, headers, random_entry)

if not args.code:
    print(f'''{Fore.RED}[!] ERROR: Debes agregar algun argumento: 
      -code, -c          Añadir codigo ISO personalizado.
      -quantity, -q         Añadir cantidad de resultados.
      -save            Guardar datos en un archivo json.
    ''')
else:
    main()
