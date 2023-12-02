from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application

## Route for a homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predictdatapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Company = request.form.get('Company'),
            TypeName = request.form.get('TypeName'),
            Ram=request.form.get('Ram'),
            Weight=float(request.form.get('Weight')),
            Touchscreen=request.form.get('Touchscreen'),
            IPS=request.form.get('IPS'),
            Screen_Resolution=request.form.get('Screen_Resolution'),
            size=float(request.form.get('size')),
            Cpu_Brand=request.form.get('Cpu_Brand'),
            HDD=int(request.form.get('HDD')),
            SSD=int(request.form.get('SSD')),
            Hybrid=int(request.form.get('Hybrid')),
            Flash_Storage=int(request.form.get('Flash_Storage')),
            Gpu_Brand=request.form.get('Gpu_Brand'),
            Os=request.form.get('Os')

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=int(np.exp(results[0])))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)