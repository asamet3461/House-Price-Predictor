from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Uploading the model
import os
model_path = os.path.join('model', 'prediction_model.pickle')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    room = int(request.form['room'])
    parking = int(request.form['parking'])
    warehouse = int(request.form['warehouse'])
    elevator = int(request.form['elevator'])
    address = request.form['address']

    address_features = [
        'Address_Andisheh', 'Address_Central Janatabad', 'Address_East Ferdows Boulevard',
        'Address_Farmanieh', 'Address_Gheitarieh', 'Address_Jeyhoon', 'Address_Niavaran',
        'Address_Ostad Moein', 'Address_Pardis', 'Address_Pasdaran', 'Address_Persian Gulf Martyrs Lake',
        'Address_Pirouzi', 'Address_Punak', 'Address_Saadat Abad', 'Address_Salsabil',
        'Address_Shahr-e-Ziba', 'Address_Shahrake Gharb', 'Address_Shahrake Qods',
        'Address_Shahran', 'Address_Southern Janatabad', 'Address_West Ferdows Boulevard',
        'Address_other', 'Address_Shahrake Mahestan'
    ]

    address_dict = {a: 0 for a in address_features}
    address_dict[address] = 1

    final_input = [area, room, parking, warehouse, elevator] + list(address_dict.values())
    log_prediction = model.predict([final_input])[0]
    prediction = np.expm1(log_prediction)

    prediction_text = f"Predicted house price: {round(prediction, 2)} USD"

    return render_template('index.html',
                           prediction_text=prediction_text,
                           area=area,
                           room=room,
                           parking=parking,
                           warehouse=warehouse,
                           elevator=elevator,
                           address=address)


if __name__ == '__main__':
    app.run(debug=True)
