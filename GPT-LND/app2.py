from flask import Flask, request, jsonify
from ultrabot import ultraChatBot
import json

app = Flask(__name__)
historique = []
@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        reponseBot,inputuser =bot.Processingـincomingـmessages(historique)
        historique.append(inputuser)
        historique.append(reponseBot)
        return reponseBot

if(__name__) == '__main__':
    app.run()