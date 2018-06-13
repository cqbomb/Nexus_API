from gevent import monkey
monkey.patch_all()
from multiprocessing.pool import ThreadPool
from flask import Flask, render_template, session, request, make_response
from flask_debugtoolbar import DebugToolbarExtension
from .models.module1 import Value1#相对导入绝对路径为qytang/module1
from .models.ALL_AUTO import vsphere_all_auto,config_asa
from .models.ALL_AUTO_N9K import ALL_AUTO_N9K
from .models.vSphere_GET_VMList import get_vm_id
from .models.vSphere_GET_PortGroupList import get_network_id
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO, emit

from .models.vSphere_Get_Token import get_token_url

import random
import time
from flask_wtf import FlaskForm
from wtforms import RadioField,SelectField,SelectMultipleField,SubmitField,validators
from random import randint
pool = ThreadPool(processes=5)

class ContactForm(FlaskForm):
    opt = RadioField('请选择操作方式',choices = [('preconfig','preconfig'),('getconfig','getconfig')],\
                                  validators = [validators.AnyOf(['preconfig','getconfig'],'请选中一个值')])
    rack = RadioField('请选择一个机架',choices = [('Rack1','Rack1'),('Rack2','Rack2'),('Rack3','Rack3')],\
                                  validators = [validators.AnyOf(['Rack1','Rack2','Rack3'],'请选中一个值')])
    submit = SubmitField('提交')

class CloudContactForm(FlaskForm):
    opt = RadioField('请选择CPU',choices = [('cpu1','1核CPU'),('cpu2','2核CPU')],\
                                  validators = [validators.AnyOf(['1核CPU','2核CPU'],'请选中一个值')])
    rack = RadioField('请选择内存',choices = [('G1','1G内存'),('G2','2G内存')],\
                                  validators = [validators.AnyOf(['1G内存','2G内存'],'请选中一个值')])
    submit = SubmitField('提交')


from gevent import monkey
monkey.patch_all()

def function1(x):
    return str(x) + "step"

application = Flask(__name__, 
                    instance_relative_config=True
                    )#获取instance目录内config.py的配置

application.config['SECRET_KEY'] = 'secret!'

application.config.from_object('config')#读取config.py内的配置
application.config.from_pyfile('config.py')#读取instance/config.py内的配置，后加载优先

#可以通过application.config['XXXX']的方式读取config.py内的值

application.debug = application.config['DEBUG']#激活debug

#toolbar = DebugToolbarExtension(application)#产生Toolbar

bootstrap = Bootstrap(application)#激活bootstrap模板

socketio = SocketIO(application,\
                    async_mode='gevent'
                    )

def getconfig(rack):
    return 'getconfig ' + rack

def preconfig(rack):
    return 'preconfig ' + rack


#静态路由
@application.route("/")
def index():
    return render_template('index.html',text = "Flask测试")

@application.route("/webconsole/<name>")
def webconsole(name):
    try:
        token_result = get_token_url(name)
        return render_template('vSphere_Web_Console.html',text = token_result)
    except:
        return render_template('wait_1_min.html')

@application.route('/socketio_simple')
def socketio_simple():
    form = ContactForm()
    return render_template('socketio_simple.html',text = "WINSOCKET测试", form = form)

@socketio.on('client_event',namespace='/socketio_simple/test1')
def client_msg(msg):
    if msg['data'][1] == 'getconfig':
        for i in range(4):
            emit('server_response', {'data': getconfig(msg['data'][0])})
            time.sleep(1)
    elif msg['data'][1] == 'preconfig':
        emit('server_response', {'data': preconfig(msg['data'][0])})
    
@socketio.on('connect_event',namespace='/socketio_simple/test1')
def connected_msg(msg):
    emit('server_response', {'data': msg['data'][0]})


@application.route('/simple_cloud')
def simple_cloud():
    form = CloudContactForm()
    return render_template('simple_cloud.html', text="简易云实战", form=form)


@socketio.on('client_event', namespace='/socketio_simple/simple_cloud')

def simple_cloud_client_msg(msg):
    if (msg['data'][0] + msg['data'][1]) == 'G1cpu1':
        temp_no = 1
    elif (msg['data'][0] + msg['data'][1]) == 'G2cpu1':
        temp_no = 2
    elif (msg['data'][0] + msg['data'][1]) == 'G1cpu2':
        temp_no = 3
    elif (msg['data'][0] + msg['data'][1]) == 'G2cpu2':
        temp_no = 4

    while True:
        VLANID = randint(1,100)
        VMID = get_vm_id()
        NETID = get_network_id()
        if VLANID in VMID:
            continue
        if VLANID in NETID:
            continue
        break
    emit('server_response', {'data': '开始配置N9K网络！'})
    # ALL_AUTO_N9K(VLANID)
    emit('server_response', {'data': 'N9K网络配置完毕！'})
    emit('server_response', {'data': '开始配置ASA！'})
    # config_asa(VLANID)
    emit('server_response', {'data': 'ASA配置完毕！'})
    emit('server_response', {'data': '开始配置vSphere虚拟机'})
    pool.apply_async(vsphere_all_auto, args=(temp_no,VLANID))
    emit('server_response', {'data': 'vSphere虚拟机配置结束！'})
    emit('server_response', {'data': '全部配置配置完毕！可能需要再等待3-4分钟直到虚拟机配置结束'})
    webconsoleurl = 'http://172.16.1.110:5000/webconsole/CentOS_' + str(VLANID)
    a_url = '<a href="' + webconsoleurl + '" target="_blank">访问WEB Console</a>'
    emit('server_response', {'data': a_url})
    #emit('server_response', {'data': msg['data'][0] + msg['data'][1]})
    # if msg['data'][1] == 'getconfig':
    #     for i in range(4):
    #         emit('server_response', {'data': getconfig(msg['data'][0])})
    #         time.sleep(1)
    # elif msg['data'][1] == 'preconfig':
    #     emit('server_response', {'data': preconfig(msg['data'][0])})


@socketio.on('connect_event', namespace='/socketio_simple/simple_cloud')
def simple_cloud_connected_msg(msg):
    emit('server_response', {'data': msg['data'][0]})

@application.route("/bs")
def bs():
    return render_template('bs.html',name='qytang')

@application.route("/import_and_value_test")
def import_and_value_test():
    return render_template('import_and_value_test.html',\
                            text = "参数导入与读取配置参数",\
    						template_name1=application.config['MAIL_FROM_EMAIL'],\
    						template_name2=application.config['USERNAME'],\
    						template_name3=Value1)

@application.route("/chart/<shape>")
def chart(shape):
    if shape == 'line':
        labels = ["January","February","March","April","May","June","July","August"]
        values = [10,9,8,7,6,4,7,8]
        return render_template('chart_线性.html', text = "乾颐堂Chart测试（线性）", values=values, labels=labels)
    elif shape == 'linecpu':
        hours = []
        for i in range(1,25):
            hours.append(str(i)+'点')
        labels = hours
        cpus = []
        for i in range(1,25):
            cpus.append(random.randint(1,100))
        values = cpus
        return render_template('chart_线性_cpu.html', text = "乾颐堂Chart测试（线性CPU）", values=values, labels=labels)
    elif shape == 'column':
        labels = ["January","February","March","April","May","June","July","August"]
        values = [10,9,8,7,6,4,7,8]
        return render_template('chart_柱状.html', text = "乾颐堂Chart测试（柱状）", values=values, labels=labels)  
    elif shape == 'pie':
        labels = ["January","February","March","April","May","June","July","August"]
        values = [10,9,8,7,6,4,7,8]
        colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
        return render_template('chart_饼状.html', text = "乾颐堂Chart测试（饼状）", set=zip(values, labels, colors))     

@application.route("/matplotlib_simple")
def matplotlib_simple():
    return render_template('matplotlib_simple.html',text='最简单图片')

@application.route("/matplotlib_cpu")
def matplotlib_cpu():
    return render_template('matplotlib_cpu.html',text='CPU利用率')

@application.route("/simple.png")
def simple():
    import datetime
    from io import BytesIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

@application.route("/cpu.png")
def CPU():
    import matplotlib
    from qytang.static.final_0_data import R1_CPU_TIME,R2_CPU_TIME
    from io import BytesIO
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    fig=Figure()

    ax1=fig.add_subplot(211)
    import matplotlib.dates as mdate
    #ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax1.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))#设置时间标签显示格式


    import matplotlib.ticker as mtick
    ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    X1 = []
    Y1 = []

    for (time,cpu) in R1_CPU_TIME:
        X1.append(time)
        Y1.append(cpu)

    font_path = matplotlib.font_manager.FontProperties(fname=r'C:\Users\Administrator\PycharmProjects\Nexus_API\qytang_6.3\qytang\qytang\static\simhei.ttf')

    ax1.set_title(u'R1 CPU利用率',fontproperties=font_path)
    ax1.set_xlabel(u'采集时间',fontproperties=font_path)
    ax1.set_ylabel(u'CPU利用率',fontproperties=font_path)
    R1, = ax1.plot(X1,Y1,linestyle='solid',color='r',label='R1')
    ax1.legend(loc='upper left')

    ax2=fig.add_subplot(212)
    import matplotlib.dates as mdate
    #ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax2.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))#设置时间标签显示格式


    import matplotlib.ticker as mtick
    ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    X2 = []
    Y2 = []

    for (time,cpu) in R2_CPU_TIME:
        X2.append(time)
        Y2.append(cpu)

    font_path = matplotlib.font_manager.FontProperties(fname=r'C:\Users\Administrator\PycharmProjects\Nexus_API\qytang_6.3\qytang\qytang\static\simhei.ttf')

    ax2.set_title(u'R2 CPU利用率',fontproperties=font_path)
    ax2.set_xlabel(u'采集时间',fontproperties=font_path)
    ax2.set_ylabel(u'CPU利用率',fontproperties=font_path)
    R2, = ax2.plot(X2,Y2,linestyle='solid',color='r',label='R2')
    ax2.legend(loc='upper left')

    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == "__main__":
    socketio.run(application,host='0.0.0.0')
