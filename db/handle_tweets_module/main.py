from datetime import date, timedelta
from pprint import pprint
import sqlite3
from time import sleep

from db.handle_tweets_module.scripts import saveTweetsByHashtagListForAllUsers, saveUsers, saveTweetsByHashtagList

hashtags = ["#przyłębska",
            "niedlazaostrzeniaustawyaborcyjne", "legalabortion", "czarnyprotest", "protestujemy", "#rownosc", "#feminism",
            "notoabortion", "blackprotest", "stopaborcji", "babylivesmatter", "zażyciem", "czarnypiątek",
            "mybodymychoice", "piekłokobiet", "godek", "#kobieta", "aborcja", "prawakobiet", "strajkkobiet", "strajk kobiet",
            "KonwencjaStambulska", "niestrajkuje", "jestemzazyciem"]

users = ["partiarazem", "ZbigniewHoldys", "AgataKowalskaTT", "Anna_Dryjanska", "LukaszKohut",
         "JacekJaworskiGd", "Aynqa", "Beata__Ka", "pigmalion55", "anita_fogler", "Justysi46819283",
         "ewollaa", "BDStanley", "BBCKasiaMadera", "amina_you", "nonunadimeno", "dabrowa_k",
         "SuperNiania", "RobertMaslak", "niedziela_pl", "trzaskowski_", "GoTracz", "AGajewska",
         "RobertBiedron", "martalempart", "KSuchanow", "barbaraanowacka", "poselTTrela", "adamSzlapka",
         "lis_tomasz", "JachiraKlaudia", "K_Smiszek", "bbudka", "KLubnauer", "GrzegorzBraun_",
         "KonradBerkowicz", "PremierRP", "JEmilewicz", "mecenasJTK", "MorawieckiM", "DariuszMatecki",
         "prezydentpl", "KrystPawlowicz", "__Lewica", "Platforma_org", "strajkkobiet", "WarszawskiSK",
         "Kom_Obr_Dem", "ObywateleRP", "gazeta_wyborcza", "oko_press", "tvn24", "TygodnikNIE",
         "Renata_Grochal", "EMichalik", "patrykmichalski", "sekielski", "KolendaK", "f_sterczewski",
         "HebanMaja", "kgonciarz", "karolpaciorek", "pisorgpl", "Partia_KORWiN", "KONFEDERACJA_",
         "JacekWronaCBS", "OrdoIuris", "tvp_info", "GPCodziennie", "Tygodnik_Sieci", "wPolityce_pl",
         "WtylewizjiINFO", "michalkarnowski", "wina_Mazurka", "cezarykrysztopa", "AKlarenbach",
         "Janusz1967", "PrawaStronaa", "J_Pospieszalski", "tomaszsamolyk", "Kaja_Godek",
          "federapl", "MdW_Polska", "Duszpasterstwa", "LadyInB43912586", "MAGDALENKA_II", "AlinaPetrowaW"]

# connect to our db:
# connection = sqlite3.connect('../tweets.db')
# db = connection.cursor()
# get all usersName from DB:
# db.execute("SELECT username from users")
# allUsersNames = db.fetchall()
# allUsersNames = [*map(lambda x: x[0], allUsersNames)]

# saving tweets:
startDate = date.today() - timedelta(days=100)
endDate = date.today()
# saveTweetsByHashtagList(hashtags, startDate, endDate)
# saveTweetsByHashtagListForAllUsers(hashtags, users)  # zapisuje tweety tylko wybranych uzytkownikow

# saving users:
# saveUsers(users)

# pprint(vars(object)) # tak mozna printowac obiekty
