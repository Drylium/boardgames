import json

name = []
players = []
time = []
age = []

name = input("Lägg till titel: ")
players = input("Spelare: ")
time = input("Tidsåtgång: ")
age = input("Rekomenderad ålder: ")

with open('games.json', 'a') as f:
    json.dump(name, f)
with open('games.json', 'a') as f:
    json.dump(players, f)
with open('games.json', 'a') as f:
    json.dump(time, f)
with open('games.json', 'a') as f:
    json.dump(age, f)

print(name)
print(players)
print(time)
print(age)