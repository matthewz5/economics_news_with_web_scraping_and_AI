from fpdf import FPDF  # type: ignore
from fpdf import TextStyle  # type: ignore
from mistletoe import markdown # type: ignore
import os

def save_pdf(text, PDF_PATH):

    html = markdown(text)

    pdf = FPDF()
    pdf.add_page()

    DejaVuSans_font_path = os.path.join(os.path.dirname(__file__), "fonts/DejaVuSans.ttf")
    DejaVuSans_Bold_font_path = os.path.join(os.path.dirname(__file__), "fonts/DejaVuSans-Bold.ttf")

    if not os.path.exists(DejaVuSans_font_path) or not os.path.exists(DejaVuSans_Bold_font_path):
        raise FileNotFoundError("Font files are missing. Ensure DejaVuSans.ttf and DejaVuSans-Bold.ttf are in the 'fonts' directory.")

    pdf.add_font('DejaVu', '', DejaVuSans_font_path, uni=True)
    pdf.add_font('DejaVu', 'B', DejaVuSans_Bold_font_path, uni=True)
    pdf.set_font('DejaVu', '', 12)

    tag_styles = {
        'b': TextStyle(font_family='DejaVu', font_style='B'),
        'strong': TextStyle(font_family='DejaVu', font_style='B'),
        'li': TextStyle(font_family='DejaVu', font_style='', font_size_pt=12),
    }

    pdf.write_html(html, tag_styles=tag_styles)

    pdf.output(PDF_PATH)