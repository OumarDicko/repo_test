import json
import requests
import datetime
import base64
import http.client
import ssl 
from Assistant_LND import gpt_functioncall
class ultraChatBot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance75165/'
        self.token = 'dkpxrprzvdqx4w4s'
   
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID,prompt):
        text = gpt_functioncall(system="Tu es un assistant",prompt=prompt,t=0.7)
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
        return answer

    def send_image(self, chatID,img_path):
        with open(img_path, "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode()

        url = f"https://api.ultramsg.com/instance75165/messages/image"
        payload = {
            'token': 'dkpxrprzvdqx4w4s',
            'to': '+212600448043',
            'image': img_base64,
            'caption': 'image Caption'
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        # Envoi de la requête
        response = requests.post(url, data=payload, headers=headers, verify=False)

        # Vérification des erreurs
        if response.status_code != 200:
            print("Erreur :", response.text)
        else:   
            print("Réponse :", response.text) 

    def send_video(self, chatID):
        data = {"to" : chatID,
                "video" : "https://file-example.s3-accelerate.amazonaws.com/video/test.mp4"}  
        answer = self.send_requests('messages/video', data)
        return answer

    def send_audio(self, chatID,audio_path):
        with open(audio_path, "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode()

        url = f"https://api.ultramsg.com/instance75165/messages/image"
        payload = {
            'token': 'dkpxrprzvdqx4w4s',
            'to': '+212600448043',
            'audio': img_base64,
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        # Envoi de la requête
        response = requests.post(url, data=payload, headers=headers, verify=False)

        # Vérification des erreurs
        if response.status_code != 200:
            print("Erreur :", response.text)
        else:   
            print("Réponse :", response.text) 


    def send_voice(self, chatID):
        data = {"to" : chatID,
                "audio" : "https://file-example.s3-accelerate.amazonaws.com/voice/oog_example.ogg"}  
        answer = self.send_requests('messages/voice', data)
        return answer

    def send_contact(self, chatID):
        data = {"to" : chatID,
                "contact" : "14000000001@c.us"}  
        answer = self.send_requests('messages/contact', data)
        return answer


    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)

    def Processingـincomingـmessages(self,historique):
        if self.dict_messages != []:
            message =self.dict_messages
            text = message['body'].split()
            if not message['fromMe']:
                chatID  = message['from']
                print(chatID)
                print(message['media'])
                texte_final = " ".join(text)
                
                texte_final += "\n Historique de chat elle commence par la question de l'user puis ta reponse : " + str(historique[-10:])
                reponse = self.send_message(chatID=chatID,prompt=texte_final)               

                return reponse, texte_final
            else: return 'NoCommand'


        
        