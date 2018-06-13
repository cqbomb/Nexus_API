# -*- coding: utf-8 -*-  
from flask import Flask, jsonify, render_template, request  
import datetime

app = Flask(__name__)  
  
@app.route("/")  
def index():  
# 主页面  
    return render_template("ajax_test_2.html")  
     
@app.route('/add')  
def add_numbers():  
    cmd = request.args.get('cmd')  
    return jsonify(result = datetime.datetime.now().strftime( '%y-%m-%d %I:%M:%S %p'))  
     
if __name__=="__main__":  
    app.run(host = "0.0.0.0", debug = True) 