import os
import sys
import dill  # Used for saving Python objects like pickle or joblib
import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(obj, path):
    """
    Saves a Python object to a file using dill.
    
    Parameters:
    obj: The Python object to be saved.
    path (str): The file path where the object should be saved.
    
    Raises:
    CustomException: If an error occurs during saving.
    """
    try:
        # Ensure the directory exists before saving the file
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the object to the specified file path
        with open(path, 'wb') as file:
            dill.dump(obj, file)
    
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train , X_test , y_test , models , param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model , para , cv = 3)
            gs.fit(X_train , y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
