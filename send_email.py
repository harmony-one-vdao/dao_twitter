from smtplib import SMTPException, SMTPHeloError, SMTPAuthenticationError
from smtplib import SMTP_SSL as SMTP  # SSL connection
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from connection import *
from utils.tools import get_message, get_users, get_blacklist

"""
Google rate-limits but the program will keep trying until all emails are exhausted.
Try playing with the delay if it is taking too long.. 
"""
subject = "🚨 Validator DAO Vote 🚨"

hips = (
    # "hip0", # Test
    # "hip25",
    "hip16",
    "vdao1",
)

_dir = "hip"

# Delay inbetween tweets
DELAY = 0.5  # 2 per second


def send_email(subject: str, message: str, EMAIL_TO: str) -> None:

    msg = MIMEMultipart()

    msg["From"] = EMAIL_FROM

    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(message))

    ServerConnect = False

    try:
        smtp_server = SMTP(EMAIL_SMTP, "465")
        smtp_server.login(EMAIL_FROM, EMAIL_PASS)
        ServerConnect = True
    except SMTPHeloError as e:
        log.error(f"Server did not reply  ::  {e}")
        return False
    except SMTPAuthenticationError as e:
        log.error(f"Incorrect username/password combination ::  {e}")
        return False
    except SMTPException as e:
        log.error(f"Authentication failed ::  {e}")
        return False

    if ServerConnect:
        try:
            smtp_server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
            log.debug(msg.as_string())
            log.info(f"Successfully sent email to {EMAIL_TO}")
        except SMTPException as e:
            log.error(f"Unable to send email  ::  {e}")
            return False
        finally:
            smtp_server.close()
            log.info("Email server connection closed")
    return True


def run(hip: str, _dir: str, subject: str = "TEST EMAIL", **kw):
    fails = ""
    msg = get_message(hip, _dir, **kw)
    users, dm_list = get_users(hip, "email_list", ";")
    blacklist = get_blacklist()
    for user in users:
        if user and user not in blacklist:
            res = send_email(subject, msg, user)
            if not res:
                fails += f"{user};"
                log.info("Google have rate-limited.. Sleeping for 5 mins..")
                sleep(300)  # 5 mins
            sleep(DELAY)
    with open(dm_list, "w") as f:
        f.write(fails)
    if fails:
        return False
    return True


def execute(**kw):
    error = False
    for hip in hips:
        res = run(hip, _dir, **kw)
        if not res:
            error = True
    return error


if __name__ == "__main__":
    do_run = True
    while do_run:
        do_run = execute(**dict(reminder=True, subject=subject))
