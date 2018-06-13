"""
<form>

</form>

1.生成表单组件的HTML代码
2.后台验证
3.向WEB端返回错误信息
4.在WEB页面上显示错误信息
5.防止跨域访问

安装第三方模块
pip3 install flask-wtf
"""
from flask import Flask,request,render_template
from flask_wtf import FlaskForm

from wtforms import TextField,SubmitField,validators

application = Flask(__name__)
application.secret_key = 'sdfsdfsdfsfwerw3342342sdfsdf'#可以用随机函数产生

class ContactForm(FlaskForm):
	firstname = TextField('姓名',[validators.Required('姓名必须输入')])
	submit = SubmitField('提交')

@application.route("/",methods=['GET','POST'])
def contract():
    form = ContactForm()
    if request.method == 'POST':
    	if form.validate_on_submit() == False:
    		print(form.firstname.errors)
    		print('error')
    return render_template('first.txt',form=form)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')