from datetime import date, timedelta
from pprint import pprint
import sqlite3
from time import sleep
import datetime

from scripts import saveTweetsByHashtagListForAllUsers, saveUsers, saveTweetsByHashtagList

hashtags = ["#przyłębska", "niedlazaostrzeniaustawyaborcyjne", "legalabortion", "czarnyprotest", "protestujemy", "#rownosc", "#feminism",
            "notoabortion", "blackprotest", "stopaborcji", "babylivesmatter", "zażyciem", "czarnypiątek",
            "mybodymychoice", "piekłokobiet", "godek", "#kobieta", "aborcja", "prawakobiet", "strajkkobiet", "strajk kobiet",
            "KonwencjaStambulska", "niestrajkuje", "jestemzazyciem", "WyrokNaKobiety", "FalaSprzeciwu", "czarnyponiedziałek",
            "OgólnopolskiStrajkKobiet", "KonwencjaPrawRodziny", "TweetUpOrdoIuris", "TakDlaRodziny", "TakDlaZycia",
            "prawodoaborcji", "razemzkobietami", "drugafala", "NieSkładamyParasolek", "KobietaDecyduje", "Alert4WomensRights"]

users = ["partiarazem", "ZbigniewHoldys", "AgataKowalskaTT", "Anna_Dryjanska", "LukaszKohut", "JacekJaworskiGd", "Aynqa", "Beata__Ka", "pigmalion55", "anita_fogler",
    "Justysi46819283", "ewollaa", "BDStanley", "BBCKasiaMadera", "amina_you", "nonunadimeno", "dabrowa_k", "SuperNiania", "RobertMaslak", "niedziela_pl", "trzaskowski_",
    "GoTracz", "AGajewska", "RobertBiedron", "martalempart", "KSuchanow", "barbaraanowacka", "poselTTrela", "adamSzlapka", "lis_tomasz", "JachiraKlaudia", "K_Smiszek",
    "bbudka", "KLubnauer", "GrzegorzBraun_", "KonradBerkowicz", "PremierRP", "JEmilewicz", "mecenasJTK", "MorawieckiM", "DariuszMatecki", "prezydentpl", "KrystPawlowicz",
    "__Lewica", "Platforma_org", "strajkkobiet", "WarszawskiSK", "Kom_Obr_Dem", "ObywateleRP", "gazeta_wyborcza", "oko_press", "tvn24", "TygodnikNIE", "Renata_Grochal",
    "EMichalik", "patrykmichalski", "sekielski", "KolendaK", "f_sterczewski", "HebanMaja", "kgonciarz", "karolpaciorek", "pisorgpl", "Partia_KORWiN", "KONFEDERACJA_",
    "JacekWronaCBS", "OrdoIuris", "tvp_info", "GPCodziennie", "Tygodnik_Sieci", "wPolityce_pl", "WtylewizjiINFO", "michalkarnowski", "wina_Mazurka", "cezarykrysztopa",
    "AKlarenbach", "Janusz1967", "PrawaStronaa", "J_Pospieszalski", "tomaszsamolyk", "Kaja_Godek", "federapl", "MdW_Polska", "Duszpasterstwa", "LadyInB43912586",
    "MAGDALENKA_II", "AlinaPetrowaW", "wdacji", "kacperparol_", "breathingvs", "SUNPIEISM", "kuba_urba", "rybosomek", "bialemieso", "ewefemme", "KaJagiello", "remekle",
    "nienaturalnosc", "thatislisbeth", "hmzagulska", "prfctsykes", "NNiepoprawna", "MarekRutka", "AMFETAMlNA", "lubielizaki", "magdadropek", "_XJulQaX_", "leniwalewaczka",
    "MiroslawSuchon", "haemad1psa", "FalejMonika", "WaclawJan", "amthreehu", "vanitesfaye", "LukaszKohut", "acczkolwiek", "everyday_loser", "MWielichowska", "SylwiaSpurek",
    "Zieloni", "moanrosa", "dallasxsunny", "unaagix", "KLubnauer", "Filmmor_", "fundacjaWoR", "DagmaraPakulska", "dawidmysior", "SylwiaSpurek", "LasekMaciej", "sylvcz",
    "ArturStelmasiak", "kujawiankaa", "MonikaaaBilska", "pawel_senkowski", "MosinskiJan", "RuchNarodowy", "IsakowiczZalesk", "RadioMaryja", "wolfstarnette", "jadespurpose",
    "matitoidiota", "perfectly_wr0ng", "TDFeV", "danutahuebner", "krytyka", "Ula_Zielinska", "hoeyannie", "szejnfeld", "M_Prokop_P", "luvmylittlelou", "KUeberhan",
    "_dimelaverdad", "dgpopiolek", "helenajaneczek", "B_Maciejewska", "GabrielaMorStan", "K_Mieszkowski", "delarabur", "SuwerenaPL", "ColombeCS", "propeertys", "m_gdula",
    "OloCzarny", "klimasara_j", "mlodalewica_", "KPH_official", "LukaszukAB", "wiosnabiedronia", "WandaNowicka", "Luearity", "JoankaSW", "TheProgressives", "RobertBiedron",
    "PiotrZiba11", "ObazRobert2", "kingamierzynska", "WKarpieszuk", "aneta_moscicka", "EuropaJens", "Maciejevvski", "eirigi1916", "nahmafia", "Norberto_BCN",
    "socjalistyczna", "fideista", "kreconefrytki", "KamilRochucki", "louieawx", "PortalWroclawpl", "rebecaflor", "pieprzmnieed", "WiolaKaminskaPL", "Pawlowska_pl",
    "piotr_borys", "JakubWu", "AnitaKDZG", "johnpaul_newman", "DemStory", "psycholog_pisze", "S_Potapowicz", "bozenalisowska", "MarekSzolc", "UGMediaLtd", "keram_iksmodar",
    "kissymoonchild", "dudumfan", "PrazonaCebula", "Albert301271", "SaaraHyrkko", "kirkyamakadin", "brightonanti", "ovvlsome", "JakubRoskosz", "LewicowyHub",
    "volnoscioviec", "JakubMedek", "madziamf", "KsymenaMatysek", "idzpodpradpl", "Evelyn_Regner", "samiraraf", "BartekPiekarski", "elukacijewska", "RFSU", "24tp_pl", "BZdrojewska",
    "ToNiePrzejdzie", "astrolavas", "ALetkiewicz", "wyborczawroclaw", "MadqueenShow", "Joanna_Lark", "businessteshno", "WojtekKardys", "Anna1Kwiecien", "Miasto_Lodz",
    "rosaantifawien", "GrupaStonewall", "michalpg", "pawpanasiuk", "zeckomag", "CEuropeCentrale", "gotowalska", "SwiftPL", "sbalcerac", "FAUGewerkschaft",
    "MarekTatala", "IL_Berlin", "ZStolicy", "PolaMatysiak", "BogdanKlich", "BatoryFundacja", "aniajaroszewska", "FundacjaFOR", "mycielski", "amnestyPL",
    "GraceOSllvn", "Greenpeace_PL", "lovekrakow", "jacek_liberski", "PolskaNormalna", "LiLaiRa95", "RaphaelleRL", "kabaretNeoNowka", "JaninaOchojska", "bogdan607", "MaciejSamcik",
    "SCHIEDER", "tlakomy", "AlicjaDef", "NZGoebbelsa", "macdac", "MarekKacprzak", "pinkstinksde", "igsonart", "luna_le", "karmel80", "gajewska_kinga", "jozefmoneta",
    "AmnestyEU", "XKubiak", "AM_Zukowska", "programZDupy", "RSF_en", "tokarczuk_olga", "oopsmypayno", "PaweSasko", "AgaBak", "rozathun", "VogulePoland", "profMarekBelka", "Bart_Wielinski",
    "ProgIntl", "natematpl", "MileyCyrusBR", "pomaska", "GreensEFA", "market_a", "KrzysztofBrejza", "brujasdelmar", "HollieB", "RenewEurope", "LukaszBok", "Gasiuk_Pihowicz",
    "Polityka_pl", "RESPEKT_CZ", "amnestyitalia", "JaroslawKuzniar", "ZDFheute", "lauraboldrini", "YourAnonCentral", "BLiberadzki", "LeniBreymaier", "tomasz_fraczak", "JagnaMarczulajt",
    "michalkowalowka", "LesJazd", "WomenReadWomen", "BaharHaghani", "kerwolter", "fred_matic", "JosefinePaul", "Melanie_Vogel_", "EPF_SRR", "max_lucks", "CreaPositiva", "MeTooEP",
    "ITolleret", "ippfen", "narkadindayanis", "Catlak_zemin", "nu_alabao", "mmatias_", "MiguelUrban", "jacekmiedlar", "CabajJoanna", "lewicki_mateusz", "Qynton", "realkatiejow",
    "MarzenaNykiel", "missmiafaith", "ArmedPatriot45", "delduduit", "Andruszkiewicz1", "TaylerUSA", "frfrankpavone", "robbystarbuck", "CSsR_PL", "RazorWire5", "retusz", "JKowalski_posel",
    "StowMarszN", "adzysk", "RzeszowNews", "Rz_mwj", "unverwertbar", "Wyrwal", "MonikaKarolinaa", "AgaSiewiereniuk", "KaziSmolinski", "edwinbendyk", "jzpinski", "JanMencwel", "Dorota_Brejza",
    "TOPTVPINFO", "BettyElaWhite", "Tysol", "freesafelegal", "tvpiKorea", "zelazna_logika", "ippf", "RMF24pl", "EELV", "V_Porowska", "AdamFabian85", "AnkaPolska", "JoannaSikorski",
    "Berni_Krynicka", "Dariusz_Lasocki", "OMAntypolonizmu", "m_bielecki_", "HannaGillPiatek", "ForfiterP", "bgraczak", "MRiPS_GOV_PL", "JkmMikke", "krawczyk_emil", "CywilizacjaZ",
    "MatKrzywousty", "nicogoncas", "P_Gasiorowski", "Marek08415702", "PawelZdun", "DariuszHarley", "BozenaPrzyluska", "Niezlomni_com", "EurowPolsce", "PawelChojecki", "Safe_Abortion",
    "Wyborcza_Krakow", "WojciechKorkuc", "Autonomie_Mag", "PoderPopularWeb", "Romanczuk_Anna", "KonradPogoda", "jflibicki", "jola_mor", "K_Galecka", "matt_magdziarz", "Droomer_NL",
    "motostork", "MartaHabior", "asta_fish", "K_Izdebski", "emocjewsieci", "punkboyinsf", "patrykchilewicz", "malyy5", "a_hrechorowicz", "Polityka_wSieci" , "IratxeGarper", "Another_Europe",
    "MEugeniaRPalop", "Diablica_Zwinna", "mmzawisza", "RBakiewicz", "fdpbt", "polskieradiopl", "rafalhubert", "nowePSL", "StollmeyerEU", "Parlimag", "PolskieRadio24", "sjkaleta", "FAKT24PL",
    "GreenpeaceEU", "TerryReintke", "RadioZET_NEWS", "RepublikaTV", "TomaszSakiewicz", "bweglarczyk", "humanite_fr", "euronews", "janinadailyblog", "6GhosT9", "JanMencwel", "Colmogorman"] 

# connect to our db:
# connection = sqlite3.connect('../tweets.db')
# db = connection.cursor()
# get all usersName from DB:
# db.execute("SELECT username from users")
# allUsersNames = db.fetchall()
# allUsersNames = [*map(lambda x: x[0], allUsersNames)]

# saving tweets:
startDate = datetime.datetime(2020,10,1)
endDate = date.today()
# saveTweetsByHashtagList(hashtags, startDate, endDate)
saveTweetsByHashtagListForAllUsers([hashtags[7 DONE]], users)  # zapisuje tweety tylko wybranych uzytkownikow

# saving users:
#saveUsers(users)

# pprint(vars(object)) # tak mozna printowac obiekty
