# Utvikling med Python/Flask

## Lag en form med et input-felt, og send dataene til serveren
Denne HTML-koden lager et enkelt skjema med et input-felt og en send-knapp. Når brukeren trykker på knappen, sendes dataene til serveren via en POST-request.
```html
<form action="/submit" method="post">
    <input type="text" name="data" required>
    <button type="submit">Send</button>
</form>
```

## Lagre informasjonen fra form-en i en database
Vi bruker Flask og PyMySQL til å lagre data i en MySQL-database. Når brukeren sender inn skjemaet, lagres innholdet i databasen.
```python
from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Koble til MySQL-databasen
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='passord',
    database='min_database',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    with connection.cursor() as cursor:
        sql = "INSERT INTO data (content) VALUES (%s)"
        cursor.execute(sql, (data,))
        connection.commit()
    return "Data lagret!"

if __name__ == '__main__':
    app.run(debug=True)
```

## Utfør en spørring mot databasen og skriv ut resultatet i en tabell
Denne Flask-ruten henter alle dataene fra databasen og sender dem til en HTML-side der de vises i en tabell.
```python
@app.route('/data')
def show_data():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM data"
        cursor.execute(sql)
        all_data = cursor.fetchall()
    return render_template('data.html', data=all_data)
```

```html
<table>
    <tr>
        <th>ID</th>
        <th>Content</th>
    </tr>
    {% for entry in data %}
    <tr>
        <td>{{ entry.id }}</td>
        <td>{{ entry.content }}</td>
    </tr>
    {% endfor %}
</table>
```

# DOM-manipulering med JavaScript

## Lag en knapp i HTML og referer til den i en variabel med `getElementById`
Denne koden lager en knapp i HTML og henter den ved hjelp av `getElementById` i JavaScript.
```html
<button id="myButton">Klikk meg</button>
<script>
    let button = document.getElementById("myButton");
</script>
```

## Lag en funksjon som skriver «Hei verden» i konsollet
Denne funksjonen skriver "Hei verden" i nettleserkonsollen når den kalles.
```javascript
function sayHello() {
    console.log("Hei verden");
}
```

## Koble funksjonen til knappen med `addEventListener`
Her kobler vi `sayHello`-funksjonen til knappen, slik at den kjører når knappen klikkes.
```javascript
button.addEventListener("click", sayHello);
```

# Utvikling/Generelt

## Funksjoner

### Lag en funksjon som skriver ut teksten «hei»
```python
def print_hei():
    print("hei")
```

### Lag en funksjon som tar imot et navn som parameter, og skriver ut dette
```python
def print_navn(navn):
    print(navn)
```

### Lag en funksjon som returnerer en tekst
```python
def return_text():
    return "Dette er en tekst"
```

### Lag en funksjon som tar imot et navn som parameter, og returnerer «hei [navn]»
```python
def hei_navn(navn):
    return f"hei {navn}"
```

## Løkker

### Skriv ut alle tallene fra 0 til 10 med en løkke
```python
for i in range(11):
    print(i)
```

### Skriv ut alle tallene fra 30 til 15 med en løkke
```python
for i in range(30, 14, -1):
    print(i)
```

### Skriv ut annethvert tall fra 1 til 45 med en løkke
```python
for i in range(1, 46, 2):
    print(i)
```

## If-statements

```python
def sesong(tall):
    if tall < 0:
        print("Vinter")
    elif 0 <= tall <= 20:
        print("Vår eller høst")
    else:
        print("Sommer")
```

## Variabler (Datatyper)
```python
tekst = "Dette er en tekst"
heltall = 42
desimaltall = 3.14
boolsk = True
```

## Arrays/Lister
```python
liste = ["a", "b", "c", "d", "e"]
print(liste[2])

liste[1] = "ny verdi"

siste_element = liste[4]

for element in liste:
    print(element)
```

## Objekter
```python
person = {"navn": "Ola", "alder": 25, "høyde": 1.75}
person["adresse"] = "Oslo"

personer = [
    {"navn": "Ola", "alder": 25, "høyde": 1.75},
    {"navn": "Kari", "alder": 30, "høyde": 1.68},
    {"navn": "Per", "alder": 22, "høyde": 1.80}
]

for p in personer:
    print(p["alder"], p["høyde"])
```

# Prosess og samarbeid

## Klon et prosjekt fra GitHub
```sh
git clone https://github.com/brukernavn/repository.git
```

## Vis hvordan du pusher en lokal endring til et repository
```sh
git add .
git commit -m "Oppdatering av kode"
git push origin main
```

## Vis hvordan du har brukt GitHub Projects til planlegging
* Bruk GitHub Projects for å lage "to-do", "in progress" og "done" kolonner
* Legg til issues i prosjektet
* Oppdater status på oppgaver fortløpende
