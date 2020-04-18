import os
import subprocess
import platform
import flask
from flask import Flask,request
from flask import render_template,send_file
from werkzeug.utils import secure_filename
import shutil
import time

app = flask.Flask(__name__)

# Check the Route Once
@app.route('/seat', methods = ["GET"])
def mainPage():
    #return app.send_static_file('seat.html')
    return render_template('seat.html')

@app.route('/submit',methods=["POST"])
def submit():
    ts = str(int(time.time()))
    src="./app"
    dest = src + ts
    shutil.copytree(src, dest)
    file1 = request.files['file1']
    file2 = request.files['file2']
    file3 = request.files['file3']
    file1.save(os.path.join(dest+'/',secure_filename(file1.filename)))
    file2.save(os.path.join(dest+'/',secure_filename(file2.filename)))
    file3.save(os.path.join(dest+'/',secure_filename(file3.filename)))

    command = "python create_groups.py {} {} {} > out.txt".format(secure_filename(file1.filename),secure_filename(file2.filename),secure_filename(file3.filename))
    p = subprocess.Popen(command,cwd=dest+"/")
    p.wait()

    shutil.make_archive(dest + '/Rooms','zip',dest + '/Rooms')
    """if(platform.system() == "Windows"):
        print("compress-archive called")
        p = subprocess.Popen("Compress-Archive Rooms Rooms.zip",shell=True,cwd=dest+'/')
    else:
        print("tar is called")
        p = subprocess.Popen("tar -czvf Rooms.zip Rooms",shell=True,cwd=dest+'/')
    p.wait()"""
    return dest + "/Rooms.zip"

@app.route('/file',methods=["GET"])
def sendFile():
    return send_file(request.args.get('filename'),as_attachment="Rooms.zip")



if __name__ == '__main__':
    app.run(debug = True,port=9000)