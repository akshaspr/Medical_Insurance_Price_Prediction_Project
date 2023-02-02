import pickle
import json
import config
import numpy as np

def load_model():
    with open(config.Model_FILE_PATH, 'rb') as f:
        model = pickle.load(f)


    with open(config.JSON_FILE_PATH, 'r') as f:
        json_data = json.load(f)

load_model(json_data)

# print(json_data['sex']['male'])
# final_array = np.array(['age', 'sex', 'bmi', 'children', 'smoker', 'region'], ndmin=2)

# age = 41
# sex = 'male'
# bmi = 28
# children = 2
# smoker = 'no'
# region = 'southwest'

# print(final_array[0][0])
# # final_array[1]]
# # final_array[2]
# # final_array[3]
# # final_array[4]
# # final_array[5]