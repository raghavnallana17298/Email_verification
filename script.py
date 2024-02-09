from flask import *
from flask_mail import *
import random 
app = Flask(__name__)
otp = random.randint(4444,6666)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "harsha10012004@gmail.com"
app.config["MAIL_PASSWORD"] = ''
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)
@app.route("/")
def view():
    return render_template("file.html")
@app.route("/details",methods=["POST","GET"])
def details():
    if request.method == "POST":
        email = request.form["Email"]
        if not email:
            return redirect(url_for("view"))
        msg = Message("OTP VERIFICATION",sender="harsha10012004@gmail.com",recipients=[email])
        msg.body = "The OTP is "+str(otp)
        mail.send(msg)
        return render_template("file1.html")
@app.route("/manage",methods = ["POST","GET"])
def manage():
    passwd = request.form["Otp"]
    if otp  == int(passwd):
        return "<h1 align = 'center'> SuccessFull </h1>"
    return redirect(url_for("details"))
if __name__=='__main__':
    app.run(debug = True)
        
        