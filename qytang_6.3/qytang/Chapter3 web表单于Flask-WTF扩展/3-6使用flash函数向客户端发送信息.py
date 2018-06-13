from flask import Flask,request,render_template,flash
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
            flash('输入成功')####flash函数
            flash('<h1>success</h1>')####flash函数
            print('输入成功')
            ok = True
    return render_template('flash.txt',form=form,ok=ok)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')