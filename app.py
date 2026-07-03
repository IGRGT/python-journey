#amiguito goes live on the web!

import json
import time
from flask import Flask, redirect

app = Flask(__name__)




@app.route("/")
def home():
    
    with open("amiguito_state.json") as file:
        data =json.load(file)
    now = time.time()
    elapsed = now-data["last_updated"]
    decay = elapsed /10
    

    for key in ["fullness", "thirst", "energy", "happiness"]:
        data[key] -= decay
        if data[key] > 100:
            data[key] =100
        if data[key] < 0:
            data[key] =0
        data[key] = round(data[key], 1)
    data["last_updated"] = now
    with open("amiguito_state.json", "w") as file:
            json.dump(data, file)

    mood = ""
    if data['fullness'] < 30:
         mood += "im feeling hungry "
         mood+= ""
    if data['thirst'] < 30:
        mood+= "im feeling thirsty "
        mood+=""
    if data['energy'] <30:
        mood+= "im feeling tired "
        mood+=""
    if data['happiness'] <30:
        mood+= "im quite sad lets play "
        mood+=""
    face = ":)"
    if mood != "":
        face = ":("
    bg = "lightgreen"
    if mood != "":
        bg = "lightgray"
    



    return '<meta http-equiv="refresh" content="10">' f" <style>body {{ background-color: {bg}; }}</style>  {face} Fullness: {data['fullness']}, Thirst: {data['thirst']}, Energy: {data['energy']}, Happiness: {data['happiness']}, {mood}" + '<form action="/feed" method="POST"><button type="submit">Feed</button></form>' + '<form action="/play" method="POST"><button type="submit">Play</button></form>'+ '<form action="/rest" method="POST"><button type="submit">Rest</button></form>' + '<form action="/drink" method="POST"><button type="submit">Drink</button></form>'
    

@app.route("/feed", methods=["POST"])
def feed():
    with open("amiguito_state.json") as file:
        data = json.load(file)
    data["fullness"] += 10
    with open("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/play", methods=["POST"])
def play():
    with open("amiguito_state.json") as file:
        data= json.load(file)
    data["happiness"] += 10
    with open ("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/rest", methods=["POST"])
def rest():
    with open("amiguito_state.json") as file:
        data = json.load(file)
    data["energy"] += 10
    with open  ("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")

@app.route("/drink", methods=["POST"])
def drink():
    with open("amiguito_state.json") as file:
        data = json.load(file)
    data["thirst"] += 10
    with open("amiguito_state.json", "w") as file:
        json.dump(data, file)
    return redirect("/")



app.run(debug=True)
