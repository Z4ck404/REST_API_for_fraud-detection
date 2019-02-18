import flask
from flask import request, jsonify
import numpy
import json
import sys
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
app = flask.Flask(__name__)
app.config["DEBUG"] = True
def pred_vect(v):
    vect = {}
    j = 1
    for i in range (0,28):
        ind = "V"+str(j)
        vect [ind] = v[i]
        j = j+1
    vect ["Amount"] = v[28]
    return pd.DataFrame([vect])
v = [-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,149.62]
filename = 'trained_model.sav'
#post a json object to see the prediction for it :
@app.route('/foo', methods=['POST']) 
def foo():
    print (request)
    #return request
    return json.dumps(request.json)
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return jsonify(content)
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Fraud Detection API : IOO</h1>
<p> A POC for the use of Machine learning to detect Credit Cards Frauds.</p>'''

@app.route('/api/v0/verify', methods=['GET','POST'])
def predict_new_transaction():
    vec = pd.DataFrame([request.json])
    loaded_model = joblib.load(filename)
    res = str(loaded_model.predict(vec)[0])
    result = [
    {'id': 0,
     'prediction': res} ]
    return jsonify(result)
@app.route('/api/v0/test', methods=['GET','POST'])
def predict_test():
    loaded_model = joblib.load(filename)
    res = str(loaded_model.predict(pred_vect(v))[0])
    result = [
    {'id': 0,
     'prediction': res} ]
    return jsonify(result)
@app.route('/api/v0/info', methods=['GET'])
def info():
    result = [
        {
            'Author' : 'IOO',
            'description' : 'A fraud detection model using a kaggle dataset',
        }
    ]
    return jsonify(result)  
app.run()

