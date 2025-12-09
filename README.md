# news-email-bot
A Python script that scrapes the BBC World News page and sends a well-formatted headline + summary mail to your inbox daily.

How to Use:

Fork the repository
Click “Fork” in the top-right corner to create your own copy.

Set up your environment variables
Go to Settings → Secrets → Actions in your fork, and add the following secrets:

`SMTP_PASSWORD` → Your email password or app-specific password

`SMTP_USER` → Your email address

NB: To use another SMTP server, replace `smtp.gmail.com` with your preferred SMTP server in line 51

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
