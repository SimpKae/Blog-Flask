from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'Zhoukai'}
    posts = [{'author':{'name':'zhoukai'},'body':'The is very cool!'},
            {'author':{'name':'yangqin'},'body':'Beautiful day in Portland'}
            
            ]
    return render_template('index.html',title='home',user=user,posts=posts)
