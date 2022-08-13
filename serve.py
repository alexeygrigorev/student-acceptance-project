import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = './artifacts/pipeline.bin'


with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)


app = Flask('serve')


@app.route('/predict', methods=['POST'])
def predict():
    student = request.get_json()

    y_pred = pipeline.predict_proba(student)[0, 1]
    admission = y_pred >= 0.5

    result = {
        'admission_probability': float(y_pred),
        'admission': bool(admission)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)