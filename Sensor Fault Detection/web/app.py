from flask import Flask, render_template, jsonify, request, send_file, session
from src.exception import CustomException
from src.logger import logging as lg
import os,sys
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredicationPipeline

app = Flask(__name__)
app.secret_key = 'damodar'  # replace 'your secret key' with your actual secret key

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        
        return "Training Completed"
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/upload',methods=['POST','GET'])
def upload():
    try:
        if request.method == "POST":
            predication_pipeline = PredicationPipeline(request)
            predication_file_details = predication_pipeline.runpipeline()
            
            lg.info("predication completed . Downloading Predication File .")
            
            # Store the file path in the session
            session['file_path'] = predication_file_details.predication_file_path
            
            return render_template('upload_file.html',  prediction_text = 'Predicted Sensor :  {}'.format(predication_file_details.predication_file_text))

        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)

@app.route('/get_file')
def get_file():
    # Retrieve the file path from the session
    file_path = session.get('file_path', None)
    if file_path is not None:
        return send_file(file_path, as_attachment=True)
    else:
        return "No file available"

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)