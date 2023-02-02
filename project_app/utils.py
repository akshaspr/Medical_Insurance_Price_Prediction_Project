import pickle
import json
import config
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def load_model(self):
        with open(config.Model_FILE_PATH, 'rb') as f:
            self.model_data = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as g:
            self.json_data = json.load(g)

    def get_predicted_charges(self):
        self.load_model()
        
        final_array = np.array([age, sex, bmi, children, smoker, region])
        print('Final Test Array is : ', final_array)
        final_array[0] = self.age
        final_array[1] = self.json_data['sex'][self.sex]
        final_array[2] = self.bmi
        final_array[3] = self.children
        final_array[4] = self.json_data['smoker'][self.smoker]
        final_array[5] = self.json_data['region'][self.region]

        f_array = [float(i) for i in final_array]

        predicted_charges = self.model_data.predict([f_array])

        print(f'Predicted Charges for Insurance are : RS.{round(predicted_charges[0], 2)}')

if __name__ == "__main__":

    # age = 41
    # sex = 'male'
    # bmi = 28
    # children = 2
    # smoker = 'no'
    # region = 'southwest'

    age = eval(input('Enter your Age : '))
    sex = input('male/female : ')
    bmi = int(input('Enter your bmi : '))
    children = int(input('Enter No of childrens : '))
    smoker = input('Smoker >> yes/no : ')
    region = input('Type your region >> southeast/southwest/northwest/northeast : ')

    med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    med_ins.get_predicted_charges()