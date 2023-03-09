from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Colombo,Sri Lanka',
        'salary':'Rs. 500,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Colombo,Sri Lanka',
        'salary':'Rs. 600,000'
    },
    {
        'id':3,
        'title':'Software Engineering',
        'location':'Colombo,Sri Lanka',
    },
    {
        'id':4,
        'title':'Frontend Developer',
        'location':'Colombo,Sri Lanka',
        'salary':'Rs. 200,000'
    },
]

@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS,company_name="EPIC DEV")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)


