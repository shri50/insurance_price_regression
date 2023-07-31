import pickle
import numpy as np
import json
from config import MODEL_PATH, IndVar_PATH


def get_model():
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)


def get_project_data():
    with open(IndVar_PATH, 'rb') as f:
        return json.load(f)


def predict_insurance_charges(age, sex, bmi, children, smoker, region):
    model = get_model()
    proj_d = get_project_data()
    test_data = np.zeros(len(proj_d['columns']))
    test_data[0] = age
    test_data[1] = sex
    test_data[2] = bmi
    test_data[3] = children
    test_data[4] = smoker
    region_index = proj_d['columns'].index(region)
    test_data[region_index] = 1
    print(test_data)
    predicted_charges = model.predict([test_data])
    print(f"Charges for Medical Insurance are : RS. {round(predicted_charges[0], 2)}")
    return round(predicted_charges[0], 2)
