# **📧 AutoJobMailer**
### **Automated Email Sender for Job Applications**

This project helps you send personalized job application emails automatically.
It reads company details from an Excel sheet, customizes your templates, generates a PDF cover letter, and sends emails with your CV attached.

The structure is clean and easy for anyone to understand or extend.

---

## **📁 Project Structure**

```
project/
│
├── assets/
│   ├── cv.pdf
│   └── cover_letter.pdf
│
├── data/
│   ├── Verified_Software_Houses_List.xlsx
│   └── output/
│       └── email_send_results.csv
│
├── src/
│   ├── __init__.py
│   └── send_cv.py
│
├── templates/
│   ├── email_body.html
│   └── cover_letter_template.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## **📦 Features**

* Automatically sends job application emails
* Reads company list from Excel
* Supports multiple email addresses per company
* Generates a personalized PDF cover letter
* Attaches both CV and cover letter
* Simple and clean project layout
* Saves results in a CSV file
* Easy to configure and extend

---

## **🚀 Getting Started**

### **1. Clone the project**

```
git clone https://github.com/SyedaMahamFahim/AutoJobMailer
cd AutoJobMailer
```

### **2. Create a virtual environment**

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### **3. Install dependencies**

```
pip install -r requirements.txt
```

---

### **4. Install wkhtmltopdf**

This is required for PDF generation.

Download from:
[https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

Update the path inside `send_cv.py` if needed:

```
pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
```

---

### **5. Add your email credentials**

Inside **src/send_cv.py**, update these two lines:

```
your_email = "your_email"
your_password = "your_password"
```

For Gmail, use an **App Password**, not your real login password.

Perfect, Maham — I’ll give you a clean section that fits naturally inside your README.
Use it exactly as it is.

Add this right after the **“Add your email credentials”** section.

---

### **🔐 Generate a Gmail App Password**

Google does not allow normal account passwords for automated emails.
You must create a **Gmail App Password** and use that in your script.

Follow one of these:

* Generate it directly from your Google account:
  **[https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)**

* Or watch this short 2-minute tutorial:
  **[https://www.youtube.com/watch?v=hGoaVus0-Mg](https://www.youtube.com/watch?v=hGoaVus0-Mg)**

After generating the password, replace this in your script:

```
your_password = "your_app_password_here"
```

That’s it — now your script will authenticate safely with Gmail.




---

## **🗂️ Prepare Your Files**

* Add your CV to:
  `assets/cv.pdf`

* The PDF cover letter will be generated automatically into:
  `assets/cover_letter.pdf`

* Edit your email templates in:
  `templates/email_body.html`
  `templates/cover_letter_template.html`

* Your company list is inside:
  `data/Verified_Software_Houses_List.xlsx`

* Original source sheet (editable by owner):
  **Google Sheet:**
  [https://docs.google.com/spreadsheets/d/1ciEqphjZan2d6zj130NY0cf72H_DAfLs2CK-xqrHV04/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1ciEqphjZan2d6zj130NY0cf72H_DAfLs2CK-xqrHV04/edit?usp=sharing)

**Important:**
If the company list in your Google Sheet changes later, download the latest Excel version and replace the existing file inside the `data/` folder. The script will automatically use the updated data the next time you run it.


---

## **▶️ Run the Script**

```
python src/send_cv.py
```

---

## **📊 Output**

After running, the results are stored here:

```
data/output/email_send_results.csv
```

This file includes:

* Company name
* Email used
* Status (Success or Failed)
* Error message (if any)

---

## **⚠️ Notes**

* Use responsibly
* Avoid sending too many emails quickly
* Start with `max_emails = 1` for testing
* Keep your credentials private

---

## **📄 License**

MIT License

---
## **📬 Contact**

If you have suggestions or want to contribute, you can reach me at:
syedamahamfahim-at-gmail.com