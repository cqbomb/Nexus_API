from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import RadioField,SelectField,SelectMultipleField,SubmitField,validators

application = Flask(__name__)
application.secret_key = 'sdfsdfsdfsfwerw3342342sdfsdf'#可以用随机函数产生

class ContactForm(FlaskForm):
    radio = RadioField('请选择一个',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],\
                                    validators = [validators.AnyOf(['值1','值2','值3'],'请选中一个值')])
    select = SelectField('请选择一个选项',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],\
                                    validators = [validators.AnyOf(['值2'],'请选择第二项')])
    selectmultiple = SelectMultipleField('请选择多个选项',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],\
                                    validators = [validators.AnyOf([['值1','值2'],['值1','值3']],'只能选择前两项或第一和第三项')])
    submit = SubmitField('提交')

@application.route("/",methods=['GET','POST'])
def contract():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
    	if form.validate_on_submit() == False:
    		print('error')
    	else:
            value1 = request.args.post('radio')
            print(value1)
            print('输入成功')
            ok = True
    return render_template('select.txt',form=form,ok=ok)

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')