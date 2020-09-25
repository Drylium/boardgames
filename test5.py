import json

a = (input("1.Lägga till ett spel\n2.Hitta ett spel\n3.Se lista över alla spel\n"))
while (a == 1):   #if you want to put in a game.
    data = {
        "games": {
            "name": input("Namn: "),
            "players": input("Antal spelare: "),
            "time": input("Tidsåtgång: "),
            "age": input("Rekomenderande ålder: ")
    }
}
    with open("games.json", "a+") as write_file:
        json.dump(data, write_file, indent=4)
        json_string = json.dumps(data)
        
    answear = input("Vill du lägga till fler spel?\n")
    while True:
        if answear == "ja":
            True
            break
        elif answear == "nej":
            input("Tack!")
            break
        else:
            answear = input("Svara med ett ja eller nej tack!\n")

if (a == 2):    #if you want to withdraw.
    pass
elif (a == 3):    #if you want to see a list of all the games.
    with open("games.json") as f:
        for a in f.readlines():
            print(a)
else:
    input("Inte ett giltigt svar, försök igen.")

#put the dict's into json file.