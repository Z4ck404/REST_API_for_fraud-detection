# REST_API_for_fraud-detection
A logistic regression model that detects the fraud in online transactions that can be acced with a REST API

## The Trained model 

Logistic regression is one of the most popular machine learning algorithms for binary classification. This is because it is a simple algorithm that performs very well on a wide range of problems.
The logistic regression model takes real-valued inputs and makes a prediction as to the probability of the input belonging to the default class (class 0)

## The Data 
Three models trained to label anonymized credit card transactions as fraudulent or genuine. Dataset from [kaggle](https://www.kaggle.com/sarathchandra/credit-card-fraud-detection-99-accuracy/comments#144915).

## The API acces points
to be able to use the api , you need first install the requirements 
```
pip install flask
```
Then test the application by runing the code : 
```
python api.py
```
the app will be running on local host port 5000 
with the endpoints : 
### /api/v0/verify 
This endpoint get a JSON object in a  post method , that represents the new transaction 
```
 {
 "V1" : -1.3598071336738,
 "V2" : -0.0727811733098497,
 "V3" : 2.53634673796914,
 "V4" : 1.37815522427443,
 "V5" : -0.338320769942518,
 "V6" : 0.462387777762292,
 "V7" : 0.239598554061257,
 "V8" : 0.0986979012610507,
 "V9" : 0.363786969611213,
 "V10" : 0.0907941719789316,
 "V11" : -0.551599533260813,
 "V12" : -0.617800855762348,
 "V13" : -0.991389847235408,
 "V14" :  -0.311169353699879,
 "V15" : 1.46817697209427,
 "V16" : -0.470400525259478,
 "V17" : 0.207971241929242,
 "V18" : 0.0257905801985591,
 "V19" : 0.403992960255733,
 "V20" : 0.251412098239705,
 "V21" : -0.018306777944153,
 "V22" : 0.277837575558899,
 "V23" : -0.110473910188767,
 "V24" : 0.0669280749146731,
 "V25" : 0.128539358273528,
 "V26" : -0.189114843888824,
 "V27" : 0.133558376740387,
 "V28" : -0.0210530534538215,
 "Amount" : 149.62
 }
```

