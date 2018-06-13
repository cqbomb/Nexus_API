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
    form.age.data = 18#设置默认值
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('输入成功')
            print('姓名:',form.name.data)
            print('年龄:',form.age.data)
            print('出生日期:',form.birth.data)
            if form.name.data == 'John':#替换客户输入内容
                form.name.data = 'Joe'
            ok = True
    return render_template('simple.txt',form=form,ok=ok)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')