#!/usr/bin/env python3
"""Generate the 3 AI Prompts PDF for Ghost Subie Adventures.

Comment-PREP funnel deliverable (Oct 6 @davecto adaptation, saved at
~/workspace/your_files/Ghost-Subie-3-AI-Prompts.md). Staged locally only —
NOT pushed live; needs Roman's tap before it ships.
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
BOXFILL = (244, 236, 220)
PROMPTFILL = (38, 33, 26)

SITE = "/home/hatch/workspace/site/ghostsubie.com"
LOGO_PATH = f"{SITE}/public/images/logo-amber.png"
SIG_PATH = f"{SITE}/public/images/signature.png"

PROMPTS = [
    (
        "1", "COMPETITOR ANALYSIS",
        "You are my social media analyst for my Instagram @ghostsubieadventures "
        '(bio: "Preparedness Without Panic, daily-driven Ghost | SATX Explorer / '
        "Subaru Overlander, EDC, Fieldcraft\"). Find 5-10 creators in my niche: "
        "overland Subaru owners, family camping creators, and \"preparedness "
        "without panic\" creators with 2K-50K followers. For each, audit their "
        "last 20 reels and report: their 3 best-performing posts with "
        "like/comment counts, the repeatable format in each (hook, structure, "
        "on-screen text pattern, caption mechanic), and what my account is "
        "missing that they do well. Rank creators by engagement relative to "
        "follower count.",
        "Paste into ChatGPT or your AI tool of choice whenever you want a fresh "
        "sweep of who's winning in your niche. Ask it to re-run quarterly - the "
        "niche moves fast.",
    ),
    (
        "2", "FEED AUDIT",
        "You are auditing my Instagram @ghostsubieadventures (bio: \"Preparedness "
        "Without Panic, daily-driven Ghost | SATX Explorer / Subaru Overlander, "
        "EDC, Fieldcraft\"). Here are my last 20 posts: [paste list with "
        "captions, like counts, comment counts]. Tell me: (a) which 3 "
        "over-performed and WHY - hook, format, timing, topic; (b) which 3 "
        "under-performed and WHY; (c) three tactical changes I can make this "
        "week - one about hooks, one about format, one about posting cadence. "
        "No generic advice. My niche: daily-driven white 2022 Subaru Forester "
        "overland rig in Texas, \"Preparedness Without Panic,\" dad + wife + "
        "kid + blue heeler, pitching brands for partnerships.",
        "Run monthly. What worked last month: story/community hooks won "
        "(\"missing my fozzy bros\" Base Camp post - 121 likes; \"raised vs "
        "lowered fozzy\" - 112 likes / 16 comments; Bluey origin story - 70). "
        "Diary-style captions and Ghost Energy meme posts sat at the bottom "
        "(10-36 likes). Repeat the comparison-joke + tags playbook that drove "
        "your best comment ratios.",
    ),
    (
        "3", "FORENSIC RETENTION",
        "You are a short-form retention analyst. Here are my last 30 reels with "
        "average watch time and drop-off points: [paste data]. Identify: the 3 "
        "biggest retention killers (first-3-second hook, mid-video sag, "
        "ending), the timestamp patterns where viewers leave, and what my "
        "best-retained video did differently. Give me one fixed opening formula "
        "and one fixed closing formula for my next 10 videos.",
        "Needs your watch-time data - Meta Business Suite > Insights > Reels > "
        "export the last 30 reels (average watch time, drop-off points). Paste "
        "the export into the prompt. Run every 1-2 months or after any big "
        "content experiment.",
    ),
]


class PromptsPDF(FPDF):
    def header(self):
        # warm paper background on every page
        self.set_fill_color(*PAPER)
        self.rect(0, 0, 216, 279, "F")

    def footer(self):
        self.set_y(-16)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(*MUTED)
        self.cell(
            0, 10,
            "www.ghostsubie.com  \u00b7  The 3 AI Prompts  \u00b7  p. "
            f"{self.page_no()}/{{nb}}",
            align="C",
        )

    def prompt_block(self, num, title, prompt, useit):
        # badge + title
        y = self.get_y()
        self.set_fill_color(*AMBER)
        self.rect(self.l_margin, y + 0.5, 8, 8, "F")
        self.set_xy(self.l_margin, y + 0.5)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*DARK)
        self.cell(8, 8, num, align="C")
        self.set_xy(self.l_margin + 11, y)
        self.set_font("DejaVu", "B", 13)
        self.set_text_color(*EMBER)
        self.cell(0, 8, f"PROMPT {num}  \u00b7  {title}",
                   new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        # the prompt itself: dark box, light text (measure, then paint)
        self.set_font("Mono", "", 9.2)
        text = "\u201c" + prompt + "\u201d"
        w = self.w - self.l_margin - self.r_margin - 8
        lines = self.multi_cell(w - 8, 4.8, text, dry_run=True, output="LINES")
        h = len(lines) * 4.8
        if self.get_y() + h + 40 > self.h - 22:
            self.add_page()
        box_y = self.get_y()
        self.set_fill_color(*PROMPTFILL)
        self.rect(self.l_margin + 4, box_y, w, h + 8, "F")
        self.set_xy(self.l_margin + 8, box_y + 4)
        self.set_text_color(245, 239, 227)
        self.multi_cell(w - 8, 4.8, text)
        self.set_y(box_y + h + 8 + 2)
        # use-it line
        self.set_x(self.l_margin + 4)
        self.set_font("DejaVu", "I", 9.5)
        self.set_text_color(*MUTED)
        self.multi_cell(w, 4.8, "USE IT: " + useit)
        self.ln(4)
        # rule
        self.set_draw_color(*RULE)
        self.set_line_width(0.5)
        self.line(self.l_margin + 4, self.get_y(),
                  self.w - self.r_margin - 4, self.get_y())
        self.ln(4)


pdf = PromptsPDF("P", "mm", "Letter")
pdf.alias_nb_pages("{nb}")
pdf.set_auto_page_break(True, margin=22)
pdf.set_margins(18, 16, 18)
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
pdf.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
pdf.add_font("DejaVu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
pdf.add_font("Mono", "", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")

pdf.add_page()

# ---- header band (page 1 only; paper bg comes from header()) ----
band_h = 46
pdf.set_fill_color(*DARK)
pdf.rect(0, 0, 216, band_h, "F")
pdf.set_fill_color(*AMBER)
pdf.rect(0, band_h, 216, 2, "F")

pdf.set_xy(18, 10)
pdf.set_font("DejaVu", "B", 24)
pdf.set_text_color(*AMBER)
pdf.cell(0, 10, "THE 3 AI PROMPTS", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "", 11.5)
pdf.set_text_color(245, 239, 227)
pdf.cell(0, 7, "Ghost Subie Adventures  \u2014  Preparedness Without Panic",
         new_x="LMARGIN", new_y="NEXT")
pdf.set_x(18)
pdf.set_font("DejaVu", "I", 10)
pdf.set_text_color(185, 171, 144)
pdf.cell(0, 6, "Steal the trend's mechanic, never its numbers. Run these like a routine, not a one-off.")

# ---- intro ----
pdf.set_y(band_h + 8)
pdf.set_font("DejaVu", "", 10.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(
    0, 5.4,
    "These are the three prompts behind every data-driven decision on "
    "@ghostsubieadventures. Copy each one into ChatGPT (or your AI tool of "
    "choice), fill in your own numbers where the brackets are, and run them "
    "on the cadence below each prompt. They are written for my niche, but the "
    "structure works for any creator.",
)
pdf.ln(3)

# ---- prompts ----
for p in PROMPTS:
    # keep prompt 2 and 3 from orphaning badly
    pdf.prompt_block(*p)

# ---- sign-off ----
pdf.ln(2)
pdf.set_draw_color(*RULE)
pdf.set_line_width(0.6)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(2)
pdf.set_font("DejaVu", "", 9.5)
pdf.set_text_color(*MUTED)
pdf.cell(0, 6, "www.ghostsubie.com   \u00b7   IG: @ghostsubieadventures",
         new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_font("DejaVu", "I", 11)
pdf.set_text_color(*INK)
pdf.cell(0, 6.2, "Stay prepared, not panicked,", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1.5)
pdf.image(SIG_PATH, x=pdf.l_margin, w=28)

out = f"{SITE}/public/3-ai-prompts.pdf"
pdf.output(out)
print(f"Wrote {out} ({pdf.page_no()} pages)")
