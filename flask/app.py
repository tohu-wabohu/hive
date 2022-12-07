from flask import Flask
from elasticsearch import Elasticsearch

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Flask!</p>\n"

# Interact with elasticsearch
@app.route("/es")
def es():
    es = Elasticsearch('http://es01:9200')
    print(es.info())
    doc = {
      'author': 'John Wick',
      'text': 'Hello world!'
    }

    #res = es.index(index="test-index", document=doc)
    res = es.index(index="test-index", id=2, document=doc)
    return res['result'] + '\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
