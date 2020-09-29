import json
from json.decoder import JSONDecodeError

class Games:
    def __init__(self):
        self.games = []
    def addGame(self, game):    #Tilläggsfunktion.
        self.games.append(game)
    def toJson(self):
        return self.__dict__
    def __repr__(self):
        return self.toJson()
    def removeGame(self, item):   #Raderingsfunktion.
        for game in self.games:
            if game == item:
                self.games.remove(game)
    def setIDs(self):   #ID generator.
        i = 0
        for games in self.games:
            game['id'] = i
            i += 1

class Game:
    def __init__(self, name, players, time, age):
        self.id = 0
        self.name = name
        self.players = players
        self.time = time
        self.age = age

def searchGame(query, value, list):  #Sökfunktion.
    result = []
    if query == "name":
        for game in list:
            if str(game.name) == str(value):
                result.append(game)
    elif query == "players":
        for game in list:
            if int(game.players) == int(value):
                result.append(game)
    elif query == "time":
        for game in list:
            if int(game.time) == int(value):
                result.append(game)
    elif query == "age":
        for game in list:
            if int(game.age) == int(value):
                result.append(game)
    return result

def arrayFromJson(data):
    games = []
    for item in data['games']:
        game = Game(None, None, None, None)
        game.id = item['id']
        game.name = item['name']
        game.players = item['players']
        game.time = item['time']
        game.age = item['age']
        games.append(game)
    return games

def gamesFromFile():
    games = Games()
    with open("games.json", "r") as f:
        # Läs in filens innehåll om det finns, annars pass
        try:
            data = json.load(f)
            gamesJson = arrayFromJson(data)
            for game in gamesJson:
                games.addGame(game.__dict__)
        except JSONDecodeError:
            pass
    return games

def printGames(games):
    print("Tillgängliga spel")
    for i in games.games:
        print(i)

def saveGames(games):
    with open("games.json", "w+") as write_file:    #Lägg till dict's till json fil.
        json.dump(games.toJson(), write_file, indent=4)
        json_string = games.toJson()

def editGame(game):  #Redigera spel.
    if game is None:
        game = Game(None, None, None, None).__dict__
    while True:
        try:
            game['name'] = input("Namn: ")
            game["players"] = int(input("Antal spelare: "))
            game["time"] = int(input("Tidsåtgång i minuter: "))
            game["age"] = int(input("Rekomenderande ålder: "))
            return game
        except ValueError:
            print("Ogiltigt värde, försök igen")
            continue
        else:
            break


while True:
    try:     #Se till att man skriver in en siffra, annars printa "ogiltigt värde"
        a = int(input("1.Lägga till ett spel\n2.Hitta ett spel\n3.Se lista över alla spel\n4.Redigera ett spel\n5.Radera ett spel\n6. Avbryt\n"))
    except ValueError:
        print("Ogiltigt värde, försök igen\n")
        continue
    if (a == 1):   #Lägga till spel.
        games = gamesFromFile()
        game = editGame(None)
        games.addGame(game)
        games.setIDs()
        saveGames(games)
            
        answer = input("Vill du lägga till fler spel?\n")    
        while input != "ja":
            if answer == "ja":
                break
            elif answer == "nej":
                quit()
            else:
                answer = input("Svara med ett ja eller nej tack!\n")

    elif (a == 2):    #Hitta spel.
        with open("games.json", "r") as f:
            data = json.load(f)
            games = arrayFromJson(data)
            print("Vad vill du söka på?")
            while True:
                try:   #Ser till att det är en siffra som fylls i.
                    answer = int(input("1. Titel\n2. Antal spelare\n3. Tidsåtgång\n4. Rekomenderad ålder\n5. Avbryt\n"))
                    result = []
                    while True:
                        if (answer == 1):
                            titel = input("Ange titel: ")
                            result = searchGame("name", titel, games)
                            break
                        elif (answer == 2):
                            players = input("Ange antal spelare: ")
                            result = searchGame("players", players, games)
                            break
                        elif (answer == 3):
                            time = input("Ange tidsåtgång: ")
                            result = searchGame("time", time, games)
                            break
                        elif (answer == 4):
                            age = input("Ange rekomenderad ålder: ")
                            result = searchGame("age", age, games)
                            break
                        elif (answer == 5):
                            quit()
                        else:
                            print("Ogiltigt värde")
                            answer = input()
                    print("Vill du lägga till en till egenskap?\n")
                    answer = int(input("1. Titel\n2. Antal spelare\n3. Tidsåtgång\n4. Rekomenderad ålder\n5. Avbryt\n"))
                    while True:
                        if (answer == 1):
                            titel = input("Ange titel: ")
                            result = searchGame("name", titel, games)
                            break
                        elif (answer == 2):
                            players = input("Ange antal spelare: ")
                            result = searchGame("players", players, games)
                            break
                        elif (answer == 3):
                            time = input("Ange tidsåtgång: ")
                            result = searchGame("time", time, games)
                            break
                        elif (answer == 4):
                            age = input("Ange rekomenderad ålder: ")
                            result = searchGame("age", age, games)
                            break
                        elif (answer == 5):
                            break
                        else:
                            print("Ogiltigt värde")
                            answer = input()
                    if len(result):
                        for i in result:
                            print(i.__dict__)
                    else:
                        print("Hittade inga spel")  

                    a = input("Vill du söka igen?\n")
                    while input != "ja":
                        if a == "ja":
                            break
                        elif a == "nej":
                            quit()
                        else:
                            a = input("Svara med ett ja eller nej")
                except ValueError:
                    print("Ogiltigt värde, försök igen\n")
                    continue      

    elif (a == 3):    #Lista över alla spel.
        games = gamesFromFile()
        printGames(games)
    elif (a == 4):    #Redigera spel.
        games = gamesFromFile()
        printGames(games)
        while True:
            answer = input("Ange ID på spelet du vill redigera:\nAnge \"avbryt\" om du vill avbryta\n ")
            if answer == "avbryt" or answer == "Avbryt":
                break
            elif answer.isnumeric() == False:
                print("ogiltigt värde")
            else:
                isGameEdited = False   
                for game in games.games:
                    if int(game['id']) == int(answer):
                        editGame(game)
                        isGameEdited = True
                print("Spel redigerat") if isGameEdited == True else print("Spel hittades ej")
                saveGames(games)

                if isGameEdited == True : break
    elif (a == 5):      #Radera spel.
        games = gamesFromFile()
        printGames(games)
        while True:
            answer = input("Ange ID på spelet du vill radera:\nAnge \"avbryt\" om du vill avbryta\n ")
            if answer == "avbryt" or answer == "Avbryt":
                break
            elif answer.isnumeric() == False:
                print("ogiltigt värde")
            else:
                isGameRemoved = False   
                for game in games.games:
                    if int(game['id']) == int(answer):
                        games.removeGame(game)
                        isGameRemoved = True
                print("Spel borttaget") if isGameRemoved == True else print("Spel hittades ej")
                saveGames(games)

                if isGameRemoved == True : break
                
    elif (a == 6):    #Avslutar programmet.
        print("Avslutar..")
        break
            
    else:    #Om man skriver in något som inte är ett alternativ.
        print("Inte ett giltigt värde, försök igen.\n")