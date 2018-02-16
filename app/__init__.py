from flask import Flask
from flask_mail import Mail 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'omaiwa'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'dcdef9106e0624'
app.config['MAIL_PASSWORD'] = 'ea264780ae216c'

mail=Mail(app)
from app import views