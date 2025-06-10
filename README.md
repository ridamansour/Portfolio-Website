# 📧 Porfolio Website with an AI-Powered Email Generator & Sender with Flask

This is a Flask web application that uses **Google Gemini-Pro** to auto-generate professional emails based on a subject and description, then sends them via **Gmail SMTP**. Great for automating communication, contact forms, or personal productivity tools.

---

## ✨ Features

* 🧠 Generates an email using **Google Gemini-Pro** AI model.
* 📤 Sends the generated email using **SMTP** (Gmail).
* 🌐 Clean and simple **Flask**-based web interface.
* 🔐 Uses `dotenv` to securely manage API keys and credentials.

---

## 📁 Project Structure

```
/project-root
│
├── app.py                 # Main Flask app
├── gemini.py              # Email content generator using Gemini
├── email_sender.py        # Handles sending email via SMTP
├── templates/             # HTML templates (index, about, contact, etc.)
├── static/                # Static files (favicon, CSS, images)
├── .env                   # Stores sensitive API keys and credentials
└── README.md              # You're here
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ridamansour/email-ai-flask.git
cd email-ai-flask
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory with:

```
EMAIL_PASS=your_gmail_app_password
API_KEY=your_google_gemini_api_key
```

> **Note:** Use an **App Password** if you have 2FA enabled on your Gmail.

---

## ▶️ Run the App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000/`

---

## 🔐 Security Tips

* Don't hardcode email addresses or credentials.
* Use HTTPS in production.
* Validate user input before sending.

---

## 💡 Future Ideas

* Store emails in a database (SQLite/PostgreSQL).
* Add user authentication.
* Support attachments or CC/BCC.
* Support multiple language email generation.

---

## 📜 License

This project is open-source and free to use.
