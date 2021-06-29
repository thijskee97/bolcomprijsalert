from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from GUI import submit


#create database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "#"
db = SQLAlchemy(app)

#line up of variabels
submit = submit()
url = submit[0]
melding_ontvangen_bij_deze_prijs = submit[1]
email = submit[2]


#tables
class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=True)
    melding_ontvangen_bij_deze_prijs = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

#adding data
db.create_all()
db.session.add(Preference(url=url, melding_ontvangen_bij_deze_prijs=melding_ontvangen_bij_deze_prijs,email=email))
db.session.commit()


#get prijs data van bol.com op het ingevoerde URL
from bs4 import BeautifulSoup
import requests

response = requests.get(url=url)
print(response.status_code)
html = response.text


soup = BeautifulSoup(html,"html.parser")

print(soup.title)

# print(soup.find_all("div", class_="price-block__highlight"))
html_piece = soup.find("span", class_="promo-price")

price = html_piece.get_text().strip()
modify_price = int(price[:3])
print(modify_price)

import smtplib
import os
send_email_list = ['thijsgeertman@hotmail.com']

MY_EMAIL = "pythonbotmail040@gmail.com"
MY_PASSWORD = os.environ.get('EMAIL_PASS')

#verstuur mail wanneer de prijs omlaag gaat.
if int(submit[1]) >= modify_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=send_email_list,
            msg=f"Een artikel op je verlanglijst is onder de gewenste prijs gekomen! ")


