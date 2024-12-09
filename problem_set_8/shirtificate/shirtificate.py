from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = Shirtificate()
    pdf.add_page()

    # Add the shirt image
    pdf.image("shirtificate.png", x=0, y=60, w=210)

    # Add the user's name on the shirt
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, txt=name)

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
