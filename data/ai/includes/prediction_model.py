import numpy as np
from pathlib import Path
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout

class PredictionModel(Sequential):
    """ Prediction model manipulation """

    # Indicates the number of input features.
    FEATURES = 146

    # Where to store the model weights. Using this path
    # since this class is used outside of this folder.
    MODELPATH = 'models/'
 
    def __init__(self, model_id):
        """
        Get specific model.

        Attributes
        ----------
        model_id : int
            The model id to initialize.
        """
        # Create model.
        super().__init__()

        self.model_id = model_id

        # Initialize layers.
        self.initialize_model()

        # Get weights, if any.
        if (self.model_exists()):
            self.load_weights()

    def model_exists(self):
        """
        Get if this model exists. Hence it is trained.

        Returns
        -------
        boolean
            True if module exists.
        """
        model_weights = Path(self.MODELPATH + 'model_' + str(self.model_id) + '.h5')
        if (model_weights.is_file()):
            return True
        else:
            return False
    
    def load_weights(self):
        """
        Load weights to model.
        """
        # Load weights into new model.
        super().load_weights(self.MODELPATH + 'model_' + str(self.model_id) + '.h5')
    
    def initialize_model(self):
        """
        Initialize model.
        """
        # Create model.
        super().add(Dense(1024, input_dim=self.FEATURES, activation='tanh'))
        super().add(Dropout(0.1))
        super().add(Dense(1024, activation='tanh'))
        super().add(Dropout(0.1))
        super().add(Dense(1024, activation='tanh'))
        super().add(Dropout(0.1))
        super().add(Dense(1, activation='relu'))
        super().compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    def train(self, values, labels, n_epochs=2):
        """
        Train the model.

        Attributes
        ----------
        values : numpy.array
            Values to train for.
        labels : numpy.array
            Labels to train against.
        epochs : int
            How many epochs.
        """
        super().fit(values, labels, epochs=n_epochs)
    
    def save(self):
        """
        Save model weights.
        """
        super().save_weights(self.MODELPATH + 'model_' + str(self.model_id) + '.h5')
