from flask import Flask, render_template, request
import os
import tumor_detection
import base64

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('page.html')
@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        f=request.files["img"]
        f.save('uploads/'+f.filename)
        result=tumor_detection.detect('uploads/'+f.filename)
        with open('uploads/'+f.filename, "rb") as img_file:
            input_file = base64.b64encode(img_file.read())
        input_file = input_file.decode('utf-8')
        os.remove('uploads/'+f.filename)
        input_file = "data:image/jpeg;base64, "+input_file
        return render_template('index.html',result="Result:"+result,input_file=input_file)
    else:
        return render_template('index.html')


if __name__ == "_main_":
    app.run()