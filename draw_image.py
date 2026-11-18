#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news front page (1024x1024).

A newspaper-style infographic: masthead + date, then six stories in a
2x3 grid, each with a kicker, a big readable headline and one summary
line. Deterministic: same input always produces the same PNG bytes.
Run:  python3 draw_image.py   -> writes entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (251, 247, 237)   # warm newsprint
INK = (18, 18, 18)
RED = (178, 24, 24)
GREY = (74, 74, 74)
RULE = (18, 18, 18)
LIGHT_RULE = (190, 184, 170)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_BOLD = f"{FONT_DIR}/DejaVuSerif-Bold.ttf"
SANS_BOLD = f"{FONT_DIR}/DejaVuSans-Bold.ttf"
SANS = f"{FONT_DIR}/DejaVuSans.ttf"
SERIF = f"{FONT_DIR}/DejaVuSerif.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("UKRAINE  •  WAR",
     "UKRAINE STRIKES KERCH BRIDGE",
     "Road span collapses in second straight day of attacks."),
    ("IRAN  •  GULF TENSIONS",
     "TANKERS HIT BY MINES NEAR HORMUZ",
     "Drones fired at US radar base in Bahrain."),
    ("DIPLOMACY  •  ASEAN",
     "TRUMP IN MANILA",
     "ASEAN summit; Xi–Trump–Putin three-way meet set for Thursday in Shenzhen."),
    ("FINANCE  •  BANKING",
     "JPMORGAN OUTAGE",
     "Software bug halts banking and Zelle; not a cyberattack."),
    ("MARKETS  •  TECH",
     "NVIDIA EARNINGS",
     "First report since Jensen Huang's exit."),
    ("SPACE  •  LAUNCH",
     "VULCAN ROCKET FAILS",
     "40 Amazon Leo satellites destroyed."),
]


def draw_story(draw, x, y, cell_w, cell_h, number, kicker, headline, summary):
    # Number badge: red disc, white numeral.
    badge_r = 17
    cx, cy = x + badge_r, y + badge_r + 2
    draw.ellipse([cx - badge_r, cy - badge_r, cx + badge_r, cy + badge_r],
                 fill=RED)
    num_font = font(SANS_BOLD, 22)
    num = str(number)
    nw = draw.textlength(num, font=num_font)
    draw.text((cx - nw / 2, cy - 13), num, font=num_font, fill=(255, 255, 255))

    # Kicker, to the right of the badge.
    kick_font = font(SANS_BOLD, 19)
    draw.text((x + 44, y + 8), kicker, font=kick_font, fill=RED)

    # Headline: big, bold, up to 3 lines.
    head_font = font(SANS_BOLD, 31)
    text_w = cell_w
    lines = wrap(draw, headline, head_font, text_w)
    hy = y + 44
    for line in lines[:3]:
        draw.text((x, hy), line, font=head_font, fill=INK)
        hy += 37

    # Summary: one or two lines, regular weight.
    sum_font = font(SANS, 21)
    slines = wrap(draw, summary, sum_font, text_w)
    sy = hy + 6
    for line in slines[:2]:
        draw.text((x, sy), line, font=sum_font, fill=GREY)
        sy += 27


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # --- Masthead -------------------------------------------------------
    mast_font = font(SERIF_BOLD, 96)
    title = "WORLD NEWS"
    tw = draw.textlength(title, font=mast_font)
    draw.text(((W - tw) / 2, 26), title, font=mast_font, fill=INK)

    # Thin rule under the masthead.
    draw.line([(36, 148), (W - 36, 148)], fill=RULE, width=2)

    # Date line, in red.
    date_font = font(SANS_BOLD, 34)
    date = "TUESDAY, 17 NOVEMBER 2026"
    dw = draw.textlength(date, font=date_font)
    draw.text(((W - dw) / 2, 160), date, font=date_font, fill=RED)

    # Tagline.
    tag_font = font(SERIF, 23)
    tag = "Six stories that defined the day"
    tgw = draw.textlength(tag, font=tag_font)
    draw.text(((W - tgw) / 2, 206), tag, font=tag_font, fill=GREY)

    # Thick double rule closing the masthead.
    draw.line([(36, 244), (W - 36, 244)], fill=RULE, width=4)
    draw.line([(36, 252), (W - 36, 252)], fill=RULE, width=1)

    # --- Story grid: 2 columns x 3 rows --------------------------------
    margin = 36
    gap_x = 28
    gap_y = 18
    col_w = (W - 2 * margin - gap_x) // 2
    top = 272
    row_h = 224
    for i, (kicker, headline, summary) in enumerate(STORIES):
        col = i % 2
        row = i // 2
        x = margin + col * (col_w + gap_x)
        y = top + row * row_h
        draw_story(draw, x, y, col_w, row_h, i + 1, kicker, headline, summary)
        # Vertical divider between the two columns.
        if col == 0:
            draw.line([(margin + col_w + gap_x // 2, y + 6),
                       (margin + col_w + gap_x // 2, y + row_h - 26)],
                      fill=LIGHT_RULE, width=1)
        # Horizontal divider between rows.
        if row < 2:
            draw.line([(x, y + row_h - 8), (x + col_w, y + row_h - 8)],
                      fill=LIGHT_RULE, width=1)

    # --- Footer ---------------------------------------------------------
    draw.line([(36, 968), (W - 36, 968)], fill=RULE, width=2)
    foot_font = font(SANS_BOLD, 18)
    foot = "17 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE"
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) / 2, 980), foot, font=foot_font, fill=INK)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
