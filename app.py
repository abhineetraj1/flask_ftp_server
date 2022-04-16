from flask import*
import datetime
import os
import shutil
import smtplib

"""def send_mail():
	sttt = smtplib.SMTP('smtp.gmail.com', 587)
	sttt.starttls()
	sttt.login("hacker.route.47@gmail.com", "12hin55t")
	sttt.sendmail("hacker.route.47@gmail.com", "abhineetraj5032@gmail.com", "Few files have been uploaded to you server")
"""
app = Flask(__name__,static_folder="f")

def rdm():
	return str(datetime.datetime.now()).replace(" ","").replace(":","").replace(".","").replace("-","")
def rf(a):
	return open(a,"r").read()

def scp(a):
	return """<center><div id="alert-box">"""+a+"""<br><button id="ok-btn-alert" onclick="document.getElementById('alert-box').remove()">Ok</button><style type="text/css">#alert-box{border-radius: 10px;border: solid;border-color:red;color:red;background:white;text-align:center;margin:1vh;padding:1vh;font-size:3vh;}#ok-btn-alert{font-size:3vh;color:white;width:40%;background:red;border:solid;text-align:center;padding:2px;}</style><script type="text/javascript">if(window.innerHeight > window.innerWidth) {document.getElementById('alert-box').style.width="90%";} else {document.getElementById('alert-box').style.width=window.innerWidth/3+"px";}</script></div></center>"""

@app.route("/",methods=["GET","POST"])
def aa2():
	if (request.method == "GET"):
		return rf("s.html")
	else:
		files = request.files.getlist('files[]')
		n = rdm()
		os.mkdir(n)
		for file in files:
			file.save(n+"/"+file.filename)
		#send_mail()
		return rf("a.html")

@app.errorhandler(404)
def kll(e):
	return rf("404.html")

@app.errorhandler(Exception)
def report_bug(n):
	open("bugs.txt","a").write("\n"+str(n)+"\n")
	return rf("err.html")

if __name__ == '__main__':
	app.run()