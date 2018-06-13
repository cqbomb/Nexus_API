# -*- coding: utf-8 -*-  
from flask import Flask, jsonify, render_template, request  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
# 主页面  
    return render_template("ajax_test_1.html")  
     
@app.route('/add')  
def add_numbers():  
    cmd = request.args.get('cmd')  
    return jsonify(result = cmd)  
     
if __name__=="__main__":  
    app.run(host = "0.0.0.0", debug = True) 