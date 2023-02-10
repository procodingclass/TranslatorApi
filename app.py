from flask import Flask, request, jsonify
from googletrans import Translator as gTrans
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def welcome():
    args = request.args
    text = args["text"]
    srcLang = args["srcLang"]
    destLang = args["destLang"]
    if destLang == "Chinese":
        destLang = "ZH-CN"
    
    if srcLang == "Chinese":
        srcLang = "ZH-CN"
    
    gTranslator = gTrans()
    gtranslation = gTranslator.translate(text ,src=srcLang, dest= destLang)
         
    p = gTranslator.translate(text, dest= destLang)
    
    if p.pronunciation == None or p.pronunciation == text:
       p.pronunciation = gtranslation.text 
    return jsonify(phrase= gtranslation.text , pronunciation= p.pronunciation)



# CORS Headers 
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(debug=True)
