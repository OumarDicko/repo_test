import streamlit as st
from Assistant_LND import gpt_functioncall

# Titre de l'application web
st.title("Chatbot avec Streamlit")

# Initialisation des historiques s'ils n'existent pas déjà dans la session
if 'historique_user' not in st.session_state:
    st.session_state['historique_user'] = []

if 'historique_assistant' not in st.session_state:
    st.session_state['historique_assistant'] = []

# Champ de texte pour l'utilisateur
user_input = st.text_input("Votre message :")

# Bouton pour envoyer le message
if st.button("Envoyer"):
    # Construction de l'historique complet pour l'envoyer
    historique_complet = ""
    for i in range(len(st.session_state['historique_user'])):
        historique_complet += "User : " + st.session_state['historique_user'][i] + "\n"
        historique_complet += "Assistant : " + st.session_state['historique_assistant'][i] + "\n"

    # Ajouter la nouvelle entrée de l'utilisateur à l'historique complet
    historique_complet += "User : " + user_input + "\n"

    # Appel de la fonction avec l'historique
    bot_response = gpt_functioncall(prompt=historique_complet, system="Tu es LND-ASSISTANT, un prof virtuel qui aide les élèves du BAC", t=0.7)

    # Ajouter la nouvelle entrée et la réponse à l'historique dans la session
    st.session_state['historique_user'].append(user_input)
    st.session_state['historique_assistant'].append(bot_response)

    # Affichage de la réponse du chatbot
    st.text_area("", value=bot_response, height=1000, max_chars=None, key=None)
