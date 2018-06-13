from flask import Flask,render_template
from flask_googlecharts import GoogleCharts,BarChart

app = Flask(__name__)
charts = GoogleCharts(app)

my_chart = BarChart("my_chart", options={'title': 'My Chart'})

my_chart.add_column("string", "Competitor")
my_chart.add_column("number", "Hot Dogs")
my_chart.add_rows([["Matthew Stonie", 62],
                        ["Joey Chestnut", 60],
                        ["Eater X", 35.5],
                        ["Erik Denmark", 33],
                        ["Adrian Morgan", 31]])

@application.route("/")
def gchart():
	return render_template('googlechart.html',charts=charts)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',debug=True)
