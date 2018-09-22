import numpy as np
import includes.train_data as train_data
import includes.prediction_model as prediction_model
import includes.modelarg as modelarg

# Load model.
model = prediction_model.PredictionModel(modelarg.get_argument())

# Load test data.
values = np.array(train_data.Data().get_test_data())

# Predictions.
predictions = []

# Create sliding window arrays.
len_values = len(values)
for w in range(len_values):
    predictions.append(model.predict(values[w].reshape(1, -1)))

# Keep last 3 days.
predictions = np.array(predictions[-72:]).flatten().reshape(-1, 24).astype(int)
print(predictions)
