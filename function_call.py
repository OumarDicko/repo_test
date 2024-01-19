from openai import OpenAI
import os
import google.generativeai as genai
import time
from PIL import Image
import io
from promptList import *

client = OpenAI(api_key="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")
genai.configure(api_key="AIzaSyButZzMI77rxMkcnVqf-bA_nYSemK0hD68")

gemini_model = genai.GenerativeModel("gemini-pro")

def geminiAI(prompt,system,t):
    promptFinal = "[SYSTEM]" + system + "[/SYSTEM] [INPUT]" + prompt + "[/INPUT]"
    reponseIA = gemini_model.generate_content(
        promptFinal,generation_config={"temperature":0,"candidate_count":1}
    )

    return reponseIA.candidates[0].content.parts[0].text

def togetherAi(prompt,system,t,model="mistralai/Mixtral-8x7B-Instruct-v0.1"):
    client = OpenAI(
    api_key= "6414ad330a1fef94b8b5b5d0c473b562d19f10a7d6aac32846a6f4d33c393f2f",
    base_url='https://api.together.xyz',
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
        "role": "system",
        "content": system,
        },
        {
        "role": "user",
        "content": prompt,
        }
    ],
    model=model,
    temperature=t
    )

    return chat_completion.choices[0].message.content


def gpt_jsonMode(prompt,system,t):
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": prompt}
        ],
    temperature=t
    )
    return response.choices[0].message.content

def gpt(prompt,system,t):
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": prompt}
        ],
    temperature=t
    )
    return response.choices[0].message.content


def Vision():
    print("Vision")

def Exercice_generation_math(leçon,difficulte):
    leçon_disponible= ["Nombres_complexes","Arithmétiques","Fonctions_numériques","Suites_numériques","Primitives_Intégrales_Calculs_daires", "Fonctions_logarithmes","Fonctions_exponentielle","Equations_différentielles","Dénombrement_Probabilité_Variable_aléatoire_Loi_binomiale_Epreuve_de_Bernoulli","Barycentres"," Applications_affines"," Statistiques","Coniques"]
    print(leçon)
    print(difficulte)
    time.sleep(6)
    programme =""
    if leçon == leçon_disponible[0]:
        programme = savoir_savoirFaire_Nombre_Complexe
    if leçon == leçon_disponible[1]:
        programme = savoir_savoirFaire_Arithmetique
    if leçon == leçon_disponible[2]:
        programme = savoir_savoirFaire_Fonction_numérique_dune_variable_reelle
    if leçon == leçon_disponible[3]:
        programme = savoir_savoirFaire_Suite_Numerique
    if leçon == leçon_disponible[4]:
        programme = savoir_savoirFaire_primitive_intégrale_calculs_daires
    if leçon == leçon_disponible[5]:
        programme = savoir_savoirFaire_Fonction_Logarithmes_Neperiens
    if leçon == leçon_disponible[6]:
        programme = savoir_savoirFaire_Fonctions_exponentielle
    if leçon == leçon_disponible[7]:
        programme = savoir_savoirFaire_Equations_différentielle
    if leçon == leçon_disponible[8]:
        programme = savoir_savoirFaire_Dénombrement_Probabilité_VariableAléatiure_LoiNinomiale_EpreuveDeBernoullie
    if leçon == leçon_disponible[9]:
        programme = savoir_savoirFaire_Barycentres
    if leçon == leçon_disponible[10]:
        programme = savoir_savoirFaire_Application_Affine
    if leçon == leçon_disponible[11]:
        programme = savoir_savoirFaire_Statistique
    if leçon == leçon_disponible[12]:
        programme = savoir_savoirFaire_Conique
    
    prompt = "programme : \n" + programme
    system = "Tu es un professeur de mathématique pour les élèves passant le BAC au Mali. Ta tâche est de fournir un exercice de mathématique à l'élèves."

    if difficulte == "facile":
        system += exercice_facile
        
    if difficulte == "moyen":
        system += exercice_moyen
    
    if difficulte == "difficile":
        system += exercice_difficile
    
    exercice_generé = gpt(prompt=prompt,system=system,t=1)

    return exercice_generé
def Explication_cours():
    print("cours")

def Audio_Prof(prompt):
    speech_file_path = "speech.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=prompt
    )

    response.stream_to_file(speech_file_path)

def Ecoute_Prof(audio_path):
    audio_file = open(audio_path, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )

    return transcript


def assistant_gpt(prompt,assistantid="asst_zb7jlSLJzvH1Q2SSUvOC6xSn"):
    #Initialisation de la réponse de l'assistant
    reponse_assistant = ""
    #Récupération des objets assistant et thread
    assistant = client.beta.assistants.retrieve(assistant_id=assistantid)
    thread = client.beta.threads.create()

    #Création du prompt de l'utilisateur dans le thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt,
    )

    #Initialisation de la variable run pour vérifier le status de nos demande
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    )

    #Cette boucle sert à attendre jusqu'à ce que la demande API pour la réponse de l'assistant reussis ou échoue
    while True:
        #Actualise l'état du run pour voir le changement dans l'état de la demande
        run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
        )

        #Actualise messages pour voir si la réponse de l'assistant n'a pas été ajouté dans le thread
        messages = client.beta.threads.messages.list(
        thread_id=thread.id
        )

        #Verifie si la demande à réussi
        if(run.status == "completed"):
                    
            #Vérifie si l'assistant à rétourner une image (Elle peut retourner un fichier mais cela n'est pas prise en compte)
            if hasattr(messages.data[0].content[0], 'image_file'):
                #Récupère l'id du fichier
                imgid = messages.data[0].content[0].image_file.file_id
                #Récupère le fichier en byte
                file = client.files.content(file_id=imgid)
                #Converti le fichier en image utilisable
                image = Image.open(io.BytesIO(file.content))

                #Sauvegarde l'image
                image.save("img_assistant.png")

                #Récupère la réponse de l'IA
                reponse_assistant = messages.data[0].content[1].text.value
            
            else:
                reponse_assistant = messages.data[0].content[0].text.value
                print("Il n'y pas d'image créer ")
            
            break
            #Fin de la verif si il y' a une image généré -------------------------------
            
        #On vérifié si le demande à échoue   
        elif run.status == "failed":
            reponse_assistant = "failed"

        #On attend la réponse de l'assistant
        time.sleep(2)
    resultat = "Voici l'exercice :" + prompt + " Voici les résultat de l'exercice. Resultat : " +reponse_assistant
    reponse_assistant = gpt(system=exoFormat, prompt=prompt,t=0)
   
    return reponse_assistant
