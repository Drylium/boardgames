import json

a = int(input("1.Lägga till ett spel\n2.Hitta ett spel\n3.Se lista över alla spel\n4.Redigera ett spel\n5.Radera ett spel\n"))
while (a == 1):   #if you want to put in a game.
    data = {      
        "games": {
            "name": input("Namn: "),
            "players": input("Antal spelare: "),
            "time": input("Tidsåtgång: "),
            "age": input("Rekomenderande ålder: ")
    }
}
    with open("games.json", "a+") as write_file:    #put the dict's into json file.
        json.dump(data, write_file, indent=4)
        json_string = json.dumps(data)
        
    answer = input("Vill du lägga till fler spel?\n")    
    while input != "ja":
        if answer == "ja":
            continue
        elif answer == "nej":
            print("Tack!")
            break
        else:
            answer = input("Svara med ett ja eller nej tack!\n")

if (a == 2):    #if you want to withdraw.
    pass
elif (a == 3):    #if you want to see a list of all the games.
    with open("games.json") as f:
        for a in f.readlines():
            print(a)
elif (a == 4):
    with open("games.json", "r+") as f:
        data = json.load(f)
        data["name"] = input()
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
elif (a == 5):
    pass
else:
    input("Inte ett giltigt svar, försök igen.\n")

#put the dict's into json file.