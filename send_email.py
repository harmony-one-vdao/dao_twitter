from smtplib import SMTPException, SMTPHeloError, SMTPAuthenticationError
from smtplib import SMTP_SSL as SMTP  # SSL connection
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from connection import *
from utils.tools import get_message, get_users, get_blacklist

"""
Google rate-limits but the program will keep trying until all emails are exhausted.
Try playing with the delay if it is taking too long.. 
"""

# subject = "🚨 Validator DAO Vote 🚨"
# subject = "🚨Mandatory Node Update - UPDATE OR YOUR NODE WILL STOP!!🚨"
subject = "vDAO Newsletter March 5th 2022"

hips = (
    # "hip0", # Test
    # "node_update",
    # "hip16",
    "newsletter",
)

_dir = "newsletter"

images = dict(page1="February28-1.png", page2="February28-2.png") # None

# Delay inbetween tweets
DELAY = 0.5  # 2 per second


def send_email(
    subject: str, message: str, EMAIL_TO: str, images: dict = {}, links: list = [], **kw
) -> None:

    msg = MIMEMultipart("related")

    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    # msg.attach(MIMEText(message))
    ServerConnect = False

    message = message.replace("\n", "<br>")

    html_output = f"<body><p>{message}"

    if images:
        for image_name in images:
            html_output += f'<br><center><img src="cid:{image_name}"></center>'
    html_output += "</p></body>"

    msg.attach(MIMEText(html_output, "html"))

    if images:
        for image_name, image_location in images.items():
            with open(join("send_data", "media", _dir, image_location), "rb") as fp:
                img = MIMEImage(fp.read())
            img.add_header("Content-ID", f"<{image_name}>")
            msg.attach(img)

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
            res = send_email(subject, msg, user, **kw)
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
        do_run = execute(
            **dict(
                reminder=True,
                subject=subject,
                images=images
            )
        )
