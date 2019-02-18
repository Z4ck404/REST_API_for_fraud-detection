import numpy
import sys
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
#transform the vector to 1d vectors
def transorm (y):
    tab =[]
    for i in y :
        tab = tab +[i[0]]
    return tab
filename = 'trained_model.sav'
data = pd.read_csv("creditcard.csv")
def train_the_model (filename,data) :
    logistic_reg_model = LogisticRegression(solver = 'lbfgs')
    features = list(data.columns.values)[1:30]
    x = data.loc[:, features].values
    y = transorm(data.loc[:,['Class']].values)
    logistic_reg_model.fit(x, y)
    joblib.dump(logistic_reg_model, filename)
#Prediction the new transaction
def predict_new_transaction(vector_transaction):
    loaded_model = joblib.load(filename)
    return loaded_model.predict(vector_transaction)
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
print (predict_new_transaction(pred_vect(v)))
#print (v[28])