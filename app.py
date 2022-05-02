# from flask import Flask
# import flask
# app = Flask(__name__)
# # @app.route('/colors/<any(blue,white,red):color>')#any转换器，任意一个都可以访问
# # def three_colors(color):
# #     return '<p> life is coloful!</p>'
# # if __name__ == '__main__':
# #     app.run(debug=True)
# @app.before_request # 处理每个请求前运行（记录请求时间）
# def before_request():
#     print("before request")
# @app.before_first_request # 处理第一个请求前运行(初始化，添加数据库，建立连接)
# def before_first_request():
#     print("before first request")
# @app.after_request # 若没有未处理的异常抛出，会在每个请求结束后运行（请求后，更新数据库表）
# def per_request_callbacks(response):
#     print("after request")
#     return response
# @app.teardown_request # 若没有未处理的异常抛出，会在每个请求结束后运行
#                       # 若发生异常会传入一场对象作为参数到注册的函数中
# def teardown_request(e): # 最后一步执行的函数（譬如：关闭连接）
#     print("teardown request")
#     print("e: %s" % e)
#
# @app.route('/A')
# def A():
#     return '<p> this is function AA</p>'
# @app.route('/B')
# def B():
#     return '<p>this is function B</p>'
# @app.route('/C')
# def C():
#     @flask.after_this_request # 处理这个请求之后来运行下面的函数
#     def after_this_request(response):
#         print("after this request")
#         # raise ValueError
#         response.status_code = 208
#         return response
#     return "<p>after this request</p>"
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, make_response
# import flask
#
# app = Flask(__name__)
#
#
# @app.route('/foo')
# def foo():
#     d = [1, 2, 3]
#     response = make_response("Hello,make a respnse by yourself")
#     # response.mimetype = 'application/json'
#     response.mimetype = 'text/plain'
#     return response
# from flask import Flask
# from flask import make_response
# app=Flask(__name__)
# @app.route('/hello/', endpoint = 'greeting')
# def hello():
#     # d=('1','2',{'server':'gloryroad'})  # 传参需要注意的地方
#     d1 = ('about page', 200, {'server':'heboan'})
#     #response = make_response('about page', 200, {'server':'heboan'})
#     #response = make_response('about page', 200, [('server','gloryroad'),('username','sam')])
#     response = make_response(d1)
#     #response = make_response(d1)
#     return response
# if __name__ == '__main__':
#     app.run(debug=True)

###################################################
# from flask import Flask
#
# app=Flask(__name__)
#
# @app.route('/redirect')
# def redirectfunc():
#     return("<p>This is a redirect page</p>")
#
# @app.route('/hello1/')
# def hello1():
#     print("redirect...")
#     return '', 302, {'Location': 'http://127.0.0.1:5000/redirect'}
#
# if __name__ == '__main__':
#     app.run(debug=True)
##############################################################
# from flask import Flask,redirect,url_for
# app=Flask(__name__)
# @app.route('/hello3/',endpoint='world')
# def hello3():
#     print(url_for('redirectfun'))  # url_for(端点名)--》返回端点对应的url规则
#     return redirect(url_for('redirectfun'))#重定向到/redirect
#
# @app.route('/redirect')
# def redirectfun():
#     return "<p>This is a redirect page</p>"
#
# if __name__ == '__main__':
#     app.run(debug=True)
#################################################
# from flask import Flask
# from flask import abort
#
# app=Flask(__name__)
#
# @app.route('/404/')
# def not_found():
#     abort(404)
#
# if __name__ == '__main__':
#     app.run(debug = True)
##########################################
# from flask import Flask, make_response, json
# from flask import jsonify
# app = Flask(__name__)
# @app.route('/foo1')
# def foo1():
#     data = {'name': 'Sam Xia', 'gender': 'male'}
#     response = make_response(json.dumps(data))  # 将json格式转换为python字典
#     response.mimetype = 'application/json'  # 这句话的含义是样式不同
#     return response
# @app.route('/foo3')
# def foo3():
#     return jsonify(name='Sam Xia', gender='make')  # 返回json格式的
# if __name__ == '__main__':
#     app.run(debug=True)
###################################################
# from flask import Flask,make_response,json,redirect,url_for
# app=Flask(__name__)
# @app.route('/hello1')
# def hello1():
#     data = {'name': 'Sam Xia', 'gender': 'male'}
#     response = make_response(json.dumps(data))
#     response.mimetype = 'application/json'
#     print("dir(response): %s" % dir(response))
#     print("respones.json: %s" % response.json)
#     print("response.get_json(): %s" % response.get_json())
#     print("response.is_json: %s" % response.is_json)
#     return  response
# @app.route('/hello/<name>')
# def hello(name):
#     return '<h1>Hello, %s !</hi>' %name
# @app.route('/set/<name>')
# def set_cookie(name):
#     """执行这个请求的时候是服务器Set-Cookie 后返回给客户端，体现在response headers里;
#     然后重定向了一次，体现在request headers里"""
#     #url_for()方法的第一个参数是端点，视图函数名；第二个参数是该函数需要的参数
#     response = make_response(redirect(url_for('hello', name = 'gloryroad')))
#     #把url中name变量的值添加到cookie中name属性中
#     response.set_cookie('username',name)
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
####################################################
# from flask import Flask,make_response,redirect,url_for,request
# app=Flask(__name__)
# @app.route('/')  # 两个都可以访问,直接访问时不带参数，故username为None
# @app.route('/hello')
# def hello():
#     username = request.args.get('username')
#     print("username: %s" % username)
#     if username is None:
#         username = request.cookies.get('username','Human')#从cookie中获取username值，没有则返回‘Human’
#     return '<h1>Hello, %s</hi>' % username
# @app.route('/set/<name>')
# def set_cookie(name):
#     #url_for()方法的第一个参数是视图函数名，第二个参数是该函数需要的参数
#     response = make_response(redirect(url_for('hello',username = '李白')))
#     #把url中name变量的值添加到cookie中name属性中
#     response.set_cookie('username',name)
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
##################################################
# from flask import Flask, redirect, session, url_for,request
# app = Flask(__name__)
# import os
# # 对cookie进行加密
# # 获取环境配置，在.env文件或.flask.env文件里找，找不到就取默认的'secret string'
# app.secret_key = os.getenv('SECRET_KEY', 'secret string')
# @app.route('/login/')
# def login():
#     session['logged_in'] = True  # 写入session
#     return redirect(url_for('hello'))
# @app.route('/')
# @app.route('/hello/')
# def hello():
#     print("app.secret_key: %s" % app.secret_key)
#     name = request.args.get('name')
#     if name is None:
#         name = request.cookies.get('name', 'Human')  # 从cookie中获取name值
#     return '<h1>Hello, %s</hi>' % name
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#############################################
# from flask import redirect, session, url_for, request
# from flask import Flask
# app = Flask(__name__)
# import os
# app.secret_key = os.getenv('SECRET_KEY','secret string')
# @app.route('/login/')
# def login():
#     session['logged_in'] = True #写入session
#     return redirect(url_for('hello'))
# @app.route('/')
# @app.route('/hello')
# def hello():
#     name = request.args.get('name')
#     print("name: %s" % name)
#     if name is None:
#         name = request.cookies.get('name','flask')#从cookie中获取name值
#     response = '<h1>Hello, %s</h1>' % name
#     #根据用户认证状态返回不同内容
#     print("session: %s" % session)
#     print("type(session): %s" % type(session))
#     print("session.get('logged_in'): %s" % session.get('logged_in'))
#     if 'logged_in' in session:
#         response += '<p>[Authenticated]</p>'
#     else:
#         response += '[Not Authenticated]'
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
###########################################
# from flask import redirect, session, url_for, request,abort,Flask
# app = Flask(__name__)
# import os
# app.secret_key = os.getenv('SECRET_KEY','secret string')
# @app.route('/login/')
# # def login():
# #     session['logged_in'] = True #写入session
# #     return redirect(url_for('hello'))
# # @app.route('/login')
# def login():
#     session['zhigang'] = True  # 写入session
#     session.permanent = True  # 设定session有效期
#     return redirect(url_for('hello/'))
# @app.route('/admin/')
# def admin():
#     if 'logged_in' not in session:
#         abort(403)
#     return 'welcom to admin page'
# @app.route('/')
# @app.route('/hello/')
# def hello():
#     name = request.args.get('name')
#     print("name: %s" % name)
#     if name is None:
#         name = request.cookies.get('name','flask')#从cookie中获取name值
#     response = '<h1>Hello, %s</h1>' % name
#     #根据用户认证状态返回不同内容
#     print("session: %s" % session)
#     print("type(session): %s" % type(session))
#     print("session.get('logged_in'): %s" % session.get('logged_in'))
#     if 'logged_in' in session:
#         response += '<p>[Authenticated]</p>'
#     else:
#         response += '[Not Authenticated]'
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
#####################################################
# from flask import g,request,Flask
#
# app = Flask(__name__)
#
# @app.before_request
# def get_username():
#     g.username = request.args.get('username')
#
# @app.route('/hello/')
# def hello():
#     print("g.username: %s" % g.username)
#     print("g.get('username'): %s" % g.get('username'))
#     return '<h1>Hello, %s</hi>' % g.username
#
# if __name__ == '__main__':
#     app.run(debug = True)
#########################################################################
# from flask import request,redirect,url_for,Flask
# app = Flask(__name__)
# @app.route('/bar')
# def bar():
#     print("request.full_path: %s" % request.full_path)
#     return '<h1>Bar page</h1><a href="%s">Do something </a>' % url_for('do_something')
# @app.route('/foo')
# def foo():
#     print("request.full_path: %s" % request.full_path)
#     return '<h1>Foo page</h1><a href="%s">Do something </a>' % url_for('do_something')
# @app.route('/do_something')
# def do_something():
#     # do something
#     return redirect(request.referrer)
# @app.route('/hello')
# def hello():
#     name = request.args.get('name')
#     if name is None:
#         name = request.cookies.get('name', 'gloryroad')  # 从cookie中获取name值
#         response = '<h1>Hello, %s</h1>' % name
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
#####################################################3
# from flask import request,redirect,url_for,Flask
# app = Flask(__name__)
# @app.route('/bar')
# def bar():
#     print("request.full_path: %s" % request.full_path)
#     return '<h1>Bar page</h1><a href="%s">Do something </a>' % url_for('do_something', next=request.full_path)
# @app.route('/foo')
# def foo():
#     print("request.full_path: %s" % request.full_path)
#     return '<h1>Foo page</h1><a href="%s">Do something </a>' % url_for('do_something', next=request.full_path)
# @app.route('/do_something')
# def do_something():
#     return redirect(request.args.get('next'))
# @app.route('/hello')
# def hello():
#     name = request.args.get('name')
#     if name is None:
#         name = request.cookies.get('name', 'gloryroad')  # 从cookie中获取name值
#         response = '<h1>Hello, %s</h1>' % name
#     return response
# if __name__ == '__main__':
#     app.run(debug = True)
######################################################
# # encoding=utf-8
# from flask import Flask,render_template
# app = Flask(__name__)
# @app.route('/watchlist')
# def watchlist():
#     return """
# <head>
#     <title>xiaxiaoxu's Watchlist</title>
# </head>
# <body>
# <h2>xiaxiaoxu</h2>
#     <i>A man who loves 看电影.</i>
# <h5>xiaxiaoxu's Watchlist:</h5>
# <ul>
#         <li>%s</li>
# </ul>
# </body>
# </html>""" % 'My Neighbor Totoro - 1988'
# app.run()
######################################################
# #encoding=utf-8
#
# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/watchlist')
# def watchlist():
#     return render_template('watchlist.html',user=user,movies = movies)
# @app.route('/hello/')
# def hello():
#     return '<p>welcome to flask template </p>'
# user = {
#     'username': 'xiaxiaoxu',
#     'bio': 'A man who loves 看电影.'
# }
# movies = [
#     {'name' : 'My Neighbor Totoro','year':'1988'},
#     {'name': 'Three Colours trilogy', 'year': '1993'},
#     {'name': 'Forrest Gump', 'year': '1994'},
#     {'name': 'Perfect Blue', 'year': '1997'},
#     {'name': 'The Matrix', 'year': '1999'},
#     {'name': 'Memento', 'year': '2000'},
#     {'name': 'The Bucket list', 'year': '2007'},
#     {'name': 'Black Swan', 'year': '2010'},
#     {'name': 'Gone Girl', 'year': '2014'},
#     {'name': 'CoCo', 'year': '2017'}]
#
# if __name__ == "__main__":
#     app.run(debug = True)
#############################################################################
# #encoding=utf-8
# from flask import Flask,render_template,render_template_string
# app = Flask(__name__)
# @app.route('/watchlist')
# def watchlist():
#     return render_template_string(
#         '''{% for movie in movies %}
#         <li>{{ movie.name }} - {{ movie.year }}</li>
#         {% endfor %}''', movies = movies)
#     #return render_template('watchlist.html',user=user,movies = movies)
# @app.route('/hello')
# def hello():
#     return '<p>welcome to flask template </p>'
# user = {'username': 'weixingguang',
#         'bio': 'Two man who loves 看电影.'}
# movies = [
#     {'name' : 'My Neighbor Totoro','year':'1988'},
#     {'name': 'Three Colours trilogy', 'year': '1993'},
#     {'name': 'Forrest Gump', 'year': '1994'},
#     {'name': 'Perfect Blue', 'year': '1997'},
#     {'name': 'The Matrix', 'year': '1999'},
#     {'name': 'Memento', 'year': '2000'},
#     {'name': 'The Bucket list', 'year': '2007'},
#     {'name': 'Black Swan', 'year': '2010'},
#     {'name': 'Gone Girl', 'year': '2014'},
#     {'name': 'CoCo', 'year': '2017'}]
# if __name__ == '__main__':
#     app.run(debug=True)
########################################################################
# # encoding=utf-8
# from flask import Flask,render_template,render_template_string
# app = Flask(__name__)
# @app.route('/watchlist')
# def watchlist():
#     return render_template_string('watchlist.html', movies = movies)
#     #return render_template('watchlist.html',user=user,movies = movies)
#
# @app.route('/index/')
# def index():
#     return render_template('index.html')
#
# @app.route('/testJinja')
# def testJinja():
#     return render_template('testJinja.html', my_list=my_list, my_tuple=my_tuple, my_dict=my_dict, my_func=my_func, my_object=my_object)
# my_list=[1,2,3,4]
# my_tuple=('a','b','c','d')
# my_dict={'d1':'abc','d2':'bcd','d3':'cde'}
# def my_func():
#     return "this is my_func~"
# my_object = "my_object"
# if __name__ == '__main__':
#     app.run(debug=True)
#####################################################
# # encoding=utf-8
# from flask import Flask, render_template, render_template_string
#
# app = Flask(__name__)
#
# @app.route('/watchlist')
# def watchlist():
#     return render_template_string('watchlist.html', movies = movies)
#     #return render_template('watchlist.html',user=user,movies = movies)
# @app.route('/hello')
# def hello():
#     return "hello flask"
# @app.route('/index/')
# def index():
#     return render_template('index.html')
#
#
# @app.context_processor
# def inject_foo():
#     foo = 'I am foo.'
#     return dict(foo=foo)  # 等同于return {'foo': foo}
# @app.template_global()
# def bar():
#     return 'I am bar.'
#
# @app.template_global(name='barfunc')
# def bar():
#     return 'I am bar.'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
####################################################################
# #encoding=utf-8
# from flask import Flask,render_template,render_template_string
# app = Flask(__name__)
# @app.route('/index/')
# def index():
#     return render_template('index.html')
# @app.route('/watchlist')
# def watchlist():
#     return render_template_string('watchlist.html', movies = movies)
#     #return render_template('watchlist.html',user=user,movies = movies)
# @app.route('/hello')
# def hello():
#     return "hello flask"
# @app.template_global()
# def bar():
#     return 'I am bar.'
# @app.context_processor
# def inject_foo():
#     return dict(my_func=my_func)
#
# def my_func():
#     return "this is my_func~"
# if __name__ == '__main__':
#     app.run(debug=True)
#######################################################
#
# #encoding=utf-8
# from flask import Flask,render_template,render_template_string
# app = Flask(__name__)
#
# # @app.template_global()
# # def bar():
# #     return 'I am bar %s'
# # app.add_template_global(bar, name='barfunc')
# @app.route('/index/')
# def index():
#     return render_template('index.html')
# @app.route('/watchlist')
# def watchlist():
#     return render_template_string('watchlist.html', movies = movies)
#     #return render_template('watchlist.html',user=user,movies = movies)
# @app.route('/hello')
# def hello():
#     return "hello flask"
# @app.context_processor
# def inject_foo():
#     return dict(my_func=my_func)
# def my_func():
#     return "this is my_func~"
# from flask import Markup
#
# @app.template_filter()
# def musical(s):
#     return str(s) + Markup(' &#9835;')
#
# if __name__ == '__main__':
#     app.run(debug=True)
################################################################
# #encoding=utf-8
# from flask import Flask,render_template,session
# from flask import Markup, flash, redirect, url_for,render_template_string
# import os
# app = Flask(__name__)
# @app.route("/baidu")
# def baidu():
#     return redirect("https://www.sogou.com")
#
# @app.route('/index/')
# def index():
#     #flash('I am flash, who is looking for me?')
#     return render_template('index.html',arg1="hello")
#
# @app.context_processor
# def inject_foo():
#     return dict(my_func=my_func)
#
# def my_func():
#     return "this is my_func"
#
# @app.template_filter()
# def musical(s):
#     return s + Markup('&#9835;')
#
# @app.template_test()
# def baz(n):
#     if n == "baz":
#         return True
#     return False
#
# @app.route("/watchlist")
# def watchlist():
#     return render_template_string(
#     '''{% for movie in movies %}
#     <li>{{ movie.name }} - {{ movie.year }}</li>
#     % endfor %}''', movies=movies)
#
# user = {
#     "username" : "huhongqiang",
#     "bio" : "读书和运动必须有一个在路上"
# }
#
# movies = [
#     {"name":"huanghuang","year":"2018"},
#     {"name":"kongsuhong","year":"2019"},
#     {"name":"weixingguang","year":"2019"}
# ]
#
# @app.template_global(name="barfunc")
# def bar():
#     return "I am bar"
#
# if __name__ == '__main__':
#     app.run(debug=True)
#############################################################
# #encoding=utf-8
# from flask import Flask, render_template, session
# from flask import Markup, flash, redirect, url_for
# import os
#
# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'secret string')
#
#
# @app.route('/flash')
# def just_flash():
#     flash('I am flash, who is looking for me?')
#     return redirect(url_for('index'))
#
#
# @app.template_test()
# def baz(n):
#     if n == 'baz':
#         return True
#     return False
#
#
# @app.template_filter()
# def musical(s):
#     return str(s) + Markup(' &#9835;')
#
#
# @app.template_global()
# def bar():
#     return 'I am bar.'
#
#
# @app.context_processor
# def inject_foo():
#     return dict(my_func=my_func)
#
#
# def my_func():
#     return "this is my_func~"
#
#
# @app.template_global(name='barfunc')
# def bar():
#     return 'I am bar.'
#
#
# @app.route('/index/')
# def index():
#     flash('I am flash, who is looking for me?')
#     return render_template('index.html', arg1='hello')
#
#
# @app.context_processor
# def inject_foo():
#     foo = 'I am foo.'
#     return dict(foo=foo)  # 等同于return {'foo': foo}
#
#
# @app.route('/watchlist')
# def watchlist():
#     return render_template('watchlist.html', user=user, movies=movies)
#
#
# @app.route('/hello')
# def hello():
#     return "hello flask"
#
#
# user = {
#     'username': 'xiaxiaoxu',
#     'bio': 'A man who loves 看电影.'
# }
# movies = [
#     {'name': 'My Neighbor Totoro', 'year': '1988'},
#     {'name': 'Three Colours trilogy', 'year': '1993'},
#     {'name': 'Forrest Gump', 'year': '1994'},
#     {'name': 'Perfect Blue', 'year': '1997'},
#     {'name': 'The Matrix', 'year': '1999'},
#     {'name': 'Memento', 'year': '2000'},
#     {'name': 'The Bucket list', 'year': '2007'},
#     {'name': 'Black Swan', 'year': '2010'},
#     {'name': 'Gone Girl', 'year': '2014'},
#     {'name': 'CoCo', 'year': '2017'}]
#
#
# @app.route('/testJinja')
# def testJinja():
#     return render_template('testJinja.html', my_list=my_list, my_tuple=my_tuple, my_dict=my_dict, my_func=my_func,
#                            my_object=my_object)
#
#
# my_list = [1, 2, 3, 4]
# my_tuple = ('a', 'b', 'c', 'd')
# my_dict = {'d1': 'abc', 'd2': 'bcd', 'd3': 'cde'}
# my_object = "my_object"
#
# if __name__ == '__main__':
#     app.run(debug=True)
################################################################
# 传入表单类实例
# encoding=utf-8
from flask import Flask, render_template, flash, session, redirect, url_for
import os
from form import LoginForm
from flask import request
from form import FortyTwoForm

# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'secret string')
#
#
# # app.config['WTF_CSRF_ENABLED'] = False
#
# @app.route('/testmacro', methods=['GET', 'POST'])
# def testmacro():
#     form = FortyTwoForm()
#     if form.validate_on_submit():
#         return redirect(url_for('hello'))
#     return render_template('htmlform.html', form=form)
#
#
# @app.route('/form', methods=['GET', 'POST'])
# def basic():
#     form = LoginForm()
#     print("request: %s" % request)
#     print("request.url: %s" % request.url)
#     print("request.form: %s" % request.form)
#     print("request.data: %s" % request.data)
#     print("request.headers: %s" % request.headers)
#     print("session before login: %s" % session)
#     print("form.username.data: %s" % form.username.data)
#     if request.method == 'POST' and form .validate():
#         print("form:%s" % form)
#         print("form.data:%s" % form.data)
#         print("request.form is valided")
#         print("session after login:%s" % form.session)
#         print("request.cookie.get('session'):%s" % request.cookie.get('session'))
#         if 'csrf_token' in session:
#             print("'csrf_token' in session:")
#             print("session.items(): %s" % session.items())
#             print("dict(session)['csrf_token']: %s" % dict(session)['csrf_token'])
#         return "<p>Hello,welcome</p>"
#     else:
#         print("request.form is not valided")
#         print(form.errors)
#         print(form.errors)
#         return render_template('bootstrap.html', form=form)
#
#
# @app.route('/bootstrap', methods=['GET', 'POST'])
# def bootstrap():
#     print("request: %s" % request)
#     print("request.url: %s" % request.url)
#     print("request.form: %s" % request.form)
#     print("request.data: %s" % request.data)
#     print("request.headers: %s" % request.headers)
#
#     form = LoginForm()
#     print("session before login:%s" % session)
#     print("form.username.data: %s" % form.username.data)
#     if request.method == "POST" and form.validate():
#         print("form:%s" % form)
#         print("form.data:%s" % form.data)
#         print("request.form is valided")
#         print("session after login:%s" % form.session)
#         print("request.cookie.get('session'):%s" % request.cookie.get('session'))
#         if 'csrf_token' in session:
#             print('"csrf_token" in session:')
#             print("session.items(): %s" % session.items())
#             print("dict(session)['csrf_token']: %s" % dict(session)['csrf_token'])
#
#     else:
#         print("request.form is not valided")
#         print(form.errors)
#         print(form.errors)
#     return render_template('bootstrap.html', form=form)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
############################################
# # encoding=utf-8
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
# import click
#
# app = Flask(__name__)
#
# app.secret_key = os.getenv('SECRET_KEY','secret string')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path,'data.db'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#
# db = SQLAlchemy(app)
#
# #定义Note模型类，映射到表note
# class Note(db.Model):
#     ID = db.Column(db.Integer,primary_key = True)
#     NAME = db.Column(db.Text)
#
#     def __repr__(self):
#         # %r 是用repr()方法处理对象，返回类型本身，而不进行类型转化
#         return '<Note ID: %r NAME:%r>' % (self.ID,self.NAME)
# @app.cli.command()
# def initdb():
#   db.create_all()
#   click.echo('Initialized database')
#
# if __name__ == "__main__":
#     app.run(debug=True)
##################################################

# encoding=utf-8
from flask import Flask,render_template,flash,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

import os
app.secret_key = os.getenv('SECRET_KEY','secret string')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path,'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 该方法跟模板上下文函数类似，返回的是一个字典，将对象以key和value
@app.shell_context_processor
def make_shell_content():
    return dict(db=db,Note=Note,Author=Author,Article=Article,Writer=Writer,Book=Book)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    articles = db.relationship('Article') # 定义关联函数，关联属性，一对多一，即为标量，出发侧，参数是关联的模型类

    def __repr__(self):
        return '<Author id: %r, name: %r>' % (self.id, self.name)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey('author.id')) #定义外键，对应多，即为集量

    # 指定显示内容，否则默认显示<表名 主键id>
    def __repr__(self):
        return '<Article id: %r, title: %r, body: %r, author_id: %r>' % (self.id, self.title,self.body,self.author_id)


class Writer(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(70),unique = True)
    # back_populats定义双向关系
    # back_populats参数的值需要设为关系另一侧的关系属性名
    books = db.relationship('Book', back_populates='writer')

    def __repr__(self):
        return '<Writer id: %r, name: %r>' %(self.id,self.name)


class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50), primary_key=True)
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))
    writer = db.relationship('Writer', back_populates='books')

    def __repr__(self):
        return '<Book id: %r, title: %r, writer_id:%r>' %(self.id,self.title,self.writer_id)
#
class Singer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    # songs = db.relationship('Song', backref='singer')
    songs = db.relationship('Song',uselist=False,backref=db.backref('singer',uselist=False))

    def __repr__(self):
        return '<Singer id: %r, name: %r>' %(self.id,self.name)
#
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    singer_id = db.Column(db.Integer, db.ForeignKey('singer.id'))

    def __repr__(self):
        return '<Song id: %r, name: %r, singer_id: %r>' %(self.id,self.name,self.singer_id)
#
class Citizen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    # back_population的值为另一侧的关系属性名
    # city = db.relationship('City')
    # relationship函数的第一个参数是另一侧的模型名（类型）
    city = db.relationship('City', back_populates='citizen')
    def __repr__(self):
        return '<Citizen id: %r, name: %r, city_id: %r>' %(self.id,self.name,self.city_id)
#
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    # back_population的值为另一侧的关系属性名
    # relationship函数的第一个参数是另一侧的模型名（类型）
    citizen = db.relationship('Citizen', back_populates='city')
    def __repr__(self):
        return '<City id: %r, name: %r>' %(self.id,self.name)
#
# 101行
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    capital = db.relationship('Capital',uselist=False)
# 109hang
    def __repr__(self):
        return '<Country id: %r, name: %r>' %(self.id,self.name)
#
class Capital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country')

    def __repr__(self):
        return '<Capital id: %r, name: %r, country_id: %r>' %(self.id,self.name,self.country_id)
# 多对多关系
association_table = db.Table('association',
                    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                    db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')),

                             )
# 125行代码
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),unique = True)
    grade = db.Column(db.String(20))
    teachers = db.relationship('Teacher',
                               secondary = association_table,
                               back_populates = 'students') # collection
    def __repr__(self):
        return '<Student id: %r, name: %r, grade: %r>' %(self.id, self.name,self.grade)
# 135行行号
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70),unique = True)
    office = db.Column(db.String(20))
    # black_populates，定义双向关系
    # back_populations参数的值需要设为关系另一侧的关系属性名
    students = db.relationship('Student',
                               secondary = association_table,
                               back_populates = 'teachers') # collection
    def __repr__(self):
        return '<Teacher id: %r,name: %r,office: %r>' %(self.id,self.name,self.office)

#定义Note模型类，映射到表note
class Note(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.Text)

    def __repr__(self):
        # %r 是用repr()方法处理对象，返回类型本身，而不进行类型转化
        return '<Note id: %r, body: %r>' % (self.id,self.body)


class NewNoteForm(FlaskForm):
    body = TextAreaField('Body',validators=[DataRequired()]) # 跳转新页面的body框
    submit = SubmitField('Save')

class EditNoteForm(FlaskForm):
    body = TextAreaField('Body',validators=[DataRequired()])
    submit = SubmitField('Update')

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')

import click
@app.cli.command()
def initdb():
  db.create_all()
  click.echo('Initialized database')

@app.route('/new/',methods=['GET','POST'])
def new_note():
    print("request.form in new_note: %s" % request.form)
    form = NewNoteForm()
    print("form:" , form)
    print("form.validate_on_submit(): " ,form.validate_on_submit())
    # if request.method == 'POST' and form validate():
    if form.validate_on_submit():
        print("pass")
        try:
            print(Note.query.all())
        except:
            print("initdb...")
            initDB()
        body = form.body.data
        note = Note(body = body)
        db.session.add(note)
        db.session.commit()
        flash("your note is saved")
        return redirect(url_for('index'))
    return render_template('new_note.html',form=form)

@app.route('/edit/<int:note_id>',methods=['GET','POST'])
def edit_note(note_id):
    print("request.form in edit_note: %s" % request.form)
    form = EditNoteForm()
    print("form.body: %s"  % form.body)
    print("form.body.data: %s"  % form.body.data)
    note = Note.query.get(note_id)
    print("note.body: %s" % note.body)
    if form.validate_on_submit(): # 判断表单提交的数据是否不为空+是post请求
        print("validated")
        note.body = form.body.data # 赋值新值
        print("note.body in validate: %s" % note.body)
        db.session.commit()
        flash("your note is edited")
        return redirect(url_for('index'))
    form.body.data = note.body #
    return render_template('edit_note.html',form=form)

@app.route('/delete/,<int:note_id>',methods=['POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id) #获取对应记录
        db.session.delete(note) #删除记录
        db.session.commit() # 提交修改
        flash('Your note is deleted')
    else:
        abort(400)
    return redirect(url_for('index'))
@app.route('/index/')
def index():
    db.create_all()
    form = NewNoteForm
    form_delete = DeleteNoteForm()
    notes = Note.query.all()
    return render_template('index.html',notes=notes,form=form,form_delete=form_delete)


if __name__ == "__main__":
    print(app.config)
    app.run(debug=True)