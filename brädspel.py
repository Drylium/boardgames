import json
"""
with open('games.json') as f:
    data = json.load(f)

for games in data['games']:
    print(games)
"""
#Fråga om man vill lägga till eller söka efter ett spel.
a = (input("1: Vill du lägga till ett spel?\n 2: Se en lista över alla spel\n 3: Söka efter ett spel\n "))
if a==1:
    with open('games.json', 'w+') as w:
        for name in games:
            w.write(f'{name}\n')
        for players in games:
            w.write(f'{players}\n')
        for time in games:
            w.write(f'{time}\n')
        for age in games:
            w.write(f'{age}\n')
elif a==2:
    with open('games.json') as f:
        for b in f.read():
            print(b)

elif a==3:
    pass
else:
    pass



#Om man vill lägga till ett sel ska de frågas efter Titel/antal spelare/tidsgång/rekomenderad ålder.


#Efter ha lagt till ett spel fråga om hen vill lägga till ett till, annars avsluta.


#För att kvitera ut ett spel ska man ange minst en utav frågorna (Titel/antal spelare/tidsgång/rekomenderad ålder) för att få fram alla alternativ.


#Kunna redigera uppgifter om spelen samt kunna radera spel.