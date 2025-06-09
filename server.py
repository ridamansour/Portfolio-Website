from flask import Flask, render_template, request, send_from_directory
import os
from email_sender import email_send
from gemini import emailCreater

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/submit_form', methods=["GET", "POST"])
def contact():
    global email_content
    if request.method == "POST":
        email_address = request.form.get("email")
        subject_sender = request.form.get("subject")
        email_content = request.form.get("message")
        description = request.form.get("description")
        x = emailCreater(subject=subject_sender, description=description)

    if email_content != "":
        print(email_send(email_sender=email_address, subject_sender=subject_sender, email_content=x))
        return render_template('./thankyou.html')
    else:
        print(email_send(email_sender=email_address, subject_sender=subject_sender, email_content=email_content))
        return render_template("contact.html", message=x, text_value=x)



@app.route('/<string:page_name>')
def main(page_name):
    return render_template(f'{page_name}')


@app.route('/about.html')
def about():
    return render_template('./about.html')


@app.route('/components.html')
def components():
    return render_template('./components.html')


@app.route('/contact.html')
def contacts():
    return render_template('./contact.html')


@app.route('/works.html')
def works():
    return render_template('./works.html')


@app.route('/work.html')
def work():
    return render_template('./work.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)