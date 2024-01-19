import os
from openai import OpenAI
import time
import json
from rag import Answer_Generator, query_generator_without_answers
from function_call import assistant_gpt,Exercice_generation_math
from promptList import function_call_toll

client = OpenAI(api_key="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")

prompt = """
Resous ce exercice : 

    Soit X une variable aléatoire suivant une loi binomiale B(n, p) avec n = 5 et p = 0.4.

    1. Calculer la probabilité que X prenne la valeur 3.
    2. Calculer l'espérance mathématique de X.
    3. Calculer la variance de X.

"""

def gpt_functioncall(prompt,system,t):
    function_reponse = ""
    response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  tools=function_call_toll,
  tool_choice="auto",
  messages=[
    {"role": "system", "content": system},
    {"role": "user", "content": prompt}
        ],
    temperature=t
    )
    r_message = response.choices[0].message
    tool_calls = r_message.tool_calls

    if tool_calls:
        available_functions = {
            "Answer_Generator": query_generator_without_answers,
            "Exercice_Generator_math":Exercice_generation_math,
            "Exercice_Solver":assistant_gpt
        } 
        for tc in tool_calls:
            print(r_message)
            function_name = tc.function.name
            function_to_call = available_functions[function_name]
            function_arg = json.loads(tc.function.arguments)
            if function_name == "Answer_Generator":
                function_reponse = function_to_call(
                    main_query=function_arg.get("question")
                )
            if function_name == "Exercice_Solver":
                function_reponse = function_to_call(
                    prompt=function_arg.get("Enonce")
                )
            if function_name == "Exercice_Generator_math":
                function_reponse = function_to_call(
                    leçon=function_arg.get("lecon"),difficulte=function_arg.get("difficulte")
                )

        return function_reponse
    else:
        return r_message.content
