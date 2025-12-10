"""
Module: email_service
Description:
    Handles sending emails using SMTP with SSL encryption.
    Automatically generates RFC 5322-compliant Message-ID headers.

Created by: Furkan (FK) KARA
Creation Date: 2025-01-25

Developers:
    - Furkan (FK) KARA

Notes:
    IMPORTANT:
    If you are not one of the developers listed above, please consult with them
    before making any changes to this module.
    This helps ensure that any modifications align with the module's intended
    design and use cases.

Changelog:
    - 2025-11-04: Added Message-ID support and enhanced error logging.
"""

# ===================== Imports BEGIN =====================
import time
import socket
import logging
import smtplib
from email.utils import make_msgid, formatdate
from email.mime.text import MIMEText
from django.conf import settings
# ===================== Imports END =======================

# Configure logging
logger = logging.getLogger(__name__)


def send_mail(to_email: str, subject: str, body: str) -> bool:
    """
    Sends an email using SMTP over SSL with RFC-compliant headers.

    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    smtp_server = settings.SMTP_SERVER
    smtp_port = settings.SMTP_PORT
    smtp_username = settings.SMTP_INFO_MAIL
    smtp_password = settings.SMTP_PASSWORD
    from_email = smtp_username

    # Create MIME message
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=socket.gethostname())

    try:
        logger.info("Connecting to SMTP server: %s:%s", smtp_server, smtp_port)
        with smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=15) as server:
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        logger.info("Email sent successfully to %s", to_email)
        return True

    except smtplib.SMTPException as smtp_err:
        logger.error("SMTP error occurred while sending email: %s", smtp_err)
    except Exception as e:
        logger.exception("Unexpected error during email sending: %s", e)

    return False
