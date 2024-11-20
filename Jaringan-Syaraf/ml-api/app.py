from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load model and preprocessing tools
model = load_model("jadwal_model.h5")
scaler = StandardScaler()  # Load your scaler object if previously saved
encoder_waktu = LabelEncoder()
encoder_ruangan = LabelEncoder()

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Parse input JSON
    data = request.json
    kode_mk = data['Kode_Mk']
    id_dosen = data['Id_Dosen']
    
    # Preprocess input
    kode_mk_encoded = LabelEncoder().fit_transform([kode_mk])[0]
    input_data = scaler.transform([[kode_mk_encoded, id_dosen]])
    
    # Perform prediction
    predictions = model.predict(input_data)
    slot_hari = int(round(predictions[0, 0]))
    slot_waktu = encoder_waktu.inverse_transform([int(round(predictions[0, 1]))])[0]
    ruangan = encoder_ruangan.inverse_transform([int(round(predictions[0, 2]))])[0]
    
    # Return response
    return jsonify({
        "Slot_Hari": slot_hari,
        "Slot_Waktu": slot_waktu,
        "Ruangan": ruangan
    })

if __name__ == "__main__":
    app.run(debug=True)
