# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Step 1: Load Dataset
data = pd.read_csv(r"C:\Users\apoor\OneDrive\Desktop\Sihs\ML Model\sample_data.csv")

# Step 2: Explore and preprocess the data
print("Initial Data:")
print(data.head())

# Rename columns for consistency
columns_mapping = {
    "Temperature (\u00b0C)": "temperature",
    "Humidity (%)": "humidity",
    "Soil Moisture (%)": "soil_moisture",
    "Rainfall (mm)": "rainfall",
    "Crop Type": "crop_type",
    "Water Usage (liters)": "water_usage"
}
data.rename(columns=columns_mapping, inplace=True)
print("Renamed Columns:", data.columns)

# Handle missing values
data = data.dropna()

# Encode categorical variables (One-Hot Encoding for 'crop_type')
data = pd.get_dummies(data, columns=['crop_type'], drop_first=True)

# Split into features (X) and target (y)
X = data.drop(columns=['Date', 'water_usage'], errors='ignore')  # Drop 'Date' and target
y = data['water_usage']

# Save feature column names for prediction consistency
feature_columns = X.columns
joblib.dump(feature_columns, 'feature_columns.pkl')

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'RMSE: {rmse}')

# Step 5: Save the model
joblib.dump(model, 'water_prediction_model.pkl')

# Step 6: Example prediction
# Load new data (replace with your actual file path)
try:
    new_data = pd.read_csv(r"C:\Users\apoor\OneDrive\Desktop\Sihs\ML Model\new_data.csv")
except FileNotFoundError:
    print("new_data.csv not found. Creating example data for testing...")
    new_data = pd.DataFrame({
        "temperature": [25],
        "humidity": [60],
        "soil_moisture": [30],
        "rainfall": [10],
        "crop_type": ["Wheat"]
    })

# Preprocess new data (Apply same transformations as training)
new_data = pd.get_dummies(new_data, columns=['crop_type'], drop_first=True)

# Ensure the new data has the same columns as training data
new_data = new_data.reindex(columns=feature_columns, fill_value=0)

# Predict water usage
predicted_water = model.predict(new_data)
print(f'Predicted Water Usage: {predicted_water} liters')
