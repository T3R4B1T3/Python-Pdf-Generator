from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, title, creation_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_text = title
        self.creation_date = creation_date

    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, self.title_text, ln=True, align="C")

        self.set_font("Arial", "", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, f"Document created on: {self.creation_date}", ln=True, align="C")

        self.set_draw_color(200, 200, 200)
        self.ln(2)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def generate_pdf(data, filepath):
    pdf = PDF(title="Personal Data", creation_date=data["creation_date"])
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()


    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Personal Information", ln=True)
    pdf.set_draw_color(220, 220, 220)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(4)

    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Name and Surname: {data['name']}", ln=True)

    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 8, f"E-mail: {data['email']}", ln=True, link=f"mailto:{data['email']}")
    pdf.set_text_color(0, 0, 0)

    pdf.cell(0, 8, f"Phone number: {data['phone']}", ln=True)
    pdf.ln(4)

 
    if data.get("photo_path"):
        try:
            current_y = pdf.get_y()
            pdf.image(data["photo_path"], x=pdf.l_margin, y=current_y, w=40)
            pdf.set_y(current_y + 42)
            pdf.ln(4)
        except Exception as e:
            pdf.set_text_color(255, 0, 0)
            pdf.cell(0, 8, f"Could not insert photo: {e}", ln=True)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(4)


    if data.get("about"):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "About me", ln=True)
        pdf.set_draw_color(220, 220, 220)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(4)

        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, data["about"])
        pdf.ln(2)


    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Interests", ln=True)
    pdf.set_draw_color(220, 220, 220)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(4)

    pdf.set_font("Arial", "", 11)
    interests = data.get("interests", [])
    if interests:
        for item in interests:
            pdf.multi_cell(0, 8, f"- {item}")
    else:
        pdf.cell(0, 8, "No interests provided.", ln=True)

    pdf.output(filepath)
