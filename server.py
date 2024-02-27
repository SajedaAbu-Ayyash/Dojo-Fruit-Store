from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['name'] = request.form['name']
    session['id'] = request.form['id']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', strawberry=session['strawberry'], raspberry=session['raspberry'], apple=session['apple'], name =session['name'], id=session['id'])


if __name__ == '__main__':
    app.run(debug=True)