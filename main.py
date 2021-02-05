from flask import Flask, request, render_template 

app = Flask(__name__) 


@app.route('/', methods =["GET", "POST"]) 
def calc(): 
	if request.method == "POST": 
		first = int(request.form.get("one"))
		second = int(request.form.get("two"))
		sum = str(first+second)
		return "Your sum is "+sum 
	return render_template("calc.html") 

if __name__=='__main__': 
	app.run(debug=True) 
