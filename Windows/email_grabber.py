import imaplib
import email
from email.header import decode_header
import os

# Credentials and server information
username = 'wwa192851@gmail.com'
password = 'mqtfqgoujrhhsmho'
imap_url = 'imap.gmail.com'

# Connect to the IMAP server and log in
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(username, password)

# Select the mailbox you want to check (INBOX, for example)
# Use mail.list() to see all your mailboxes
mail.select("inbox")

# Search for a specific email
# You can modify the search criteria to find the specific email you need
# For example, '(SUBJECT "Your Subject Here")'
status, messages = mail.search(None, '(FROM "abelhamlincoln14@gmail.com" SUBJECT "New Audio Recording")')

# Convert the result list to an array of message numbers
messages = messages[0].split()

# Iterate over each message
for mail_id in messages:
    # Fetch the email by its ID
    status, data = mail.fetch(mail_id, '(RFC822)')
    
    # Parse the email content
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            
            # Decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding)
            
            # Check if the email has an attachment
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                
                # Extract and save the attachment
                filename = part.get_filename()
                if filename:
                    filepath = os.path.join('/home/wa/test', filename)
                    with open(filepath, 'wb') as f:
                        f.write(part.get_payload(decode=True))
                    print(f'Downloaded {filename} to {filepath}')

# Close the mail connection
mail.close()
mail.logout()
