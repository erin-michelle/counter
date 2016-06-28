from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1
  return render_template('index.html')

@app.route('/add_two')

def addTwo():
	session['counter'] += 2
	return render_template('index.html')

@app.route('/reset')

def resetSessionCounter():
	session['counter'] = 0;
	return redirect('/')    

app.run(debug=True)



# to redirect: return redirect('/route_goes_here')