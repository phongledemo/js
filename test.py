from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime

SENDER = 'noreply@cisco.com'
RECEIVERS = ['phonghle@cisco.com', 'dnguyent@cisco.com']
# set email headers
smtp_client = smtplib.SMTP('email.cisco.com')
message = MIMEMultipart('alternative')
message['Subject'] = f'DNAC DashBoard report on date {datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")}(UTC)'
message['From'] = SENDER
message['To'] = ','.join(RECEIVERS)
try:
    send_ = smtp_client.sendmail(
        from_addr=SENDER,
        to_addrs=RECEIVERS,
        msg = message.as_string()
    )
    if send_ == {}:
        print("Successfully sent email")
    else:
        print(f"Warning: send response: {send_}")

except Exception as e:
    print(f'Hitting exception when sending email: {e}')

