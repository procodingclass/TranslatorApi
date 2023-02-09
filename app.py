from flask import Flask, request, jsonify
from googletrans import Translator as gTrans

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    args = request.args
    text = args["text"]
    lang = args["lang"]
    
    gTranslator = gTrans()
    gtranslation = gTranslator.translate(text , dest= lang)
         
    p = gTranslator.translate(text, dest=lang)
    
    return jsonify(phrase= gtranslation.text , pr= p.pronunciation)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
