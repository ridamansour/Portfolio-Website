# 📧 Porfolio Website with an AI-Powered Email Generator & Sender with Flask

This is a Flask web application that uses **Google Gemini-Pro** to auto-generate professional emails based on a subject and description, then sends them via **Gmail SMTP**. Great for automating communication, contact forms, or personal productivity tools.

---

## ✨ Features

* 🧠 Generates emails using **Google Gemini-Pro** AI.
* 📤 Sends emails via **Gmail SMTP**.
* 🌐 Flask-based web interface.
* 🐳 **Docker** support for easy deployment.
* 🔐 Environment variables via `.env`.

---

## 📁 Project Structure

```
/project-root
│
├── app.py                 # Main Flask app
├── gemini.py              # Email content generator using Gemini
├── email_sender.py        # Handles sending email via SMTP
├── templates/             # HTML templates
├── static/                # Static files (CSS, images, favicon)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build file
├── docker-compose.yml     # Docker Compose config (optional)
├── .env                   # Environment variables
└── README.md              # Project documentation
```

---

## 🛠️ Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/email-ai-flask.git
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

```env
EMAIL_PASS=your_gmail_app_password
API_KEY=your_google_gemini_api_key
```

> ⚠️ Use an **App Password** if Gmail 2FA is enabled.

---

## ▶️ Run Locally

```bash
python app.py
```

Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Run with Docker

### 1. Build the Image

```bash
docker build -t email-ai-flask .
```

### 2. Run the Container

```bash
docker run -p 5000:5000 --env-file .env email-ai-flask
```

### Or Use Docker Compose

```bash
docker-compose up --build
```

---

## 🔐 Security Tips

* Keep `.env` secret and add it to `.gitignore`.
* Use HTTPS and email validation in production.
* Avoid hardcoding credentials.

---

## 💡 Future Ideas

* Save emails to a database.
* Add login functionality.
* Export generated emails to PDF.
* Support multiple languages and attachments.

---

## 📜 License

Free to use and modify.
