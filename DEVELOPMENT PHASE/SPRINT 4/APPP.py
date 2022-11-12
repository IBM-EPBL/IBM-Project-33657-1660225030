from flask import Flask, render_template,request   
import numpy as np
import pandas
import pickle

app = Flask(__name__)
model = pickle.load(open(r'MYMODEL.pkl','rb'))
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
    
@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        project_name=request.form['full-name']
        print(project_name)
    return render_template("predict.html",project_name=project_name)

@app.route("/success",methods=['POST','GET'])
def evaluate():
    input_feature = [int(x) for x in request.form.values()]
    print(input_feature)
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self Employed', 'Applicant Income', 'Coapplicant Income', 'Loan Amount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'] 
    data = pandas.DataFrame(input_feature, columns=names)
    print(data)
    prediction=model.predict(data)
    print(prediction)
    prediction = int(prediction) 
    print(type(prediction))
    loan=1
    if (prediction == 0):
        loan=0
        return render_template("success.html",result = "Loan will Not be Approved",loan=loan)
    else:
        return render_template("success.html",result = "Loan will be Approved",loan=loan)
    return render_template("success.html")

    
if __name__ == "__main__":
    app.run(debug=True)