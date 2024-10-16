# integrate HTML with Flask
## HTTP Verb GET and POST
## Jinja2 template engine
'''
{%...%} conditions, for loops
{{  }} expressions to print output
{#...#} for comments
'''

from flask import Flask, redirect, url_for, render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score':score, 'res':res}
    return render_template('result3.html', result=exp)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The person has failed and the marks is " + str(score)

#result checker html page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.form['Maths'])
        c=float(request.form['C'])
        data_science=float(request.form['DataScience'])
        total_score=(science+maths+c+data_science)/4
    
    return redirect(url_for('success', score=total_score))




if __name__=="__main__":
    app.run(debug=True)

