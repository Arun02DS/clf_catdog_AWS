from flask import Flask,request,jsonify,render_template
import os,sys
from flask_cors import CORS,cross_origin
from catdog_src.prediction import CatDog
from catdog_src.logger import logging
from catdog_src.exception import CatDogException
from catdog_src.utils import decodeImage,encodeImageIntoBase64


#Setting environment variables to ensure the correct UTF-8 encoding. 
#This is often done to avoid potential encoding issues when working with strings.
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=CatDog(self.filename)

@app.route("/",methods=['GET'])
@cross_origin()

def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
@cross_origin()

def PredictRoute():
    image=request.json['image']
    decodeImage(image,clApp.filename)
    result=clApp.classifier.predictioncatdog()
    return jsonify(result)


if __name__=="__main__":
    try:
        clApp=ClientApp()
        app.run(host='0.0.0.0',port=8080)
    except Exception as e:
        raise CatDogException(e,sys)




