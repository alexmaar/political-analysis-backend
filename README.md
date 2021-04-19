## Installation and Setup Instructions
Clone down this repository. You will need node and npm installed on your machine.
## Installation:
```npm install```

You can run the system with command:

```npm start```

## Database
Ponieważ nie działało poprawnie zapisywanie do bazy przez twinta oraz pobieranie uzytkowników zrobiłem trochę zmian w plikach twintego.

Instrukcja instalacji twinta:
- cd twint
- pip3 install . -r requirements.txt

Dodałem również limit followersów od ilu zapisuje użytkownika do bazy. Żeby to zmienić należy zmienić linijke 180 w pliku output.py(if config.Database and user.followers > 5000:), a nastepnie zaistalować twintego ponownie.