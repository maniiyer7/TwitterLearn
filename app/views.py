from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    tweets = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user, posts=tweets)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    #if request.method == 'POST' and 'hotcsv' in request.files:
    #    filename = hotcsvs.save(request.files['hotcsv'])
    #    flash("Photo saved.")
    return render_template('index.html', title='Home', user={'nickname': 'Mig'})
