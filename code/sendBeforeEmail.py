__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

"""
python_3_email_with_attachment.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.
This script works with Python 3.x
NOTE: replace values in ALL CAPS with your own values
"""

import os
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from variables import email_from, email_to, folder_tmp, pdf_folder, email_from_pass, result_no_blank_lines, \
    result_no_page_numbers

email_from = 'rciwnwro@gmail.com'
email_to = 'rciwnwro@gmail.com'
email_from_pass = 'y!mhsubx'
# from csv2xlsx import xlsx_file, done_folder

COMMASPACE = ', '


def sendbeforeemail(filename):
    sender = email_from
    gmail_password = email_from_pass
    recipients = [email_to]

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Konwersja pliku: ' + filename
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = [folder_tmp + result_no_blank_lines, pdf_folder + filename,
                   folder_tmp + result_no_page_numbers,
                   folder_tmp + "result.txt"]

    # Add the attachments to
    # the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()
    # Send
    # the
    # email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.ehlo()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise
