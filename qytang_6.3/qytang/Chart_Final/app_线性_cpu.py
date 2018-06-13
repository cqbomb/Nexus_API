from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
import random
app = Flask(__name__)
 
@app.route("/")
def chart():
	hours = []
	for i in range(1,25):
		hours.append(str(i)+'点')
	labels = hours
	cpus = []
	for i in range(1,25):
		cpus.append(random.randint(1,100))
	values = cpus
	return render_template('chart_线性_cpu.html', values=values, labels=labels)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000,debug=True)