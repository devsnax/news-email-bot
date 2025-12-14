# news-email-bot
A Python script that scrapes the BBC World News page and sends a well-formatted headline + summary mail to your inbox daily.

How to Use:

Fork the repository
Click “Fork” in the top-right corner to create your own copy.

Set up your environment variables
Go to Settings → Secrets → Actions in your fork, and add the following secrets:

`SMTP_PASSWORD` → Your email app-specific password. If Gmail, must enable 2FA to create and view App Password

`EMAIL_SENDER` → Your sending email address. Must be the email address for the SMTP password.

`EMAIL_RECEIVER` → Your receiving email address

NB: To use another SMTP server, replace `smtp.gmail.com` with your preferred SMTP server in `config.py`

Install dependencies

```bash
pip install -r requirements.txt
```

Run the bot
```bash
python3 main.py
```

Optional: Automate daily emails
Set up GitHub Actions (already included in this repo) or use a local scheduler like cron.

Arigato!
