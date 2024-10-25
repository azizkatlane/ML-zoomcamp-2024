import pickle

dv = 'dv.bin'
model1 = 'model1.bin'

with open(dv , 'rb') as vectorizer:
    dv = pickle.load(vectorizer)

with open(model1 , 'rb') as moddel:
    model = pickle.load(moddel)

customer= {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform([customer])


pred = model.predict_proba(X)[0,1]

print(pred)