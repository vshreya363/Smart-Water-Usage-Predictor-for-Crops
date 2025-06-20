from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Create Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model and feature columns
model = joblib.load('water_prediction_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')  # Load saved feature columns from training

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the frontend
        data = request.get_json()

        # Convert input JSON to DataFrame
        input_data = pd.DataFrame([data])

        # Map crop names to standardized categories (used during training)
        crop_mapping = {
            "wheat": "crop_type_Wheat",
            "rice": "crop_type_Rice",
            "soybean": "crop_type_Soybean",
            "maize": "crop_type_Maize"
        }

        # Add one-hot encoded crop columns
        for crop in crop_mapping.values():
            input_data[crop] = 0  # Initialize all crops with 0

        # Set the correct crop column to 1
        if data.get("crop_type") in crop_mapping:
            input_data[crop_mapping[data["crop_type"]]] = 1
        else:
            return jsonify({'error': 'Invalid crop type provided.'}), 400

        # Drop the raw 'crop_type' column as it is no longer needed
        input_data.drop(columns=['crop_type'], inplace=True)

        # Ensure input data matches the feature columns used during training
        input_data = input_data.reindex(columns=feature_columns, fill_value=0)

        # Make the prediction
        predicted_water = model.predict(input_data)

        # Return the prediction result
        return jsonify({'predicted_water_usage': predicted_water[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
