from flask import Flask, request, jsonify
from googletrans import Translator as gTrans
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    args = request.args
    text = args["text"]
    lang = args["lang"]
    if lang =="Chinese":
        lang = "ZH-CN"
    
    gTranslator = gTrans()
    gtranslation = gTranslator.translate(text , dest= lang)
         
    p = gTranslator.translate(text, dest=lang)
    
    if p.pronunciation == None or p.pronunciation == text:
       p.pronunciation = gtranslation.text 
    return jsonify(phrase= gtranslation.text , pronunciation= p.pronunciation)

@app.route('/language', method=['GET)
def detectLanguage():
    args = request.args
    text = args["text"]
    gTranslator = gTrans()
    lang = gTranslator.detect(text)                           
    return jsonify(language= lang)

# CORS Headers 
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(debug=True)
