from flask import Flask,render_template

app=Flask(__name__)
JOBS=[
    {
        'id':1,
        'Project':'Data Analyst',
        'Place':'Bengaluru,India',
        'Skill set':'Rs.10,00,000'
    },
    {
        'id':2,
        'Project':'Data Scientist',
        'Place':'Delhi,India',
        'Skill set':'Rs.15,00,000'
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)
  
if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')