from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import TextField,IntegerField,TextAreaField,BooleanField,DateField,SubmitField,validators

application = Flask(__name__)
application.secret_key = 'sdfsdfsdfsfwerw3342342sdfsdf'#可以用随机函数产生

class ContactForm(FlaskForm):
	name = TextField('姓名',[validators.Required('姓名必须输入')])
	age = IntegerField('年龄',[validators.Required('姓名必须输入年龄'),\
							   validators.NumberRange(10,30,'年龄必须在10到30之间')])
	birth = DateField('出生日期',[validators.Required('必须输入出生日期[YYYY-MM-DD]')])
	isStudent = BooleanField('是否为学生')
	resume = TextAreaField('简历',[validators.Length(10,200,'简历长度必须在10-200个字符之间')])
	submit = SubmitField('提交')

@application.route("/",methods=['GET','POST'])
def contract():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
    	if form.validate_on_submit() == False:
    		print('error')
    	else:
    		print('输入成功')
    		ok = True
    if ok == True:
        return render_template('mytestok.txt',name=form.name.data,age=form.age.data,birth=form.birth.data,ok=ok)
    elif ok == False:
        return render_template('mytestnook.txt',form=form)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')