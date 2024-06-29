import imaplib
import email
from email.utils import parsedate_to_datetime
import json
import os
import re

def connect_to_email(username, password, imap_server):
    try:
        print(f"Connecting to IMAP server: {imap_server}")
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        print("Connected to the email server successfully.")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def fetch_emails(mail, folder):
    if mail is None:
        print("Mail object is None. Cannot fetch emails.")
        return []

    try:
        mail.select(folder)
        status, messages = mail.search(None, 'ALL')  # 'ALL' to fetch both seen and unseen emails
        if status != "OK":
            print(f"Failed to retrieve emails from {folder}.")
            return []

        email_ids = messages[0].split()

        email_data = []
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            if status != "OK":
                print(f"Failed to fetch email with ID {email_id} from {folder}.")
                continue

            msg = email.message_from_bytes(msg_data[0][1])

            # Extract sender's email address
            sender = msg.get("From", "Unknown")

            # Extract email subject
            subject = msg.get("Subject", "No Subject")

            # Extract email date
            date = msg.get("Date")
            if date:
                date = parsedate_to_datetime(date).isoformat()
            else:
                date = "Unknown"

            # Extract email content
            content = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        content += part.get_payload(decode=True).decode('utf-8', errors='ignore')
            else:
                content = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

            email_data.append({
                "sender": sender,
                "subject": subject,
                "date": date,
                "content": content
            })

        return email_data
    except Exception as e:
        print(f"An error occurred while fetching emails from {folder}: {e}")
        return []

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', filename)


def save_emails_to_json(email_data, folder_path):
    try:
        # Ensure the folder_path is a directory
        if os.path.exists(folder_path):
            if not os.path.isdir(folder_path):
                raise Exception(f"The path '{folder_path}' exists and is not a directory.")
        else:
            os.makedirs(folder_path)

        for email in enumerate(email_data):
            sender = email['sender']
            subject = email['subject']
            date = email['date']
            sanitized_subject = sanitize_filename(subject)[:15]
            filename = f"email_{sanitized_subject}.json"
            filepath = os.path.join(folder_path, filename)

            with open(filepath, 'w') as f:
                json.dump(email, f, indent=4)

            print(f"Email from {sender} with subject '{subject}' saved to {filepath}")
    except Exception as e:
        print(f"An error occurred while saving emails to JSON: {e}")

# Example usage
if __name__ == "__main__":
    EMAIL_ACCOUNT = "sendspammailstome@gmail.com"
    EMAIL_PASSWORD = "vqhz zcfa acez tpuf"
    IMAP_SERVER = "imap.gmail.com"
    EMAIL_SAVE_FOLDER = "email_extraction/extracted_emails"
    FOLDERS_TO_FETCH = ["inbox", "[Gmail]/Spam"]

    mail = connect_to_email(EMAIL_ACCOUNT, EMAIL_PASSWORD, IMAP_SERVER)
    if mail:
        all_emails = []
        for folder in FOLDERS_TO_FETCH:
            emails = fetch_emails(mail, folder)
            all_emails.extend(emails)
        save_emails_to_json(all_emails, EMAIL_SAVE_FOLDER)
    else:
        print("Failed to connect to the email server. Please check your settings.")