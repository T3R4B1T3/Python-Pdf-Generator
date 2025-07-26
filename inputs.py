import os
from datetime import datetime
from utils import (
    ensure_dir,
    normalize_pdf_filename,
    is_valid_email,
    is_valid_phone,
)

def ask_list(prompt, end_char="/"):
    print(prompt)
    items = []
    while True:
        val = input(" - ").strip()
        if val == end_char:
            break
        if val:
            items.append(val)
    return items

def collect_user_data():
    name = input("Please enter your name and surname: ").strip()

    # prosta walidacja e-maila/telefonu (możesz wyłączyć, jeśli niepotrzebna)
    while True:
        email = input("Please enter your email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email. Try again.")

    while True:
        phone = input("Please enter your phone number: ").strip()
        if is_valid_phone(phone):
            break
        print("Invalid phone number. Try again.")

    about = input("Write a short description about yourself (optional): ").strip()
    interests = ask_list("Please enter your interests (press '/', to end):")

    photo_path = input("Enter path to your photo (optional): ").strip()
    if photo_path and not os.path.isfile(photo_path):
        print("Photo not found. Skipping.")
        photo_path = ""

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "about": about,
        "interests": interests,
        "photo_path": photo_path,
        "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def choose_save_path(default_filename="personal_data"):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    target_dir = input(f"Enter folder path (Enter for Desktop: {desktop}): ").strip() or desktop
    ensure_dir(target_dir)

    filename = input(f"Enter filename (default: {default_filename}): ").strip() or default_filename
    filename = normalize_pdf_filename(filename)

    return os.path.join(target_dir, filename)
