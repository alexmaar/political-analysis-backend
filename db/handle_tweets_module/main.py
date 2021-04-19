from handle_tweets_module.api.twintScripts import *
from handle_tweets_module.api.scripts import *
from datetime import date, timedelta
from pprint import pprint
import sqlite3

hashtags = ["#przyłębska",
            "niedlazaostrzeniaustawyaborcyjne", "legalabortion", "czarnyprotest", "protestujemy", "#rownosc", "#feminism",
            "notoabortion", "blackprotest", "stopaborcji", "babylivesmatter", "zażyciem", "czarnypiątek",
            "mybodymychoice", "piekłokobiet", "godek", "#kobieta", "aborcja", "prawakobiet", "strajkkobiet", "strajk kobiet",
            "KonwencjaStambulska", "niestrajkuje", "jestemzazyciem"]

users = ["trzaskowski_", "GoTracz", "AGajewska", "RobertBiedron", "martalempart",
         "KSuchanow", "barbaraanowacka", "poselTTrela", "adamSzlapka", "lis_tomasz",
         "JachiraKlaudia", "K_Smiszek", "bbudka", "KLubnauer", "Kaja_Godek",
         "KajaUlaGodek", "GrzegorzBraun_", "KonradBerkowicz", "PremierRP", "JEmilewicz",
         "mecenasJTK", "MorawieckiM", "DariuszMatecki", "prezydentpl", "KrystPawlowicz"]

users2 = ["partiarazem", "__Lewica", "Platforma_org", "strajkkobiet", "WarszawskiSK",
         "Kom_Obr_Dem", "federapl", "ObywateleRP", "gazeta_wyborcza",
         "oko_press", "tvn24", "TygodnikNIE", "Anna_Dryjanska", "Renata_Grochal",
         "EMichalik", "patrykmichalski", "sekielski", "KolendaK", "f_sterczewski",
         "HebanMaja", "kgonciarz", "karolpaciorek", "pisorgpl", "Partia_KORWiN",
         "KONFEDERACJA_", "MdW_Polska", "Duszpasterstwa", "JacekWronaCBS", "OrdoIuris",
         "tvp_info", "GPCodziennie", "Tygodnik_Sieci", "wPolityce_pl", "WtylewizjiINFO",
         "michalkarnowski", "wina_Mazurka", "cezarykrysztopa", "AKlarenbach",
         "Janusz1967", "LadyInB43912586", "MAGDALENKA_II", "PrawaStronaa", "Aynqa",
         "J_Pospieszalski", "AlinaPetrowaW", "tomaszsamolyk"]

# connect to our db:
# connection = sqlite3.connect('./tweets.db')
# db = connection.cursor()

# saving tweets:
startDate = date.today() - timedelta(days=100)
endDate = date.today()
# saveTweetsByHashtagList(hashtags, startDate, endDate)
saveTweetsByHashtagListForAllUsers(hashtags, users)  # zapisuje tweety tylko wybranych uzytkownikow

# get all users from saved tweets from DB:
# db.execute("SELECT distinct screen_name from tweets")
# allUsersNames = db.fetchall()

# saving users:
saveUsers(users2)

# pprint(vars(object)) # tak mozna printowac obiekty
