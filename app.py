from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Misalnya, load model
model = tf.keras.models.load_model('path_to_model/diabetes_classification_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Ambil data dari request POST
    prediction = model.predict(data["input"])  # Lakukan prediksi
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Port dari Railway
    app.run(host="0.0.0.0", port=port)
