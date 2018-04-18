from flask import Flask, render_template, request

import requests

def send_confirmation_message(name, email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox37d8b5fe16294488948620c354c7eabb.mailgun.org/messages",
        auth=("api", "key-d69efd003013847104f007cf8d871a3d"),
        data={"from": "Olwen Wilson <olwenwilson95@gmail.com>",
              "to": [email],
              "subject": [name],
              "text": "Thanks for submitting your TV show idea! We will read through your pitch and get back to you within 3 weeks to discuss next steps."})

app = Flask("confirmReceipt")

@app.route("/emails_registration", methods=['GET','POST'])
def emails_registration():
	form_data = request.form
	name = form_data["name"]
	email = form_data["email"]
	title = form_data["title"]
	genre = form_data["genre"]
	topline = form_data["topline"]
	summary = form_data["summary"]

	print name
	print email
	print title
	print genre
	print topline
	print summary

	send_simple_message("Hello {}".format(name), email)

app.run(debug=True)


#@app.route("/emails_registration", methods=['POST'])
#def sign_up():
#	form_data = request.form
#	name = form_data["name"]
#	email = form_data["email"]
#	title = form_data["title"]
#	genre = form_data["genre"]
#	topline = form_data["topline"]
#	summary = form_data["summary"]

#	print name
#	print email
#	print title
#	print genre
#	print topline
#	print summary



#def send_confirmation_message():
#	form_data = request.form
#	name = form_data["name"]
#	email = form_data["email"]
#	title = form_data["title"]
#	genre = form_data["genre"]
#	topline = form_data["topline"]
#	summary = form_data["summary"]
#   return requests.post(
#      "https://api.mailgun.net/v3/sandbox37d8b5fe16294488948620c354c7eabb.mailgun.org/messages",
#      auth=("api", "key-d69efd003013847104f007cf8d871a3d"),
#      data={"from": "SHOW.me Team <olwenwilson95@gmail.com>",
#             "to": email
#             "subject": "Thanks for submitting your idea to SHOW.me!",
#             "text": "Thanks for submitting your TV show idea! We will read through your pitch and get back to you within 3 weeks to discuss next steps.",
#             "html": 	<html>
#            				<body>
#								<p>"Thanks for submitting your TV show idea!"</p>
#								<p>"We will read through your pitch and get back to you within 3 weeks to discuss next steps."</p>
#							</body> 
#						</html>

