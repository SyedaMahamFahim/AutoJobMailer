# ===== Imports ===== #

import time
import pdfkit
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from datetime import datetime
import os




# ===== Config ===== #
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
options = {
    'enable-local-file-access': True,
}

cv_file_name = os.path.join(BASE_DIR, "assets", "cv.pdf")
cover_letter_pdf_file = os.path.join(BASE_DIR, "assets", "cover_letter.pdf")
excel_file = os.path.join(BASE_DIR, "data", "Verified_Software_Houses_List.xlsx")
email_template_path = os.path.join(BASE_DIR, "templates", "email_body.html")
cover_letter_template_path = os.path.join(BASE_DIR, "templates", "cover_letter_template.html")
email_results = []
your_email = "your_email"
your_password = "your_password"
email_counter = 0
max_emails = 1



# ===== Load Logs + Templates ===== #

df = pd.read_excel(excel_file)
sent_companies = set()

with open(email_template_path, 'r') as file:
    email_body_template = file.read()

with open(cover_letter_template_path , 'r') as file:
    cover_letter_template = file.read()

current_date = datetime.now().strftime('%d/%b/%Y')

# ===== Email Loop ===== #
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_password)

for index, row in df.iterrows():
    if email_counter >= max_emails:
        break

    company_name = row['COMPANY']
    website = row['WEBSITE']

    if company_name in sent_companies:
        continue

    emails = [email.strip() for email in row['email'].split(',') if email.strip()]

    for to_email in emails:
        if email_counter >= max_emails:
            break
        
        email_body = email_body_template.replace('{{company_name}}', company_name)
        email_body = email_body.replace('{{website}}', website)

        cover_letter_body = cover_letter_template.replace('{{company_name}}', company_name)
        cover_letter_body = cover_letter_body.replace('{{current_date}}', current_date)

        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = to_email
        msg['Subject'] = f"Syeda Maham Fahim - Application for Software Engineer Position at {company_name}"

        msg.attach(MIMEText(email_body, 'html'))

        filename_cv = cv_file_name
        with open(filename_cv, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename_cv}')
            msg.attach(part)

        cover_letter_pdf = cover_letter_pdf_file
        pdfkit.from_string(cover_letter_body, cover_letter_pdf, configuration=config, options=options)

        with open(cover_letter_pdf, "rb") as cover_letter:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(cover_letter.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={cover_letter_pdf}')
            msg.attach(part)

        try:
            server.send_message(msg)
            print(f"Email sent to {to_email} at {company_name}")
            email_results.append({**row.to_dict(), 'Email': to_email, 'Status': 'Success'})

            
            email_counter += 1
        except Exception as e:
            print(f"Failed to send email to {to_email} at {company_name}: {e}")
            email_results.append({**row.to_dict(), 'Email': to_email, 'Status': 'Failed', 'Error': str(e)})
        time.sleep(3)

# ===== Save Output + Close ===== #
output_file = os.path.join(BASE_DIR,"output", "email_send_results.csv")
results_df = pd.DataFrame(email_results)
results_df.to_csv(output_file, index=False)
server.quit()
