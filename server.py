from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as user_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = user_database.write(f'[EMAIL] {email} [SUBJECT] {subject} [MESSAGE] {message}\n')

def write_to_csv(data):
    with open('database.csv', newline='',mode='a') as user_database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(user_database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong"
