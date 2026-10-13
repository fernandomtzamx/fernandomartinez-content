#!/usr/bin/env python3
"""Portadas de fernandomartinez.mx (1200x630), con el sistema visual de la marca:
papel cálido, tinta, rojo de la corbata del logo y llaves de código.

Uso:
  python scripts/cover.py --out images/slug.png --kicker "IA Y TECNOLOGÍA" \
      --title "Qué es el internet de las cosas" --chip "IoT"
"""
import argparse

from PIL import Image, ImageDraw, ImageFont

W, H, S = 1200, 630, 2
F = "/usr/share/fonts/opentype/inter/"
PAPER, INK, MUTED = (251, 248, 241), (22, 23, 27), (110, 112, 125)
RED, HL, LINE = (226, 6, 19), (255, 228, 92), (230, 224, 211)


def font(name, size):
    return ImageFont.truetype(F + name, int(size * S))


def wrap(draw, text, fnt, max_w):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w * S:
            line = trial
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--kicker", default="BLOG")
    ap.add_argument("--chip", default="")
    a = ap.parse_args()

    img = Image.new("RGB", (W * S, H * S), PAPER)
    d = ImageDraw.Draw(img)
    x0, text_w = 72, 640

    # Panel derecho de tinta con las llaves y el chip
    px = 790
    d.rectangle([px * S, 0, W * S, H * S], fill=INK)
    brace = font("InterDisplay-Light.otf", 300)
    d.text(((px + 26) * S, 120 * S), "{", font=brace, fill=RED)
    d.text(((W - 120) * S, 120 * S), "}", font=brace, fill=RED)
    if a.chip:
        for size in (96, 84, 72, 60, 50, 42):
            cf = font("InterDisplay-Black.otf", size)
            if d.textlength(a.chip, font=cf) <= 220 * S:
                break
        cw = d.textlength(a.chip, font=cf)
        bbox = d.textbbox((0, 0), a.chip, font=cf)
        ch = bbox[3] - bbox[1]
        cx = (px + (W - px) / 2) * S - cw / 2
        cy = (H / 2) * S - ch / 2 - bbox[1]
        d.text((cx, cy), a.chip, font=cf, fill=PAPER)

    # Marca y categoría
    d.text((x0 * S, 64 * S), "{ FERNANDO MARTÍNEZ }", font=font("InterDisplay-Black.otf", 19), fill=RED)
    d.text((x0 * S, 96 * S), a.kicker.upper(), font=font("Inter-SemiBold.otf", 16), fill=MUTED)

    # Titular: el tamaño más grande que quepa en 5 líneas
    for size in (60, 56, 52, 48, 44, 40, 36):
        f = font("InterDisplay-ExtraBold.otf", size)
        lines = wrap(d, a.title, f, text_w)
        if len(lines) <= 5:
            break
    lh = int(size * 1.16)
    block = lh * len(lines)
    y = max(150, (H - block) // 2 + 20)
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            # Resaltador amarillo en la última línea
            lw = d.textlength(line, font=f) / S
            d.rectangle([(x0 - 6) * S, (y + lh * 0.48) * S, (x0 + lw + 8) * S, (y + lh * 0.98) * S], fill=HL)
        d.text((x0 * S, y * S), line, font=f, fill=INK)
        y += lh

    d.line([x0 * S, (H - 70) * S, (px - 60) * S, (H - 70) * S], fill=LINE, width=2 * S)
    d.text((x0 * S, (H - 54) * S), "fernandomartinez.mx", font=font("Inter-Medium.otf", 16), fill=MUTED)

    img.resize((W, H), Image.LANCZOS).save(a.out, optimize=True)


if __name__ == "__main__":
    main()
