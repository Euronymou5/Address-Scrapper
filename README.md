# Address-Scrapper
Un simple script que recaba falsas direcciones utilizando web scrapping de la web [Bestrandoms](https://www.bestrandoms.com/random-address-in-0). 

El script recaba códigos de pais ISO, para facilitar el uso mediante web scrapping. Decidí utilizar un [archivo de datos csv,](https://gist.github.com/tadast/8827699) para obtener diferentes códigos iso e implementarlos como un uso aleatorio del script, aunque el usuario puede agregar uno personalizado.

````python
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
````

## Instalacion

Clonar repositorio.
```
git clone https://github.com/Euronymou5/Address-Scrapper
```

Instalar dependencias.
```
pip install -r requirements.txt
```

Iniciar script.
```
python main.py
````

## Imagenes
