from openai import OpenAI
from promptList import function_call_toll,tool_english
from function_call import togetherAi,geminiAI,gpt
client = OpenAI(api_key="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")

def gpt_functioncall(message,t):
    function_reponse = ""
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  tools=tool_english,
  tool_choice="auto",
  messages=message,
    temperature=t
    )
    r_message = response.choices[0].message
    tool_calls = r_message.tool_calls

    return r_message

prompt = "Tu connais les logarithmes"
exo = """
#Exercice Moyennement Difficile :

Enoncé de l'exercice :
Soit z un nombre complexe tel que \(z = 2 + 3i\) et w un nombre complexe tel que \(w = -1 - 2i\).
On note \(z' = \frac{1}{z}\) le quotient de z par l'opposé de z et \(w' = \frac{\bar{w}}{w}\) le quotient du conjugué de w par w.

1. Question 1 :
   - Calculer z' et écrire le résultat sous forme algébrique.

2. Question 2 :
   - Calculer w' et écrire le résultat sous forme algébrique.

3. Question 3 :
   - Soit \(z_1 = 1 - i\) et \(z_2 = 3 + 2i\), déterminer \(|z_1|, |z_2|\) et \(arg(z_1)\), \(arg(z_2)\).

4. Question 4 :
   - Calculer le produit \(z_1 \times z_2\) et écrire le résultat sous forme algébrique.

Veillez à donner les réponses sous forme algébrique."""
message = [
    {"role":"system","content":"Tu es un assistant that always respond in french. Tu te base sur les anciens messages donné précédement par l'utilisateur pour determiner la meilleur reponse à donné ou la meilleur action à prendre. Tu as 3 actions que tu peux prendre, résoudre l'exercice pour cela il te faut fournir l'enoncé de l'exercice avec les questions relative à l'exercice, généré un exercice pour cela il te faut demander à l'utilisateur la leçon sur laquelle l'exercice doit porter et la difficulté qui varie entre facile, moyen et difficile ou Répondre à une question.Ne génère jamais un exercice sans connaitre le niveau de difficulté et la leçon et ces informations doivent toujours être fournis par l'utilisateur et tu ne dois pas les déduire, si tu as la leçon mais pas la difficulté insiste pour connaitre la difficulté de l'exercice"},
    ]
message.append({"role":"user","content":"Genere moi un exercice"})
message.append({"role":"assistant","content":exo})
message.append({"role":"user","content":"C'est cool merci"})
message.append({"role":"assistant","content":"derien"})
message.append({"role":"user","content":"C'est un exercice sur quoi ?"})
message.append({"role":"assistant","content":"les nombres complexes"})
message.append(    {"role":"system","content":"Tu es un assistant. Tu te base sur les anciens messages donné précédement par l'utilisateur pour determiner la meilleur reponse à donné ou la meilleur action à prendre. Tu as 3 actions que tu peux prendre, résoudre l'exercice pour cela il te faut fournir l'enoncé de l'exercice avec les questions relative à l'exercice, généré un exercice pour cela il te faut demander à l'utilisateur la leçon sur laquelle l'exercice doit porter et la difficulté qui varie entre facile, moyen et difficile ou Répondre à une question.Ne génère jamais un exercice sans connaitre le niveau de difficulté et la leçon et ces informations doivent toujours être fournis par l'utilisateur et tu ne dois pas les déduire"},
)
msg_en = "Give me an exercice on integrale, medium"
msg_fr = "Genere un exercice sur les fonction log neperiens"
message.append({"role":"user","content":msg_en})

r = gpt_functioncall(message=message,t=0)
print(r)