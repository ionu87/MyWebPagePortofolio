from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#write to a .txt file
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('newdatabase.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database2, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

# route for writing to a .txt file
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again.'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again.'

# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# export FLASK_APP=hello.py
# flask run

# export FLASK_ENV=development
# flask run