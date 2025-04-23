import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_to_self(sender_email, sender_password, subject, body):
    try:
        # Setting up the email details
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = sender_email
        msg["Subject"] = subject

        # Adding the email body
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Establish a connection to the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to your account
            server.sendmail(sender_email, sender_email, msg.as_string())  # Send the email
            print(f"Email sent successfully to {sender_email}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    aws_access_key_id = AKIAIOSFODNN7EXAMPLE
    aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    subject = "Test Email"
    body = "This is a test email sent to myself using Python."
    send_email_to_self(your_email, your_password, subject, body)
