import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open(r'C:\Users\Prikshit Batta\Downloads\finalized_model.sav','rb'))

@app.route('/predict')
def predict():
    # Extract the features from the URL query parameters
    vol_moving_avg = float(request.args.get('vol_moving_avg'))
    adj_close_rolling_med = float(request.args.get('adj_close_rolling_med'))
    print(vol_moving_avg)
    print(adj_close_rolling_med)
    # Make the prediction
    prediction = model.predict([[vol_moving_avg, adj_close_rolling_med]])
    predicted_volume = int(prediction[0])
    print(predicted_volume)
    # return (predicted_volume)
    # Return the prediction as a JSON response
    response = {'predicted_volume': predicted_volume}
    print(response )
    return jsonify(response)

# import requests

# url = 'http://localhost:5000/predict?vol_moving_avg=12345&adj_close_rolling_med=25'
# response = requests.post(url)

# print(response.text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)