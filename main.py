print("Git_handson")
import json

DATA = [
    {
        "imię": "Burek",
        "gatunek": "Kot",
        "waga": 3,
        "wiek": 4
    },
    {
        "imię": "Bruno",
        "gatunek": "Pies",
        "waga": 35,
        "wiek": 3
    }
]

def display(data):
    print(data)
   
f = open("data.json")
DATA = json.load(f)

f2 = open("data2.json")
DATA2 = json.load(f2)

DATA.extend(DATA2)
display(DATA)