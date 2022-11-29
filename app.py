import os
from flask import Flask, render_template,request, flash, send_file, url_for, redirect
from rembg import remove

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        if "file" not in request.files:
            print("File not uploaded.")
            return
        file = request.files['file']
        imageName = file.filename

        image = file.read()
        uri, id = remove(image, imageName)
        flash("GET api Image ID: {}".format(id))
        return render_template('index.html')

    
@app.route('/get_image/<int:pid>')
def get_image(pid):
    filename = "removed_bg_downloaded/{}.png".format(pid)
    return send_file(filename, mimetype='image/png')


if __name__ == "__main__":
#    app.run(host='127.0.0.1', port=8888)
    #http_server = WSGIServer(('127.0.0.1', 8888), app)
    #http_server.serve_forever()
    app.run()    
