# Address-Scrapper
Un simple script que recaba falsas direcciones utilizando web scrapping de la web [Bestrandoms](https://www.bestrandoms.com/random-address-in-0). 

El script recaba códigos de pais ISO, para facilitar el uso mediante web scrapping. Decidí utilizar un [archivo de datos csv,](https://gist.github.com/tadast/8827699) para obtener diferentes códigos iso e implementarlos como un uso aleatorio del script, aunque se pueden agregar de manera personalizada.

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

### Ejemplos de uso

> Mostrar ayuda.

```
python3 main.py -h
```
```
usage: main.py [-h] [-code CODE] [-quantity QUANTITY] [-save SAVE]

options:
  -h, --help            show this help message and exit
  -code CODE, -c CODE   Añadir codigo ISO personalizado.
  -quantity QUANTITY, -q QUANTITY,  Añadir cantidad de resultados.
  -save SAVE            Guardar datos en un archivo json.
```

Ejemplo de uso basico.
```
python3 main.py -c mx
```

Guardar datos en un archivo json.
```
python3 main.py -c br -save json
```

Eleccion random del codigo iso.
```
python3 main.py -c random
```

Modificar cantidad de resultados.
```
python3 main.py -q 3 -c cl
```

## Imagenes

![scrapper-gif](https://github.com/user-attachments/assets/309037af-c60b-4a12-bd4c-841874d87162)


## 🌐 Contacto 🌐
[![discord](https://img.shields.io/badge/Discord-euronymou5-a?style=plastic&logo=discord&logoColor=white&labelColor=black&color=7289DA)](https://discord.com/users/452720652500205579)

![email](https://img.shields.io/badge/ProtonMail-mr.euron%40proton.me-a?style=plastic&logo=protonmail&logoColor=white&labelColor=black&color=8B89CC)

[![X](https://img.shields.io/twitter/follow/Euronymou51?style=plastic&logo=X&label=%40Euronymou51&labelColor=%23000000&color=%23000000)](https://x.com/Euronymou51)
