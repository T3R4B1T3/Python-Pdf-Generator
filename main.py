from inputs import collect_user_data, choose_save_path
from pdf_generator import generate_pdf

def main():
    data = collect_user_data()
    filepath = choose_save_path()
    generate_pdf(data, filepath)
    print(f"PDF saved as: {filepath}")

if __name__ == "__main__":
    main()
