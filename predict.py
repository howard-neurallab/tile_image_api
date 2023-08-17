import numpy as np

from flask import Flask, jsonify, request

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
#model = load_model('FV.h5')




app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return jsonify(error="Please try again. The Image doesn't exist")

    file = request.files.get('file')
    img_bytes = file.read()
    img_path = dir_path+'/upload_images/testdddddddd.jpg'
    curpath = os.path.abspath(os.curdir)
    print(f"Current path is: {curpath}")
    print(f"Trying to open:{os.path.join(curpath, img_path)}")
    with open(img_path, "wb") as img:
        img.write(img_bytes)
    result = "result"
    return jsonify(prediction=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)