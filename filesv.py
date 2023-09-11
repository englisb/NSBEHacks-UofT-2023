from flask import Flask, request
import sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{file.filename}")
        txt = srec.spchTotxt(file.filename)