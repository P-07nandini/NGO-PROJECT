from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mainngopage.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

@app.route('/getinvolved')
def getinvolved():
    return render_template('getinvolved.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/joinwithus')
def joinwithus():
    return render_template('joinwithus.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/contactus')
def contactus():
    return render_template('contacus.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

# Optional: Handle /index.html
@app.route('/index.html')
def index_redirect():
    return render_template('mainngopage.html')

if __name__ == '__main__':
    app.run(debug=True)
