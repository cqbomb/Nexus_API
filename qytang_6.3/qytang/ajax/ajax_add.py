# -*- coding: utf-8 -*-  
from flask import Flask, jsonify, render_template, request  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
# 主页面  
    return render_template("ajax.html")  
     
@app.route('/add')  
def add_numbers():  
    a = request.args.get('a', 0, type=int)  
    b = request.args.get('b', 0, type=int)  
    return jsonify(result = a + b*200)  
     
if __name__=="__main__":  
    app.run(host = "0.0.0.0",debug = True) 