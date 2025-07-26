import os
import re

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def normalize_pdf_filename(name: str) -> str:
    return name if name.lower().endswith(".pdf") else f"{name}.pdf"

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_PHONE_RE = re.compile(r"^[0-9+\-\s()]{5,}$")

def is_valid_email(email: str) -> bool:
    return bool(_EMAIL_RE.match(email))

def is_valid_phone(phone: str) -> bool:
    return bool(_PHONE_RE.match(phone))
