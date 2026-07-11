#amiguito goes live on the web!

import json
import time
from flask import Flask, redirect

app = Flask(__name__)




@app.route("/")
def home():
    
    with open("amiguito_state.json") as file:
        data =json.load(file)
        stats = data["stats"]
        inventory = data["inventory"]

    now = time.time()
    elapsed = now-stats["last_updated"]
    decay = elapsed /10
    

    for key in ["fullness", "thirst", "energy", "happiness"]:
        stats[key] -= decay
        if stats[key] > 100:
            stats[key] =100
        if stats[key] < 0:
            stats[key] =0
        stats[key] = round(stats[key], 1)
    stats["last_updated"] = now
    with open("amiguito_state.json", "w") as file:
            json.dump(data, file)
    
    mood = ""
    if stats['fullness'] < 30:
         mood += "im feeling hungry "
         mood+= ""
    if stats['thirst'] < 30:
        mood+= "im feeling thirsty "
        mood+=""
    if stats['energy'] <30:
        mood+= "im feeling tired "
        mood+=""
    if stats['happiness'] <30:
        mood+= "im quite sad lets play "
        mood+=""
    face = ":)"
    if mood != "":
        face = ":("
    bg = "lightgreen"
    if mood != "":
        bg = "lightgray"
        
    inventory_display = ""
    for item in inventory:
        inventory_display += item + ", "


    return '<br>' + '<meta http-equiv="refresh" content="10">' f" <style>body {{ background-color: {bg};font-size: 40px; }}</style>  {face} Fullness: {stats['fullness']}, Thirst: {stats['thirst']}, Energy: {stats['energy']}, Happiness: {stats['happiness']}, {mood}" + '<br>' + '<br>' + '<br>'+ '<form action="/feed" method="POST"><button type="submit">Feed</button></form>' + '<form action="/play" method="POST"><button type="submit">Play</button></form>'+ '<form action="/rest" method="POST"><button type="submit">Rest</button></form>' + '<form action="/drink" method="POST"><button type="submit">Drink</button></form>' + '<form action="/reset" method="POST"><button type="submit">Reset</button></form>' + '<br>' + '<br>' + inventory_display

@app.route("/reset", methods=["POST"])
def reset():
    with open("amiguito_state.json") as file:
        data = json.load(file)
        stats = data["stats"]
    stats["fullness"] = 100
    stats["thirst"] = 100
    stats["energy"] = 100
    stats["happiness"] = 100
    with open("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")
@app.route("/feed", methods=["POST"])
def feed():
    with open("amiguito_state.json") as file:
        data = json.load(file)
        stats = data["stats"]
    stats["fullness"] += 10
    with open("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/play", methods=["POST"])
def play():
    with open("amiguito_state.json") as file:
        data= json.load(file)
        stats = data["stats"]
    stats["happiness"] += 10
    with open ("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/rest", methods=["POST"])
def rest():
    with open("amiguito_state.json") as file:
        data = json.load(file)
        stats = data["stats"]
    stats["energy"] += 10
    with open  ("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/drink", methods=["POST"])
def drink():
    with open("amiguito_state.json") as file:
        data = json.load(file)
        stats = data["stats"]
    stats["thirst"] += 10
    with open("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")



app.run(debug=True)
