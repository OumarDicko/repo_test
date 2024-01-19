import re
from openai import OpenAI
client = OpenAI(api_key="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")

def gpt(prompt, nbr):
    system_message = """
    Composez un rapport professionnel en tant qu'étudiant universitaire.
    Ne donne pas de titre au texte, juste fournis le contenu.
    Ne fait pas de sous titre juste utilise le contenu qu'on ta donné.
    Ne fait pas un résumé à la fin du texte.
    Si le texte orginale point vers un tableau ne parle pas de cela, n'inclus pas de reference vers d'autre source dans le texte.
    La structure de votre rapport doit inclure le titre distinct suivi du contenu. 
    Assurez-vous que la longueur de votre texte sois aussi long que le texte fournis. 
    Votre tâche consiste à modifier de manière créative le texte, et en étendant le contenu uniquement dans les limites du texte original. 
    Utilisez un vocabulaire à la fois simple et compréhensible, et évitez de fournir un excès d'exemples. 
    Assurez-vous que les exemples que vous incluez sont clairs et adaptés à un public universitaire.
    utilise un n vocabulaire simple qui ne montre qu'on est pas un expert dans la langue mais une personne qui le parle courament
    Le texte doit contenir au moins ce nombre de charactère : 
    """ + str(nbr) + "\n Ne fait pas de conclusion, te"
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ],
    temperature=0.7
    )

    return response.choices[0].message.content

def extract_bold_text(text):
    pattern = r'\*\*\*(.*?)\*\*\*'
    matches = re.findall(pattern, text)
    return matches

def extract_text_between_delimiters(text, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    parts = re.split(pattern, text)
    return parts

# Exemple d'utilisation
document = []
text = ""
with open('enjeux.md', 'r', encoding='utf-8') as f :
    text = f.read()

delimiteur = extract_bold_text(text=text)
element_text = extract_text_between_delimiters(text=text,delimiters=delimiteur)

final_texte = []


for i in range(len(element_text)):
    if i < 26:
        t = delimiteur[i] + "\n"+ element_text[i+1]
    else:
        pass
    final_texte.append(t)


for e in delimiteur:
    print(e)
"""
for i in range(len(final_texte)):
    print(i)
    nbr = len(final_texte[i])
    t = gpt(final_texte[i], nbr=nbr)
    print(len(t))
    print(len(final_texte[i]))
    t+= "\n-----------------------------------------------------------------------\n\n"
    with open('expose.txt','a',encoding='utf-8') as f:
        f.write(t)
"""
test = 'test'