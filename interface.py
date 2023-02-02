from flask import Flask, request, render_template
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)

# Load the pre-trained linear regression model
model = joblib.load('C:\Users\Aakash\Desktop\Velocity DS 10 Sept Batch\My Project\Toy Projects\Medical Charges Linear Model\project_app\Linear_Model.pkl')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve the inputs from the form
    age = float(request.form["age"])
    sex = request.form["sex"]
    bmi = float(request.form["bmi"])
    children = int(request.form["children"])
    smoker = request.form["smoker"]
    region = request.form["region"]
    

    # Use the model to make a prediction
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)
    
    # Format the prediction for display
    result = "${:,.2f}".format(prediction[0])
    
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
