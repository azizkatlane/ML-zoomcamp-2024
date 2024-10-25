import pickle
from flask import Flask, jsonify, request


dv = 'dv.bin'
model1 = 'model1.bin'

with open(dv , 'rb') as vectorizer:
    dv = pickle.load(vectorizer)

with open(model1 , 'rb') as moddel:
    model = pickle.load(moddel)

app=Flask('homew5')

@app.route('/predict' , methods=['POST'])
def predict():

    customer = request.get_json()

    X = dv.transform([customer])

    y_pred = model.predict_proba(X)[0,1]

    result={
        'probability' : float(y_pred)
    }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True , host='0.0.0.0' , port=5353)