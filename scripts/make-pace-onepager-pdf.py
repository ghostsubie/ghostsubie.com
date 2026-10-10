#!/usr/bin/env python3
"""Generate the PACE Plan one-pager PDF for Ghost Subie Adventures.

Freebie #2 in the freebie-menu growth play (after the Rig-Ready Checklist).
Brand: warm paper, dark header band, campfire amber accents. One page.
"""
from fpdf import FPDF

DARK = (20, 17, 12)
AMBER = (245, 158, 11)
EMBER = (234, 88, 12)
INK = (42, 36, 28)
MUTED = (112, 100, 84)
PAPER = (250, 247, 240)
RULE = (228, 218, 200)
BOXFILL = (255, 244, 226)

SITE = "/home/hatch/workspace/site/ghostsubie.com"
LOGO_PATH = f"{SITE}/public/images/logo-amber.png"
SIG_PATH = f"{SITE}/public/images/signature.png"

LAYERS = [
    (
        "P", "PRIMARY", "Phone + CarPlay",
        "Works great \u2014 until it doesn\u2019t. Share your live location with your check-in "
        "person before you leave signal.",
        ["Check-in person:", "Check-in times:"],
    ),
    (
        "A", "ALTERNATE", "Offline maps downloaded",
        "OnX Offroad \u2014 the one we use. Download your full route plus the bailout roads "
        "before you leave wifi.",
        ["Map areas downloaded:"],
    ),
    (
        "C", "CONTINGENCY", "GMRS radio",
        "Midland USA in the Ghost. No cell needed \u2014 rig-to-rig and camp comms. "
        "Agree on the channel before you need it.",
        ["Channel / callsign:"],
    ),
    (
        "E", "EMERGENCY", "Satellite SOS",
        "InReach or your phone\u2019s satellite SOS. The button you never want to press \u2014 "
        "which is exactly why you test it before every big trip.",
        ["Tested on:"],
    ),
]


class PacePDF(FPDF):
    def footer(self):
        self.set_y(-16)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(*MUTED)
        self.cell(
            0, 10,
            f"www.ghostsubie.com  \u00b7  Your PACE Plan  \u00b7  p. {self.page_no()}/{{nb}}",
            align="C",
        )

    def fill_line(self, label):
        """Label followed by a handwriting line to the right margin; own row."""
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*MUTED)
        x0 = self.get_x()
        y0 = self.get_y()
        self.cell(self.get_string_width(label) + 2, 5.5, label)
        x1 = self.get_x()
        self.set_draw_color(*RULE)
        self.set_line_width(0.5)
        self.line(x1, y0 + 4.6, self.w - self.r_margin, y0 + 4.6)
        self.set_xy(x0, y0 + 6.0)

    def layer_block(self, letter, kind, name, desc, fills):
        y = self.get_y()
        # amber badge with letter
        self.set_fill_color(*AMBER)
        self.rect(self.l_margin, y + 0.5, 8, 8, "F")
        self.set_xy(self.l_margin, y + 0.5)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*DARK)
        self.cell(8, 8, letter, align="C")
        # title
        self.set_xy(self.l_margin + 11, y)
        self.set_font("DejaVu", "B", 11.5)
        self.set_text_color(*EMBER)
        self.cell(0, 8, f"{kind}  \u00b7  {name.upper()}", new_x="LMARGIN", new_y="NEXT")
        # description
        self.set_x(self.l_margin + 11)
        self.set_font("DejaVu", "", 10)
        self.set_text_color(*INK)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 11, 5.0, desc)
        # fill-ins, one per row
        for label in fills:
            self.set_x(self.l_margin + 11)
            self.fill_line(label)
        self.ln(1)
        self.set_x(self.l_margin)


pdf = PacePDF("P", "mm", "Letter")
pdf.alias_nb_pages("{nb}")
pdf.set_auto_page_break(True, margin=22)
pdf.set_margins(18, 16, 18)
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
pdf.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
pdf.add_font("DejaVu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")

pdf.add_page()
pdf.set_fill_color(*PAPER)
pdf.rect(0, 0, 216, 279, "F")

# ---- header band ----
band_h = 44
pdf.set_fill_color(*DARK)
pdf.rect(0, 0, 216, band_h, "F")
pdf.set_fill_color(*AMBER)
pdf.rect(0, band_h, 216, 2, "F")

logo_w = 30
logo_h = logo_w * 704 / 1202
pdf.set_font("DejaVu", "B", 26)
title_w = pdf.get_string_width("YOUR PACE PLAN")
logo_x = max(18 + title_w + 10, 216 - 18 - logo_w)
pdf.image(LOGO_PATH, x=logo_x, y=(band_h - logo_h) / 2, w=logo_w)

pdf.set_xy(18, 10)
pdf.set_font("DejaVu", "B", 26)
pdf.set_text_color(*AMBER)
pdf.cell(0, 11, "YOUR PACE PLAN", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "", 11.5)
pdf.set_text_color(245, 239, 227)
pdf.cell(0, 7, "Ghost Subie Adventures  \u2014  Preparedness Without Panic", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "I", 10)
pdf.set_text_color(185, 171, 144)
pdf.cell(0, 6, "A comms + nav backup plan for every trip. Cell towers don\u2019t follow you off the pavement.")

# ---- intro ----
pdf.set_y(band_h + 8)
pdf.set_font("DejaVu", "", 10.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(
    0, 5.4,
    "PACE is a military planning tool: Primary, Alternate, Contingency, Emergency. "
    "Four layers of communication and navigation, stacked so when one fails the next is already ready. "
    "This is the exact setup we run in the Ghost on every family trip \u2014 the blank lines are yours to fill before you roll.",
)
pdf.ln(2)

# ---- the four layers ----
for layer in LAYERS:
    pdf.layer_block(*layer)

# ---- the rule box ----
pdf.ln(1)
box_y = pdf.get_y()
pdf.set_fill_color(*BOXFILL)
pdf.set_draw_color(*EMBER)
pdf.set_line_width(0.8)
pdf.rect(pdf.l_margin, box_y, pdf.w - pdf.l_margin - pdf.r_margin, 11, "DF")
pdf.set_xy(pdf.l_margin, box_y + 3)
pdf.set_font("DejaVu", "B", 10.5)
pdf.set_text_color(*EMBER)
pdf.cell(pdf.w - pdf.l_margin - pdf.r_margin, 6,
         "\u201cTwo is one, one is none.\u201d  If you only have one way to call for help, you have zero.",
         align="C")
pdf.set_y(box_y + 14)

# ---- your trip ----
pdf.set_font("DejaVu", "B", 11.5)
pdf.set_text_color(*EMBER)
pdf.cell(0, 7, "YOUR TRIP", new_x="LMARGIN", new_y="NEXT")
pdf.set_draw_color(*RULE)
pdf.set_line_width(0.6)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(1.5)
for _label in ["Route:", "Wheels down / back by:", "If we\u2019re overdue, call:"]:
    pdf.set_x(pdf.l_margin)
    pdf.fill_line(_label)
pdf.ln(1)

# ---- sign-off ----
pdf.set_draw_color(*RULE)
pdf.set_line_width(0.6)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(2)
pdf.set_font("DejaVu", "", 9.5)
pdf.set_text_color(*MUTED)
pdf.cell(0, 6, "www.ghostsubie.com   \u00b7   IG: @ghostsubieadventures", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_font("DejaVu", "I", 11)
pdf.set_text_color(*INK)
pdf.cell(0, 6.2, "Stay prepared, not panicked,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1.5)
pdf.image(SIG_PATH, x=pdf.l_margin, w=28)

out = f"{SITE}/public/pace-plan-onepager.pdf"
pdf.output(out)
print(f"Wrote {out} ({pdf.page_no()} pages)")
