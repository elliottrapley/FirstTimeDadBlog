from flask import Flask, render_template, url_for, request, redirect
import datetime

app = Flask(__name__)
print(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # Stores the name of the page as page_name variable, as a string.
def html_page(page_name):
    return render_template(page_name)

# This function returns a date and time stamp. This is used for when messages are sent.
def get_date_time():
  x = datetime.datetime.now()
  return x.strftime("%c")

# This function is for the user to join mailing list. Name and email is inserted as txt file. 
def write_to_file_subscriber(data):
    with open('new_subscribers.txt', mode='a') as new_subscribers:
        name = data["name"]
        email = data["email"]
        file = new_subscribers.write(f'\nName: {name} \nEmail: {email}\n')
        new_subscribers.write('\n')  # This creates a blank line to separate the messages in the txt file.
        new_subscribers.close()  # Closes the file safely.


# This function is for the contact me page when user inputs contact details and message. Writes to CSV file.
def write_to_file_message(data):
    with open('new_message.txt', newline='', mode='a') as new_message:
        name = data["name"]
        email = data["email"]
        telephone = data["telephone"]
        message = data["message"]
        new_message.write(get_date_time()) #Adds current date and time stamp when message was sent
        file = new_message.write(f'\nName: {name} \nEmail: {email} \nTelephone: {telephone} \nMessage: {message}')
        new_message.write('\n')  # This creates a blank line to separate the messages in the txt file.
        new_message.close()  # Closes the file safely.


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file_message(data)
            return render_template('message-sent-confirmation.html')
        except:
            return render_template('error.html')


@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file_subscriber(data)
            return render_template('registration-confirmation.html')
        except:
            return render_template('error.html')


