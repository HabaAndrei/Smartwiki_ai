# env =>>> Wiki_env

from langchain.retrievers import WikipediaRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

retriever = WikipediaRetriever()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
model = ChatOpenAI(model_name="gpt-3.5-turbo")  # switch to 'gpt-4'
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)



app = Flask(__name__)
CORS(app)

@app.route("/cerereAI" , methods = ['POST'])
def index():

    data = request.json
    intrebare = data['intrebare']
    context = data['context']

    istoric = []

    for obiect in context:
        istoric.append((obiect['intrebare'], obiect['raspuns']))

    # print('---------          ', istoric, '     --------------------------')

    result = qa({"question": intrebare, "chat_history": istoric, "load_max_docs":1500 })
    # print(result)
    ##################################
    return {'raspuns': result['answer']}

if __name__ == '__main__':
    app.run(host='195.201.17.190', port=8010, debug=True)



