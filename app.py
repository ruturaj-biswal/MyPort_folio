from flask import Flask, render_template, request, flash, redirect, url_for
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Use env var or fallback

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/index")
def index():
    return render_template("index.html", title="Index")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/clint")
def clint():
    return render_template("clint.html", title="Clint")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        try:
            # Build the email
            email_content = Mail(
                from_email=os.getenv("FROM_EMAIL", "your@email.com"),
                to_emails=os.getenv("TO_EMAIL", "your@email.com"),
                subject=f"Contact Form Submission from {name}",
                plain_text_content=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
            )

            # SendGrid API key from environment variable
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            response = sg.send(email_content)

            print("✅ Email sent! Status code:", response.status_code)
            flash("Your message has been sent successfully!", "success")

        except Exception as e:
            print("❌ Error sending email:", repr(e))
            flash("Failed to send your message. Please try again later.", "danger")

        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))