import os
from openai import OpenAI
import time
import json
from PIL import Image
import io

client = OpenAI(api_key="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")
assistantid = "asst_w3HQx1Pl3yv4DgFDiljuL3gb"
threadid = "thread_dB9YeZywkPUHwf9BGv65ke6B"
messageid = "msg_mD971kedFWRCgoocBSjyVubK"
# Définir une variable d'environnement
os.environ['TOGETHER_API_KEY'] = "6414ad330a1fef94b8b5b5d0c473b562d19f10a7d6aac32846a6f4d33c393f2f"
os.environ.get('TOGETHER_API_KEY')

assistant = client.beta.assistants.retrieve(assistant_id=assistantid)
thread = client.beta.threads.retrieve(thread_id=threadid)
imgid = ""

def get_weather(location):
    print("Voici la météo")
    return "La temperature de " + location + " est de 20 dégré"

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="genere moi un image d'un graphique histogramme de la population de chaque 6 pays pris au hasard, genere les datas de maniere aleatoire"
)
message.content[0].text.annotations
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
)

content = client.files.content("file-Jo0a8KtFxSwLhmd9WOmARcIY")
messageid = message.id

while True:
    run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

    messages = client.beta.threads.messages.list(
      thread_id=thread.id
)

    time.sleep(5)
    if(run.status == "completed"):
        print(messages.data[0])
        if hasattr(messages.data[0].content[0], 'image_file'):
            print(messages.data[0].content[0].image_file.file_id)
            imgid = messages.data[0].content[0].image_file.file_id
            file = client.files.content(file_id=imgid)
            image = Image.open(io.BytesIO(file.content))

            image.show()

        else:
            print("Il n'y pas d'image créer ")
        break
    elif (run.status == "requires_action"):
        tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
        name = tool_call.function.name
        argument = json.loads(tool_call.function.arguments)
        r = get_weather(argument['location'])

        run = client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=[
                {
                    "tool_call_id":tool_call.id,
                    "output": r
                }
            ]
        )
        print("Execution tool terminé")

    print(run.status)


# Extract the message content


