import os
import sys
import dill  # Used for saving Python objects like pickle or joblib
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
