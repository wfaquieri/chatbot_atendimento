# Chatbot de Atendimento ao Cliente

## Objetivo
Este projeto tem como objetivo criar um chatbot que responda a perguntas frequentes sobre um produto ou serviço, utilizando um modelo de linguagem natural.

## Estrutura do Projeto

A estrutura do repositório é a seguinte:

```
chatbot_atendimento/
│
├── faq.csv              # Conjunto de dados com perguntas e respostas
├── chatbot.py           # Código do chatbot
└── README.md            # Documentação do projeto
```

### Coleta de Dados
Um pequeno conjunto de dados é construído com perguntas frequentes e suas respectivas respostas. Um exemplo do dataset (`faq.csv`):

| Pergunta                               | Resposta                                                      |
|----------------------------------------|--------------------------------------------------------------|
| Quais são as opções de pagamento?     | Aceitamos cartões de crédito, PayPal e transferência bancária. |
| Como posso rastrear meu pedido?       | Você pode rastrear seu pedido através do link que enviamos por e-mail. |
| Qual é a política de devolução?       | Aceitamos devoluções em até 30 dias após a entrega.          |

## Instalação das Bibliotecas Necessárias

Para instalar as dependências necessárias, utilize o seguinte comando:

```bash
pip install transformers pandas flask
```

## Implementação do Chatbot

Crie um arquivo chamado `chatbot.py` e insira o seguinte código:

```python
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
```

## Executar o Chatbot

Para executar o chatbot, utilize o comando:

```bash
python chatbot.py
```

O chatbot estará disponível em `http://127.0.0.1:5000/ask`.

## Testar o Chatbot

Você pode usar ferramentas como Postman ou curl para enviar perguntas ao chatbot. Aqui está um exemplo de comando curl:

```bash
curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d '{"question": "Quais são as opções de pagamento?"}'
```

## Documentação do Projeto

Este arquivo `README.md` contém informações sobre como instalar as dependências, executar o chatbot e exemplos de chamadas de API.

## Dicas para Apresentação no Currículo

- Inclua um link para o repositório GitHub com o projeto completo.
- Destaque as tecnologias utilizadas e a importância do projeto para a área de atendimento ao cliente.
- Mencione a experiência adquirida com LLMs e a construção de aplicações web.

## Conclusão

Esse protótipo de chatbot é uma ótima maneira de demonstrar suas habilidades em LLMs, Python e desenvolvimento de aplicações. Com a documentação adequada e um código bem estruturado, você terá um projeto sólido para apresentar na sua candidatura. Boa sorte!
