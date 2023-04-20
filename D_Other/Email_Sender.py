from email.message import EmailMessage
import ssl 
import smtplib

email_sender = 'mmumuhammadrefal44@gmail.com'
email_password = 'masalahlu125'

email_reciver = 'yacaf41603@lieboe.com'

subject = "Hope don't love you again"
body = """
    It's really hurt when i take ur photo with another guy yesterday
    I know i don't already do a confess to you but, my silent love when that event
    hurt me a lot, more than usually u do to me,, i thought i don't want to see you and you
    meet you for a while time
"""

em = EmailMessage()
em['From'] = email_sender
em['to'] = email_reciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())