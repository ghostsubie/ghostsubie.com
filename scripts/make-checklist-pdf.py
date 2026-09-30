#!/usr/bin/env python3
"""Generate the Rig-Ready Checklist PDF for Ghost Subie Adventures.

DRAFT — content needs Roman's review before launch.
Brand: warm paper, dark header band, campfire amber accents.
"""
from fpdf import FPDF

DARK = (20, 17, 12)
AMBER = (245, 158, 11)
EMBER = (234, 88, 12)
INK = (42, 36, 28)
MUTED = (112, 100, 84)
PAPER = (250, 247, 240)
RULE = (228, 218, 200)

SECTIONS = [
    (
        "Vehicle — Before You Roll",
        [
            "Tires at proper pressure, **including the spare** — and you know where the jack lives",
            "Fluids topped: oil, coolant, washer fluid. No new leaks underneath.",
            "Battery terminals clean and tight; jumper pack charged",
            "All lights working: headlights, brake lights, turn signals, hazards",
            "Fuel: enough range for the route **plus a reserve** — know your next fill-up",
            "Recovery gear reachable, not buried: straps, shackles, traction boards",
            "Roof load and awning secured — nothing that can shift at highway speed",
            "Brakes feel right on a test stop before you hit the highway",
        ],
    ),
    (
        "Camp Systems",
        [
            "Shelter: tent or rooftop tent, stakes, guylines, ground tarp",
            "Sleep: bags rated for the forecast low, sleeping pads, pillows",
            "Kitchen: stove + fuel, lighter **and** backup, pot/pan, utensils, cooler with a meal plan",
            "Water: drinking supply plus a filter or treatment backup",
            "Fire kit in a waterproof bag — and know the local burn rules before you strike a match",
            "Power: battery bank charged, headlamps for everyone, spare batteries",
            "Chairs, trash bags, and a plan to leave camp cleaner than you found it",
        ],
    ),
    (
        "Personal Readiness",
        [
            "First-aid kit stocked for the realistic stuff — and you actually know how to use it",
            "Personal meds, sunscreen, bug protection",
            "Warm layer per person, rain layer if the sky looks moody",
            "Phones charged, offline maps downloaded, and **someone knows your route and return time**",
            "Kid kit: snacks, water, layers, headlamp, comfort item",
            "Dog kit: water, food, leash, waste bags",
        ],
    ),
    (
        "The 60-Second Trailhead Scan",
        [
            "**Walk the full rig:** tires, roof, hitch, awning — anything loose or low?",
            "**Look underneath:** fresh drips or anything hanging?",
            "**Check the dash:** fuel level, warning lights, tire pressure light",
            "**Seatbelts on,** kid and dog secured",
            "**One last look at camp:** nothing left behind, fire dead out",
        ],
    ),
    (
        "Emergency If-Thens",
        [
            "**IF stuck:** stop, assess, air down, traction boards before the shovel — never spin blindly",
            "**IF lost:** stop moving, check the paper map, retrace to your last known point",
            "**IF someone's hurt:** stabilize, treat what you can, **call for help early** — don't wait until it's worse",
            "**IF weather turns:** secure camp first, then decide — the mountain will be there next weekend",
            "**IF the rig won't start:** jumper pack first, then the call list — know who you're calling and whether you have signal",
        ],
    ),
    (
        "The ~$50 Starter Kit",
        [
            "Tire plug kit (~$10) — the number-one trip saver",
            "Budget 12V tire compressor (~$25) — pairs with the plug kit",
            "Basic first-aid kit (~$10) — blisters, burns, bandages",
            "Headlamp (~$8) — because the sun sets mid-task, every time",
            "All of it available at any auto parts or big-box store. Prices vary, capability doesn't.",
        ],
    ),
]


class ChecklistPDF(FPDF):
    def footer(self):
        self.set_y(-16)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(*MUTED)
        self.cell(
            0, 10,
            f"ghostsubie.com  ·  The Rig-Ready Checklist  ·  p. {self.page_no()}/{{nb}}",
            align="C",
        )

    def section_title(self, title):
        if self.get_y() > 235:
            self.add_page()
        self.set_font("DejaVu", "B", 13)
        self.set_text_color(*EMBER)
        self.cell(0, 8, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*RULE)
        self.set_line_width(0.6)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(3)

    def check_item(self, text, last=False):
        x0 = self.get_x()
        y0 = self.get_y()
        # checkbox square
        self.set_draw_color(*AMBER)
        self.set_line_width(0.7)
        self.rect(x0 + 1, y0 + 1.2, 4, 4)
        # text
        self.set_xy(x0 + 8, y0)
        self.set_font("DejaVu", "", 10.5)
        self.set_text_color(*INK)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 8, 5.6, text, markdown=True)
        self.ln(1.2)


pdf = ChecklistPDF("P", "mm", "Letter")
pdf.alias_nb_pages("{nb}")
pdf.set_auto_page_break(True, margin=22)
pdf.set_margins(18, 16, 18)
pdf.set_fill_color(*PAPER)
# Unicode TTF fonts (core fonts can't do em-dashes)
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
pdf.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
pdf.add_font("DejaVu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")

# ---- Page 1: header band ----
pdf.add_page()
pdf.set_fill_color(*PAPER)
pdf.rect(0, 0, 216, 297, "F")

band_h = 44
pdf.set_fill_color(*DARK)
pdf.rect(0, 0, 216, band_h, "F")
# amber rule under band
pdf.set_fill_color(*AMBER)
pdf.rect(0, band_h, 216, 2, "F")

pdf.set_xy(18, 10)
pdf.set_font("DejaVu", "B", 26)
pdf.set_text_color(*AMBER)
pdf.cell(0, 11, "THE RIG-READY CHECKLIST", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "", 11.5)
pdf.set_text_color(245, 239, 227)
pdf.cell(0, 7, "Ghost Subie Adventures  —  Preparedness Without Panic", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "I", 10)
pdf.set_text_color(185, 171, 144)
pdf.cell(0, 6, "The exact pre-trip checklist we run before every family camp.")

pdf.set_y(band_h + 10)

intro = (
    "Print this. Laminate it. Keep it in the glovebox. "
    "Run it top to bottom before every trip — the whole thing takes ten minutes "
    "and it has saved us more weekends than we can count."
)
pdf.set_font("DejaVu", "", 10.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 5.8, intro)
pdf.ln(4)

for title, items in SECTIONS:
    pdf.section_title(title)
    for i, item in enumerate(items):
        pdf.check_item(item, last=(i == len(items) - 1))
    pdf.ln(3)

# ---- Sign-off ----
pdf.ln(2)
pdf.set_draw_color(*RULE)
pdf.set_line_width(0.6)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(4)
pdf.set_font("DejaVu", "I", 11)
pdf.set_text_color(*INK)
pdf.multi_cell(
    0, 6.2,
    "Capability isn't bought — it's built, one checklist at a time. See you out there.\n— Roman",
)
pdf.ln(2)
pdf.set_font("DejaVu", "", 9.5)
pdf.set_text_color(*MUTED)
pdf.cell(0, 6, "ghostsubie.com  ·  hello@ghostsubie.com")

out = "/home/hatch/workspace/goals/ghost-subie-adventures-website-rebuild/site/public/rig-ready-checklist.pdf"
pdf.output(out)
print(f"Wrote {out} ({pdf.page_no()} pages)")
