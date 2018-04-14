from flask import Flask, render_template, request

import requests

def send_confirmation_message(name, email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox37d8b5fe16294488948620c354c7eabb.mailgun.org/messages",
        auth=("api", "key-d69efd003013847104f007cf8d871a3d"),
        data={"from": "Olwen Wilson <olwenwilson95@gmail.com>",
              "to": [email],
              "subject": [name],
              "text": "True."})

app = Flask("MyApp")

@app.route("/registration")
def email_registration():
	return render_template("emails_registration.html")

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form
	name = form_data["name"]
	email = form_data["email"]
	title = form_data["title"]
	genre = form_data["genre"]
	topline = form_data["topline"]
	summary = form_data["summary"]
	}

	print name
	print email
	print title
	print genre
	print topline
	print summary

	send_simple_message("Hello {}".format(name), email)

	return "ALL OK"

app.run(debug=True)

