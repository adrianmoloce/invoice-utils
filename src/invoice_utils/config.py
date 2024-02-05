import os


def _str_to_bool(arg: str) -> bool:
    return arg in {"True", "1", "y", "true", "yes", "Yes", "Y"}


DEFAULT_MAIL_HOST = "smtp.gmail.com"
DEFAULT_PORT = 587
DEFAULT_MAIL_SUBJECT = "Invoice generated with invoice-utils"
DEFAULT_BODY_TEMPLATE_NAME = "default_template.html"
DEFAULT_BODY_TEMPLATE_PACKAGE = "invoice_utils"
DEFAULT_BODY_TEMPLATE_DIRECTORY = "email_templates"

INVOICE_UTILS_MAIL_HOST = os.getenv("INVOICE_UTILS_MAIL_HOST", DEFAULT_MAIL_HOST)
INVOICE_UTILS_MAIL_PORT = os.getenv("INVOICE_UTILS_MAIL_PORT", DEFAULT_PORT)
INVOICE_UTILS_MAIL_SUBJECT = os.getenv("INVOICE_UTILS_MAIL_SUBJECT", DEFAULT_MAIL_SUBJECT)
INVOICE_UTILS_MAIL_LOGIN_USER = os.getenv("INVOICE_UTILS_MAIL_LOGIN_USER")
INVOICE_UTILS_MAIL_LOGIN_PASSWORD = os.getenv("INVOICE_UTILS_MAIL_LOGIN_PASSWORD")
INVOICE_UTILS_SENDER_EMAIL = os.getenv("INVOICE_UTILS_SENDER_EMAIL")
INVOICE_UTILS_SMTP_TLS = _str_to_bool(os.getenv("INVOICE_UTILS_SMTP_TLS"))
INVOICE_UTILS_BODY_TEMPLATE_NAME = os.getenv("INVOICE_UTILS_BODY_TEMPLATE_NAME", DEFAULT_BODY_TEMPLATE_NAME)
INVOICE_UTILS_BODY_TEMPLATE_PACKAGE = os.getenv("INVOICE_UTILS_BODY_TEMPLATE_PACKAGE", DEFAULT_BODY_TEMPLATE_PACKAGE)
INVOICE_UTILS_TEMPLATES_DIR = os.getenv(
    "INVOICE_UTILS_TEMPLATES_DIR",
    DEFAULT_BODY_TEMPLATE_DIRECTORY
)
