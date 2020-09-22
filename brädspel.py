import json

with open('games.json') as f:
    data = json.load(f)

for games in data['games']:
    print(games)
#Fråga om man vill lägga till eller söka efter ett spel.


#Om man vill lägga till ett sel ska de frågas efter Titel/antal spelare/tidsgång/rekomenderad ålder.


#Efter ha lagt till ett spel fråga om hen vill lägga till ett till, annars avsluta.


#För att kvitera ut ett spel ska man ange minst en utav frågorna (Titel/antal spelare/tidsgång/rekomenderad ålder) för att få fram alla alternativ.


#Kunna redigera uppgifter om spelen samt kunna radera spel.