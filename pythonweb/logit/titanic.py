from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/',methods=["GET"])
def main():
    return render_template(('titanic/input.html'))

@app.route('/result',methods=["POST"])
def result():
    model = joblib.load("c:/data/titanic/titanic_logit.model")
    sex = request.form["sex"]
    if sex == "male":
        male = 1
        female = 0
        gender = "남성"
    else :
        male = 0
        female = 1
        gender = "여성"

    pclass = request.form["pclass"]
    if pclass == "1":
        pclass1 = 1
        pclass2 = 0
        pclass3 = 0
    elif pclass == "2":
        pclass1 = 0
        pclass2 = 1
        pclass3 = 0
    elif pclass == "3":
        pclass1 = 0
        pclass2 = 0
        pclass3 = 1

    age = int(request.form["age"])
    sibsp = int(request.form["sibsp"])

    test_set = np.array([pclass1, pclass2, pclass3, male, female, age, sibsp]).reshape(1,7)
    rate = model.predict_proba(test_set)
    if rate[0][-1]>=0.5:
        result="생존"
    else:
        result="사망"
    return render_template("titanic/result.html",
                           rate="{:.2f}%".format(rate[0][-1]*100),
                           result=result, sex=gender, pclass=pclass, age=age, sibsp=sibsp)

if __name__ == '__main__':
    app.run(port=80, threaded=False)