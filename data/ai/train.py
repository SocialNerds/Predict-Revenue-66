from keras.callbacks import TensorBoard, Callback
import numpy as np
import includes.train_data as train_data
import includes.prediction_model as prediction_model
import includes.modelarg as modelarg

# Load model.
model = prediction_model.PredictionModel(modelarg.get_argument())

# Get train/test data.
values, labels = train_data.Data().get_train_data()

# Set batch.
batch_number = 5000
batch_train = []
len_values = len(values)
for w in range(len_values):
    batch_train.append([values[w], labels[w]])

    if (len(batch_train) == batch_number or len_values - w == 1):
        batch_train_values = np.array([item[0] for item in batch_train])
        batch_train_labels = np.array([item[1] for item in batch_train])
        print('Value', w + 1, 'from', len_values)
        # Train model.
        model.train(batch_train_values, batch_train_labels, 3)
        batch_train = []

# Save model.
model.save()
print('Saved model to disk')
