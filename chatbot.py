import pandas as pd
from transformers import pipeline
from flask import Flask, request, jsonify

# Carregar dados
df = pd.read_csv('faq.csv')

# Treinar modelo com perguntas e respostas
chatbot = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Iniciar aplicação Flask
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    context = ' '.join(df['Pergunta'].tolist() + df['Resposta'].tolist())
    
    # Responder à pergunta
    answer = chatbot(question=user_question, context=context)
    return jsonify({'answer': answer['answer']})

if __name__ == '__main__':
    app.run(debug=True)
