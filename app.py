from flask import*
from flask import render_template
import datetime
import os
import shutil
import smtplib

app = Flask(__name__,static_folder="f", template_folder=os.getcwd())

def rdm():
	return str(datetime.datetime.now()).replace(" ","").replace(":","").replace(".","").replace("-","")


@app.route("/",methods=["GET","POST"])
def aa2():
	if (request.method == "GET"):
		return render_template("s.html", msg="none")
	else:
		files = request.files.getlist('files[]')
		n = rdm()
		os.mkdir(n)
		for file in files:
			file.save(n+"/"+file.filename)
		return render_template("s.html", msg="File uploaded successfully")

@app.errorhandler(404)
def kll(e):
	return render_template("err.html", error="404 page not found")

@app.errorhandler(Exception)
def report_bug(n):
	open("bugs.txt","a").write("\n"+str(n)+"\n")
	return render_template("err.html", error="500 Internal server error")

if __name__ == '__main__':
	app.run()
