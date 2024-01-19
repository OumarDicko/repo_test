from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import faiss
from promptList import search_query_generator,hypothesis_generator, SystemUserAnswer
from function_call import gpt_jsonMode,geminiAI,togetherAi,gpt
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.embeddings import OpenAIEmbeddings
import json
import os

embedding = OpenAIEmbeddings(api_key="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")
os.environ["SERPER_API_KEY"] = "2df05fe35fa0e542bf77b7a3b2602b2cf7b9456d"

def Save_VectorStore():
    text = PyPDFLoader("mathCours.pdf")
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=10)
    document = text.load()
    docs = text_spliter.split_documents(document)

    db = faiss.FAISS.from_documents(docs,embedding)

    db.save_local("MathVectorStore")

def OnlineSearch(query):
    searchonline = GoogleSerperAPIWrapper()
    infoFinal =""
    recherche = searchonline.run(query)

    return recherche 


def Vector_Search(search,k):
    db = faiss.FAISS.load_local("MathVectorStore", embeddings=embedding)

    infoVector = db.similarity_search_with_relevance_scores(search, k=k)

    infoFinal =""

    for data,score in infoVector:
        infoFinal += data.page_content + " \n "

    return infoFinal

def query_generator_with_answers(main_query):
    querysearchList = gpt_jsonMode(prompt=main_query, system=search_query_generator,t=0.35)
    querysearchList_JSON = json.loads(querysearchList)
    reponse_query = {}
    for q in querysearchList_JSON.values():
         reponse_query[q] = OnlineSearch(q)
    
    return reponse_query

def query_generator_without_answers(main_query):
    querysearchList = gpt_jsonMode(prompt=main_query, system=search_query_generator,t=0.35)
    querysearchList_JSON = json.loads(querysearchList)
    reponse_query = []
    for q in querysearchList_JSON.values():
         reponse_query.append(q)
    
    prompt = "Main Query " + main_query + ". Complement Question : " + str(reponse_query)
    
    system = """
    Créez une synthèse bien structurée et détaillée qui répond à la question principale ainsi qu'à toutes les sous-questions qui vous seront fournis. Analysez attentivement la question principale et les sous-questions pour identifier les points clés et les thèmes communs. Dans votre synthèse, veillez à fournir une réponse claire à la question principale en utilisant des arguments logiques et des exemples pertinents. Tout en abordant les sous-questions, reliez-les à la question principale pour montrer leur importance et leur relation. Assurez-vous d'organiser votre synthèse de manière cohérente et d'inclure des transitions fluides entre les différentes parties afin de faciliter la compréhension et la lisibilité. Utilisez des citations et des sources appropriées pour renforcer votre argumentation, le cas échéant.
    """
    try:
        r = geminiAI(prompt=prompt,system=system,t=0.6)
    except Exception as e:
        r = gpt(prompt=prompt,system=system,t=0.6)
    return r


def Answer_Generator(main_query):

    information = query_generator_with_answers(main_query=main_query)

    prompt = "Main Query : " + main_query + "\n "
    isExplication = False
    for query, query_answer in information.items():
        if str(query).lower() != 'oui' and str(query_answer).lower() != 'oui':
            prompt += "Query : " + query + " Answers : " + query_answer + " \n"
        else:
            isExplication=True

    print(str(isExplication))
    if isExplication == False:
        reponse = geminiAI(prompt=prompt,system=hypothesis_generator,t=0.4)
    else:
        prompt = main_query
        reponse = togetherAi(system=SystemUserAnswer("User Name : Oumar Dicko"), prompt=prompt,t=0.7)

    return reponse

def GetProgramme(matiere):
    query_savoir = "Quels sont les savoirs et les savoirs faire de cette matière :" + matiere
    query_savoirfaire = "Quels sont les savoirs et les savoirs faire de cette matière :" + matiere
    programme_vectorSearch = Vector_Search(query_savoir,k=2) + "\n" + Vector_Search(query_savoirfaire,k=2)

    get_savoir = "Quels sont les savoirs faires et les savoirs de cette matiere : " + matiere + ". \nBase toi sur ces information : " + programme_vectorSearch
    system = "Ta tâche est de répondre à la question posé en te basant sur les information qu'on te donne. Contente toi de donner la réponse sans parler. Presente le sous ce format : #Savoir \n .... \n #Savoir Faire \n ...."

    programme = geminiAI(system=system,prompt=get_savoir,t=0)

    return programme
