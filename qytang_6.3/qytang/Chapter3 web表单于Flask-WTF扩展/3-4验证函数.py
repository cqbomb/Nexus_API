from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import TextField,IntegerField,PasswordField,RadioField,TextAreaField,BooleanField,DateField,SubmitField,validators

application = Flask(__name__)
application.secret_key = 'sdfsdfsdfsfwerw3342342sdfsdf'#可以用随机函数产生

class ContactForm(FlaskForm):
    name = TextField('姓名',[validators.Required('姓名必须输入')])
    
    email = TextField('Email',[validators.Required('请输入Email'),\
                               validators.Email('请输入正确的Email格式')])
    
    ip = TextField('IP',[validators.Required('请输入IP地址'),\
                         validators.IPAddress(message = '请输入正确的IPv4地址格式')])
    
    password1 = PasswordField('密码',[validators.Required('请输入密码')])
    
    password2 = PasswordField('确认密码',[validators.Required('请输入确认密码'),\
                                          validators.EqualTo('password1','两次输入的密码不一致')])
    
    value = TextField('电子邮件',[validators.Email('请输入正确的Email格式'),validators.optional()])
    
    url = TextField('URL',[validators.URL(message='请输入正确的URL格式'),validators.optional()])
    
    regexpValue = TextField('正则表达式',[validators.Regexp('^[a-z]{3}-[1-9]{3}$',message='格式错误，正确格式abc-123'),validators.optional()])
    
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
    return render_template('validate.txt',form=form,ok=ok)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')