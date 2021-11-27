from flask import Flask, render_template, request, redirect, url_for, Response
import os
from os.path import join, dirname, realpath

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL
#@app.route('/')
#def index():
     # Set The upload HTML template '\templates\index.html'
  #  return render_template('index.html')
    #return "<p>Hello, World!</p>"


# Get the uploaded files
#@app.route("/", methods=['POST'])
#def uploadFiles():
      # get the uploaded file
 #     uploaded_file = request.files['file']
 #     if uploaded_file.filename != '':
 #          file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
 #          uploaded_file.save(file_path)
          # save the file
 #     return redirect(url_for('index'))
  
  
# Get http method
@app.route("/", methods=['GET'])
def get_method():
    with open("static/files/prediction.csv") as fp:
         csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=prediction.csv"})
    #return render_template('index.html')
    
    


if (__name__ == "__main__"):
     app.run(host='0.0.0.0',port = 10000)