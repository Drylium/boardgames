import json

a = int(input("1.Lägga till ett spel\n2.Hitta ett spel\n3.Se lista över alla spel\n"))
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
        
    if input("Vill du lägga till fler?\n") != True:
        continue
    else:
        print("Tack!")
        break
if (a == 2):    #if you want to withdraw.
    print(name)
    print(players)
    print(time)
    print(age)
elif (a == 3):    #if you want to see a list of all the games.
    with open("games.json") as f:
        for a in f.readlines():
            print(a)
else:
    print("Inte ett giltigt svar, försök igen.")

#put the dict's into json file.